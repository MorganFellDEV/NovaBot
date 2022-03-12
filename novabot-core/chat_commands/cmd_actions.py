from os import listdir
from os.path import isfile, join
import random
import os

resources_location = os.getenv("novabot_resources")


def random_action_image(action):
    onlyfiles = [f for f in listdir(str(resources_location) + "/"+action+"/") if
                 isfile(join(str(resources_location) + "/"+action+"/", f))]
    file = str((str(resources_location) + "/"+action+"/" + random.choice(onlyfiles)))
    return file


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
