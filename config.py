import os
import sys
import logging

DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")
GUILD_ID = os.getenv("DISCORD_GUILD")

# VALIDATE IMPORTANT VARIABLE
if not DISCORD_API_KEY or not GUILD_ID:
    logging.critical("DISCORD_API_KEY or DISCORD_GUILD not set!")
    sys.exit(1)

guild_id_str = os.getenv("DISCORD_GUILD","0")
guild_id_list = guild_id_str.split(",")
GUILD_ID = []
for id in guild_id_list:
    guild_id_int = int(id)
    GUILD_ID.append(guild_id_int)

ENABLE_GLOBAL = bool(os.getenv("ENABLE_GLOBAL"))

# --- GEMINI CONFIGURATION ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_INSTRUCTION = os.getenv("GEMINI_GLOBAL_INSTRUCTION")

ENABLE_CHATBOT = False #bool(GEMINI_API_KEY)

# --- LAVALINK CONFIGURATION ---
LAVALINK_HOST = os.getenv("LAVALINK_HOST")
LAVALINK_PORT = os.getenv("LAVALINK_PORT")
LAVALINK_PASS = os.getenv("LAVALINK_PASSWORD")

ENABLE_MUSIC = all([LAVALINK_HOST, LAVALINK_PORT, LAVALINK_PASS])