from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "26954495"))
API_HASH = environ.get("API_HASH", "2061c55207cfee4f106ff0dc331fe3d9")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7045947967")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002608186529")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://nitishraj66770:nitishraj66770@cluster0.u2jbx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
