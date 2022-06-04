from os import listdir
from os.path import isfile, join
import random
import os
from azure.storage.blob import *

resources_location = os.getenv("novabot_resources")
connection_string = os.getenv("azure_connection_string")
cdn_location = os.getenv("cdn_location")
blob_container = os.getenv("blob_container")

def random_action_image(action):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(blob_container)
    blob_list = list(container_client.list_blobs(name_starts_with=action+"/"))
    blob = random.choice(blob_list)

    url = cdn_location+blob.name
    return url


def print_action(ctx,action):
    action_string = ""

    for incrementer, value in enumerate(ctx.message.mentions):
        print("length list " + str(len(ctx.message.mentions)))
        if len(ctx.message.mentions) > 2:
            print("more than two people")
            if incrementer == 0:
                # first person
                action_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions) - 1:
                action_string += ", " + str(ctx.message.mentions[incrementer].name)
            else:
                action_string += " and " + str(ctx.message.mentions[incrementer].name)

        else:
            if incrementer == 0:
                # first person
                action_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions):
                action_string += " and " + str(ctx.message.mentions[incrementer].name)

    return ctx.message.author.name + " " + action +"s " + action_string + "!"
