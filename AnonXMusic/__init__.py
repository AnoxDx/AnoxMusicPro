from WtfAno.core.bot import Anony
from WtfAno.core.dir import dirr
from WtfAno.core.git import git
from WtfAno.core.userbot import Userbot
from WtfAno.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
