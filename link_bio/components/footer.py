import reflex as rx
import datetime
from link_bio.styles.styles import Size,TextColor,Color
import link_bio.constanst as const
def footer()->rx.Component:
    return rx.vstack(
        rx.image(
            src="/batman.avif",
        #     width="50px", 
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            ),
        rx.link(
                f"© 2023-{datetime.datetime.today().year} ALIDEV by Ali Guerrero v1.",
                href="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7",
                is_external=True,
                font_size=Size.MEDIUM.value,
                margin_top=Size.DEFAULT.value,
                ),
        
            rx.link(
                rx.hstack(
                rx.image(
                    src="/icons/github2.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.SMALL.value,
                    ),
                    ),
                href=const.GITHUB_URL,
                is_external=True,
                color=TextColor.BODY.value
                
            ),
        
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        align="center",
        color=TextColor.FOOTER.value,
        padding_left=Size.MEDIUM.value,
        spacing="0"

        # max_width="600px",
    )
    