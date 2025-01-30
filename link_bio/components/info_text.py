import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size,TextColor,Color

def info_text(title:str,body:str)->rx.Component:
    return rx.box(
        rx.text(
            rx.text.strong(
                title,
                font_weight="bold",
                color=Color.PRIMARY.value)
                ," ",
                body
            ),
            font_size=Size.MEDIUM.value,
            color=TextColor.BODY.value
    )