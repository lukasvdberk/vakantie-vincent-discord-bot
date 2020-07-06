import discord
from src.send_video import send_random_video


class VakantieVincentDiscordClient(discord.Client):
    async def on_ready(self):
        await send_random_video(self)
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
