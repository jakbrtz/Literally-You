import discord
import pickle
from repeater import owo
from repeater import clap
from repeater import dobby

try:
	with open('channels.pkl', 'rb') as f:
		channels = pickle.load(f)
except:
	channels = {}

try:
	with open('modes.pkl', 'rb') as f:
		modes = pickle.load(f)
except:
	modes = {}

# Everything that the bot does is inside this class:
class MyClient(discord.Client):

	# When you're ready, log in
	async def on_ready(self):
		print('Logged on as', self.user)
		
	# When you recieve a message, respond to it
	async def on_message(self, message):
		# if the author of the message was a bot don't respond
		if message.author.bot:
			return
		if message.content == '':
			return
		
		if message.channel.guild.id in channels:
			if channels[message.channel.guild.id] == message.channel.id:
				await message.delete()
				try:
					mode = modes[message.channel.guild.id]
				except:
					mode = "uwu"
				if mode == "clap":
					await message.channel.send("**" + message.author.name + ":** " + clap(message.content))
				elif mode == "dobby":
					await message.channel.send("**" + message.author.name + ":** " + dobby(message.content, message.author.name))
				else:
					await message.channel.send("**" + message.author.name + ":** " + owo(message.content))
		
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
		
		if message.content[:7] == "UwUmode":
			modes[message.channel.guild.id] = message.content.lower()[8:]
			with open('modes.pkl', 'wb') as f:
				pickle.dump(modes, f, pickle.HIGHEST_PROTOCOL)
			await message.channel.send("Mode set to " + message.content.lower()[8:])

# Run the bot
client = MyClient()
token = open("token.txt", 'r').read()
client.run(token)