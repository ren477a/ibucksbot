# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

queue = []

def display_queue():
    names_in_queue = list(map(lambda x: x.global_name, queue))
    text = "```\n"
    for name in names_in_queue:
        text += f"{name}\n"
    text += "```"
    return f"({len(queue)}/5)\n" +text

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f"Hello {message.author}!")

    if message.content.startswith('!valo clear'):
        queue.clear()
        await message.channel.send(f"Queue cleared.")

    if message.content.startswith('!valo show'):
        await message.channel.send(f"Current queue: {display_queue()}")

    if message.content.startswith('!valo +1'):
        if message.author in queue:
            response = f"{message.author} already in queue. Current queue: {display_queue()}"
        elif len(queue) >= 5:
            response = "Queue is full!"
        else:
            queue.append(message.author)
            response = f"<@&1022482553933934612> Added to queue {message.author}. Current queue: {display_queue()}"

        await message.channel.send(response)

    if message.content.startswith('!valo -1'):
        queue.remove(message.author)
        await message.channel.send(f"Removed {message.author}. Current queue: {display_queue()}")

    if message.content.startswith('!valo help'):
        help_message = """
```
!valo +1
!valo -1
!valo show
!valo clear
```
"""
        await message.channel.send(help_message)


client.run('replace_this')
