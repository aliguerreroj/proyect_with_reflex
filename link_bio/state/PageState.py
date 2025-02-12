import reflex as rx
from link_bio.api.api import live,featured,schedule
from link_bio.model.live import Live
from link_bio.model.featured import Featured
from link_bio.utils import next_date
from link_bio.api.ConfigCat import ConfigCatAPI
from link_bio.utils import LOCAL_TIMEZONE_SCRIPT,next_date
USER="alidevs"

class PageState(rx.State):
    # live_status=Live(live=False,title="")
    is_live:bool = False 
    live_title:str = ""
    featured_info:list[Featured]
    next_live:str= ""
    timezone=""


    async def check_live(self):
        self.is_live = await live(USER)  
        print(f"is_live: {self.is_live}")
        if self.is_live:
            self.next_live = ""  
        else:
            if not self.timezone:
                # Si no hay zona horaria, obtenerla
                self.check_schedule()
            else:
                # Si ya hay una zona horaria, calcular el próximo live
                schedule_data = await schedule()  
                print(f"Schedule data: {schedule_data}")
                self.next_live = next_date(schedule_data, self.timezone)  # Calcular el próximo live
                print(f"next_live: {self.next_live}") 


    def check_schedule(self):
        if self.timezone == "":
            # Si no hay zona horaria, obtenerla usando JavaScript
            return rx.call_script(
                LOCAL_TIMEZONE_SCRIPT,
                PageState.update_timezone
            )
        else:
            # Si ya hay una zona horaria, actualizar el próximo live
            self.update_timezone(self.timezone)

    async def update_timezone(self, timezone: str):
        self.timezone = timezone  # Actualizar la zona horaria
        schedule_data = await schedule()  # Obtener el horario de los lives
        self.next_live  = next_date(schedule_data, self.timezone)


    
    
    # esto ya no 
    # async def check_live(self):
    #     live_data= await live(USER)
    #     self.is_live=live_data["live"]
    #     self.live_tittle=live_data["title"]

    async def featured_links(self):
        self.featured_info = await featured()
        

