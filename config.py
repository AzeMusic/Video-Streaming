import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env")
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "tenha055")
ALIVE_NAME = getenv("ALIVE_NAME", "Pistoncu AĞA")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "SOQrup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ledyplaylist")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b3ff4cfca14c4e47fdf72.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AzeMusic/Video-Streaming")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/e877179fe18a04192a00a.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/74d45f53fc287e9c316d1.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/54fe4851c51bfd440fcb6.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/059fc2fbad833b5c266f9.jpg")

# Don't Change It Bro ❣️ 😂


MY_SERVER = getenv("MY_SERVER", "SOQrup")
REPO_OWNER = getenv("REPO_OWNER", "tenha055")
MY_HEART = getenv("MY_HEART", "ruzgar_alican")
BOT_UPDATE = getenv("BOT_UPDATE", "ledyplaylist")
MY_BRO = getenv("MY_BRO", "HarshitSharma361")
