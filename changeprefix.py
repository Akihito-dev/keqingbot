import discord
import json
from discord.ext import commands

class ChangePrefix(commands.Cog):
  def __init__(self,client):
    self.client = client

  def get_prefix(self,client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    return prefixes[str(message.guild.id)]

  # change prefix


  @commands.Cog.listener()
  async def on_guild_join(self,guild):
      with open('prefixes.json', 'r') as f:
          prefixes = json.load(f)

      prefixes[str(guild.id)] = '.'

      with open('prefixes.json', 'w') as f:
          json.dump(prefixes, f, indent=5)


  @commands.Cog.listener()
  async def on_guild_remove(self,guild):
      with open('prefixes.json', 'r') as f:
          prefixes = json.load(f)

      prefixes.pop(str(guild.id))

      with open('prefixes.json', 'w') as f:
          json.dump(prefixes, f, indent=5)


  @commands.command()
  async def changeprefix(self,ctx, prefix):
      with open('prefixes.json', 'r') as f:
          prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = prefix

      with open('prefixes.json', 'w') as f:
          json.dump(prefixes, f, indent=5)
      
      await ctx.reply(f'Prefix changed to: {prefix}')

def setup(client):
  client.add_cog(ChangePrefix(client))