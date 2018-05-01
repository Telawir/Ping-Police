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
    if any(word in message.content for word in["<@224809879884398592>", "<@354641560979111936>", "<@371976663098982400>", "<@311130875461107722>", "<@334269708268470293>", "<@163270868938653698>", "<@281067479927881740>", "<@405654489987547146>", "<@197130820975067137>", "<@249187671912611840>", "<@146009550699364352>", "<@258540501261746176>", "<@300978444962103296>"]):
        user_roles = [r.name.lower() for r in message.author.roles]
        belo = int(server.id)
        mem = str(message.author)
        memid = str(message.author.id)
                
        if belo == 359426518730145802:
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
            if not any(r in user_roles for r in["senior moderator", "moderators", "staff", "kogamate"]):
                try:
                    msg = await client.send_message(message.channel, "Don't ping the devs," + " " + str(mem) + " with userid " + str(memid))                   
                except Exception as e:
                    print(e)

                if "warning" in user_roles:
                    try:
                        await client.add_roles(message.author, mutedrole)
                    except:
                        try:
                            await client.send_message(kergo, "Server: " + str(server) + ", server id: " + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date + '\n' + "**Punishment:** ~~Mute~~ / exeption occured - no punishment")
                        except:
                            pass
                        norolemuted = await client.send_message(message.channel, "``` I can't find Muted role, it's the higher rank than my highest role or I don't have permission to manage roles."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
                        await asyncio.sleep(30)
                        try:
                            await client.delete_message(norolemuted)
                        except:
                            return
                        return
                    try:
                        await client.send_message(kergo, "Server: " + str(server) + ", server id: " + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date + '\n' + "**Punishment:** Mute")
                    except:
                        pass
                    warn = await client.send_message(message.channel, message.author.mention + ", you have been muted for disregarding the previous warning and pinging the developer.")
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
                        await client.add_roles(message.author, warningrole)
                    except Exception as e:
                        try:
                            await client.send_message(kergo, "Server: " + str(server) + ", server id: " + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date + '\n' + "**Punishment:** ~~Warning~~ / exeption occured - no punishment")
                        except:
                            pass
                        norolewarning = await client.send_message(message.channel, "``` I couldn't find Warning role, it's the higher rank than my highest role or I don't have permission to manage roles."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
                        await asyncio.sleep(30)
                        try:
                            await client.delete_message(norolewarning)
                        except:
                            return
                    try:
                        await client.send_message(kergo, "Server: " + str(server) + ", server id: " + server.id + '\n' + "**User:** " + mem + " " + memid + '\n' + date + '\n' + "**Punishment:** Warning")
                    except:
                        pass
                        
    await client.process_commands(message)

    
#3.1
@client.command(pass_context = True)
async def unmute(ctx, *, member : discord.Member = None):

    try:

        user_roles = [r.name.lower() for r in ctx.message.author.roles] 
        server = ctx.message.server
        channel = ctx.message.channel
        can_manage_roles = channel.permissions_for(server.me).manage_roles
        role = discord.utils.get(server.roles,name="Muted")  

        if not any(r in user_roles for r in["senior moderator", "moderators", "staff"]):
            return
        
        if member == None:
            ment = await client.say("```" + str(ctx.message.author) +  ", no user mentioned." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
            await asyncio.sleep(30)
            await client.delete_message(ment)
            return
        member_roles = [r.name.lower() for r in member.roles]
        
        if can_manage_roles == False:
            botperm = await client.say("```" + str(ctx.message.author) + ", I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
            await asyncio.sleep(30)
            await client.delete_message(botperm)
            return
       
        if "muted" not in member_roles:
            pedro = await client.say("```" + str(ctx.message.author) + ", I can't unmute them, they're not muted." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
            await asyncio.sleep(30)
            await client.delete_message(pedro)        
            return 
        
        pass
        
        await client.remove_roles(member, role)
        await client.say("**" + str(member) + "** has no longer Muted role!")
        
    except:
        server = server
        
        
@client.command(pass_context = True)
async def delwarn(ctx, *, member : discord.Member = None):

    try:
        user_roles = [r.name.lower() for r in ctx.message.author.roles] 
        server = ctx.message.server
        channel = ctx.message.channel
        can_manage_roles = channel.permissions_for(server.me).manage_roles
        role = discord.utils.get(server.roles,name="Warning")  

        if not any(r in user_roles for r in["senior moderator", "moderators", "staff"]):
            return
        
        if member == None:
            ment = await client.say("```" + str(ctx.message.author) +  ", no user mentioned." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
            await asyncio.sleep(30)
            await client.delete_message(ment)
            return
        member_roles = [r.name.lower() for r in member.roles]
        
        if can_manage_roles == False:
            botperm = await client.say("```" + str(ctx.message.author) + ", I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
            await asyncio.sleep(30)
            await client.delete_message(botperm)
            return
       
        if "warning" not in member_roles:
            pedro = await client.say("```" + str(ctx.message.author) + ", this user doesn't have Warning role." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```")
            await asyncio.sleep(30)
            await client.delete_message(pedro)        
            return 
        
        pass
        
        await client.remove_roles(member, role)
        await client.say("**" + str(member) + "** has no longer Warning role!")
        
    except:
        server = server                   


#m3
@client.command(pass_context=True)
async def setgame(ctx, *, game):
    """Sets my game (Owner only)"""
    if ctx.message.author.id == (ownerid):
        message = ctx.message
        await client.whisper("Game was set to **{}**!".format(game))
        await client.change_presence(game=discord.Game(name=game))

client.run(os.getenv('TOKEN')) 
