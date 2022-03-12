import os
import sys
import discord
import discord.emoji
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks
import requests
import json

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

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(extension)
    embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0xff00c8)
    await ctx.send(embed=embed)

@bot.command()
async def version(ctx):
    jsondata= json.loads(requests.get("https://api.github.com/repos/MorganFellDEV/NovaBot/commits/main").content)
    await ctx.send("NovaBot is currently version *"+ jsondata["sha"][0:7] + "*")

bot.load_extension("chat_commands.cmd_cog")
bot.run(TOKEN)
