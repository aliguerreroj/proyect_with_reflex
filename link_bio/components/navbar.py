import reflex as rx
from link_bio.styles.styles import Size,Color,TextColor,navbar_tittle_style
from link_bio.routes import Route
from link_bio.components.ant_design import float_button
# from reflex_antd import navigation



def navbar()->rx.Component:
    return rx.hstack(
        rx.link(
        rx.box(
            "ali",
            rx.text(
                    "dev",color=Color.SECONDARY.value),
                    heigh=Size.BIG.value,
                    color=Color.PRIMARY.value,
                    style=navbar_tittle_style,
                    display="flex"
                    ),
                href=Route.INDEX.value
            ),
            # float_button(),
            position="sticky",
            top=0,
            z_index="999",
            bg=Color.CONTENT.value,
            padding_x=Size.DEFAULT.value,
            padding_y=Size.DEFAULT.value,
            width="100%"
        )
 