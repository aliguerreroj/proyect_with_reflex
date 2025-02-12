import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size,TextColor,Color
from link_bio.components.link_buttons_image import link_buttons_image
from link_bio.constanst import GITHUB_URL,TWITTER_X_URL,INSTAGRAM_URL,TIKTOK_URL,SPOTIFY_URL,LINKEDIN_URL
# from link_bio.assets
from datetime import date
from link_bio.state.PageState import PageState
from link_bio.model.live import Live
def my_experencia():
    inicio = date.fromisoformat("2023-01-01")
    hoy = date.today()
    experiencia = hoy.year - inicio.year
    if (hoy.month, hoy.day) < (inicio.month, inicio.day):
        experiencia -= 1
    
    return experiencia

# css_file = "/css/styles.css"

# def header(details:True, live=Live(live=False,title=""))->rx.Component:
def header(details:True)->rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.box(
                rx.cond(
                    PageState.is_live,
                    # live_status.live,
                    rx.link(
                        rx.image(
                            src="/icons/twitch.svg",
                            height=Size.DEFAULT.value,
                            width=Size.DEFAULT.value
                        ),
                        href="https://github.com/aliguerreroj/proyect_with_reflex",
                        is_external=True,
                        class_name="blink",
                        border_radius="50%",
                        padding=Size.MEDIUM.value,
                        bg=Color.PURPLE.value,
                        position="fixed",
                        bottom="0",
                        right="0",
                        margin=Size.BIG.value
                        ),
                    ),
            # rx.avatar(src="/batman.avif", fallback="RU", size="9"),
                    rx.avatar(
                        src="/batman0.jpg",
                        fallback="AG",
                        radius="full",
                        size="7",
                        border=f"4px solid {Color.SECONDARY.value}",
                        color_scheme="gray",
                        variant="soft",
                        
                        high_contrast=True 
                        ),
                    ),
            rx.vstack(
            rx.heading("ALI GUERRERO", color_scheme="gray",size="6",color=TextColor.HEADER.value),
            rx.text("@Ali_Guerrero_Dev", weight="bold", size="2",color=TextColor.BODY.value),
            rx.hstack(
                link_icon(
                    icon="twitch",
                    url=GITHUB_URL),
                link_icon(
                    icon="youtube",
                    url=TWITTER_X_URL),
                link_icon(
                    icon="instagram",
                    url=INSTAGRAM_URL),
                link_icon(
                    icon="twitter",
                    url=TIKTOK_URL),
                link_icon(
                    icon="rss",
                    url=SPOTIFY_URL),
                link_icon(
                    icon="facebook",
                    url=LINKEDIN_URL),
            ),
            gap="0",
            margin_y="0px",
            align_items="start",
            # spacing="1",
            # height="100%",
            # width="100%"
            ),
            spacing="4",

            # align_self="center"
            # justify="center"
            ),
            rx.cond(
                details,
                rx.vstack(
                    rx.flex(
                        info_text(f"+{my_experencia()}","años de experiencia"),
                        rx.spacer(),
                        info_text(f"+10","aplicaciones desarroladas"),
                        rx.spacer(),
                        info_text(f"+1M","seguidores"),
                        width="100%",
                            ),
                            rx.cond(
                                PageState.is_live,
                                # live_status.live,
                                link_buttons_image(
                                    "En directo",
                                    # "en vivo",
                                    PageState.live_title,
                                    # live_status.title,
                                    "/icons/twitch.svg",
                                    url="https://github.com/aliguerreroj/proyect_with_reflex",
                                    # highlight=True
                                    highlight_color=Color.PURPLE.value,
                                    animated=True
                                ),
                            ),
                            rx.box(
                             rx.cond(
                                    PageState.next_live,
                                    # next_live,
                                        link_buttons_image(
                                        "Proximo directo",

                                        PageState.next_live,
                                        
                                        "/icons/twitch.svg",
                                        url="https://github.com/aliguerreroj/proyect_with_reflex",
                                        
                                        highlight_color=Color.PURPLE.value,
                                        animated=True
                                    ),

                                ),
                                width="100%",
                                on_mount=PageState.check_schedule
                                ),
                            
                        rx.text("Soy ingeniero de software desde hace mas de 6 meses. Actualmente estoy estudiando para ser senior en python",      
                                color=TextColor.BODY.value,
                                font_size=Size.DEFAULT.value,
                                ),
                                width="100%",
                                spacing="5",
                        ),
                ),
            padding_left=Size.DEFAULT.value,



            
            # gap="0",
            # gap=Size.BIG.value,
  

        ),
            spacing="5",
            align_items="start",
            margin_top=Size.VERY_BIG.value,
            max_width="600px",
            width="100%"
        )


#  icon="twitch",
# icon="youtube",
# icon="instagram",
# icon="cable",
# icon="rss",
# icon="twitter",