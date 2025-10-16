from pyswitch.clients.local.callbacks.splashes import SplashesCallback
from pyswitch.ui.ui import DisplayElement, DisplayBounds
from pyswitch.ui.elements import DisplayLabel
from pyswitch.colors import Colors
from micropython import const

# Dimensions de l'écran
_DISPLAY_WIDTH = const(240)
_DISPLAY_HEIGHT = const(240)

# Hauteur des sections (divisé en 3 : top, middle, bottom)
_SECTION_HEIGHT = const(80)

# Largeur de chaque label (3 par ligne)
_LABEL_WIDTH = const(80)

# Configuration des labels pour chaque switch
# Disposition physique souhaitée :
#   Rangée du HAUT : TREM (A), DELAY (B), RVB (C)
#   Rangée du BAS : DIST (1), BOOST (2), CHO (3)

SWITCH_LABELS = {
    1: {"text": "DIST", "color": Colors.RED},
    2: {"text": "BOOST", "color": Colors.GREEN},
    3: {"text": "CHO", "color": Colors.YELLOW},
    "A": {"text": "TREM", "color": Colors.PURPLE},
    "B": {"text": "DELAY", "color": Colors.WHITE},
    "C": {"text": "RVB", "color": Colors.BLUE}
}

# Layout pour les labels des switches
_SWITCH_LABEL_LAYOUT = {
    "font": "/fonts/H20.pcf",
    "backColor": Colors.BLACK,
    "stroke": 1,
}

# Label central "BOSS"
_BOSS_LABEL_LAYOUT = {
    "font": "/fonts/PTSans-NarrowBold-40.pcf",
    "backColor": Colors.BLACK,
}

# Création des labels pour les switches du haut (A, B, C)
DISPLAY_SWITCH_A = DisplayLabel(
    layout = _SWITCH_LABEL_LAYOUT,
    bounds = DisplayBounds(
        x = 0,
        y = 0,
        w = _LABEL_WIDTH,
        h = _SECTION_HEIGHT
    )
)

DISPLAY_SWITCH_B = DisplayLabel(
    layout = _SWITCH_LABEL_LAYOUT,
    bounds = DisplayBounds(
        x = _LABEL_WIDTH,
        y = 0,
        w = _LABEL_WIDTH,
        h = _SECTION_HEIGHT
    )
)

DISPLAY_SWITCH_C = DisplayLabel(
    layout = _SWITCH_LABEL_LAYOUT,
    bounds = DisplayBounds(
        x = _LABEL_WIDTH * 2,
        y = 0,
        w = _LABEL_WIDTH,
        h = _SECTION_HEIGHT
    )
)

# Label central "BOSS"
DISPLAY_BOSS = DisplayLabel(
    layout = _BOSS_LABEL_LAYOUT,
    bounds = DisplayBounds(
        x = 0,
        y = _SECTION_HEIGHT,
        w = _DISPLAY_WIDTH,
        h = _SECTION_HEIGHT
    )
)

# Création des labels pour les switches du bas (1, 2, 3)
DISPLAY_SWITCH_1 = DisplayLabel(
    layout = _SWITCH_LABEL_LAYOUT,
    bounds = DisplayBounds(
        x = 0,
        y = _SECTION_HEIGHT * 2,
        w = _LABEL_WIDTH,
        h = _SECTION_HEIGHT
    )
)

DISPLAY_SWITCH_2 = DisplayLabel(
    layout = _SWITCH_LABEL_LAYOUT,
    bounds = DisplayBounds(
        x = _LABEL_WIDTH,
        y = _SECTION_HEIGHT * 2,
        w = _LABEL_WIDTH,
        h = _SECTION_HEIGHT
    )
)

DISPLAY_SWITCH_3 = DisplayLabel(
    layout = _SWITCH_LABEL_LAYOUT,
    bounds = DisplayBounds(
        x = _LABEL_WIDTH * 2,
        y = _SECTION_HEIGHT * 2,
        w = _LABEL_WIDTH,
        h = _SECTION_HEIGHT
    )
)

# Initialisation du texte "BOSS"
DISPLAY_BOSS.text = "BOSS"

# Initialisation des textes et couleurs pour chaque switch
for switch_num, label in [("A", DISPLAY_SWITCH_A), ("B", DISPLAY_SWITCH_B), ("C", DISPLAY_SWITCH_C),
                          (1, DISPLAY_SWITCH_1), (2, DISPLAY_SWITCH_2), (3, DISPLAY_SWITCH_3)]:
    label.text = SWITCH_LABELS[switch_num]["text"]

# Élément racine contenant tous les éléments d'affichage
# Ordre : rangée du haut (A, B, C), BOSS au centre, rangée du bas (1, 2, 3)
Splashes = SplashesCallback(
    splashes = DisplayElement(
        bounds = DisplayBounds(
            x = 0,
            y = 0,
            w = _DISPLAY_WIDTH,
            h = _DISPLAY_HEIGHT
        ),
        children = [
            DISPLAY_SWITCH_A,
            DISPLAY_SWITCH_B,
            DISPLAY_SWITCH_C,
            DISPLAY_BOSS,
            DISPLAY_SWITCH_1,
            DISPLAY_SWITCH_2,
            DISPLAY_SWITCH_3
        ]
    )
)