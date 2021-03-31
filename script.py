#!/usr/bin/python3

import discord
import owo
import secrets

client = discord.Client()
TOKEN = secrets.token

owo_strings = ("owo", "uwu", "^w^", "0w0", "vwv")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel

    if message.content.lower().startswith(tuple(owo_strings)):
        messages = await channel.history(limit=3).flatten()
        p_message = messages[1].content
        await channel.send(owo.owo(p_message))

client.run(TOKEN)
