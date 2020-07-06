from dotenv import load_dotenv
import os
load_dotenv()


def get_youtube_api_key():
    return os.getenv("YOUTUBE_TOKEN")


def get_discord_key():
    return os.getenv("DISCORD_TOKEN")
