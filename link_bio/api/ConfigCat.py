import logging
import dotenv
import os
import configcatclient
import json


# Set the log level to INFO to track how your feature flags were evaluated. When moving to production, you can remove this line to avoid too detailed logging.
logging.basicConfig(level=logging.INFO)



# class ConfigCatAPI:

#     dotenv.load_dotenv()

#     CONFIGCAT_SDK_KEY = os.environ.get("CONFIGCAT_SDK_KEY")

#     def __init__(self) -> None:
#         if self.CONFIGCAT_SDK_KEY != None:
#             self.configcat = configcatclient.get(self.CONFIGCAT_SDK_KEY)

#     def schedule(self) -> dict:
#         response = self.configcat.get_value("live_schedule", "")
#         return json.loads(str(response))

class ConfigCatAPI:
    dotenv.load_dotenv()

    CONFIGCAT_SDK_KEY = os.environ.get("CONFIGCAT_SDK_KEY")
   
    def __init__(self) -> None:
        if self.CONFIGCAT_SDK_KEY is not None:
            self.configcat_client = configcatclient.get(self.CONFIGCAT_SDK_KEY)
        else:
            raise ValueError("CONFIGCAT_SDK_KEY no está configurado en las variables de entorno.")

    async def schedule(self) -> dict:  # Asegúrate de que sea async
        response = self.configcat_client.get_value("live_schedule", "")  # Si no está "live_schedule", retorna ""

        # Verifica si response es un diccionario (no necesitas json.loads)
        if isinstance(response, dict):
            return response

        # Si response es una cadena JSON, intenta cargarla
        if isinstance(response, str):
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                logging.error("La respuesta no es un JSON válido.")
                return {}

        # Si response es None o no es un tipo válido, retorna un diccionario vacío
        logging.warning("La respuesta no es un diccionario ni un JSON válido.")
        return {}