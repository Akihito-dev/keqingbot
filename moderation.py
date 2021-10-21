import discord
from discord.ext import commands

class Moderation(commands.Cog):
  def __init__(self,client):
    self.client = client

  # moderation functions
  # kick


  @commands.command(help=".kick @User_Name")
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx, member: discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.reply(f'{member.mention} has been kicked for {reason}')

  @kick.error
  async def kick_error(self,ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("You dont have the permissions to execute that command ╰(*°▽°*)╯")

  @kick.error
  async def kick_error_missing_args(self,ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Please give mew the username of the person! ╰(*°▽°*)╯")

  # ban


  @commands.command(help=".ban @User_Name")
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx, member: discord.Member, *, reason=None):
      await member.ban(reason=reason)
      await ctx.reply(f'{member.mention} has been banned for {reason}')

  @ban.error
  async def ban_error_missing_args(self,ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.reply("Please give mew the username of the person! ╰(*°▽°*)╯")

  @ban.error
  async def ban_error(self,ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("You dont have the permissions to execute that command ╰(*°▽°*)╯")
  # unban


  @commands.command(help=".unban @User_Name")
  @commands.has_permissions(ban_members=True)
  async def unban(self,ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
          user = ban_entry.user

          if (user.name, user.discriminator) == (member_name, member_discriminator):
              await ctx.guild.unban(user)
              await ctx.reply(f'{user.mention} has been unbanned')
              return


  @unban.error
  async def unban_error(self,ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("You dont have the permissions to execute that command ╰(*°▽°*)╯")
  
  @unban.error
  async def unban_error_missing_args(self,ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.reply("Please give mew the username of the person! ╰(*°▽°*)╯")


  @commands.command(help=".clear amount (which must be > 0)")
  @commands.has_permissions(manage_messages=True)
  async def clear(self,ctx, amount=0):
      if amount == 0:
          await ctx.reply("The specified amount can't be 0 ＞︿＜")
      if amount >= 100:
        await ctx.reply("The specified amount can't be greater than or equals to 100 for safety reasons ＞︿＜")
      else:
          await ctx.channel.purge(limit=amount + 1)
          await ctx.send(f'{amount} messages were deleted')


  @clear.error
  async def clear_error_args(self,ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.reply("Please specify the number of messages to be deleted nyaa")


  @clear.error
  async def clear_error_perms(self,ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("You dont have the permissions to execute that command ╰(*°▽°*)╯")

  @commands.command(help=".mute @User_Name")
  @commands.has_permissions(manage_messages=True)
  async def mute(self,ctx,member:discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name= "Muted")
    
    if not mutedRole:
      mutedRole = await guild.create_role(name="Muted")

      for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak=False, send_messages=False)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.reply(f"Muted {member.mention} for {reason}")
  
  @mute.error
  async def mute_error_missing_args(self,ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.reply("Please give mew the username of the person! ╰(*°▽°*)╯")
  
  @mute.error
  async def mute_error(self,ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.reply("You dont have the permissions to execute that command ╰(*°▽°*)╯")

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self,ctx,member:discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name= "Muted")

    await member.remove_roles(mutedRole)
    await ctx.reply(f'Unmuted {member.mention}')

  @unmute.error
  async def unmute_error_missing_args(self,ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.reply("Please give mew the username of the person! ╰(*°▽°*)╯")

  @unmute.error
  async def unmute_error(self,ctx, error):
    if isinstance(error, commands.MissingPermissions):
       await ctx.reply("You dont have the permissions to execute that command ╰(*°▽°*)╯")

  @commands.command()
  @commands.has_permissions(manage_nicknames=True)
  async def setnick(self,ctx, member: discord.Member,*, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

  



def setup(client):
  client.add_cog(Moderation(client))