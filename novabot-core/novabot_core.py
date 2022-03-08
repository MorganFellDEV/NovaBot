import os
import discord
import discord.emoji
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks

TOKEN = os.getenv('discord_token')
resources_location = os.getenv('novabot_resources')

# 'nd!' is the DEV prefix for NovaBot
bot = Bot(command_prefix="nd!")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print("Resources Location: " + str(resources_location))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, world!')
    

bot.run(TOKEN)
