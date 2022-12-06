import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("5908115020:AAGrQDdGYL3vb73rP6T9hNH7BvgwrbBgp2g")
BOT_NAME = getenv("ergilbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MusicBotErgil")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/7abb8a949cd72fe1af04a.png")
admins = {}
API_ID = int(getenv("28452250", ""))
API_HASH = getenv("cf0bea99c8e706d8d7341aa37c5234c8")
BOT_USERNAME = getenv("ErgilMusic")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ErgilGemoy")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ErgilMusic")
PROJECT_NAME = getenv("PROJECT_NAME", "ErgilMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Ergilgge")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
