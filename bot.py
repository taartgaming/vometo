import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests
import json



bot = commands.Bot(command_prefix='?')
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.command()
async def animegif(ctx, arg):
    await ctx.send(arg)
    animeJSON = requests.get("https://api.giphy.com/v1/gifs/random?api_key=" + os.getenv('giphyToken') + "&tag=anime&rating=pg").json()
    print(animeJSON["data"]["embed_url"])

    


client = MyClient()
client.run(os.getenv('botToken'))