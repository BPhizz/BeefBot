import discord
from random import randint
from discord.ext.commands import Bot
import logging
import datetime, re
import sys


logging.basicConfig(level=logging.info)


import secret

beef_bot = Bot(command_prefix="!")

@beef_bot.event
async def on_read():
    print('Logged in as:')
    print('Username: ' + beef_bot.user.name)
    print('ID: ' + beef_bot.user.id)
    print('------')
    if not hasattr(beef_bot, 'uptime'):
        beef_bot.uptime = datetime.datetime.utcnow()


		
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
async def add(left : int, right : int):
	"""Adds two numbers together."""
	await beef_bot.say("%d + %d = %d" % (left,right,left + right))

# @beef_bot.event
# async def on_message(message):
	# if message.content.startswith('Am I a Winner?'):
		# await beef_bot.send_message(message.channel,'Are you a winner?')
		# for i in range(4):
			# msg = await beef_bot.wait_for_message(author=message.author,content='yes')
			# temp = randint(1,4)
			# if temp==1:
				# fmt = "No?"
			# elif temp==2:
				# fmt = "Yes?"
			# elif temp==3:
				# fmt = "Try again?"
			# elif temp==4:
				# fmt = "Nah you is scrub"
			# await beef_bot.send_message(message.channel, fmt)	
		# await beef_bot.send_message(message.channel, 'Ok... you are Winner')
	
@beef_bot.command()
async def Kyle(*args):
	temp = randint(1,4)
	if temp==1:
		return await beef_bot.say("Take your shirt off!")
	elif temp==2:
		return await beef_bot.say("Doube What?! Triple What?! Don't make me go killtacular on your ass!")
	elif temp==3:
		return await beef_bot.say("Hey Chris, whats up?")
	elif temp==4:
		return await beef_bot.say("[placeholder]")

@beef_bot.command()
async def game(*args):
	temp = randint(1,5)
	if temp==1:
		return await beef_bot.say("Heroes of the Storm")
	elif temp==2:
		return await beef_bot.say("Diablo III")
	elif temp==3:
		return await beef_bot.say("PUBG")
	elif temp==4:
		return await beef_bot.say("Overwatch")
	elif temp==5:
		return await beef_bot.say("Sleep")
	elif temp==6:
		return await beef_bot.say("League of Legends")

"""@beef_bot.command()   WHY DIS NO WORK
async def code(*args):
	name = display_name(self)
	return await beef_bot.say(name)
"""
beef_bot.run(secret.BOT_TOKEN)
