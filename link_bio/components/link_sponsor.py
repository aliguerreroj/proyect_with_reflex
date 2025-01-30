import reflex as rx
from link_bio.components.tittle import title
from link_bio.styles.styles import Size,TextColor,Color
def link_sponsor(imagen:str,url:str,alt:str)->rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height="3.5em",
            width="auto",
            alt=alt,


        ),
        href=url,
        is_external=True
    )