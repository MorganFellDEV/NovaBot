from os import listdir
from os.path import isfile, join
import random
import os

resources_location = os.getenv("novabot_resources")


def random_throw_image():
    onlyfiles = [f for f in listdir(str(resources_location) + "/throw/") if
                 isfile(join(str(resources_location) + "/throw/", f))]
    file = str((str(resources_location) + "/throw/" + random.choice(onlyfiles)))
    return file


def give_throw(ctx):
    throw_string = ""

    for incrementer, value in enumerate(ctx.message.mentions):
        print("length list " + str(len(ctx.message.mentions)))
        if len(ctx.message.mentions) > 2:
            print("more than two people")
            if incrementer == 0:
                # first person
                throw_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions) - 1:
                throw_string += ", " + str(ctx.message.mentions[incrementer].name)
            else:
                throw_string += " and " + str(ctx.message.mentions[incrementer].name)

        else:
            if incrementer == 0:
                # first person
                throw_string += str(ctx.message.mentions[incrementer].name)
                pass
            elif incrementer != len(ctx.message.mentions):
                throw_string += " and " + str(ctx.message.mentions[incrementer].name)

    return ctx.message.author.name + " throws " + throw_string + "!"
