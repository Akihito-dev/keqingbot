import discord
from discord.ext import commands
import random
import asyncpraw
import os
import random
import asyncio
import datetime
import keqingimages


class Fun(commands.Cog):
    # mini games

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['red', 'reddit'], help="using .meme will default the subreddit to r/memes however you can use any subreddit of your choosing. Eg: .meme animemes")
    async def meme(self, ctx, subred="memes"):

        reddit = asyncpraw.Reddit(client_id="",
                                  client_secret='',
                                  username='',
                                  password='',
                                  user_agent="")

        subreddit = await reddit.subreddit(subred)
        all_subs = []

        async for submission in subreddit.hot(limit=50):
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title=name)
        embed.set_image(url=url)
        embed.set_footer(icon_url='https://cdn.discordapp.com/attachments/772334064849649695/864516800113147924/E4GxMs_WYAAbnbL.jpg',
                         text=f'Was that funny? No? ok')
        await ctx.reply(embed=embed)

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['nope',
                     'yes',
                     'maybe',
                     'humu~ humu~']
        await ctx.reply(f'Question: {question} \nAnswer: {random.choice(responses)}')

    @commands.command(aliases=['choose'])
    async def choice(self, ctx, *, choice):
        choices = choice.split()
        await ctx.reply(random.choice(choices))

        await ctx.reply()

    @commands.command()
    async def say(self, ctx, *, message,):

        await ctx.message.delete()  # delete this if it dont work
        await ctx.send(f'{message}')

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Please tell mew what to say .·´¯\`(>▂<)´¯`·. ")

    @commands.command(aliases=['keqpic'])
    async def keqingpic(self, ctx):
        embed = discord.Embed(color=discord.Colour.purple())
        random_link = random.choice(keqingimages.images)
        embed.set_image(url=random_link)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def remind(self, ctx, time: int, unit, *, reminder):
        await ctx.send("Reminder started")

        def check(message):
            return message.channel == ctx.channel and message.author == ctx.author and message.content.lower() == "cancel"
        try:
            m = await self.client.wait_for("message", check=check, timeout=time)
            await ctx.send("Reminder cancelled")
        except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author.mention} you had a reminder saying - {reminder}")

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url
        embed = discord.Embed(color=discord.Colour.purple())
        embed.set_image(url=userAvatar)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Fun(client))
