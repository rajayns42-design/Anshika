# config.py
import os

# -------- BASIC --------
BOT_NAME = os.getenv("BOT_NAME", "Anshika")
OWNER_ID = int(os.getenv("OWNER_ID", 0))

# -------- API --------
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MODEL = os.getenv("MODEL", "mistral-free-latest")

# -------- DATABASE --------
MONGO_URL = os.getenv("MONGO_URL")

# -------- LOGGING --------
LOGGER_GROUP = int(os.getenv("LOGGER_GROUP", 0))

# -------- SUPPORT --------
SUPPORT_GROUP = int(os.getenv("SUPPORT_GROUP", 0))
SUPPORT_CHANNEL = int(os.getenv("SUPPORT_CHANNEL", 0))

# -------- PAYMENTS --------
UPI_ID = os.getenv("UPI_ID")

# -------- LIMITS --------
MAX_HISTORY = int(os.getenv("MAX_HISTORY", 10))
SPAM_LIMIT = int(os.getenv("SPAM_LIMIT", 6))
SPAM_WINDOW = int(os.getenv("SPAM_WINDOW", 10))
ABUSE_WARN_LIMIT = int(os.getenv("ABUSE_WARN_LIMIT", 2))
MUTE_SECONDS = int(os.getenv("MUTE_SECONDS", 120))
BREAKUP_COOLDOWN = int(os.getenv("BREAKUP_COOLDOWN", 3600))
PROPOSAL_XP = int(os.getenv("PROPOSAL_XP", 650))
