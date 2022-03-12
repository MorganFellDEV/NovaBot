import discord
import discord.emoji
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks

from chat_commands import cmd_throw

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command(description="Throw someone!")
    async def throw(self,ctx):
        try:
            await ctx.send(cmd_throw.give_throw(ctx), file=discord.File(cmd_throw.random_throw_image()))
        except:
            print(sys.exc_info())

def setup(bot):
    bot.add_cog(BotCommands(bot))