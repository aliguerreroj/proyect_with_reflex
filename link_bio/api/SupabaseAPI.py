import os
from supabase import create_client, Client
import dotenv
import requests
import time
from link_bio.model.featured import Featured

class SuperBaseAPI:
    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
    # supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


    def __init__(self)->None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client=None
            self.create_client()
    # def __init__(self)->None:
    #     self.supabase: Client=None
    #     self.create_client()

    def create_client(self):
        if self.supabase is None:
            self.supabase = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)


    def featured(self) -> list[Featured]:
        try:
            if self.supabase is None:
                self.create_client()

            response = self.supabase.table("featured").select("*").order("init_date",desc=True).limit(2).execute()
            # print("Datos obtenidos de la base de datos:", response.data)

            featured_list = [
                Featured(title=item["title"], image=item["image"], url=item["url"])
                for item in response.data
            ]
            # print(featured_list)
            return featured_list
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        # response = self.supabase.table("featured").select("*").execute()
        # featured_data = []
        # if len(response.data) > 0:
        #     for featured_item in response.data:
        #         featured_data.append(featured_item)
        # print(featured_data)

        # return featured_data
# miclase= SuperBaseAPI()
# datos= miclase.featured()


