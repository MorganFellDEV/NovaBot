import discord
import discord.emoji
import requests
import os
import sys
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks
from chat_commands import cmd_actions
from chat_commands import get_emote
from twilio.rest import Client

from chat_commands.FileStore import FileStore

fileStore = FileStore()

twilio_account_sid = os.getenv("twilio_sid")
twilio_account_token = os.getenv("twilio_token")
nova_phone_number = os.getenv("nova_phone_number")
novabot_prefix = os.getenv("novabot_prefix")

twilioclient = Client(twilio_account_sid, twilio_account_token)

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

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def textnova(self,ctx):
        try:
            user_message_string = ctx.message.content
            user_message_string = user_message_string.replace(str(novabot_prefix+"annoynova "),"")
            print (user_message_string)
            if (len(user_message_string) < 100):
                twilioclient.api.account.messages.create(
                    to=nova_phone_number,
                    from_="NovaBot",
                    body=str(ctx.message.author) + ' says ' + '"' + user_message_string + '"')
                await ctx.send("Text message sent to Nova!")
            else:
                await ctx.send("Text message too long!")
        except:
            print(sys.exc_info())

    @commands.command()
    async def repeat(self,ctx):
        try:
            
            await ctx.send(user_message_string)
        except:
            print(sys.exc_info())

def setup(bot):
    bot.add_cog(BotCommands(bot))