import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "19408128"))
    API_HASH = os.environ.get("API_HASH", "8c49afc538bd4e2029e32adfc1a0cacc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5435067066:AAG1m7pDl5asLhAonpS1rcNwWHvyUwYV7HQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHgBu07-Y0KQmqjpd7m6xZz5rIHO_MYLIAhH-9Oi8kZdm0qck5nmt-n3Ah0CXIY1TbbLWvv6O3GgBxT7aDmSIOTDZ5iC5fFxcKhAptj5JCIAPnmibGWzvQY7RkVII6YZcIkNl17yygPkps7ZDv-aLuZ53h-IZh5pBRx0qCkf8rc2VHpGbN7PGskejVTdohaK-8OmvF8wBAAY0adtZ75yy1UCwG0KgP-wB5vJeiC5qk9zKQJ0eN-OOL4UMwoe7Q3KIHHetzV2GRgyUD_L6S8xv7Tr4Q4nNH4Tkwa3y9p-Ew_mQyW8mNSAESXix6_myws865Lg2kqMX7ssd1-PI7Fastmb2UM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Tgm_Drugs_Of_Yuvan_bot")
    SUPPORT = os.environ.get("SUPPORT", "throwpathidpworld") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Alinallmovies") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/e2021dfd84a80c17cfff8.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/3f0c65d3899e9985eb202.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5373395703")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True" #optional
