import requests
import os
import discord
import glob

from chat_commands.FileStore import FileStore

resources_location = os.getenv('novabot_resources')


def get_emote_image(ctx, emoji: discord.PartialEmoji, files_store: FileStore):
    extension = ".gif" if emoji.animated else ".png"
    if emoji.id not in files_store.links:
        request_file = requests.get("https://cdn.discordapp.com/emojis/%s%s" % (emoji.id, extension))
        image_location = "%s/emotes_grabbed/%s%s" % (resources_location, emoji.id, extension)
        open(image_location, 'wb').write(request_file.content)
        files_store.add_link(emoji.id, image_location)
    return discord.File(files_store.get_link(emoji.id))


def cleanup_emote():
    for files_found in glob.glob(str(resources_location) + "/emotes_grabbed/*"):
        os.remove(files_found)