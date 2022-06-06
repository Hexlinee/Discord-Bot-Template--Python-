import os, ast, importlib, commands,discord
from os import listdir, walk
from os.path import dirname, basename, isfile, join
from discord import app_commands

with open("config.txt") as config:
    context = config.readlines()

class _client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id="902507873437876224"))
            self.synced = True
        print("The bot is currently online")

client = _client()
tree = app_commands.CommandTree(client)
files = []

for (dirpath, dirnames, filenames) in walk("commands"):
    files.extend(filenames)
    for name_ in filenames:
        @tree.command(name=name_.split(".")[0],description="🏓",guild=discord.Object(id=902507873437876224))
        async def self(interaction: discord.Interaction,):
            module = importlib.import_module(".{}".format(name_.split(".")[0]), package="commands")
            await module.run(client,interaction,True)

    break

@client.event
async def on_message(message):
    if not message.author == client.user:
        username = str(message.author).split("#")[0]
        message_content = str(message.content)
        channel = str(message.channel.name)

        if "{}.py".format(message_content.lower()) in files:
            module = importlib.import_module(".ping", package="commands")
            await module.run(client,message,False)

client.run(context[0].split("=")[1])


