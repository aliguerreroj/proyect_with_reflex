import reflex as rx
from link_bio.styles.styles import Size,button_title_style,button_body_style
from link_bio.styles.colors import Color
import link_bio.styles.styles as styles

def link_buttons_image(title:str,body:str,image:str,url:str,is_external=True,highlight_color=None,animated=False)->rx.Component:
    return rx.link(
        
        rx.button(
            rx.image(
                src=image,
                width=Size.LARGE.value,
                height=Size.LARGE.value,
                margin=Size.MEDIUM.value,
                alt=title
            ),
            rx.vstack(
                rx.text(title,style=button_title_style),
                rx.text(body,style=button_body_style),
                spacing="1",
                align_items="start",
                # margin=Size.ZERO.value,
            ),
        
            display="flex",
            justify_content="flex-start",
            align_content="center",
            border_width="2px" if highlight_color != None else "0px", # Ancho del borde
            border_style="solid",  # Estilo del borde
            border_color=highlight_color,  # Color del borde
            class_name=styles.BOUNCEIN_ANIMATION if animated else None,
        
        ),
        border_color= highlight_color,
        border_widthr= "2px" if highlight_color != None else None,
        width="100%",
        class_name=styles.BOUNCEIN_ANIMATION if animated else None,
        # text,width="100%"
        href=url,
        is_external=is_external,
        margin_top=Size.ZERO.value
        

    )
    
 