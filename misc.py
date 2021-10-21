import discord
from discord.ext import commands
import asyncio


class Misc(commands.Cog):
    # mini games

    def __init__(self, client):
        self.client = client

    @commands.command(category='Ping', help='Displays bot latency')
    async def ping(self, ctx):
        await ctx.reply(f'Latency? Hah what a joke i am faster than light.. anyways this is my ping {round(self.client.latency * 1000)}ms')

    
    
    @commands.Cog.listener()
    async def on_message_delete(self,message):
        self.client.sniped_messages = {}
        if message.attachments:
            bob = message.attachments[0]
            self.client.sniped_messages[message.guild.id] = (bob.proxy_url, message.content, message.author, message.channel.name, message.created_at)
        else:
            self.client.sniped_messages[message.guild.id] = (message.content,message.author, message.channel.name, message.created_at)

    @commands.command()
    async def snipe(self,ctx):
        try:
            bob_proxy_url, contents,author, channel_name, time = self.client.sniped_messages[ctx.guild.id]
        except:
            contents,author, channel_name, time = self.client.sniped_messages[ctx.guild.id]
        try:
            embed = discord.Embed(description=contents , color=discord.Color.purple(), timestamp=time)
            embed.set_image(url=bob_proxy_url)
            embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
            embed.set_footer(text=f"Deleted in : #{channel_name}")
            await ctx.channel.send(embed=embed)
        except:
            embed = discord.Embed(description=contents , color=discord.Color.purple(), timestamp=time)
            embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
            embed.set_footer(text=f"Deleted in : #{channel_name}")
            await ctx.channel.send(embed=embed)
        

def setup(client):
    client.add_cog(Misc(client))