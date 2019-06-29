import discord
import pickle
from repeater import owo
from repeater import clap
from repeater import dobby

# Attempt to remember channel settings
try:
	with open('channels.pkl', 'rb') as f:
		channels = pickle.load(f)
except:
	channels = {}

# Attempt to remember mode settings
try:
	with open('modes.pkl', 'rb') as f:
		modes = pickle.load(f)
except:
	modes = {}

# Class to run the bot
class MyClient(discord.Client):

	# When you're ready, log in
	async def on_ready(self):
		print('Logged on as', self.user)
		
	# When you recieve a message, respond
	async def on_message(self, message):
		# if the author of the message was a bot, do nothing
		if message.author.bot:
			return
		# if the message is blank, do nothing
		if message.content == '':
			return
		
		# if the message was sent in the designated channel, run the algorithm
		if message.channel.guild.id in channels:
			if channels[message.channel.guild.id] == message.channel.id:
				# delete the message
				await message.delete()
				# figure out how to replace the text. The defaul setting is `uwu`
				try:
					mode = modes[message.channel.guild.id]
				except:
					mode = "uwu"
				# replace the message
				if mode == "clap":
					await message.channel.send("**" + message.author.name + ":** " + clap(message.content))
				elif mode == "dobby":
					await message.channel.send("**" + message.author.name + ":** " + dobby(message.content, message.author.name))
				else:
					await message.channel.send("**" + message.author.name + ":** " + owo(message.content))
		
		# Change the designmated channel
		if message.content[:10] == "UwUchannel":
			channelint = message.channel.id
			channelint = int(message.content[13: len(message.content)-1])
			channels[message.channel.guild.id] = channelint
			if not message.channel.guild.id in modes:
				modes[message.channel.guild.id] = 'uwu'
			with open('channels.pkl', 'wb') as f:
				pickle.dump(channels, f, pickle.HIGHEST_PROTOCOL)
			await message.channel.send("I will now lurk in <#" + str(channelint) + ">")
			await message.channel.guild.me.edit(nick = "Literally")
		
		# Change the replacement mode
		if message.content[:7] == "UwUmode":
			modes[message.channel.guild.id] = message.content.lower()[8:]
			with open('modes.pkl', 'wb') as f:
				pickle.dump(modes, f, pickle.HIGHEST_PROTOCOL)
			await message.channel.send("Mode set to " + message.content.lower()[8:])

# Run the bot
client = MyClient()
token = open("token.txt", 'r').read()
client.run(token)