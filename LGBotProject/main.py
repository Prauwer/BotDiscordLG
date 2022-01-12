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

@client.event
async def displayembed(ctx):
    channel = ctx.message.channel
    embed=discord.Embed(
        title="Ordinary Townfolk", url="https://werewolf-the-game.fandom.com/wiki/The_Villagers", 
        description="The Villagers are a team seeking to kill all of the Werewolves. A Villager is a player character with no abilities, but the Village also includes any role not on the same team of the Werewolves, like the Guard, the Seer, the Witch, and others. Giving the Villagers addition powers, like the Guard or the Masons, tilts the balance toward them. To balance against the Village add roles that hamper them like the Fool or the Hapless Victim. The Village wins if all Werewolves are killed.",
        color=0xFF5733)
    await client.send_message(channel, embed=embed)

client.run("OTMwNzMzNTI1MzI0NDA2ODE0.Yd6LJA.PvzRkMRBjyPQWR-IH1am1kfItCk")