import discord
import discord.emoji
import requests
import sys
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks
from chat_commands import cmd_actions
from chat_commands import get_emote

from chat_commands.FileStore import FileStore

fileStore = FileStore()

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

    @commands.command(description="Posts the image of the emote sent to it.")
    async def jumbo(self,ctx, emoji: discord.PartialEmoji):
        try:
            await ctx.send(file=get_emote.get_emote_image(ctx, emoji, fileStore))
        except:
            print(sys.exc_info())

def setup(bot):
    bot.add_cog(BotCommands(bot))