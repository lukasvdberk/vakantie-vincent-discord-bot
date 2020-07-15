import discord
from video import send_random_video, get_random_video


class VakantieVincentDiscordClient(discord.Client):
    bot_command = "!ikwilvincent"

    async def on_ready(self):
        await send_random_video(self)
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        if message.content == self.bot_command:
            await message.channel.send(get_random_video())
