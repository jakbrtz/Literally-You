import discord
from repeater import owo
from repeater import clap
from repeater import lisp

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
		
		await message.channel.send(message.author.name + ": " + owo(message.content))
		await message.channel.send(message.author.name + ": " + clap(message.content))
		await message.channel.send(message.author.name + ": " + lisp(message.content))

# Run the bot
client = MyClient()
token = open("token.txt", 'r').read()
client.run(token)