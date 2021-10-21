import discord
from discord.ext import commands

class Join_Leave(commands.Cog):
  def __init__(self,client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_member_join(self,member):
    guild = member.guild
    true_member_count = len([m for m in guild.members if not m.bot])
    embed = discord.Embed(title=f'{member.name} joined {guild.name}',description=f'Welcome to {guild.name}, {member.name}. Make sure to get your reaction roles and read the rules! ',color = discord.Colour.purple())

    embed.set_image(url = 'https://cdn.discordapp.com/attachments/772334064849649695/864516754923061278/genshin-impact-ganyu-genshin-impact-keqing-genshin-impact-hd-wallpaper-preview.jpg')

    embed.set_thumbnail(url=member.avatar_url)

    embed.set_footer(icon_url='https://cdn.discordapp.com/attachments/772334064849649695/864518818798108672/130256173_196916332044367_1228585580782993887_n.png',text=f"{true_member_count} members in server")


    await guild.system_channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_remove(self,member):
    guild = member.guild
    true_member_count = len([m for m in guild.members if not m.bot])
    embed = discord.Embed(title=f'{member.name} left the server',description=f'Goodbye {member.name} we hope to see you again ',color = discord.Colour.purple())

    embed.set_image(url = 'https://cdn.discordapp.com/attachments/772334064849649695/864763351602561054/og-image.jpg')

    embed.set_thumbnail(url=member.avatar_url)

    embed.set_footer(icon_url='https://cdn.discordapp.com/attachments/772334064849649695/864518818798108672/130256173_196916332044367_1228585580782993887_n.png',text=f"{true_member_count} members in server")

    await guild.system_channel.send(embed=embed)



  
  
def setup(client):
  client.add_cog(Join_Leave(client))

  