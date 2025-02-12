import reflex as rx
from link_bio.components.link_buttons import link_buttons
from link_bio.components.tittle import title
from link_bio.components.featured_link import featured_link
from link_bio.styles.styles import Size
from link_bio.constanst import EMAIL
from link_bio.routes import Route
from link_bio.styles.colors import Color
from link_bio.model.featured import Featured
from link_bio.state.PageState import PageState



def index_links(featured:list[Featured])->rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_buttons(
            icon="code-xml",
            title="Cursos Gratis",
            body="tutoriales para aprender programacion",
            url=Route.COURSES.value,
            is_external=False,
            highlight_color= Color.SECONDARY.value
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



        rx.cond(
            featured,
            rx.vstack(
                title("Destacados"),
                rx.grid(
                rx.foreach(
                    featured,
                    featured_link
                    ),
                columns=rx.breakpoints(initial="1", sm="2", lg="2")
                ),
                on_mount=PageState.featured_links,
                spacing="4"
                # rx.foreach(
                #     featured,
                #     lambda item: rx.grid(
                        # rx.link(
                        #     rx.image(
                        #         item["image"]
                        #     ),
                        #     rx.text(
                        #         item["title"]
                        #     ),
                        #     href=item["url"],
                        #     is_external=True
                        # ),
                    # ),
                # ),
            ),

        ),



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
 