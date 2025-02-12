import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header import header
from link_bio.views.index_links import index_links
from link_bio.views.sponsors import sponsor
from link_bio.components.footer import footer
from link_bio.styles.styles import *
from link_bio.routes import Route
from link_bio.api.api import live
from link_bio.state.PageState import PageState
import link_bio.constanst as const
import link_bio.utils as utils



@rx.page(
        route=Route.INDEX.value, 
        image="python_highlighted.png",
        title=utils.index_title,
        description=utils.index_description,
        meta=utils.index_meta,
        on_load=[PageState.check_live, PageState.featured_links]
        )
def index()->rx.Component:
    return rx.box(
        utils.lang(),
        rx.hstack(
        navbar(),

        ),
        rx.center(
        rx.vstack(
        header(
            details=True, 
            # live=PageState.is_live,
            # live_title= PageState.live_title,
            # next_live=PageState.next_live
            # live=PageState.live_status   ahora solo deveria ir esto 
            # live=PageState.is_live,
            
            ),
        index_links(PageState.featured_info),
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
        # padding=Size.BIG.value,
        # margin_y=Size.BIG.value,
        width="100%",
 
        
        # background_color="white"
    ),
    
# app = rx.App(
#     style=BASE_STYLE
# )