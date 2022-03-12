import os
import sys
import discord
import discord.emoji
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks

from chat_commands import cmd_throw

TOKEN = os.getenv("discord_token")
resources_location = os.getenv("novabot_resources")

# 'nd!' is the DEV prefix for NovaBot
bot = Bot(command_prefix="nd!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    print("Resources Location: " + str(resources_location))

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Command error, error dumped to logs.")
    raise error

@bot.command(description="Throw someone!")
async def throw(ctx):
    try:
        await ctx.send(cmd_throw.give_throw(ctx), file=discord.File(cmd_throw.random_throw_image()))
    except:
        print(sys.exc_info())

bot.run(TOKEN)
