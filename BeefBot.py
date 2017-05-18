import discord
from discord.ext.commands import Bot

import secret

beef_bot = Bot(command_prefix="!")

@beef_bot.event
async def on_read():
	print("Client logged in")

@beef_bot.command()
async def hello(*args):
	return await beef_bot.say("Hello World!")

@beef_bot.command()
async def beef(*args):
	return await beef_bot.say("I am winner!")
	
@beef_bot.command()
async def fuDarcy(*args):
	return await beef_bot.say("Go back to bed bitch")	
	
@beef_bot.command()
async def darcy(*args):
	return await beef_bot.say("Whos that? ")



beef_bot.run(secret.BOT_TOKEN)
