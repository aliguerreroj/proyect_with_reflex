from enum import Enum
import reflex as rx
from .colors import Color,TextColor
from .fonts import Font,FontWeight
# Constants
MAX_WIDTH= "600px"



# sizes
class Size(Enum):
    ZERO="0px !important"
    SMALL="0.5em"
    MEDIUM="0.85em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    VERY_BIG="4em"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css"
]

BASE_STYLE={
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    "font_weight": FontWeight.LIGHT.value,
    


    rx.button:{
        "width":"100%",
        "height":"100%",
        "padding":Size.SMALL.value,
        "border_radius":Size.SMALL.value,
        "color":TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
            "background_color":Color.SECONDARY.value
        }
    },
    rx.link:{
        "text_decoration":"None",
        "_hover":{}
    },
    rx.heading:{
        "font_weight": FontWeight.MEDIUM.value,
        
    },
    rx.hstack:{
        # "padding_left":Size.MEDIUM.value,
    }
}

button_title_style= dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value
)
button_body_style= dict(
    font_family=Font.DEFAULT.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)
navbar_tittle_style= dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.LIGHT.value,
    font_size=Size.BIG.value
)

tittle_style= dict(
    font_family=Font.TITLE.value,
    widht="100%",
    padding_top=Size.LARGE.value

)