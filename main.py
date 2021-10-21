import discord
from discord.ext import commands, tasks
import json
from itertools import cycle
import asyncio

import music
import moderation
import calc
import fun
import changeprefix
import join_leave
import misc 
import keqingmainsguides

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


cogs = [moderation, calc, fun, changeprefix, join_leave, music,misc,keqingmainsguides]


games = ["Genshin Impact", '.help', 'with aki']
client = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())
status = cycle(games)


class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(color=discord.Color.purple(), description='')
        embed.set_footer(icon_url='https://cdn.discordapp.com/attachments/772334064849649695/864518818798108672/130256173_196916332044367_1228585580782993887_n.png',
                         text='This is my help page  o(￣┰￣*)ゞ ')
        for page in self.paginator.pages:
            embed.description += page
        await destination.send(embed=embed)


client.help_command = MyHelpCommand()


for i in range(len(cogs)):
    cogs[i].setup(client)



# bot online


@client.event
async def on_ready():
    change_status.start()
    print(f'{client.user.name} is online')


@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))


# bot token
client.run('')
