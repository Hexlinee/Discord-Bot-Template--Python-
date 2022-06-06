import discord

async def run(client,message,slash):
    if slash == True:
        await message.response.send_message("Pong 🏓")
    else:
        await message.channel.send("Pong 🏓")

