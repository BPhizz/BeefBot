import discord
from discord.ext.commands import Bot

import secret
print('Logged in as')

beef_bot = Bot(command_prefix="!")

@beef_bot.event
async def on_read():
	print('Logged in as')
	print('Username: ' + beef_bot.user.name)
	print('ID: ' + beef_bot.user.id)
	print('------')
	print(beef_bot)

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
async def Craysin(*args):
	return await beef_bot.say("He's the amazing craysin!")
	
@beef_bot.command()
async def KKCrispus(*args):
	return await beef_bot.say("Where's Brandon?")	
	
@beef_bot.command()
async def darcy(*args):
	return await beef_bot.say("Whos that? <:Kappa:240828655385837568> ")
	



beef_bot.run(secret.BOT_TOKEN)
