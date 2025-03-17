import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "29728878"))
  API_HASH = os.environ.get("API_HASH", "a961168f7807061e77e1fb39c3f6ef71")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Gdhffsfjbot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002480353700"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "softurl.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "cb6243bee96a21ea399e214f1484a7de4652edc9")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "YaduvanshiXD"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sushankm16:411WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002190750585")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002168042476"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
├🔹 Hosted On: [Heroku](https://heroku.com)
│
├🔸 Developer: [𝗬𝗮𝗱𝘂𝘃𝗮𝗻𝘀𝗵𝗶](https://t.me/YaduvanshiXD) 
│
├🔹 Bot Support: [Support Group](https://t.me/YaduvanshiXsupport)
│
├🔸 Bot Updates: [Bots Channel](https://t.me/YaduvanshiXbotz)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [𝗬𝗮𝗱𝘂𝘃𝗮𝗻𝘀𝗵𝗶](https://telegram.me/YaduvanshiXD)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/YaduvanshiXbotz)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
