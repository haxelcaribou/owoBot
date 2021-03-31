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

    message_content = message.content.lower()

    if message_content .startswith(tuple(owo_strings)):
        messages = await channel.history(limit=2).flatten()
        p_message = messages[1].content
        await channel.send(owo.owo(p_message))

    elif "twagedy" in message_content:
        await channel.send(owo.owo("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."))


client.run(TOKEN)
