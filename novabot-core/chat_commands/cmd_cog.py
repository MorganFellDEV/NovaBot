import discord
import discord.emoji
import requests
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

    @commands.command()
    async def tickle(self,ctx):
        try:
            await ctx.send(cmd_actions.print_action(ctx,"tickle"), file=discord.File(cmd_actions.random_action_image("tickle")))
        except:
            print(sys.exc_info())


    @commands.command()
    async def patpfp(self,ctx):
        if (ctx.message.mentions):
            user = ctx.message.mentions[0]
            pfp = str(user.avatar_url)
            request_string = "https://api.jeyy.xyz/image/patpat?image_url="+pfp
            requester = requests.get(request_string)
            with open('farts.gif', 'wb') as file:
                file.write(requester.content)
            await ctx.send(file=discord.File("farts.gif"))
        else:
            user = ctx.message.author
            pfp = str(user.avatar_url)
            request_string = "https://api.jeyy.xyz/image/patpat?image_url="+pfp
            requester = requests.get(request_string)
            with open('farts.gif', 'wb') as file:
                file.write(requester.content)
            await ctx.send(file=discord.File("farts.gif"))


def setup(bot):
    bot.add_cog(BotCommands(bot))