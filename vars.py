

from os import environ

API_ID = int(environ.get("API_ID", "21595709"))
API_HASH = environ.get("API_HASH", "6b683b86a90c6fae0fbe50a6494bdd53")
BOT_TOKEN = environ.get("BOT_TOKEN", "8919674457:AAFoqHcf-ywkOCxJJupfEenU2C0LC4hYEWU")

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "8032590813").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "7578460365"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





