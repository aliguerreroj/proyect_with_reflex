import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.courses_links import courses_links
from link_bio.views.sponsors import sponsor
from link_bio.components.footer import footer
from link_bio.styles.styles import *
from link_bio.routes import Route
import link_bio.constanst as const
import link_bio.utils as utils

# class State(rx.state):
#     pass

@rx.page(
        route=Route.COURSES.value, 
        image="python_highlighted.png",
        title=utils.index_title,
        description=utils.index_description)
def courses()->rx.Component:
    return rx.box(
        utils.lang(),
        rx.hstack(
        navbar(),

        ),
        rx.center(
        rx.vstack(
        
        header(details=False),
        courses_links(),
        # align="center",
        sponsor(),
        max_with=MAX_WIDTH,
        width="100%",
        align="center",
        margin_y=Size.BIG.value,
        padding=Size.BIG.value

        )),
        
        footer(),

        align="center",
        width="100%",
 
        
        # background_color="white"
    ),
    
# app = rx.App(
#     style=BASE_STYLE
# )