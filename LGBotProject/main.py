# bot.py
import os

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == 'fuck lucas':
        # response = random.choice(brooklyn_99_quotes)
        await message.channel.send("yes of course")


client.run("OTMwNzMzNTI1MzI0NDA2ODE0.Yd6LJA.PvzRkMRBjyPQWR-IH1am1kfItCk")