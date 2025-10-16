##############################################################################################################################################
# 
# Configuration pour contrôleur MIDI générique - BOSS GT-1000 Core
#
##############################################################################################################################################

Config = {
    # Canal MIDI pour les messages sortants (1-16)
    "midiOutChannel": 1,
    
    # Canal MIDI pour les messages entrants (1-16, ou None pour tous les canaux)
    "midiInChannel": None,
    
    # Activer le filtrage MIDI via filter.py
    "enableMidiFilter": True,
    
    # Intervalle de mise à jour (millisecondes)
    "updateInterval": 50,
    
    # Luminosité des LEDs
    "ledBrightnessOn": 0.3,      # LED allumée
    "ledBrightnessOff": 0.02,    # LED éteinte (minimum pour visibilité dans le noir)
    
    # Facteurs d'atténuation pour l'affichage
    "displayDimFactorOn": 1,
    "displayDimFactorOff": 0.3,
    
    # Désactiver les fonctionnalités non nécessaires
    "enableMidiBridge": False,
    "clearBuffers": True,
    
    # Mode exploration (laisser à False)
    "exploreMode": False
}