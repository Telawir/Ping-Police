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
    server.id = message.server.id
    mutedrole = discord.utils.get(server.roles,name="Muted")
    warningrole = discord.utils.get(server.roles,name="Warning")
    kergo = message.channel
    kergo = client.get_channel("433644659018039296")

    date = datetime.now().strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M:%S %p")
    
    await client.change_presence(game=discord.Game(name="Don't ping the devs"))       
    if any(word in message.content for word in["<@224809879884398592>", "<@354641560979111936>", "<@371976663098982400>", "<@311130875461107722>", "<@334269708268470293>", "<@163270868938653698>", "<@281067479927881740>", "<@405654489987547146>", "<@197130820975067137>", "<@249187671912611840>", "<@146009550699364352>", "<@258540501261746176>"]):
        user_roles = [r.name.lower() for r in message.author.roles]
        belo = int(server.id)
        mem = str(message.author)
        memid = str(message.author.id)
                
        if belo == 359426518730145802:
            
            msg0 = await client.send_message(message.channel, "0")
            if message.author.server_permissions.ban_members == False:
                try:
                    await client.send_message(kergo, str(server) + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date)
                except:
                    pass
                try:
                    msg = await client.send_message(message.channel, "Don't ping the devs," + " " + str(mem) + " with userid " + str(memid))                    
                except Exception as e:
                    print(e)
                    return
        else:         
            
            msg1 = await client.send_message(message.channel, "1")
            if not any(r in user_roles for r in["senior moderator", "moderators", "staff", "kogamate"]):
                
                msg2= await client.send_message(message.channel, "2")
                try:
                    msg3 = await client.send_message(message.channel, "3Don't ping the devs," + " " + str(mem) + " with userid " + str(memid))                    
                except Exception as e:
                    print(e)
                    
                    msg4 = await client.send_message(message.channel, "4")

                if "warning" in user_roles:
                    
                    msg5 = await client.send_message(message.channel, "5")
                    try:
                        await client.add_roles(message.author, mutedrole)
                        
                        msg6 = await client.send_message(message.channel, "6")
                    except:
                        try:
                            
                            msg7 = await client.send_message(message.channel, "7")
                            await client.send_message(kergo, "Server: " + str(server) + ", server id: " + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date + '\n' + "**Punishment:** ~~Mute~~ / exeption occured - no punishment")
                        except:
                            
                            msg8 = await client.send_message(message.channel, "8")
                            pass
                        norolemuted = await client.send_message(message.channel, "``` 9I can't find Muted role, it's the higher rank than my highest role or I don't have permission to manage roles."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
                        await asyncio.sleep(30)
                        try:
                            await client.delete_message(norolemuted)
                        except:
                            return
                        return
                    try:
                        
                        msg10 = await client.send_message(message.channel, "10")
                        await client.send_message(kergo, "Server: " + str(server) + ", server id: " + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date + '\n' + "**Punishment:** Mute")
                    except:
                        
                        msg11 = await client.send_message(message.channel, "11")
                        pass
                    warn = await client.send_message(message.channel, message.author.mention + ", 12you have been muted for disregarding the previous warning and pinging the developer.")
                    try:
                        await client.remove_roles(message.author, warningrole)
                    except:
                        pass
                    await asyncio.sleep(600)
                    try:                        
                        await client.remove_roles(message.author, mutedrole)
                    except:
                        return
                else:
                    try:
                        
                        msg13 = await client.send_message(message.channel, "13")
                        await client.add_roles(message.author, warningrole)
                    except Exception as e:
                        try:
                            
                            msg14 = await client.send_message(message.channel, "14" + str(e))
                            await client.send_message(kergo, "Server: " + str(server) + ", server id: " + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date + '\n' + "**Punishment:** ~~Warning~~ / exeption occured - no punishment")
                        except:
                            pass
                        norolewarning = await client.send_message(message.channel, "```15 I couldn't find Warning role, it's the higher rank than my highest role or I don't have permission to manage roles."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
                        await asyncio.sleep(30)
                        try:
                            await client.delete_message(norolewarning)
                        except:
                            return
                    try:
                        
                        msg16 = await client.send_message(message.channel, "16")
                        await client.send_message(kergo, "Server: " + str(server) + ", server id: " + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date + '\n' + "**Punishment:** Warning")
                    except:
                        pass
                    
                    



    
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
