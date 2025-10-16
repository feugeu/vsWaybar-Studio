"""
Processeur de filtrage MIDI basé sur les règles définies dans filter.py
"""

from adafruit_midi.control_change import ControlChange
from adafruit_midi.program_change import ProgramChange
from adafruit_midi.system_exclusive import SystemExclusive
from adafruit_midi.midi_message import MIDIUnknownEvent

try:
    from filter import FILTER_RULES, DEFAULT_BEHAVIOR, ALWAYS_PASS
except ImportError:
    # Si filter.py n'existe pas, comportement par défaut
    FILTER_RULES = []
    DEFAULT_BEHAVIOR = "PASS"
    ALWAYS_PASS = []


class MidiFilterProcessor:
    """
    Classe pour traiter le filtrage et la transformation des messages MIDI
    """
    
    def __init__(self):
        self.rules = FILTER_RULES
        self.default_behavior = DEFAULT_BEHAVIOR
        self.always_pass = ALWAYS_PASS
        
        # Compteur pour debug (optionnel)
        self.processed_count = 0
        self.blocked_count = 0
    
    def process_message(self, midi_message):
        """
        Traite un message MIDI selon les règles de filtrage
        
        Args:
            midi_message: Message MIDI à traiter
            
        Returns:
            Message MIDI transformé, None si bloqué, ou le message original
        """
        if not midi_message or isinstance(midi_message, MIDIUnknownEvent):
            return None
        
        # SysEx passe toujours directement (pas de transformation possible)
        if isinstance(midi_message, SystemExclusive):
            return midi_message
        
        self.processed_count += 1
        
        # Identifier le type de message
        msg_type = self._get_message_type(midi_message)
        if not msg_type:
            return midi_message  # Type inconnu, laisser passer
        
        # Extraire les informations du message
        msg_info = self._extract_message_info(midi_message, msg_type)
        
        # Vérifier si le message doit toujours passer
        if self._is_always_pass(msg_info):
            return midi_message
        
        # Chercher une règle correspondante
        for rule in self.rules:
            if self._rule_matches(rule, msg_info):
                result = self._apply_rule(rule, msg_info, midi_message)
                if result is None:
                    self.blocked_count += 1
                return result
        
        # Aucune règle ne correspond : appliquer le comportement par défaut
        if self.default_behavior == "BLOCK":
            self.blocked_count += 1
            return None
        else:
            return midi_message
    
    def _get_message_type(self, midi_message):
        """Détermine le type de message MIDI"""
        if isinstance(midi_message, ControlChange):
            return "CC"
        elif isinstance(midi_message, ProgramChange):
            return "PC"
        elif isinstance(midi_message, SystemExclusive):
            return "SYSEX"
        return None
    
    def _extract_message_info(self, midi_message, msg_type):
        """Extrait les informations d'un message MIDI"""
        info = {"type": msg_type}
        
        if msg_type == "CC":
            # Extraire le canal (conversion 0-15 vers 1-16)
            channel = getattr(midi_message, "channel", None)
            if channel is not None:
                info["channel"] = channel + 1
            else:
                info["channel"] = None
            
            info["num"] = midi_message.control
            info["value"] = midi_message.value
        
        elif msg_type == "PC":
            # Extraire le canal (conversion 0-15 vers 1-16)
            channel = getattr(midi_message, "channel", None)
            if channel is not None:
                info["channel"] = channel + 1
            else:
                info["channel"] = None
                
            info["num"] = midi_message.patch
        
        elif msg_type == "SYSEX":
            info["channel"] = None
        
        return info
    
    def _is_always_pass(self, msg_info):
        """Vérifie si le message doit toujours passer"""
        if not self.always_pass:
            return False
            
        for allowed in self.always_pass:
            # Vérifier le type
            if "type" in allowed and allowed["type"] != msg_info["type"]:
                continue
            
            # Vérifier le canal
            if "channel" in allowed and allowed["channel"] is not None:
                if allowed["channel"] != msg_info.get("channel"):
                    continue
            
            # Vérifier le numéro
            if "num" in allowed and allowed["num"] is not None:
                if allowed["num"] != msg_info.get("num"):
                    continue
            
            # Si tout correspond, laisser passer
            return True
        
        return False
    
    def _rule_matches(self, rule, msg_info):
        """Vérifie si une règle correspond au message"""
        # Vérifier le type
        if "in_type" in rule and rule["in_type"] != msg_info["type"]:
            return False
        
        # Vérifier le canal (si spécifié)
        if "in_channel" in rule and rule["in_channel"] is not None:
            if rule["in_channel"] != msg_info.get("channel"):
                return False
        
        # Vérifier le numéro (si spécifié)
        if "in_num" in rule and rule["in_num"] is not None:
            if rule["in_num"] != msg_info.get("num"):
                return False
        
        # Vérifier la valeur (si spécifiée)
        if "in_value" in rule and rule["in_value"] is not None:
            if rule["in_value"] != msg_info.get("value"):
                return False
        
        return True
    
    def _apply_rule(self, rule, msg_info, original_message):
        """Applique une règle de transformation"""
        out_type = rule.get("out_type")
        
        # Si la règle demande de bloquer
        if out_type == "BLOCK":
            return None
        
        # Si pas de transformation spécifiée, retourner l'original
        if not out_type:
            return original_message
        
        # Créer le nouveau message selon le type de sortie
        out_channel = rule.get("out_channel")
        if out_channel is not None:
            out_channel = out_channel - 1  # Conversion 1-16 vers 0-15
        else:
            # Utiliser le canal d'origine si disponible
            channel = msg_info.get("channel")
            out_channel = (channel - 1) if channel is not None else 0
        
        if out_type == "CC":
            out_num = rule.get("out_num", msg_info.get("num", 0))
            out_value = rule.get("out_value", msg_info.get("value", 0))
            
            # Créer le nouveau CC avec le bon canal
            new_msg = ControlChange(out_num, out_value)
            new_msg.channel = out_channel
            return new_msg
        
        elif out_type == "PC":
            out_num = rule.get("out_num", msg_info.get("num", 0))
            
            # Créer le nouveau PC avec le bon canal
            new_msg = ProgramChange(out_num)
            new_msg.channel = out_channel
            return new_msg
        
        # Type de sortie non supporté, retourner l'original
        return original_message


# Instance globale du processeur
_filter_processor = None

def get_filter_processor():
    """Retourne l'instance du processeur de filtrage (singleton)"""
    global _filter_processor
    if _filter_processor is None:
        _filter_processor = MidiFilterProcessor()
    return _filter_processor