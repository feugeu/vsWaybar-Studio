from pyswitch.colors import Colors
from display import DISPLAY_HEADER_1, DISPLAY_HEADER_2, DISPLAY_HEADER_3, DISPLAY_FOOTER_1, DISPLAY_FOOTER_2, DISPLAY_FOOTER_3
from pyswitch.hardware.devices.pa_midicaptain_mini_6 import *
from pyswitch.controller.callbacks import BinaryParameterCallback
from pyswitch.controller.actions import PushButtonAction
from pyswitch.controller.client import ClientParameterMapping
from adafruit_midi.control_change import ControlChange

Inputs = [
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_A,
        "actions": [
            PushButtonAction({
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "SwitchA",
                            set = ControlChange(1,0),
                            response = ControlChange(1,0)
                        ), 
                        color = Colors.RED,
                        text = "DIST",
                        value_enable = 127
                    ),
                    "display": DISPLAY_FOOTER_1,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH                   
                }
            )            
        ],  
    },
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_B,
        "actions": [
            PushButtonAction({
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "SwitchB",
                            set = ControlChange(2,0),
                            response = ControlChange(2,0)
                        ), 
                        color = Colors.GREEN,
                        text = "BOOST",
                        value_enable = 127
                    ),
                    "display": DISPLAY_FOOTER_2,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH                 
                }
            )            
        ],  
    },
        {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_C,
        "actions": [
            PushButtonAction({
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "SwitchC",
                            set = ControlChange(3,0),
                            response = ControlChange(3,0)
                        ), 
                        color = Colors.YELLOW,
                        text = "CHO",
                        value_enable = 127
                    ),
                    "display": DISPLAY_FOOTER_3,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH               
                }
            )            
        ],  
    },
   {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_1,
        "actions": [
            PushButtonAction({
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "Switch1",
                            set = ControlChange(4,0),
                            response = ControlChange(4,0)
                        ), 
                        color = Colors.PURPLE,
                        text = "TREM",
                        value_enable = 127
                    ),
                    "display": DISPLAY_HEADER_1,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH                 
                }
            )            
        ]   
    },
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_2,
        "actions": [
            PushButtonAction({
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "Switch2",
                            set = ControlChange(5,0),
                            response = ControlChange(5,0)
                        ), 
                        color = Colors.WHITE,
                        text = "DELAY",
                        value_enable = 127
                    ),
                    "display": DISPLAY_HEADER_2,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH                   
                }
            )            
        ],  
    },
    {
        "assignment": PA_MIDICAPTAIN_MINI_SWITCH_3,
        "actions": [
            PushButtonAction({
                    "callback": BinaryParameterCallback(
                        mapping = ClientParameterMapping.get(
                            name = "Switch3",
                            set = ControlChange(6,0),
                            response = ControlChange(6,0)
                        ), 
                        color = Colors.BLUE,
                        text = "RVB",
                        value_enable = 127
                    ),
                    "display": DISPLAY_HEADER_3,
                    "useSwitchLeds": True,
                    "mode": PushButtonAction.LATCH                  
                }
            )            
        ],  
    },
]
