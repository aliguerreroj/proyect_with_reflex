import reflex as rx
from link_bio.components.link_buttons_image import link_buttons_image
from link_bio.components.tittle import title
from link_bio.styles.styles import Size
from link_bio.constanst import EMAIL
from link_bio.routes import Route
import link_bio.constanst as const
from link_bio.styles.styles import Color
# from link_bio.components.newsletter import newsletter



def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_buttons_image(
            "Retos de programación",
            "Ruta de estudio semanal para practicar lógica",
            "/icons/challenges.png",
            const.CODE_CHALLENGES_URL,
            # highlight_color=Color.SECONDARY.value
        ),
        link_buttons_image(
            "JavaScript desde cero",
            "¡Nuevo! Curso en desarrollo",
            "/icons/js.svg",
            const.JS_COURSE_URL
        ),
        link_buttons_image(
            "Python desde cero",
            "Curso de +44h: Fundamentos, frontend, backend, testing...",
            "/icons/python.svg",
            const.PYTHON_COURSE_URL
        ),
        link_buttons_image(
            "Git y GitHub",
            "Curso de 5h para aprender Git y GitHub desde cero",
            "/icons/git.svg",
            const.GIT_COURSE_URL
        ),
        link_buttons_image(
            "SQL y Bases de Datos",
            "Curso de 7h desde cero para aprender los fundamentos de SQL",
            "/icons/sql.svg",
            const.SQL_COURSE_URL
        ),
        link_buttons_image(
            "Un día, un lenguaje",
            "Primeros pasos en los 11 lenguajes de programación más usados",
            "/icons/code.svg",
            const.LANGUAGES_COURSE_URL
        ),

        title("Mucho más en"),
        link_buttons_image(
            "Twitch",
            "Transmisiones sobre programación de lunes a viernes",
            "/icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_buttons_image(
            "YouTube",
            "Tutoriales sobre desarrollo de software semanales",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        link_buttons_image(
            "YouTube [canal secundario]",
            "Emisiones en directo destacadas",
            "/icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        # newsletter(),
        max_width="600px",
        width="100%",
        spacing="4"
    )
 