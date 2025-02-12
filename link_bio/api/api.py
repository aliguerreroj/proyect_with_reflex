from link_bio.api.twitchApi import TwitchAPI
from link_bio.api.SupabaseAPI import SuperBaseAPI
from link_bio.api.ConfigCat import ConfigCatAPI
from link_bio.model.live import Live
from link_bio.model.featured import Featured

TWTCH_API= TwitchAPI()
SUPABASE_API=SuperBaseAPI()
CONFIGCAT_API=ConfigCatAPI()

async def repo() -> str:
    return "https://github.com/aliguerreroj/proyect_with_reflex"

async def live(user:str) -> bool:
    if user == "alidev":
        return True
    return False
# async def live(user:str) -> Live:
#     return TWTCH_API.live(user)


# esto ya no 
# async def live(user:str) -> dict:
#     return TWTCH_API.live(user)

async def featured() -> list[Featured]:
    return SUPABASE_API.featured()

async def schedule() -> dict:
    return await  CONFIGCAT_API.schedule()