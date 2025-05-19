import discord
from discord.ext import commands
import wavelink

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.start_lavalink())

    async def start_lavalink(self):
        await self.bot.wait_until_ready()

        await wavelink.Pool.connect(
            client=self.bot,
            nodes=[
                wavelink.Node(
                    uri="https://lavalink.corsariobot.xyz:443",
                    password="youshallnotpass"
                )
            ]
        )

@commands.Cog.listener()
async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload):
    print(f"Node {payload.node.identifier} está pronto!")


    @commands.command()
    async def play(self, ctx, *, search: str):
        if not ctx.author.voice or not ctx.author.voice.channel:
            return await ctx.send("Você precisa estar em um canal de voz.")
        
        channel = ctx.author.voice.channel
        vc: wavelink.Player = await channel.connect(cls=wavelink.Player) if not ctx.voice_client else ctx.voice_client

        track = await wavelink.YouTubeTrack.search(search, return_first=True)
        await vc.play(track)
        await ctx.send(f"Tocando: {track.title}")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Saí do canal de voz.")

async def setup(bot):
    await bot.add_cog(Music(bot))
