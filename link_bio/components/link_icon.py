from link_bio.styles.styles import Size

import reflex as rx

def link_icon(url:str,icon)->rx.Component:
    return rx.link(
        rx.icon(icon),
        # width=Size.MEDIUM.value,
        # height=Size.MEDIUM.value,

        widht="100%",
        height="100%",
        href=url,
        padding_right=Size.SMALL.value,
        padding_top=Size.SMALL.value,
        is_external=True,
    )



