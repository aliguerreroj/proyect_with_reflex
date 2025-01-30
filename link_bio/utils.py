import reflex as rx
# import pytz
from datetime import datetime, timedelta


# Común
preview = "https://moure.dev/preview.jpg"

# funcion para colocar como predeterminado el idioma español 
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"}
]




# Index

index_title = "practicando reflex with AliDev | praticamos programación y desarrollo de software"
index_description = "hola, mi nombre es Ali Guerrero. soy ingeniero de software."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)


# Cursos

courses_title = "MoureDev | Cursos gratis de programación"
courses_description = "Este es un listado con algunos cursos gratis para aprender programación y desarrollo de software. Python, SQL, Git..."

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)