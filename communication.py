##############################################################################################################################################
# 
# Definition of communication wrappers. This is where the client specific (i.e. Kemper) implementations are linked to the framework.
#
##############################################################################################################################################

from pyswitch.controller.midi import MidiRouting
from pyswitch.hardware.devices.pa_midicaptain import PA_MIDICAPTAIN_DIN_MIDI, PA_MIDICAPTAIN_USB_MIDI

# MIDI Devices in use (optionally you can specify the in/out channels here, too)
_DIN_MIDI = PA_MIDICAPTAIN_DIN_MIDI(
    in_channel = 0, # omni = None, CH1 = 0, CH2 = 1...
    out_channel = 0
)
_USB_MIDI = PA_MIDICAPTAIN_USB_MIDI(
    in_channel = 0,
    out_channel = 0
)

# Communication configuration
Communication = {

    "midi": {
        "routings": [
            # Application: Receive MIDI messages from USB
            MidiRouting(
                source = _USB_MIDI,
                target = MidiRouting.APPLICATION
            ),

            # Application: Send MIDI messages to USB
            MidiRouting(
                source = MidiRouting.APPLICATION,
                target = _USB_MIDI
            ),

            # Application: Receive MIDI messages from DIN
            MidiRouting(
                source = _DIN_MIDI,
                target = MidiRouting.APPLICATION
            ),

            # Application: Send MIDI messages to DIN
            MidiRouting(
                source = MidiRouting.APPLICATION,
                target = _DIN_MIDI
            ),
        ]
    }
}
