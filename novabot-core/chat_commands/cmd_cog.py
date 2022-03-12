import discord
import discord.emoji
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks

from chat_commands import cmd_actions

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command(description="Throw someone!")
    async def throw(self,ctx):
        try:
            await ctx.send(cmd_actions.print_action(ctx,"throw"), file=discord.File(cmd_actions.random_action_image("throw")))
        except:
            print(sys.exc_info())

def setup(bot):
    bot.add_cog(BotCommands(bot))