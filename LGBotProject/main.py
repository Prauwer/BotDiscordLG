# bot.py
import os

import discord
from discord.utils import get

import random

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

    if message.content == 'EUQINIMOD':
        # response = random.choice(brooklyn_99_quotes)
        await message.channel.send("yes of course")

    if message.content =='role':
        embed = discord.Embed(title="Simple villageois", description="The one nobody wants to be", color=0xffdd00)
        embed.set_thumbnail(
            url="https://static.wikia.nocookie.net/loupgaroumal/images/d/d6/Carte_SimpleVillaegois.png/revision/latest/scale-to-width-down/350?cb=20210104170925&path-prefix=fr")
        embed.add_field(name="Description",
                        value="They don't have any special power except thinking, being smart and the right to vote.")
        embed.set_footer(text="Use them as cannon fodder")
        await message.channel.send(embed=embed)


    if message.content.startswith('test'):
        username = await client.fetch_user(235341365062402048)
        print(username)
        content="Hello world!"
        channel = await username.create_dm()
        await channel.send(content)

@client.event
async def on_raw_reaction_add(payload):
    print("YO")
    print(payload.user_id)
    user=await client.fetch_user(payload.user_id)
    channel = await user.create_dm()
    await channel.send("yo")



TOKEN = 'OTMwNzMzNTI1MzI0NDA2ODE0.Yd6LJA.lPZ7ACFR0RjTsUAlFLMtL8MugPI'
client.run(TOKEN)
