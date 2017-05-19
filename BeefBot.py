import discord
from random import randint
from discord.ext.commands import Bot

import secret

beef_bot = Bot(command_prefix="!")
beef_bot.get_all_emojis()

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
async def Craysin(*args):
	return await beef_bot.say("He's the amazing craysin!")
	
@beef_bot.command()
async def KKCrispus(*args):
	return await beef_bot.say("Where's Brandon?")	
	
@beef_bot.command()
async def darcy(*args):
	return await beef_bot.say("Whos that? <:Kappa:240828655385837568> ")

@beef_bot.command()
async def Kyle(*args):
	temp = randint(1,4)
	if temp==1
		return await beef_bot.say("Take your shirt off!")
	elif temp==2
		return await beef_bot.say("Doube What?! Triple What?! Don't make me go killtacular on your ass!")
	elif temp==3
		return await beef_bot.say("Hey Chris, whats up?")
	elif temp==4
		return await beef_bot.say("[placeholder]")



beef_bot.run(secret.BOT_TOKEN)
