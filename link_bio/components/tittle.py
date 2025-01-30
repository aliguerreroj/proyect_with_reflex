import reflex as rx
from link_bio.styles.styles import tittle_style
from link_bio.styles.styles import Size
def title(text:str)->rx.Component:
    return rx.flex(rx.heading(
        text,
        size="8",
        style=tittle_style
        # as_="3",
        # style={
            
        #     "font_size": "3em",
        #     "padding_y":Size.SMALL.value
 
        # },
    ))