import os
import random
import discord
from discord import client
from dotenv import load_dotenv
from discord.ext import commands
import requests
import json

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD_NAME = os.getenv('GUILD_NAME')



def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from B99.')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates a rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_slides: int):
    try:
        dice = [
            str(random.choice(range(1, number_of_slides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))
    except commands.errors.BadArgument:
        await ctx.send('Number of dice and number of sides should be numbers.')


@bot.command(name='inspire', help='Generates a motivational quote.')
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)




bot.run(TOKEN)