import reflex as rx

config = rx.Config(
    app_name="link_bio",
    # api_url="https://proyect-reflex.up.railway.app",
    cors_allowed_origins = [
        "http://localhost:3000",
        "https://proyect-reflex.up.railway.app"
    ]
)