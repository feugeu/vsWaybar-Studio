##############################################################################################################################################
# 
# Configuration de la communication MIDI DIN pour contrôleur générique
#
##############################################################################################################################################

from pyswitch.controller.midi import MidiRouting
from pyswitch.hardware.devices.pa_midicaptain import PA_MIDICAPTAIN_DIN_MIDI
from config import Config

# Configuration du port MIDI DIN
_DIN_MIDI = PA_MIDICAPTAIN_DIN_MIDI(
    in_channel = Config.get("midiInChannel"),
    out_channel = Config.get("midiOutChannel", 1) - 1  # Conversion 1-16 vers 0-15
)

# Configuration de la communication
Communication = {
    # Pas de protocole bidirectionnel
    "protocol": None,

    # Configuration MIDI : routage depuis/vers l'application via DIN MIDI
    "midi": {
        "routings": [
            # Application reçoit les messages MIDI du port DIN
            MidiRouting(
                source = _DIN_MIDI,
                target = MidiRouting.APPLICATION
            ),

            # Application envoie les messages MIDI vers le port DIN
            MidiRouting(
                source = MidiRouting.APPLICATION,
                target = _DIN_MIDI
            ),
        ]
    }
}