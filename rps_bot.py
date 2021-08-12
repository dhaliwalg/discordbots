#All the imports that we'd need through Discord.py
import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

#Utilizes a .env file so I can keep the token a secret
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

#Sets command prefix to '!'
bot = commands.Bot(command_prefix="!")

#When bot's ready, prints this to terminal
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


#First command, chooses a random quote from the list and prints it into whatever channel it was called in (ctx)
#aka context channel
@bot.command(name="99", help='Responds with a random quote from Brooklyn 99!')
async def nine_nine(ctx):

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'I wasn\'t hurt that badly. The doctor said all my bleeding was internal. That\'s where the blood\'s supposed to be.',
        'What about me? What if something happens to Jake, and he never gets to meet my baby? I don\'t want to hang out with some stupid baby who\'s never met Jake.',
        'Terry loves yogurt.',


    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

#Rolls x amount of dice with y sides in the context channel (x and y passed with command: !dice 1 6)
@bot.command(name='dice', help='Simulates rolling 2 dice, giving a roll of 2-12.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(' & '.join(dice))

#Flips a coin, printing it in the context channel
@bot.command(name='coinflip', help='Flips a fair coin!')
async def coinflip(ctx):

    coin = [
        'Heads!',
        'Tails!',
    ]

    response = random.choice(coin)
    await ctx.send(response)

#Plays rock paper scissors! Player sends a move with the command, then bot randomly picks an option
#then goes through the if ladder to determine winner: !rps rock
#case doesn't matter but it does need to be spelled correctly
@bot.command(name='rps', help='Play some rock, paper, scissors with me!')
async def rps(ctx, playerMove: str):
    #creates list of bots options
    botMove = [
        'rock',
        'paper',
        'scissors',
    ]
    
    #makes sure the move is valid
    playerMove = playerMove.lower()
    if playerMove not in botMove:
        await ctx.send("Invalid move! Can't fool me!")

    #otherwise, go through the game logic to determine winner (in relation to the player NOT bot)
    #so bot chooses rock, player chooses paper, the player wins so status becomes "win!"
    else:
        botChoice = random.choice(botMove)
        status = ''

        #logic if bot plays rock
        if botChoice == 'rock':
            if playerMove == 'rock':
                status = 'draw!'
            elif playerMove == 'paper':
                status = 'win!'
            else:                       #player plays scissors
                status = 'lose!'

        #logic if bot plays paper
        elif botChoice == 'paper':
            if playerMove == 'rock':
                status = 'lose!'
            elif playerMove == 'paper':
                status = 'draw!'
            else:                       #player plays scissors
                status = 'win!'

        #logic if bot plays scissors
        else:                          
            if playerMove == 'rock':
                status = 'win!'
            elif playerMove == 'paper':
                status = 'lose!'
            else:                       #assume scissors
                status = 'draw!'
        
        #Prints 'botchoice! dang, you status'
        await ctx.send(botChoice + '! dang, you ' + status)

#actually runs the bot with our token, allowing access to the discord api
bot.run(DISCORD_TOKEN)