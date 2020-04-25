import discord
from discord.ext import commands
from time import asctime
import random
# from testingCommands import flipCoin

TOKEN = "NzAxOTMwODA2Njc0ODQ5Nzk0.Xp4qfw.V9fQrMKksl5Gm4usUcXEnmtMRQI"

client = commands.Bot(command_prefix= '_')

@client.event
async def on_ready():
    print("I'm ready\n")
    print(asctime())

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    created_at = message.created_at
    print("At {}\n{} said the following: {}".format(created_at, author, content))
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    # await client.send_message(channel, "{} has deleted something".format(author))
    await channel.send("{} has deleted something here".format(author))

# some commands

@client.command()
async def flipCoin(ctx,*args):
    print(args)
    if args:
        choice = args[0]
    else:
        choice = None
    aux = random.randint(0,1)
    if aux == 1:
        r = "heads"
    elif aux == 0:
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
            await ctx.send("Sorry, didn't understand you there, what is '{}'?".format(choice.upper()))

@client.command()
async def getRandom(ctx,*args):
    print(args)
    try:
        r = random.randint(int(args[0]),int(args[1]))
    except:
        try:
            r = random.randint(0,int(args[0]))
        except:
            try:
                r =random.randint(int(args[0]),0)
            except:
                r =random.randint(0,10)
    await ctx.send("Number is {}".format(r))

# @client.command()
# async def setReminder(ctx, *args):


client.run(TOKEN)


