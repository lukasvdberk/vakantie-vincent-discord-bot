from dotenv import load_dotenv
from src.client import VakantieVincentDiscordClient
from src.keys import get_discord_key

# NOTE
# before running this script create a file called .env with your DISCORD_TOKEN in it

# krijg video op commando
# stuur elke 24 uur een nieuwe video (houd bij in bestand ofzo


if __name__ == "__main__":
    print("starting bot")
    load_dotenv()

    print(get_discord_key())
    client = VakantieVincentDiscordClient()
    client.run(get_discord_key())


