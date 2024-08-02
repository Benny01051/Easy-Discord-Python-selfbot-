import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="." , intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user} ')

@client.event
async def on_message(ping):
    if ping.author == client.user:
        return

    if ping.content.startswith('.ping'):
        await ping.channel.send('.pong')



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

###Code by crime aka Celestino :) enjoy


client.run("YOUR DISCORD BOT TOKEN HERE")


    

