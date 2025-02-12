import reflex as rx
import pytz
from datetime import datetime, timedelta, timezone


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

# Date 

# calcula la proxima decha  del live 





LOCAL_TIMEZONE_SCRIPT = "Intl.DateTimeFormat().resolvedOptions().timeZone"

WEEKDAYS = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

MONTHS = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

# def next_date(dates: dict) -> str:
#     if dates is None or len(dates) == 0:  # Verifica si dates es None o está vacío
#         return ""
    
#     now = datetime.now()
#     current_weekday = now.weekday()
#     current_time = now.astimezone().timetz()
    
#     for index in range(7):
#         day = str((current_weekday + index) % 7)

#         if day not in dates or dates[day] == "":
#             continue

#         time_utc = datetime.strptime(
#             dates[day],
#             "%H:%M"  # Corregí el formato de la hora
#         ).replace(tzinfo=timezone.utc).timetz()

#         time = datetime.combine(now.date(), time_utc).astimezone().timetz()

#         if current_time < time or index > 0:
#             next_date = now + timedelta(days=index)

#             format_next_day = next_date.strftime(
#                 "Hoy, %d/%m" if index == 0 else next_date.strftime("%A, %d/%m")
#             )
#             format_next_time = time_utc.strftime("%H:%M")

#             return f"{format_next_day} a las {format_next_time} ({dates[day]})"

#     return ""


def next_date(dates: dict, timezone: str) -> str:

    if len(dates) == 0:
        return ""

    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    current_time = now.timetz()

    for weekday in range(7):

        current_weekday = str((now.weekday() + weekday) % 7)

        if current_weekday not in dates or dates[current_weekday] == "":
            continue

        time_utc = datetime.strptime(dates[current_weekday], "%H:%M").replace(
            tzinfo=pytz.UTC).timetz()

        next_time = datetime.combine(
            now.date(), time_utc).astimezone(tz).timetz()

        if current_time < next_time or weekday > 0:

            next_date = now + timedelta(days=weekday)

            local_date = datetime(
                next_date.year, next_date.month, next_date.day,
                time_utc.hour, time_utc.minute, tzinfo=pytz.UTC).astimezone(tz)

            day = "Hoy" if weekday == 0 else WEEKDAYS[local_date.weekday()]
            zones = timezone.replace('_', ' ').split('/')

            return local_date.strftime(
                f"{day}, %d de {MONTHS[local_date.month]} a las %H:%M | Zona horaria: {zones[len(zones) - 1]}")

    return ""