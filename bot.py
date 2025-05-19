
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.music")

intents = discord.Intents.all()
bot = MyBot(command_prefix="!", intents=intents)

bot.run(os.getenv("DISCORD_TOKEN"))
