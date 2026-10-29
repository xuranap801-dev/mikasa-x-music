import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


def _env(name, default=None):
    value = os.getenv(name)
    return value.strip() if value and value.strip() else default


def _int_env(name, default=None):
    value = _env(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError as exc:
        raise SystemExit(f"[ERROR] {name} must be an integer") from exc


API_ID = _int_env("API_ID")
API_HASH = _env("API_HASH")
BOT_TOKEN = _env("BOT_TOKEN")
OWNER_ID = _int_env("OWNER_ID")
OWNER_USERNAME = _env("OWNER_USERNAME")
BOT_NAME = _env("BOT_NAME", "Mikasa x Musix")
BOT_USERNAME = _env("BOT_USERNAME")
MONGO_DB_URI = _env("MONGO_DB_URI")
LOG_GROUP_ID = _int_env("LOG_GROUP_ID")
HEROKU_APP_NAME = _env("HEROKU_APP_NAME")
HEROKU_API_KEY = _env("HEROKU_API_KEY")
UPSTREAM_REPO = _env("UPSTREAM_REPO")
UPSTREAM_BRANCH = _env("UPSTREAM_BRANCH", "main")
GIT_TOKEN = _env("GIT_TOKEN")
SUPPORT_CHANNEL = _env("SUPPORT_CHANNEL")
SUPPORT_GROUP = _env("SUPPORT_GROUP")
INSTAGRAM = _env("INSTAGRAM")
YOUTUBE = _env("YOUTUBE")
GITHUB = _env("GITHUB")
DONATE = _env("DONATE")
PRIVACY_LINK = _env("PRIVACY_LINK")
DURATION_LIMIT_MIN = _int_env("DURATION_LIMIT", 300)
PLAYLIST_FETCH_LIMIT = _int_env("PLAYLIST_FETCH_LIMIT", 25)
TG_AUDIO_FILESIZE_LIMIT = _int_env("TG_AUDIO_FILESIZE_LIMIT", 104857600)
TG_VIDEO_FILESIZE_LIMIT = _int_env("TG_VIDEO_FILESIZE_LIMIT", 2145386496)
SPOTIFY_CLIENT_ID = _env("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = _env("SPOTIFY_CLIENT_SECRET")
STRING1 = _env("STRING_SESSION")
STRING2 = _env("STRING_SESSION2")
STRING3 = _env("STRING_SESSION3")
STRING4 = _env("STRING_SESSION4")
STRING5 = _env("STRING_SESSION5")
AUTO_LEAVING_ASSISTANT = _env("AUTO_LEAVING_ASSISTANT", "false").lower() in {"1", "true", "yes", "on"}
START_IMG_URL = _env("START_IMG_URL")
PING_IMG_URL = _env("PING_IMG_URL", START_IMG_URL)
PLAYLIST_IMG_URL = _env("PLAYLIST_IMG_URL", START_IMG_URL)
STATS_IMG_URL = _env("STATS_IMG_URL", START_IMG_URL)
TELEGRAM_AUDIO_URL = _env("TELEGRAM_AUDIO_URL", START_IMG_URL)
TELEGRAM_VIDEO_URL = _env("TELEGRAM_VIDEO_URL", START_IMG_URL)
STREAM_IMG_URL = _env("STREAM_IMG_URL", START_IMG_URL)
SOUNCLOUD_IMG_URL = _env("SOUNCLOUD_IMG_URL", START_IMG_URL)
YOUTUBE_IMG_URL = _env("YOUTUBE_IMG_URL", START_IMG_URL)
SPOTIFY_ARTIST_IMG_URL = _env("SPOTIFY_ARTIST_IMG_URL", START_IMG_URL)
SPOTIFY_ALBUM_IMG_URL = _env("SPOTIFY_ALBUM_IMG_URL", START_IMG_URL)
SPOTIFY_PLAYLIST_IMG_URL = _env("SPOTIFY_PLAYLIST_IMG_URL", START_IMG_URL)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
TEMP_DB_FOLDER = "tempdb"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ERROR_FORMAT = 0

for name, value in (("SUPPORT_CHANNEL", SUPPORT_CHANNEL), ("SUPPORT_GROUP", SUPPORT_GROUP)):
    if value and not re.match(r"(?:http|https)://", value):
        raise SystemExit(f"[ERROR] - {name} URL must start with https://")
