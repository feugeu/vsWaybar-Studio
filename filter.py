"""
Fichier de configuration pour le filtrage et la transformation de messages MIDI

Ce fichier permet de définir des règles pour :
- Filtrer les messages MIDI entrants
- Transformer un type de message en un autre
- Changer les numéros de contrôle/programme
- Router entre différents canaux MIDI

Format des règles :
FILTER_RULES = [
    {
        "in_type": Type de message entrant ("CC", "PC", "NOTE_ON", "NOTE_OFF")
        "in_channel": Canal MIDI entrant (1-16, ou None pour tous)
        "in_num": Numéro du contrôle/note/programme (optionnel selon le type)
        "in_value": Valeur spécifique à filtrer (optionnel, pour CC et notes)
        
        "out_type": Type de message sortant ("CC", "PC", "NOTE_ON", "NOTE_OFF", ou "BLOCK" pour bloquer)
        "out_channel": Canal MIDI sortant (1-16)
        "out_num": Numéro du contrôle/note/programme en sortie
        "out_value": Valeur en sortie (optionnel, par défaut utilise la valeur entrante)
    }
]

Types de messages supportés :
- "CC" : Control Change
- "PC" : Program Change  
- "NOTE_ON" : Note On
- "NOTE_OFF" : Note Off
- "SYSEX" : System Exclusive (passage direct uniquement)
- "BLOCK" : Bloquer le message (ne pas transmettre)
"""

# ============================================================================
# RÈGLES DE FILTRAGE MIDI
# ============================================================================

FILTER_RULES = [
    # ========== EXEMPLES DE RÈGLES ==========
    
    # Exemple 1 : Transformer un CC10 du canal 2 en PC5 sur le canal 1
    # {
    #     "in_type": "CC",
    #     "in_channel": 2,
    #     "in_num": 10,
    #     "out_type": "PC",
    #     "out_channel": 1,
    #     "out_num": 5
    # },
    
    # Exemple 2 : Transformer un PC3 en CC20 avec valeur 127
    # {
    #     "in_type": "PC",
    #     "in_num": 3,
    #     "out_type": "CC",
    #     "out_channel": 1,
    #     "out_num": 20,
    #     "out_value": 127
    # },
    
    # Exemple 3 : Bloquer tous les messages CC du canal 5
    # {
    #     "in_type": "CC",
    #     "in_channel": 5,
    #     "out_type": "BLOCK"
    # },
    
    # Exemple 4 : Transférer les notes du canal 10 vers le canal 1
    # {
    #     "in_type": "NOTE_ON",
    #     "in_channel": 10,
    #     "out_type": "NOTE_ON",
    #     "out_channel": 1
    # },
    # {
    #     "in_type": "NOTE_OFF",
    #     "in_channel": 10,
    #     "out_type": "NOTE_OFF",
    #     "out_channel": 1
    # },
    
    # Exemple 5 : Transformer une note spécifique en CC
    # {
    #     "in_type": "NOTE_ON",
    #     "in_num": 60,  # Note C4
    #     "out_type": "CC",
    #     "out_channel": 1,
    #     "out_num": 30
    # },
    
    # ========== VOS RÈGLES PERSONNALISÉES ==========
    # Ajoutez vos règles ci-dessous :
    
]

# ============================================================================
# COMPORTEMENT PAR DÉFAUT
# ============================================================================

# Comportement pour les messages qui ne correspondent à aucune règle :
# - "PASS" : Laisser passer sans modification
# - "BLOCK" : Bloquer tous les messages non filtrés
DEFAULT_BEHAVIOR = "PASS"

# ============================================================================
# MESSAGES À TOUJOURS LAISSER PASSER (sécurité)
# ============================================================================

# Ces types de messages passent toujours, même avec DEFAULT_BEHAVIOR = "BLOCK"
# Cela garantit que les switches 1-6 (CC 1-6 sur canal 1) fonctionnent toujours
ALWAYS_PASS = [
    {"type": "CC", "channel": 1, "num": 1},  # Switch 1
    {"type": "CC", "channel": 1, "num": 2},  # Switch 2
    {"type": "CC", "channel": 1, "num": 3},  # Switch 3
    {"type": "CC", "channel": 1, "num": 4},  # Switch A
    {"type": "CC", "channel": 1, "num": 5},  # Switch B
    {"type": "CC", "channel": 1, "num": 6},  # Switch C
]