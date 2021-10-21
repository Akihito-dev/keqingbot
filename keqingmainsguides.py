import discord
from discord.ext import commands


class Guides(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help="Eg- .guide keqing")
    async def guides(self, ctx, character):
        guide = f'https://keqingmains.com/{character}/'

        await ctx.reply(guide)


def setup(client):
    client.add_cog(Guides(client))
