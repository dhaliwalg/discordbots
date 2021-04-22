import discord
import logging

logging.basicConfig(level=logging.INFO)
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hi! i can ping')

    if message.content == "$help":
        message.channel.send('**I\'m a pretty small bot!**')
        message.channel.send('*Commands:*')
        message.channel.send('$help -> Brings up this small help prompt')
        message.channel.send('$haiku -> Prints a small haiku')
        message.channel.send('Honestly, that\'s all I do for now!')

    

client.run('ODE2MzI4ODgxNzU3MDkzOTAw.YD5XhA.1u99WNuB-2L0BMh9S3ShD7stgLI')