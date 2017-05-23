import discord
from random import randint
from discord.ext.commands import Bot
import logging
import datetime, re
import sys

import secrets

logging.basicConfig(level=logging.INFO)

theskypecall_bot = Bot(command_prefix="!")

red = "";
blue = "";
solo = "";

@theskypecall_bot.event
async def on_read():
    print('Logged in as:')
    print('Username: ' + theskypecall_bot.user.name)
    print('ID: ' + theskypecall_bot.user.id)
    print('------')
    if not hasattr(theskypecall_bot, 'uptime'):
        theskypecall_bot.uptime = datetime.datetime.utcnow()


		
@theskypecall_bot.command()
async def hello(*args):
	return await theskypecall_bot.say("Hello World!")

@theskypecall_bot.command()
async def beef(*args):
	return await theskypecall_bot.say("I am winner!")	

@theskypecall_bot.command()
async def Craysin(*args):
	return await theskypecall_bot.say("He's the amazing craysin!")
	
@theskypecall_bot.command()
async def KKCrispus(*args):
	return await theskypecall_bot.say("Where's Brandon?")	
	
@theskypecall_bot.command()
async def darcy(*args):
	return await theskypecall_bot.say("Whos that? <:Kappa:240828655385837568> ")
	
@theskypecall_bot.command()
async def add(left : int, right : int):
	"""Adds two numbers together."""
	await theskypecall_bot.say("%d + %d = %d" % (left,right,left + right))

# @theskypecall_bot.event
# async def on_message(message):
	# if message.content.startswith('Am I a Winner?'):
		# await theskypecall_bot.send_message(message.channel,'Are you a winner?')
		# for i in range(4):
			# msg = await theskypecall_bot.wait_for_message(author=message.author,content='yes')
			# temp = randint(1,4)
			# if temp==1:
				# fmt = "No?"
			# elif temp==2:
				# fmt = "Yes?"
			# elif temp==3:
				# fmt = "Try again?"
			# elif temp==4:
				# fmt = "Nah you is scrub"
			# await theskypecall_bot.send_message(message.channel, fmt)	
		# await theskypecall_bot.send_message(message.channel, 'Ok... you are Winner')
	
@theskypecall_bot.command()
async def Kyle(*args):
	temp = randint(1,4)
	if temp==1:
		return await theskypecall_bot.say("Take your shirt off!")
	elif temp==2:
		return await theskypecall_bot.say("Doube What?! Triple What?! Don't make me go killtacular on your ass!")
	elif temp==3:
		return await theskypecall_bot.say("Hey Chris, whats up?")
	elif temp==4:
		return await theskypecall_bot.say("[placeholder]")

@theskypecall_bot.command()
async def game(*args):
	temp = randint(1,5)
	if temp==1:
		return await theskypecall_bot.say("Heroes of the Storm")
	elif temp==2:
		return await theskypecall_bot.say("Diablo III")
	elif temp==3:
		return await theskypecall_bot.say("PUBG")
	elif temp==4:
		return await theskypecall_bot.say("Overwatch")
	elif temp==5:
		return await theskypecall_bot.say("Sleep")
	elif temp==6:
		return await theskypecall_bot.say("League of Legends")

"""@theskypecall_bot.command()   WHY DIS NO WORK
async def code(*args):
	name = display_name(self)
	return await theskypecall_bot.say(name)
"""
	
@theskypecall_bot.command()
async def roll(user):
	global red
	global blue
	global solo
	temp = randint(1,7)
	if user=="clearroll":
		red=""
		blue=""
		solo=""
		return await theskypecall_bot.say("Roll Board has been cleared!")
	if temp==1:
		blue += " " + user
		await theskypecall_bot.say("User %s rolled a %d : Team Blue! " % (user,temp))
	elif temp==2:
		blue += " " + user
		await theskypecall_bot.say("User %s rolled a %d : Team Blue!" % (user,temp))
	elif temp==3:
		blue += " " + user
		await theskypecall_bot.say("User %s rolled a %d : Team Blue!" % (user,temp))
	elif temp==4:
		red += " " + user
		await theskypecall_bot.say("User %s rolled a %d : Team Red!" % (user,temp))
	elif temp==5:
		red += " " + user
		await theskypecall_bot.say("User %s rolled a %d : Team Red!" % (user,temp))
	elif temp==6:
		red += " " + user
		await theskypecall_bot.say("User %s rolled a %d : Team Red!" % (user,temp))
	elif temp==7:
		solo += " " + user
		await theskypecall_bot.say("User %s rolled a %d : You are Solo! <:FeelsBadMan:240829348603494400>" % (user,temp))
	return await theskypecall_bot.say(" %s : RED   ||   BLUE : %s  || Solo %s <:Kappa:240828655385837568>" % (red,blue,solo))


		
theskypecall_bot.run(secrets.BOT_TOKEN)
