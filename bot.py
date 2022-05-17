# @filename bot.py
# @author Dysan
# @notice This is a simple python discord bot
# @custom:todo 
#   Add config file 
#   Load commands from command folder (specified in the config file)
#   Add ability to read texts from specific channel

#imports
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import configparser
import inspect

### Global Vars
config_dict = {} #dictionary that contains the config

### Global Constants
DEFAULTCONFIGFILE = 'botconfig.ini'
DEFAULTCOMMANDPREFIX = 'b!'
DEFAULTCOMMANDFOLDER = '.\commands'
DEBUG = 1

def debug_message(message):
    global DEBUG
    if (DEBUG):
        print ("---DEBUG Message:", inspect.stack()[1].function , "() :" , inspect.stack()[1].lineno , " - " , message)
        

def load_config():
    try:
        global config_dict
        config = configparser.ConfigParser()
        config.read({DEFAULTCONFIGFILE}) 
        config_dict = dict(config.items('botconfig'))
        debug_message(config_dict)

    except:
        print ("Failed to read or parsing {DEFAULTCONFIGFILE} file. Loading Default Config...")
        config_dict['command_prefix'] = DEFAULTCOMMANDPREFIX
        config_dict['command_folder'] = DEFAULTCOMMANDFOLDER
    
    print ("Following settings are loaded:")    
    print ("command_prefix:", config_dict['command_prefix'])    
    print ("command_folder:", config_dict['command_folder'])


load_dotenv() #load .env file
load_config() #load the botconfig.ini file




TOKEN = os.getenv('DISCORD_TOKEN') #grab the DISCORD_TOKEN from env var
GUILD = os.getenv('DISCORD_GUILD') #grab the DISCORD_GUILD from env var

#set bot prefix
bot = commands.Bot(command_prefix = config_dict['command_prefix'])


# @notice DM command, will send DM to specified user with a message. Only members who have the role 'Infosec' will be able to call this command.
# @param username Discord username to send a DM
# @param message the message to send to the discord user
# @custom:role Infosec is a required role for this command
# @custom:example !DM @user this is a test
@bot.command()
@commands.has_role('Infosec')
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)

# @notice echo command for bot
# @param message to echo
# @custom:role Infosec is a required role for this command
# @custom:example !echo this is a message
@bot.command()
@commands.has_role('Infosec')
async def echo(ctx, *, message=None):
    await ctx.send(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(error)


bot.run(TOKEN)

