import discord
from random import randint
from discord.ext.commands import Bot
import logging
import datetime, re
import sys

import secrets

theskypecall_bot = Bot(command_prefix="!")

red = "";
blue = "";
solo = "";

@theskypecall_bot.event
async def on_read():
	print("Client logged in")
  
@theskypecall_bot.command()
async def hello(*args):
	return await theskypecall_bot.say("Hello World!")
	
@theskypecall_bot.command()
async def beef(*args):
	return await theskypecall_bot.say("I am winner!")
	
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
