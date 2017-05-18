import discord
from discord.ext.commands import Bot

import Secret

beefbot = Bot(command_prefix="!")

@beefbot.event
async def on_read():
    print("Client logged in")

@beefbot.command()
async def hello(args):
    return await beefbot.say("Hello World!")

@beefbot.command()
async def beef(args):
    return await beefbot.say("I am winner!")


beefbot.run(Secret.BOT_TOKEN)