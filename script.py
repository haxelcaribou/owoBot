#!/usr/bin/python3

import discord
import owo
import secrets
import re
import random

client = discord.Client()
TOKEN = secrets.token

owo_strings = ("owo", "uwu", "^w^", "0w0", "vwv")

url_regex = re.compile(
    r"(https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)")
ping_regex = re.compile(r"@&?(?=\S)")
channel_regex = re.compile(r"#(?=\S)")
emote_regex = re.compile(r"( )?:\w+:(?(1)| )?")
id_regex = re.compile(r"( ?<a?:\w+:\d{18}> ?)+")
empty_regex = re.compile(r"\s*")
num_regex = re.compile(r"[1-4]?[0-9]")

status = "*Nuzzles U*"


def parse_message(message):
    output = ""
    parts = url_regex.split(message)
    for i in range(len(parts)):
        if i % 2 == 1:
            output += parts[i]
        else:
            output += owo.substitute(parts[i])
    output = ping_regex.sub("@ ", output)
    output = channel_regex.sub("# ", output)
    output = emote_regex.sub("", output)
    output = output.replace("||||", "")
    if empty_regex.fullmatch(output):
        return random.choice(owo.PREFIXES)
    return owo.add_affixes(output)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(status))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel

    message_content = message.clean_content.lower()

    if message_content.startswith(tuple(owo_strings)):
        num_input = num_regex.search(message_content[4:])
        if num_input:
            num = int(num_input.group(0))
            p_messages = await channel.history(limit=num + 1).flatten()
            p_message = p_messages[num]
            p_message_content = p_message.clean_content
            if p_message.author != client.user and p_message_content[-1:] != "¬" and not url_regex.fullmatch(p_message_content) and not id_regex.fullmatch(p_message_content) and len(p_message_content) > 1 and not p_message_content.startswith(tuple(owo_strings)):
                await channel.send(parse_message(p_message_content))
                return
            channel.send(random.choice(owo.PREFIXES))
        else:
            async for p_message in channel.history(limit=25):
                p_message_content = p_message.clean_content
                if p_message.author != client.user and p_message_content[-1:] != "¬" and not url_regex.fullmatch(p_message_content) and not id_regex.fullmatch(p_message_content) and len(p_message_content) > 1 and not p_message_content.startswith(tuple(owo_strings)):
                    await channel.send(parse_message(p_message_content))
                    return
            channel.send(random.choice(owo.PREFIXES))

    elif message_content == "moo":
        await channel.send(owo.substitute("I'm not a cow, shut up."))
        return
    elif message_content == "moo -v":
        await channel.send(owo.substitute("I already told you I'm not a cow."))
        return
    elif message_content.startswith("moo -vv"):
        await channel.send(owo.substitute("Please Stop"))
        return
    elif message_content == "sudo moo":
        await channel.send(owo.substitute("Moo"))
        return

    elif "twagedy" in message_content:
        await channel.send(owo.owo("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."))
        return


@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if message.author != client.user:
        return

    if str(reaction.emoji) == "🔇":
        await message.delete()

client.run(TOKEN)
