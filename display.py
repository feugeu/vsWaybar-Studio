from micropython import const
from pyswitch.colors import DEFAULT_LABEL_COLOR
from pyswitch.ui.ui import DisplayElement, DisplayBounds
from pyswitch.ui.elements import DisplayLabel
from pyswitch.controller.callbacks import Callback

_ACTION_LABEL_LAYOUT = {
    "font": "/fonts/H20.pcf",
    "backColor": DEFAULT_LABEL_COLOR,
    "stroke": 1,
}

_DISPLAY_WIDTH = const(
    240
)
_DISPLAY_HEIGHT = const(
    240
)
_SLOT_WIDTH = const(
    80
)
_SLOT_HEIGHT = const(
    40
)
_FOOTER_Y = const(
    200
)
_RIG_NAME_HEIGHT = const(
    160
)

DISPLAY_HEADER_1 = DisplayLabel(
    layout = _ACTION_LABEL_LAYOUT, 
    bounds = DisplayBounds(
        x = 0, 
        y = 0, 
        w = _SLOT_WIDTH, 
        h = _SLOT_HEIGHT
    )
)
DISPLAY_HEADER_2 = DisplayLabel(
    layout = _ACTION_LABEL_LAYOUT, 
    bounds = DisplayBounds(
        x = _SLOT_WIDTH, 
        y = 0, 
        w = _SLOT_WIDTH, 
        h = _SLOT_HEIGHT
    )
)
DISPLAY_HEADER_3 = DisplayLabel(
    layout = _ACTION_LABEL_LAYOUT, 
    bounds = DisplayBounds(
        x = _DISPLAY_WIDTH-_SLOT_WIDTH, 
        y = 0, 
        w = _SLOT_WIDTH, 
        h = _SLOT_HEIGHT
    )
)
DISPLAY_FOOTER_1 = DisplayLabel(
    layout = _ACTION_LABEL_LAYOUT, 
    bounds = DisplayBounds(
        x = 0, 
        y = _FOOTER_Y, 
        w = _SLOT_WIDTH, 
        h = _SLOT_HEIGHT
    )
)
DISPLAY_FOOTER_2 = DisplayLabel(
    layout = _ACTION_LABEL_LAYOUT, 
    bounds = DisplayBounds(
        x = _SLOT_WIDTH, 
        y = _FOOTER_Y, 
        w = _SLOT_WIDTH, 
        h = _SLOT_HEIGHT
    )
)
DISPLAY_FOOTER_3 = DisplayLabel(
    layout = _ACTION_LABEL_LAYOUT, 
    bounds = DisplayBounds(
        x = _DISPLAY_WIDTH-_SLOT_WIDTH, 
        y = _FOOTER_Y, 
        w = _SLOT_WIDTH, 
        h = _SLOT_HEIGHT
    )
)

class SimpleDisplayCallback(Callback):
    def get_root(self):
        return DisplayElement(
            bounds = DisplayBounds(0, 0, 240, 240),
            children = [
                DISPLAY_HEADER_1,
                DISPLAY_HEADER_2,
                DISPLAY_HEADER_3,
                DISPLAY_FOOTER_1,
                DISPLAY_FOOTER_2,
                DISPLAY_FOOTER_3,
                DisplayLabel(
                    bounds = DisplayBounds(0, _SLOT_HEIGHT, _DISPLAY_WIDTH, _RIG_NAME_HEIGHT),
                    layout = {
                        "font": "/fonts/PTSans-NarrowBold-40.pcf",
                        "lineSpacing": 0.8,
                        "maxTextWidth": 220,
                        "text": "GT-1000 Core",
                    },
                )
            ]
        )
    
# Instance du callback
Splashes = SimpleDisplayCallback()