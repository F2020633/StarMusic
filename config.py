# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 |
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12394287"))
API_HASH = getenv("API_HASH", "adf9d0f1457cbe17c24576432b38c476
")
BOT_TOKEN = getenv("BOT_TOKEN", "5678409854:AAG8C9OAqmHpEO8s4AlYBuSZAHSimUmqgEw")
OWNER_USERNAME = getenv("OWNER_USERNAME", "t.me/yerigetdeeeee")
BOT_USERNAME = getenv("BOT_USERNAME", "KazimovaMusicBot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DKbteam")
BOT_NAME = getenv("BOT_NAME","KazimovaMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
SESSION_NAME = getenv("SESSION_NAME", "KazimovaMusicAsisstant")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5237976814").split()))
