import discord
from repeater import owo
from repeater import clap
from repeater import dobby

channels = {}
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
				if modes[message.channel.guild.id] == "clap":
					await message.channel.send("**" + message.author.name + ":** " + clap(message.content))
				elif modes[message.channel.guild.id] == "dobby":
					await message.channel.send("**" + message.author.name + ":** " + dobby(message.content, message.author.name))
				else:
					await message.channel.send("**" + message.author.name + ":** " + owo(message.content))
		
		if message.content[:10] == "UwUchannel":
			channelint = message.channel.id
			channelint = int(message.content[13: len(message.content)-1])
			channels[message.channel.guild.id] = channelint
			modes[message.channel.guild.id] = 'uwu'
			await message.channel.send("I will now lurk in <#" + str(channelint) + ">")
			await message.channel.guild.me.edit(nick = "Literally")
		
		if message.content[:7] == "UwUmode":
			modes[message.channel.guild.id] = message.content.lower()[8:]
			await message.channel.send("Mode set to " + message.content.lower()[8:])

# Run the bot
client = MyClient()
token = open("token.txt", 'r').read()
client.run(token)