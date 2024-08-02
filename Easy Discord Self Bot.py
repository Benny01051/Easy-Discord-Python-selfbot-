import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="." , intents=intents)     # You can also use Bot if you want 

@client.event
async def on_ready():
    print(f'We have logged in as {client.user} ')
 
@client.event
async def ping(ctx):
    ping = round(bot.latency * 1000)
    response = f"Pong! {ping}ms"
    await ctx.send(content=response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

###Code by crime aka Celestino :) enjoy


client.run("YOUR DISCORD BOT TOKEN HERE")


    

