import reflex as rx
from link_bio.styles.styles import Size,button_title_style,button_body_style

def link_buttons(title:str,body:str,icon:str,url:str,is_external=True,highlight_color=None)->rx.Component:
    return rx.link(
        
        rx.button(
            rx.hstack(
                rx.icon(icon),
                width=Size.BIG.value,
                height=Size.BIG.value,
                margin=Size.MEDIUM.value,
            ),
            rx.vstack(
                rx.text(title,style=button_title_style),
                rx.text(body,style=button_body_style),
                spacing="1",
                align_items="start",
                margin=Size.ZERO.value,
            ),

        display= "flex",
        justify_content= "flex-start",
        align_content="center",
        border_width="2px" if highlight_color != None else "0px", # Ancho del borde
        border_style="solid",  # Estilo del borde
        border_color=highlight_color,
        
        ),
        # text,width="100%"
        href=url,
        is_external=is_external,
        width="100%",
        

    )
    
 