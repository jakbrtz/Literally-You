# Literally-You
Discord Bot that repeats what you say, but differently

## Setup

* Create a bot at [https://discordapp.com/developers/applications/](https://discordapp.com/developers/applications/)

* Make sure the bot has 'manage messages' permission

* Copy the token into `token.txt`

* Make sure you have the discord wrapper installed. This can be done with `pip install discord`

## Using the bot

The bot designates one channel per server. Every message in that message gets deleted, and replaced with what you literally just said.

To designate a channel, type `UwUchannel #channelname`. Make sure that #channelname turns into a hyperlink.

To pick a type of repetition, type `UwUmode mode`. The modes could be:

* uwu

* clap

* dobby

## Remarks

This bot was created for [Discord's Hack Week](https://blog.discordapp.com/discord-community-hack-week-build-and-create-alongside-us-6b2a7b7bba33). 
I made this in a rush after realising that my other submission (RNN trained on text channel) was too impractical to be a discord bot.

Only after I made this I realised that the features in this bot are already available online, however I could not find a discord bot that does this.

All code is licenced as Creative Commons *(or whatever, idk the legal jargon)*