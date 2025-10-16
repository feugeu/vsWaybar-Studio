"""
Actions personnalisées pour le contrôleur MIDI générique
"""

from pyswitch.controller.actions import PushButtonAction
from pyswitch.controller.callbacks import BinaryParameterCallback
from pyswitch.controller.client import ClientParameterMapping
from adafruit_midi.control_change import ControlChange
from pyswitch.colors import dim_color
from config import Config

# Dictionnaire global pour suivre l'état de chaque CC
_CC_STATES = {}

def GENERIC_CC_TOGGLE(cc_number, switch_id, display, text, color):
    """
    Action générique pour envoyer/recevoir des Control Change en mode toggle
    
    Args:
        cc_number: Numéro du Control Change (1-127)
        switch_id: Identifiant du switch pour le tracking
        display: Label d'affichage
        text: Texte à afficher
        color: Couleur du switch/label
    """
    
    # Initialiser l'état si nécessaire
    if cc_number not in _CC_STATES:
        _CC_STATES[cc_number] = False
    
    # Créer le mapping pour ce CC
    mapping = ClientParameterMapping.get(
        name = f"CC{cc_number}",
        set = ControlChange(cc_number, 0),
        response = ControlChange(cc_number, 0)
    )
    
    return PushButtonAction({
        "callback": GenericCCCallback(
            mapping = mapping,
            cc_number = cc_number,
            text = text,
            color = color
        ),
        "mode": PushButtonAction.LATCH,
        "display": display,
        "id": switch_id,
        "useSwitchLeds": True
    })


class GenericCCCallback(BinaryParameterCallback):
    """
    Callback pour gérer l'envoi et la réception de Control Change
    """
    
    def __init__(self, mapping, cc_number, text, color):
        super().__init__(
            mapping = mapping,
            text = text,
            color = color,
            value_enable = 127,
            value_disable = 0,
            reference_value = 64,  # Considère ON si >= 64
            comparison_mode = BinaryParameterCallback.GREATER_EQUAL,
            use_internal_state = False  # Attend les messages MIDI pour confirmer
        )
        
        self.__cc_number = cc_number
    
    def state_changed_by_user(self):
        """
        Appelé quand l'utilisateur appuie sur le switch
        """
        # Inverser l'état
        _CC_STATES[self.__cc_number] = not _CC_STATES[self.__cc_number]
        
        # Envoyer le message MIDI approprié
        value = 127 if _CC_STATES[self.__cc_number] else 0
        self.action.appl.client.set(self.mapping, value)
        
        # Mettre à jour l'affichage
        self.update_displays()
    
    def evaluate_value(self, value):
        """
        Appelé quand un message MIDI est reçu
        """
        if value is not None:
            # Mettre à jour l'état selon la valeur reçue
            _CC_STATES[self.__cc_number] = (value >= 64)
            self.action.feedback_state(_CC_STATES[self.__cc_number])
        
        super().evaluate_value(value)
    
    def set_switch_color(self, color):
        """
        Gère l'affichage des LEDs : 
        - ON : les 3 anneaux avec luminosité normale
        - OFF : seulement le premier anneau avec luminosité minimale
        """
        if not hasattr(self.action, 'switch'):
            return
        
        switch = self.action.switch
        state = _CC_STATES.get(self.__cc_number, False)
        
        if state:
            # État ON : tous les anneaux allumés
            switch.color = color
            switch.brightness = Config.get("ledBrightnessOn", 0.3)
        else:
            # État OFF : seulement le premier anneau, luminosité minimale
            colors = [color, (0, 0, 0), (0, 0, 0)]
            brightnesses = [Config.get("ledBrightnessOff", 0.02), 0, 0]
            
            switch.colors = colors
            switch.brightnesses = brightnesses
    
    def set_label_color(self, color):
        """
        Gère la couleur du label selon l'état
        """
        if not self.action.label:
            return
        
        state = _CC_STATES.get(self.__cc_number, False)
        
        if state:
            dim_factor = Config.get("displayDimFactorOn", 1)
        else:
            dim_factor = Config.get("displayDimFactorOff", 0.3)
        
        self.action.label.back_color = dim_color(color, dim_factor)