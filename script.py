#!/usr/bin/python3

import discord
import owo
import secrets
import re

client = discord.Client()
TOKEN = secrets.token

owo_strings = ("owo", "uwu", "^w^", "0w0", "vwv")

url_regex = re.compile(r"(https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)")
ping_regex = re.compile(r"(\<[@#]&?\d+\>)")

def parse_message(message):
    output = ""
    parts = url_regex.split(message)
    for i in range(len(parts)):
        if i % 2 == 1:
            output += parts[i]
        else:
            output += owo.substitute(parts[i])
    output = ping_regex.sub("@", output) # TODO: Display role/user/channel name
    # output = ""
    # for i in range(len(parts)):
    #     part = parts[i]
    #     if i % 2 == 1:
    #         output += part
    #     else:
    #         id = part[2:-1]
    #         if part.startswith("<@&"): # Role
    #             id = id[1:]
    #             pass
    #         elif part.startswith("<@"): # User
    #             output += "@ " + client.get_user(id).display_name
    #         elif part.startswith("<#"): # Channel
    #             output += "# " + client.get_channel(id).name
    return owo.add_affixes(output)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel

    message_content = message.clean_content.lower()

    if message_content.startswith(tuple(owo_strings)):
        messages = await channel.history(limit=2).flatten()
        p_message = messages[1].content
        await channel.send(parse_message(p_message))

    elif "twagedy" in message_content:
        await channel.send(owo.owo("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself."))


client.run(TOKEN)
