############################
# Code will be added after #
# I finish all my other    #
# Projects im working on   #
############################
import discord
from discord.ext import commands

prefix = '$'
token = 'DiscordToken'
client = commands.Bot(description='Easy-Anti', command_prefix=prefix)

@client.event
async def on_ready():
  print('Bot Ready')

client.run(token, reconnect=True)
