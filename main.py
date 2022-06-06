import os, ast, discord, importlib, commands
from os import listdir, walk
from os.path import dirname, basename, isfile, join

with open("config.txt") as config:
    context = config.readlines()

client = discord.Client()

f = []

for (dirpath, dirnames, filenames) in walk("commands"):
    f.extend(filenames)
    break

@client.event
async def on_ready():
    print("The bot is currently online.")

@client.event
async def on_message(message):
    if not message.author == client.user:
        username = str(message.author).split("#")[0]
        message_content = str(message.content)
        channel = str(message.channel.name)

        if "{}.py".format(message_content.lower()) in f:
            module = importlib.import_module(".{}".format(message_content.lower()), package="commands")
            await module.run(client,message)
try:
    client.run(context[0].split("=")[1])
except:
    print("Oops, we encountered a problem while starting your discord bot.")

