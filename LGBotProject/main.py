# bot.py
import os

import discord
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
        embed = discord.Embed(title="Villager", description="The one nobody wants to be", url="https://werewolf-the-game.fandom.com/wiki/The_Villagers", color=0xffdd00)
        embed.set_thumbnail(
            url="https://static.wikia.nocookie.net/loupgaroumal/images/d/d6/Carte_SimpleVillaegois.png/revision/latest/scale-to-width-down/350?cb=20210104170925&path-prefix=fr")
        embed.add_field(name="Description",
                        value="The Villagers are a team seeking to kill all of the Werewolves. \n\n A Villager is a player character with no abilities, but the Village also includes any role not on the same team of the Werewolves, like the Guard, the Seer, the Witch, and others. \n\n Giving the Villagers addition powers, like the Guard or the Masons, tilts the balance toward them. To balance against the Village add roles that hamper them like the Fool or the Hapless Victim.  \n\n The Village wins if all Werewolves are killed.")
        await message.channel.send(embed=embed)

        embed = discord.Embed(title="Werewolf", description="The one everybody wants to be", url="https://werewolf-the-game.fandom.com/wiki/The_Werewolves", color=0xff0000)
        embed.set_thumbnail(
            url="http://p9.storage.canalblog.com/98/39/1355275/103540675_o.jpg")
        embed.add_field(name="Description",
                        value="The Werewolves are a team working against the Villagers. The Werewolves collectively choose a player to kill each night. Each night the Moderator will wake them up as a group and allow them to choose a victim to kill for that night. \n\n The Moderator tells the victim as the day phase starts. \n\n The Werewolves win my achieving parity, or an equal number of remaining Villagers and Werewolves.")
        await message.channel.send(embed=embed)

        embed = discord.Embed(title="Sorcerer", description="The one everybody wants to be", url="https://werewolf-the-game.fandom.com/wiki/The_Sorcerer", color=0xff7300)
        embed.set_thumbnail(
            url="https://www.loups-garous-en-ligne.com/jeu/assets/images/carte5.png")
        embed.add_field(name="Description",
                        value="The Sorcerer is a player on their own team. They choose a player to attempt to dominate each night. If a Villager is chosen, nothing happens. If a Werewolf is chosen, that player joins the Sorcerer’s team, but does not wake with the Sorcerer. \n\nEach night, The Sorcerer chooses a target for the dominated Werewolf. That player is killed. The Dominated Werewolf still wakes with the other Werewolves, but is not allowed to reveal his dominated status. Dominated Werewolves die if the Sorcerer is killed.\n\n The Sorcerer wins if they have dominated a Werewolf and achieved parity with the members of his team and any remaining players. The Werewolves cannot win while the Sorcerer is still alive.\n\n The balance for the Sorcerer is against both the Villagers and the Werewolves. Forming a third team makes the death rate increase.")
        await message.channel.send(embed=embed)

        embed = discord.Embed(title="Cupid", description="The one everybody wants to be", url="https://werewolf-the-game.fandom.com/wiki/The_Cupid", color=0x00aaff)
        embed.set_thumbnail(
            url="https://3.bp.blogspot.com/_0Pz0L1XQR1k/TCG3HLj3fbI/AAAAAAAAAVQ/bRy6FLcG_UA/s320/cupido.png")
        embed.add_field(name="Description",
                        value="On the first night the Cupid chooses two players. The Moderator sets the Cupid back to sleep and then wakes the two players the Cupid has chosen. Those players are now the Lovers. If one of those players dies for any reason the other one dies immediately. After the first night the Cupid is an ordinary Villager. \n\n The Lovers only win if they are both alive at the end of the game. If they are on the same team then they can share in the victories of the others. If they are on opposite teams then they need to be the last two players alive. In which case, the Cupid also wins, living or dead. \n\n The Cupid balances against the Villagers. While they could cause the death of an extra Werewolf, the chances are slim. Most often the Cupid chooses Lovers that cause an extra Villager death.")
        await message.channel.send(embed=embed)

        embed = discord.Embed(title="Seer", description="The one everybody wants to be", url="https://werewolf-the-game.fandom.com/wiki/The_Seer", color=0xc800ff)
        embed.set_thumbnail(
            url="https://p4.storage.canalblog.com/40/56/1355275/103540669_o.jpg")
        embed.add_field(name="Description",
                        value="The Seer is arguably the most powerful and important Villager. The Seer wakes each night and targets a player. The Moderator silently indicates whether that player is a Villager or a Werewolf. Usually the Moderator gives a peace signal for a Villager or makes a Claw motion for a Werewolf. The Seer must find a way to use that knowledge to help the Villagers without becoming the next target of the Werewolves. \n\n The Seer tilts the balance towards the Villagers. They allow for quicker identification of the Werewolves. Frankly without special roles included game theory states that the Werewolves should almost always win.")
        await message.channel.send(embed=embed)

        embed = discord.Embed(title="Hunter", description="The one everybody wants to be", url="https://werewolf-the-game.fandom.com/wiki/The_Hunter", color=0x00ff40)
        embed.set_thumbnail(
            url="https://p6.storage.canalblog.com/65/92/1355275/103540680_o.jpg")
        embed.add_field(name="Description",
                        value="The Hunter is a Villager that chooses a player to kill whenever the Hunter is killed. In a no-reveal game the Hunter tells the Moderator who to kill on the following night before anyone has woken up. \n\n The Hunter is basically neutral. They could kill a Werewolf and help the Villagers, but it is more likely that they will kill a Villager.")
        await message.channel.send(embed=embed)

    if message.content == "test":
        user=message.author
        print(user)
        content="Hello"
        channel = await user.create_dm()
        await channel.send(content)

TOKEN = ''
client.run(TOKEN)
