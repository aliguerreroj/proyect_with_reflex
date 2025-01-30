import reflex as rx
from link_bio.components.link_buttons import link_buttons
from link_bio.components.tittle import title
from link_bio.styles.styles import Size
from link_bio.constanst import EMAIL
from link_bio.routes import Route



def index_links()->rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_buttons(
            icon="code-xml",
        title="Cursos Gratis",
        body="tutoriales para aprender programacion",
        url=Route.COURSES.value,
        is_external=False,
        ),
    
        link_buttons(
            icon="twitch",
        title="Twich",
        body="Directos de Lunes a Viernes",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),
        link_buttons(
            icon="cable",
        title="Discord",
        body="Chat de la comunidad",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),

        link_buttons(
            icon="youtube",
        title="Youtube",
        body="Mi canal de Youtube",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),
        link_buttons(
            icon="instagram",
        title="Instagram",
        body="Mi cuenta de Instagram",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),

                title("Comunidad"),
        link_buttons(
            icon="twitch",
        title="Twich",
        body="Directos de Lunes a Viernes",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),
        link_buttons(
            icon="youtube",
        title="Youtube",
        body="Mi canal de Youtube",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),
        link_buttons(
            icon="instagram",
        title="Instagram",
        body="Mi cuenta de Instagram",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),
        link_buttons(
            icon="cable",
        title="Discord",
        body="Chat de la comunidad",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),

        title("Contacto"),

        link_buttons(
        icon="cable",
        title="MyPublicInbox",
        body="respuesta rapida y con preferencia",
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),
        link_buttons(
        icon="cable",
        title="Email",
        body=EMAIL,
        url="https://www.youtube.com/watch?v=n2YrGsXJC6Y&list=PLNdFk2_brsRdgQXLIlKBXQDeRf3qvXVU_&index=7"),

        max_width="600px",
        width="100%",
        spacing="4"
        # align="center",
        )
 