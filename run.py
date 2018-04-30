import discord
import asyncio
import config
import time
import os

from config import link, prefix, ownerid
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
    await client.change_presence(game=discord.Game(name="Don't ping the devs"))       
    if any(word in message.content for word in["<@215761992474951681>", "<@224809879884398592>", "<@354641560979111936>", "<@371976663098982400>", "<@311130875461107722>", "<@334269708268470293>", "<@163270868938653698>", "<@281067479927881740>", "<@405654489987547146>", "<@197130820975067137>", "<@249187671912611840>", "<@146009550699364352>", "<@258540501261746176>"]):
        user_roles = [r.name.lower() for r in ctx.message.author.roles]
        belo = int(server.id)
        if belo == 359426518730145802:
            if message.author.server_permissions.ban_members == False:
                mem = str(message.author)
                memid = str(message.author.id)
                try:
                    msg = await client.send_message(message.channel, "Don't ping the devs," + " " + str(mem) + " with userid " + str(memid))                    
                except Exception as e:
                    print(e)
                    return
        else:         
            if not any(r in user_roles for r in["senior moderator", "moderator", "staff"]):
                mem = str(message.author)
                memid = str(message.author.id)
                try:
                    msg = await client.send_message(message.channel, "Don't ping the devs," + " " + str(mem) + " with userid " + str(memid))                    
                except Exception as e:
                    print(e)

    
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

client.run(os.getenv('TOKEN')) 
