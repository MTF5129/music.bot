import os
import discord
from discord.ext import commands
import wavelink

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        await self.bot.wait_until_ready()
        await wavelink.NodePool.create_node(
            bot=self.bot,
            host=os.getenv('LAVALINK_HOST'),
            port=int(os.getenv('LAVALINK_PORT')),
            password=os.getenv('LAVALINK_PASSWORD'),
            region='us_central'
        )

    @commands.command()
    async def play(self, ctx, *, search: str):
        if not ctx.author.voice or not ctx.author.voice.channel:
            return await ctx.send("Você precisa estar em um canal de voz para usar este comando.")

        channel = ctx.author.voice.channel

        if not ctx.voice_client:
            vc: wavelink.Player = await channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        track = await wavelink.YouTubeTrack.search(search, return_first=True)
        await vc.play(track)
        await ctx.send(f"Tocando: {track.title}")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Desconectado do canal de voz.")

async def setup(bot):
    await bot.add_cog(Music(bot))