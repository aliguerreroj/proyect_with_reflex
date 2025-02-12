import reflex as rx
from link_bio.model.featured import Featured
from link_bio.styles.styles import Size
from link_bio.styles.styles import button_body_style

def featured_link(item:Featured)-> rx.Component:
    return rx.link(
          rx.vstack(
            rx.image(
                    src=item.image,
                    border_radius= Size.DEFAULT.value
                ),
                rx.text(
                    item.title,
                    style=button_body_style
                ),
                spacing="4",
                align_items="start"
            ),
            href=item.url,
            is_external=True,
            
    )