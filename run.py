import discord
import asyncio
import config
import time
import os

from config import link, prefix, ownerid, pinglist
from discord.ext.commands import Bot
from datetime import datetime, timezone

client = Bot(prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print("----------------------")
    print("Logged in")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("----------------------")
    
@client.event
async def on_message(message):
    server = message.server
          
    if any(word in message.content for word in["<@215761992474951681>", "<@402561083950366730>", "<@438819749065916417>"]):
        mem = str(message.author)
        memid = str(message.author.id)
        try:
            msg = await client.send_message(message.channel, "Don't ping the devs," + " " + str(mem) + " with userid " + str(memid))
        except:
            return

    
#m2
@client.command()
async def ping():
    '''See if The Bot is Working'''
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = time.time() - pingtime
    await client.edit_message(pingms, ":ping_pong:  time is `%.0001f seconds`" % ping)

#m3
@client.command(pass_context=True)
async def setgame(ctx, *, game):
    """Sets my game (Owner only)"""
    if ctx.message.author.id == (ownerid):
        message = ctx.message
        await client.whisper("Game was set to **{}**!".format(game))
        await client.change_presence(game=discord.Game(name=game))

#m4 
@client.command()
async def botinvite():
    '''Gives you a link to invite this bot to your server!'''
    await client.say("Check Your Dm's :wink:")
    await client.whisper(link)



client.run(os.getenv('TOKEN')) 
