import discord
from discord.ext.commands import Bot

import Secret

beef_bot = Bot(command_prefix="!")

@beef_bot.event
async def on_read():
	print("Client logged in")

@beef_bot.command()
async def hello(args):
	return await beef_bot.say("Hello World!")

@beef_bot.command()
async def beef(args):
	return await beef_bot.say("I am winner!")


<<<<<<< HEAD
beefbot.run(Secret.BOT_TOKEN)
=======
beef_bot.run(secret.BOT_TOKEN)
>>>>>>> e2b2631790e011da3cba54b87107ca5bfcf79f5b
