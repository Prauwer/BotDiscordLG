# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import discord
import os


def print_hi(name):
    TOKEN = 'OTMwNzMzNTI1MzI0NDA2ODE0.Yd6LJA.ysL4rR9kWF_PqyOiqws92JwpKAU'

    client = discord.Client()

    @client.event
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    client.run(TOKEN)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
