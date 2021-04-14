#!/usr/bin/python3

import discord
import secrets
import sys

client = discord.Client()
TOKEN = secrets.token

#
#def deleteMessage(id):
#     pass

async def change_status(status):
    await client.change_presence(activity=discord.Game(status))

async def remove_phrase(id, num, phrase):
    channel = await client.fetch_channel(id)
    print("got channel ", channel)
    async for message in channel.history(limit=num):
        if message.author == client.user and phrase in message.clean_content:
            await message.delete()


async def dm(id, message):
    user = await client.fetch_user(id)
    print("got user ", user)
    if user.dm_channel:
        user.dm_channel.send(message)
    else:
        dmChannel = await user.create_dm()
        await dmChannel.send(message)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.close()


client.run(TOKEN)
