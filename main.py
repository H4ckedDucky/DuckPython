# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')



@bot.event
async def on_ready():
    os.system('color a')
    os.system('cls')
    print(f'{bot.user} has succsessfully connected to Discord!')

@bot.command(name='Ping', help='Respondes with Pong!', aliases = ['ping'])
async def pong_command(ctx):
    Pong = [
        f'Pong!, {ctx.message.author.mention}',
       
      
    ]

    response = random.choice(Pong)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.', category='misc')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

#Moderatiom

@bot.command(aliases= ['purge', 'delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=None): # Set default value as None
    if amount == None:
        await ctx.channel.purge(limit=1000000)
    else:
        try:
            int(amount)
        except: # Error handler
            await ctx.send('Please enter a valid integer as amount.')
        else:
            await ctx.channel.purge(limit=amount)




bot.run('OTczMjA0MTcyMzE5MTA5MTcx.GVN48o.3-BXnmMS4DuWqqNHlvWXAayTytXNPMLQhg9IH0')