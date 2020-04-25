import discord
from discord.ext import commands
import numpy as np
import random

from testing import client
client = commands.Bot(command_prefix= '_')
@client.command()
async def flipCoin(ctx,*args):
    print(args)
    if args:
        choice = args[0]
    else:
        choice = None
    aux = random.randint(0,1)
    if aux ==1:
        r = "heads"
    elif aux ==0:
        r = 'tails'
    await ctx.send("It was {}\n".format(r))
    if choice != None:
        choice = choice.lower()
        if choice == 'heads' or choice == 'tails':
            if choice != r:
                await ctx.send("You lose")
            else:
                await ctx.send("You win")
        else:
            await ctx.send("Sorry, didn't understand you there, what is {}?".format(choice.upper()))
