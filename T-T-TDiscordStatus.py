import discord
from discord.ext import commands
import asyncio
from itertools import cycle

TOKEN = "YOUR_TOKEN_HERE"

client = commands.Bot(command_prefix = "YOUR_PREFIX")

statusmsg = ['Message 1','Message 2', 'Message 3']

async def change_status():
    await client.wait_until_ready()
    messages = cycle(statusmsg)

    while not client.is_closed:
        current_status = next(messages)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(60)


@client.event
async def on_ready():
    print('Ready.')


client.loop.create_task(change_status())
client.run('token')
