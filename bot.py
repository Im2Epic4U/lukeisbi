# https://discordapp.com/oauth2/authorize?client_id=582644815519547404&scope=bot&permissions=67648

import discord
import os
from discord import activity
from discord.ext import commands

sendmessages = 'true'
client = discord.Client()
OwnerID = 379400007410909186
Nick = 269946726918389770
Luke = 189850839660101632
Claire = 333694007379230720

@client.event
async def on_ready():
	await client.wait_until_ready()
	await client.change_presence(activity=discord.Activity(type=2, name='luke being bisexual'))
	print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	if sendmessages == 'true':
		if message.author == client.user:
			return
		else:
			await message.channel.send(f"luke is bisexual lmao")
	else:
		return

	if "lib.help" == message.content.lower():
		embed = discord.Embed(title="LukeIsBi", description="Help menu", colour=discord.Colour.red())
		embed.add_field(name="lib.logout", value="Logs out the bot")
		embed.add_field(name="Messages", value="The bot also auto responds to messages")
		await message.channel.send(content=None, embed=embed)

	elif "lib.logout" == message.content.lower():
		if message.author.id == Clayton or Nick:
			await message.channel.send(f"Logging out... :wave:")
			await client.logout()
		else:
			await message.channel.send(f"You do not have permission to use this command!")

	elif message.author.id == Luke:
		await message.channel.send(f"luke you are bisexual, you got 67.9% heterosexual 67.9% homosexual\nwhich makes you bisexual")

	elif message.author.id == Nick:
		await message.channel.send(f"good one nick")

	elif message.author.id == Clayton:
		await message.channel.send(f"clayton is right")

	elif message.author.id == Claire:
		await message.channel.send(f"claire is a short-horned cow and\na black angus cow")

	elif "lib.messages" == message.content.lower():
		if message.author.id == Clayton or Nick:
			if sendmessages == 'true':
				sendmessages = 'false'
				await message.channel.send(f"Messages have been turned off!")
			else:
				sendmessages = 'true'
				await message.channel.send(f"Messages have been turned on!")

client.run(os.getenv('TOKEN'))