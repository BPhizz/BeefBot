import discord
from discord.ext.commands import Bot

import Secret

BeefBot = Bot(command_prefix="!")

@BeefBot.event
async def on_read():
    print("Client logged in")

@BeefBot.command()
async def hello(args):
    return await BeefBot.say("Hello World!")

@BeefBot.command()
async def beef(args):
    return await BeefBot.say("I am winner!")


BeefBot.run(Secret.BOT_TOKEN)