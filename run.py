import discord
import asyncio
import config
import time
import os

from config import link, prefix, ownerid
from dontpingthedevslist import nmlist
from discord.ext.commands import Bot
from datetime import datetime, timezone

##
client = Bot(prefix)
client.remove_command('help')


@client.event
async def on_ready():
    print("----------------------")
    print("Logged in")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print(" ")
    date = datetime.now().strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M:%S %p")
    await client.get_channel(546670935986405390).send(str(date))
    await client.change_presence(activity=discord.Game(name="Don't ping the devs || v1.01"))
    print("----------------------")
    print("NIE ZAMYKAĆ TEGO OKNA! xD")
    print("----------------------")
    
#fukcja ELIF elif(sth): do sth -> else + if
    
@client.event
async def on_command_error(ctx, error):
    user_roles = [r.name.lower() for r in ctx.message.author.roles] 
    if any(r in user_roles for r in["senior moderator", "moderators", "staff", "kogamate"]):        
        klorg=str(error)
        if (ctx.command == unmute or ctx.command == delwarn): #and ("not found" in klorg):                      
            if isinstance(error, discord.ext.commands.errors.UserInputError):
                #await ctx.send("```An error occured: " + str(error) + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
                print(error)
            else:
                print(error)
                #await ctx.send("```An error occured" + str(error) + '\n' + "Please contact Superplus#2392 if you get that message" + '\n' + "-- This message will be deleted automatically in 180 seconds. --```", delete_after=180)

    
@client.event
async def on_message(message):
    channel = message.channel
    channel.id = message.channel.id
    server = message.guild
    server.id = message.guild.id
    bum = server.get_member(message.author.id) 
    mutedrole = discord.utils.get(server.roles,name="Muted")
    warningrole = discord.utils.get(server.roles,name="Warning")
    
    #kergo = message.channel
    kergo = await client.fetch_channel(str("433644659018039296")) #kogama-log
    #harpo = message.channel
    harpo = await client.fetch_channel(str("444589577341108225")) #kds-log
    #cerbo = message.channel
    cerbo = await client.fetch_channel(str("547516455785070612")) #kogamabr-log
    
    
    date = datetime.now().strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M:%S %p")
    user_roles = [r.name.lower() for r in bum.roles]
    belo = int(message.guild.id)
    chano = int(message.channel.id)
    mem = str(message.author)
    memid = str(message.author.id)
    
    if int(message.author.id) == int(client.user.id):
        return
    
    if message.content == "<@258664801465532416>":
        if belo == 415885418903371777:
            if not any(r in user_roles for r in["senior moderator", "moderators", "staff", "kogamate"]):
                if chano == 436444254173397009:
                    try:
                        msg = await channel.send("Por favor, escreva sua mensagem na mesma linha da menção," + " " + str(mem) + " with userid " + str(memid))                   
                    except Exception as e:
                        print(e)
                else:
                    pass
                                    
    if any(x in message.content for x in nmlist):
                                
        if belo == 415885418903371777: #kogama
            if message.author.id == 415794283744985098:
                return
            if not any(r in user_roles for r in["senior moderator", "moderators", "staff", "kogamate", "bots"]):
                try:
                    msg = await channel.send("Don't ping the devs," + " " + str(mem) + " with userid " + str(memid))                   
                except Exception as e:
                    print(e)
                if "warning" in user_roles:
                    try:
                        await message.author.add_roles(mutedrole, reason = "Pinging the developer")
                    except:
                        try:
                            await kergo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** ~~Mute~~ / exeption occured - no punishment" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                        except:
                            pass
                        norolemuted = await channel.send("``` I can't find Muted role, it's the higher rank than my highest role or I don't have permission to manage roles."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
                        return
                    try:
                        await kergo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** Mute" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                    except:
                        pass
                    warn = await channel.send(message.author.mention + ", you have been muted for disregarding the previous warning and pinging the developer.")
                    try:
                        await message.author.remove_roles(warningrole)
                    except:
                        pass
                    await asyncio.sleep(600)
                    try:                        
                        await message.author.remove_roles(mutedrole, reason = "Auto")
                    except:
                        return
                else:   
                    try:
                        await message.author.add_roles(warningrole, reason = "Pinging the developer")
                    except Exception as e:
                        try:
                            await kergo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** ~~Warning~~ / exeption occured - no punishment" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                        except Exception as zero:
                            print(zero)
                            pass
                        norolewarning = await channel.send("``` I couldn't find Warning role, it's the higher rank than my highest role or I don't have permission to manage roles."  + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
                        return
                    try:
                        await kergo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** Warning" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                    except:
                        pass
                    
        if belo == 547448615187251200: #kogamabr
            if message.author.id == 415794283744985098:
                return
            if not any(r in user_roles for r in["staff", "gerente da comunidade", "moderador iniciante"]):
                try:
                    msg = await channel.send("Não mencione os Desenvolvedores," + " " + str(mem) + " com ID de usuário " + str(memid))                   
                except Exception as e:
                    print(e)
                if "warning" in user_roles:
                    try:
                        await message.author.add_roles(mutedrole, reason = "Mencionar os desenvolvedores") 
                    except Exception as e:
                        try:
                            await cerbo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** ~~Mute~~ / exeption occured - no punishment" + '\n' + "**Exception: **" + str(e) + '\n' + "**Message content**: ```" + str(message.content) + "```")
                        except:
                            pass
                        norolemuted = await channel.send("``` Eu não consegui achar o cargo de Muted, ele está em um nível acima do meu cargo mais alto ou eu não tenho permissão para gerenciar cargos."  + '\n' + "-- Esta mensagem será apagada automaticamente em 30 segundos. --```", delete_after=30)
                        return
                    try:
                        await cerbo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** Mute" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                    except:
                        pass
                    warn = await channel.send(message.author.mention + ", você foi silenciado por ignorar seu aviso anterior sobre mencionar os desenvolvedores.")
                    try:
                        await message.author.remove_roles(warningrole)
                    except:
                        pass
                    await asyncio.sleep(10)
                    try:                        
                        await message.author.remove_roles(mutedrole, reason = "Auto")
                    except:
                        return
                else:   
                    try:
                        await message.author.add_roles(warningrole, reason = "Mencionar os desenvolvedores")
                    except Exception as e:
                        try:
                            await cerbo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** ~~Warning~~ / exeption occured - no punishment" + '\n' + "**Exception: **" + str(e) + '\n' + "**Message content**: ```" + str(message.content) + "```")
                        except:
                            pass
                        norolewarning = await channel.send("``` Eu não consegui achar o cargo de Warning, ele está em um nível acima do meu cargo mais alto ou eu não tenho permissão para gerenciar cargos."  + '\n' + "-- Esta mensagem será apagada automaticamente em 30 segundos. --```", delete_after=30)
                        return
                    try:
                        await cerbo.send("Server: " + str(server) + ", server id: " + str(server.id) + '\n' + "**Channel**: " + str(channel) + ", channel id: " + str(channel.id) + '\n' + "**User:** " + str(mem) + " " + str(memid) + '\n' + str(date) + '\n' + "**Punishment:** Warning" + '\n' + "**Message content**: ```" + str(message.content) + "```")
                    except:
                        pass                
    await client.process_commands(message)
    
#3.1
@client.command(pass_context = True)
async def unmute(ctx, *, member : discord.Member = None):
 
    server = ctx.message.guild
   # bum = server.get_member(ctx.message.author.id)
    bum = await server.fetch_member(str(ctx.message.author.id))
    channel = ctx.message.channel
    user_roles = [r.name.lower() for r in bum.roles]
    can_manage_roles = (server.me).guild_permissions.manage_roles
    role = discord.utils.get(server.roles,name="Muted")  

    if not any(r in user_roles for r in["senior moderator", "moderators", "junior moderators", "staff", "gerente da comunidade"]):
        return        
    if member == None:
        ment = await ctx.send("```" + str(ctx.message.author) +  ", no user mentioned." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
        return
    member_roles = [r.name.lower() for r in member.roles]        
    if can_manage_roles == False:
        botperm = await ctx.send("```" + str(ctx.message.author) + ", I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
        return
       
    if "muted" not in member_roles:
        pedro = await ctx.send("```" + str(ctx.message.author) + ", I can't unmute them, they're not muted." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)     
        return 

    await member.remove_roles(role, reason=("Role removed by moderator | " + "Responsible moderator: " + (str(ctx.message.author.name) + " (ID:" + str(ctx.message.author.id) + ")")))   
    await ctx.send("**" + str(member) + "** has no longer Muted role!")
        
        
@client.command(pass_context = True)
async def delwarn(ctx, member : discord.Member = None):

    server = ctx.message.guild
    #bum = server.get_member(ctx.message.author.id)
    bum = await server.fetch_member(str(ctx.message.author.id))
    user_roles = [r.name.lower() for r in bum.roles]
    channel = ctx.message.channel
    can_manage_roles = (server.me).guild_permissions.manage_roles
    role = discord.utils.get(server.roles,name="Warning")  

    if not any(r in user_roles for r in["senior moderator", "moderators", "junior moderators", "staff", "gerente da comunidade"]):
        return        
    if (member == None):
        ment = await ctx.send("```" + str(ctx.message.author) +  ", no user mentioned." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
        return
    member_roles = [r.name.lower() for r in member.roles]       
    if can_manage_roles == False:
        botperm = await ctx.send("```" + str(ctx.message.author) + ", I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)
        return
       
    if "warning" not in member_roles:
        pedro = await ctx.send("```" + str(ctx.message.author) + ", this user doesn't have Warning role." + '\n' + "-- This message will be deleted automatically in 30 seconds. --```", delete_after=30)        
        return 

    await member.remove_roles(role, reason=("Role removed by moderator | " + "Responsible moderator: " + (str(ctx.message.author.name) + " (ID:" + str(ctx.message.author.id) + ")")))   
    await ctx.send("**" + str(member) + "** has no longer Warning role!")
                  


#m3
@client.command(pass_context=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id == ownerid:
        await client.change_presence(activity=discord.Game(name=game))
        await ctx.message.delete()

client.run(os.getenv('TOKEN')) 
