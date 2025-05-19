import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.music")

intents = discord.Intents.all()
bot = MyBot(command_prefix="!", intents=intents)

async def main():
    async with bot:
        await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
