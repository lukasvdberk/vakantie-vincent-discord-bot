import discord
from video import send_random_video


class VakantieVincentDiscordClient(discord.Client):
    async def on_ready(self):
        await send_random_video(self)
        print('Logged on as {0}!'.format(self.user))
