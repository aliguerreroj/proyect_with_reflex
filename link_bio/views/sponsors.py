import reflex as rx
from link_bio.components.tittle import title
# from link_bio.styles.styles import Size,TextColor,Color
from link_bio.components.link_sponsor import link_sponsor
import link_bio.constanst as const
def sponsor()->rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.grid(
            link_sponsor(
                "/elgato.png",
                const.ELGATO_URL,
                alt="logotipo del gato"
            ),
            link_sponsor(
                "/mvp.png",
                const.MVP_URL,
                alt="logotipo de Microsoft MBP"
            ),
            link_sponsor(
                "/githubstar.png",
                const.GITHUB_STAR_URL,
                alt="logotipo de GitHub Star"
            ),
            columns=rx.breakpoints(initial="1", sm="2", lg="3"),
            spacing="8"
        ),
        max_width="600px",
        width="100%",
        align_items="start",
        spacing="5"
    )