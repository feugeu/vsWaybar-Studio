from pyswitch.hardware.devices.pa_midicaptain_mini_6 import *
from pyswitch.clients.local.actions.custom import CUSTOM_MESSAGE
from pyswitch.controller.actions import PushButtonAction
from display import DISPLAY_SWITCH_1, DISPLAY_SWITCH_2, DISPLAY_SWITCH_3
from display import DISPLAY_SWITCH_A, DISPLAY_SWITCH_B, DISPLAY_SWITCH_C
from display import SWITCH_LABELS
from config import Config

# Fonction pour créer une action de switch générique
def create_switch_action(cc_number, switch_id, display_label):
    """
    Crée une action pour un switch qui :
    - Envoie un CC toggle (127/0)
    - Affiche le label avec la couleur appropriée
    - Gère les LEDs selon l'état
    """
    from generic_actions import GENERIC_CC_TOGGLE
    
    return GENERIC_CC_TOGGLE(
        cc_number = cc_number,
        switch_id = switch_id,
        display = display_label,
        text = SWITCH_LABELS[switch_id]["text"],
        color = SWITCH_LABELS[switch_id]["color"]
    )

# Configuration des inputs
# Labels PHYSIQUES sur l'appareil :
#   Rangée du HAUT : Switch "1", "2", "3"
#   Rangée du BAS : Switch "A", "B", "C"
# 
# Disposition souhaitée à l'écran :
#   Rangée du HAUT de l'écran : TREM (CC4), DELAY (CC5), RVB (CC6)
#   Rangée du BAS de l'écran : DIST (CC1), BOOST (CC2), CHO (CC3)

Inputs = [
    # Switch physique "1" (HAUT À GAUCHE) → Label TREM à l'écran (CC4, Violet)
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_1,
        "actions": [
            create_switch_action(4, "A", DISPLAY_SWITCH_A)
        ]
    },
    
    # Switch physique "2" (HAUT AU CENTRE) → Label DELAY à l'écran (CC5, Blanc)
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_2,
        "actions": [
            create_switch_action(5, "B", DISPLAY_SWITCH_B)
        ]
    },
    
    # Switch physique "3" (HAUT À DROITE) → Label RVB à l'écran (CC6, Bleu)
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_3,
        "actions": [
            create_switch_action(6, "C", DISPLAY_SWITCH_C)
        ]
    },
    
    # Switch physique "A" (BAS À GAUCHE) → Label DIST à l'écran (CC1, Rouge)
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_A,
        "actions": [
            create_switch_action(1, 1, DISPLAY_SWITCH_1)
        ]
    },
    
    # Switch physique "B" (BAS AU CENTRE) → Label BOOST à l'écran (CC2, Vert)
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_B,
        "actions": [
            create_switch_action(2, 2, DISPLAY_SWITCH_2)
        ]
    },
    
    # Switch physique "C" (BAS À DROITE) → Label CHO à l'écran (CC3, Jaune)
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_C,
        "actions": [
            create_switch_action(3, 3, DISPLAY_SWITCH_3)
        ]
    }
]