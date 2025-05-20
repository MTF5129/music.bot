import discord
from discord.ext import commands
import os
import asyncio

class MyBot(commands.Bot):
    async def setup_hook(self):
        print("DEBUG: setup_hook iniciado")
        await self.load_extension("cogs.music")

intents = discord.Intents.all()
bot = MyBot(command_prefix="!", intents=intents)

async def main():
    print("DEBUG: Iniciando main() do bot.")
    async with bot:
        await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
