"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from link_bio.styles.styles import *
import link_bio.constanst as const
from link_bio.pages.index import index
from link_bio.pages.courses import courses
# class State(rx.state):
#     pass


app = rx.App(
    style=BASE_STYLE
)
# app.add_page(index,title="practicando reflex with AliDev",description="hola, mi nombre es Ali Guerrero. soy ingeniero de software",image="logo.jpg")


# app = rx.App(
#     stylesheets=STYLESHEETS,
#     style=BASE_STYLE,
#     head_components=[
#         rx.script(
#             src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
#         rx.script(
#             f"""
# window.dataLayer = window.dataLayer || [];
# function gtag(){{dataLayer.push(arguments);}}
# gtag('js', new Date());
# gtag('config', '{const.G_TAG}');
# """
#         ),
#     ],
# )
