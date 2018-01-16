import discord
import asyncio
import config
import time
import os


from config import link, prefix, ownerid
from discord.ext.commands import Bot

client = Bot(prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print("----------------------")
    print("Logged in")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("----------------------")


#m1 
@client.command(pass_context=True)
async def help(ctx):
    pref0 = str(prefix)
    author = ctx.message.author
   
    m1 = str("**help**               :: Shows this message")
    m2 = str("**ping**               :: Checks if the bot works")
    m3 = str("**setgame**       :: Sets my game (owner only)")
    m4 = str("**botinvite**      :: Gives you a link to invite this bot to your server")
    
    g1 = str("**serverinvite**         :: Gives you an invitation link to this server")
    g2 = str("**serverbans**                    :: Gets a list of banned users")    
    g3 = str("**userinfo [user]**   :: Displays Info About The User // __in development__ //")
    g4 = str("**serverinfo**            :: Displays Info About The Server")

    t1 = str("**mute [user] <reason>**   :: Mutes a member (requires Silenced role)")
    t2 = str("**unmute [user]**                 :: Unmutes a member:")
    t3 = str("**purge [amount]**               :: Deletes 2-100 messages from the channel")
    t4 = str("**kick [user]**                        :: Kicks a member")
    t5 = str("**ban [user] <reason>**      :: Bans a member")
    t6 = str("**soft [user] <reason>**     :: Bans and automatically unbans a member, deletes their messages from the last 24h.")


    got = str(pref0)     
    mwot = str(m1 + '\n' + m2 + '\n' + m3 + '\n' + m4) 
    gwot = str(g1 + '\n' + g2 + '\n' + g3 + '\n' + g4)
    twot = str(t1 + '\n' + t2 + '\n' + t3 + '\n' + t4 + '\n' + t5 + '\n' + t6)
    
    join = discord.Embed(title = 'All the available bot commands', description = 'Glop Blop v1.0', colour = 0x0085ff);
    join.add_field(name = '> Prefix:', value = 'The current bot prefix is **' + str(pref0) + '**');
    join.add_field(name = '> Bot:', value = str(mwot));
    join.add_field(name = '> Server:', value = str(gwot));
    join.add_field(name = '> Administration:', value = str(twot));
    join.set_footer(text = 'Created for: %s'%author);

    try:
        await client.say(embed = join);
    except:
        miss = await client.say(ctx.message.author.mention + " Embed links permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(miss)
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

#g1 gets a server invite and pms it to the user who requested it  

@client.command(pass_context = True)
async def serverinvite(ctx):
    """Pm's invitation link to the server to the user who requested it"""
    invite = await client.create_invite(ctx.message.channel,max_uses=1,xkcd=True)
    await client.whisper(invite.url)
    await client.say("Check Your Dm's :wink: ")

#g2 Gets a List of Bans From The Server

@client.command(pass_context = True)
async def serverbans(ctx):
    '''Gets a list of banned users'''  
    if ctx.message.author.server_permissions.manage_server == False:
        erg = await client.say(ctx.message.author.mention + " You do not have permission to view audit log. " + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(erg)
        return
    try:
        x = await client.get_bans(ctx.message.server)
    except:
        miss = await client.say(ctx.message.author.mention + " I don't have permissions to do that." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(miss)
        return
    
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of the banned users", description = x, color = 0xFFFFF)
    try:
        await client.say(embed = embed);
    except:
        miss = await client.say(ctx.message.author.mention + " Embed links permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(miss)
        return

####
#g3
@client.command(pass_context = True)
async def userinfo(ctx, member : discord.Member=None):
    '''Displays Info About The User ----- WORK IN PROGRESS! '\n' '''

    server = ctx.message.server
    user = ctx.message.author
    joined_at = user.joined_at
    user_joined = joined_at.strftime("%d %b %Y %H:%M")
    joined_on = "{}".format(user_joined)

    if member == None:
        nous = await client.say(ctx.message.author.mention + " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(nous)
        return     
       
    emb = discord.Embed(title= '%s '%str(member), description = member.mention + ' (ID: ' + str(member.id) + ')', colour = 0x0085ff);
    emb.set_thumbnail(url = member.avatar_url);
    emb.add_field(name = '__JOINED__', value = joined_on);    
    emb.set_footer(text = (user.mention));

    try:
        await client.say(embed = emb);
    except:
        miss = await client.say(ctx.message.author.mention + " Embed links permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(miss)
        return   

#g4 - Lists Info About The server

@client.command(pass_context = True, aliases=['sinfo', 'si'])
async def serverinfo(ctx):

        server = ctx.message.server
        roles = [x.name for x in server.role_hierarchy]
        role_length = len(roles)
        roles = ', '.join(roles);
        channels = len(server.channels);
        time = str(server.created_at); time = time.split(' '); time= time[0];

        embed = discord.Embed(description= "(ID: " + str(server.id) + ")",title = 'Info on ' + str(server), colour = 0x0085ff);
        embed.set_thumbnail(url = server.icon_url);
        embed.add_field(name = ' > Channels', value = "* " + str(channels) + " channels" + '\n' + "* AFK: " + str(server.afk_channel) + '\n' + "* AFK Timeout: " + str(server.afk_timeout));
        embed.add_field(name = ' > Members', value = "* " + str(server.member_count) + " members" + '\n' + "* Owner: " + str(server.owner) + '\n' + "* Onwer ID: " + str(server.owner.id));
        embed.add_field(name = ' > Other', value = "* Server Region: '%s'"%str(server.region) + '\n' + "* Created on: " + server.created_at.__format__(' %d %B %Y at %H:%M:%S') + '\n' + "* Verification Level: " + str(server.verification_level) + '\n' + "* Roles: '%s'"%str(role_length));

        try:
            await client.say(embed = embed);
        except:
            miss = await client.say(ctx.message.author.mention + " Embed links permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            await client.delete_message(miss)
        return

#t1 - Mutes a Member From The server

@client.command(pass_context = True)

async def mute(ctx, member : discord.Member = None, *, reason : str = 1):
    
    '''Mutes A Memeber'''

    server = ctx.message.server
    role = discord.utils.get(server.roles,name="Silenced")
    channel = ctx.message.channel
    can_manage_roles = channel.permissions_for(server.me).manage_roles

    if ctx.message.author.server_permissions.administrator == False:
        perm = await client.say(ctx.message.author.mention + " You do not have admin permissions." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(perm)
        return
    
    if can_manage_roles == False:
        botperm = await client.say(ctx.message.author.mention + " I don't have permission to manage roles." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(botperm)
        return     
    
    if member == None:
        ment = await client.say(ctx.message.author.mention +  " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(ment)
        return
    pass

    await client.add_roles(member, role)
    mutestart = await client.say(":mute: **%s** is now muted for 5 minutes! Wait for an unmute "%member.mention)
    channel = ctx.message.channel
    
    join = discord.Embed(description="trutututut",title = "Wyciszenie", colour = 0xFF7A00);
    join.add_field(name = 'User', value = str(member.mention) + '\n' + str(member));
    join.add_field(name = 'Moderator', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    join.add_field(name = 'Length', value = str("300 seconds"));
    join.add_field(name = 'Reason', value = str((reason)));
    join.set_footer(text ='Glop Blop v1.0');
        
    ujoin = discord.Embed(description="trutututut",title = "Wyciszenie", colour = 0xFF7A00);
    ujoin.add_field(name = 'User', value = str(member.mention) + '\n' + str(member));
    ujoin.add_field(name = 'Moderator', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    ujoin.add_field(name = 'Lenght', value = str("300 seconds"));
    ujoin.set_footer(text ='Glop Blop v1.0');

    if reason == 1:
        try:
            await client.say(embed = ujoin);
        except:
            await client.say("Moderator: " + str(ctx.message.author))
            return
    else:
        try:
            await client.say(embed = join);
        except:
            await client.say("Moderator: " + str(ctx.message.author) + ", reason: " + str(reason) + ".")
            return
    
    await asyncio.sleep(300)
    role = discord.utils.get(server.roles,name="Silenced")
    member_roles = [r.name.lower() for r in member.roles]
    if "silenced" in member_roles:
        await client.remove_roles(member, role)
        mutestop = await client.say(":loud_sound: **%s** is now Unmuted!"%member.mention)   
    return

#t2 - Unmutes a member

@client.command(pass_context = True)
async def unmute(ctx, *, member : discord.Member):
    '''Unmutes The Muted Memeber'''
    
    server = ctx.message.server
    role = discord.utils.get(server.roles,name="Silenced")
    member_roles = [r.name.lower() for r in member.roles]
    user_roles = [r.name.lower() for r in ctx.message.author.roles]
    
    if ctx.message.author.server_permissions.administrator == False:
        perm = await client.say(ctx.message.author.mention + " You're not server admin." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(perm)        
        return
    if "silenced" not in member_roles:
        pedro = await client.say(ctx.message.author.mention + " I can't unmute them, they're not muted." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(pedro)        
        return 
        
    pass

    await client.remove_roles(member, role)
    await client.say(":loud_sound: **%s** is now Unmuted!"%member.mention)


#t3 - Clears The Chat

@client.command(pass_context=True)       
async def purge(ctx, number : int = 34871):
    '''Clears The Chat 2-100'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]
    server = ctx.message.server
    channel = ctx.message.channel
    can_deletemessages = channel.permissions_for(server.me).manage_messages
    can_sendmessages = channel.permissions_for(server.me).send_messages

    if  not can_sendmessages:
        return 
    
    if ctx.message.author.server_permissions.manage_messages == False:
        borg = await client.say(ctx.message.author.mention + " You do not have permission to manage and delete messages." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        try: 
            await client.delete_message(borg)
        except:
            return
        return
    
    if  not can_deletemessages:
        perm = await client.say(ctx.message.author.mention + " Manage messages permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        try: 
            await client.delete_message(perm)
        except:
            return
        return
    
    if number == 34871:
        terp = await client.say(ctx.message.author.mention + " No message number was selected." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        try: 
            await client.delete_message(terp)
            return
        except:
            return
        return
                                
    if not number > 1 or not number < 101:
        dekr = await client.say(ctx.message.author.mention + " You can only delete messages in the range of [2, 100]." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        try: 
            await client.delete_message(dekr)
        except:
            return
        return
        
    pass

    try:
        await client.delete_message(ctx.message)
    except:
        print('o')
        return
    mgs = []
    number1 = int(number)
    try:
        async for x in client.logs_from(ctx.message.channel, limit = number1):
            mgs.append(x)

    except:
        print('no chyba nie')
        return

    try:
        await client.delete_messages(mgs)
        number = str(number1)
    except Exception as e:
        if 'BAD REQUEST' in str(e):
            miser = await client.say(ctx.message.author.mention + " I can only bulk delete messages that are under 14 days old." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            try:
                await client.delete_message(miser)
            except:
                return
            return
        if 'Forbidden' in str(e):
            miss = await client.say(ctx.message.author.mention + " Manage messages permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            try:
                await client.delete_message(miss)
            except:
                return
            return
        if 'Unknown Message' in str(e):
            miss = await client.say(ctx.message.author.mention + " Manage messages permission required." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            try:
                await client.delete_message(miss)
            except:
                return
            return
        else:
            print("errorcode" + '\n' + str(e)  + '\n Channel: '+ str(channel)  + ', channel ID: ' + str(channel.id)  + '\n Server: ' + str(server)  + ', server ID: ' + str(server.id))
            bula = await client.say(ctx.message.author.mention + " No messages to delete." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")         
            await asyncio.sleep(10)
            try:
                await client.delete_message(bula)
            except:
                return
            return
        return
 
    number2 = str(number1)
    if number2 == 1:
        done = await client.say(":white_check_mark: Successfully deleted one message from the <#" + str(channel.id) + ">" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
    else:    
        done = await client.say(":white_check_mark: Successfully deleted " + (number2) + " messages from the <#" + str(channel.id) + ">" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
    await asyncio.sleep(10)
    
    try:
        await client.delete_message(done)
    except Exception as e:
        if 'NOT FOUND' in str(e):
            print('ab')
            return
        if 'Not Found' in str(e):
            print('cd')
            return
        if 'NotFound' in str(e):
            print('ef')
            return
        else:
            print('szapa')
            return
    return

@client.command(pass_context=True)       
async def clear(ctx, number : int = 0):
    '''Clears The Chat 2-100'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles] 
    channel = ctx.message.channel
    server = ctx.message.server
    can_del = channel.permissions_for(server.me).manage_messages
    
    if ctx.message.author.server_permissions.manage_messages == False:
        borg = await client.say(ctx.message.author.mention + " You do not have permission to manage and delete messages" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(borg)
        return
    if not can_del:
        bory = await client.say(ctx.message.author.mention + " Manage messages permission required. " + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(bory)
        return
    if number == 0:
        terp = await client.say(ctx.message.author.mention + " Please specify a valid number of messages to delete" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(terp)
        return
    if number < 2 or number > 100:
        dekr = await client.say(ctx.message.author.mention + " You can only delete messages in the range of [2, 100]" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(dekr)
        return

    pass
    mgs = []
    number = int(number)
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
        try:
            await client.delete_messages(mgs)
        except:
            miss = await client.say(ctx.message.author.mention + " I can't delete these messages." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            await client.delete_message(miss)
            return
    number = str(number)
    done = await client.say(":white_check_mark: Successfully deleted " + (number) + " messages.")
    await asyncio.sleep(5)
    await client.delete_message(done)
    return

#t4 - Kicks a Member From The Server

@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member=None):
    '''Kicks A User From The Server'''
    
    server = ctx.message.server  
    channel = ctx.message.channel
    user_roles = [r.name.lower() for r in ctx.message.author.roles]
    can_kick = channel.permissions_for(server.me).kick_members


    if ctx.message.author.server_permissions.kick_members == False:
        perm = await client.say(ctx.message.author.mention + " You do not have permission to kick members" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(perm)
        return
    
    if not can_kick:
        wong = await client.say(ctx.message.author.mention + " I don't have permission to kick members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return
    
    if not member:
        loi = await client.say(ctx.message.author.mention + " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(loi)
        return
    
    pass

    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            lol = await client.say(ctx.message.author.mention + " You can't ban this user" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            await client.delete_message(lol)
            return
 
    embed = discord.Embed(description = "**%s** has been kicked."%member.name, color = 0xF00000)
    embed.set_footer(text='Glop Blop v1.0')
    try:
        await client.say(embed = embed)
    except:
        await client.say("**%s** has been kicked."%member.name)   
    
#t5 - BAN DZIALA #

@client.command(pass_context = True)
async def ban(ctx, member : discord.Member = None, *, reason : str = 1):
    """Bans specified member from the server."""
    
    server = ctx.message.server
    channel = ctx.message.channel
    can_ban = channel.permissions_for(server.me).ban_members
  
    if ctx.message.author.server_permissions.ban_members == False:
        if ctx.message.author.id == (ownerid):
            pass
        else:
            missed = await client.say(ctx.message.author.mention + " You do not have permission to ban members" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            await client.delete_message(missed)
            return
    
    if not can_ban:
        wong = await client.say(ctx.message.author.mention + " I don't have permission to ban members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return
    
    if member == None:
        spec = await client.say(ctx.message.author.mention + " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(spec)
        return


    user_roles = [r.name.lower() for r in ctx.message.author.roles]
    member_roles = [r.name.lower() for r in member.roles]


    if member.id == ctx.message.author.id:
        self = await client.say(ctx.message.author.mention + ", you cannot ban yourself." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(self)
        return

    if "admin" in member_roles:
        adme = await client.say(ctx.message.author.mention + ", you cannot ban an admin." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(adme)
        return
    
    if "moderator" in member_roles:
        mode = await client.say(ctx.message.author.mention + ", you cannot ban a moderator." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(mode)
        return

    if "mod bot" in member_roles:
        modb = await client.say(ctx.message.author.mention + ", you cannot ban a bot moderator." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(modb)
        return
   
    pass
               
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            lol = await client.say(ctx.message.author.mention +  " You can't ban this user" + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
            await asyncio.sleep(10)
            await client.delete_message(lol)
            return
    channel = ctx.message.channel
    time = str(server.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(title = ":regional_indicator_b: :regional_indicator_a: :regional_indicator_n:", colour = 0xF00000);
    join.add_field(name = 'USER', value = str(member.mention) + '\n' + str(member) + '\n' + str(member.id));
    join.add_field(name = 'MODERATOR', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    join.add_field(name = 'REASON', value = str((reason)));
    join.set_footer(text = 'Glop Blop v1.0');
        
    ujoin = discord.Embed(title = ":regional_indicator_b: :regional_indicator_a: :regional_indicator_n:", colour = 0xF00000);
    ujoin.add_field(name = 'USER', value = str(member.mention) + '\n' + str(member) + '\n' + str(member.id));
    ujoin.add_field(name = 'MODERATOR', value = str(ctx.message.author.mention) + '\n' + str(ctx.message.author));
    ujoin.set_footer(text = 'Glop Blop v1.0');


    if reason == 1:
        try:
            await client.say(embed = ujoin);
        except:
            await client.say(str(member) + " has been banned.")
    else:
        try:
            await client.say(embed = join);
        except:
            await client.say(str(member) + " has been banned. Reason:" + str(reason))
    return

#t6

@client.command(pass_context=True)
async def soft(ctx, user: discord.Member = None, *, reason: str = None):
    """Kicks the user, deleting 1 day worth of messages."""
    server = ctx.message.server
    channel = ctx.message.channel
    can_ban = channel.permissions_for(server.me).ban_members
    author = ctx.message.author

    if ctx.message.author.server_permissions.ban_members == False:
        missed = await client.say(ctx.message.author.mention + " You do not have permission to ban members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(missed)
        return

    if not can_ban:
        wong = await client.say(ctx.message.author.mention + " I don't have permission to ban members." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(wong)
        return
        
    if user == None:
        spec = await client.say(ctx.message.author.mention + " No user mentioned." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(spec)
        return

    if user == ctx.message.author:
        self = await client.say(ctx.message.author.mention + ", you cannot ban yourself." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(self)
        return
    
    
    try:
        invite = await client.create_invite(ctx.message.channel,max_uses=1,xkcd=True)        
        invite = invite.url

    except:
        invite = ""

    try:
        try:
            msg = await client.send_message(user, " You have been softbanned. Now, you can join the server again:" + invite)
        except:
            pass
        
        await client.ban(user, 1)
        await client.unban(server, user)
        if reason == None:
            await client.say("**" + str(user) + "** has been banned by **" + str(author) + "**.")
        else:
            await client.say("**" + str(user) + "** has been banned by **" + str(author) + "**, reason: " + str(reason))
    except discord.errors.Forbidden:
        clog = await client.say(ctx.message.author.mention + " I can't ban this member." + '\n' + "-- This message will be deleted automatically in 10 seconds. --")
        await asyncio.sleep(10)
        await client.delete_message(clog)
    except Exception as e:
        print(e)

 ###############################----------------------########################### 

@client.command(pass_context = True)
async def warn(ctx, *, member : discord.Member, reason : str = 1, n : str = 1):

    """Warns a Member"""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    if not member:
        return await client.say(":x: No user Mentioned")
    if reason == 1:
        return await client.say(":x: No reason entered!")
    if n == 1:
        return await client.say(":x: No Warn Number was selected")
    channel = client.get_channel(channel)
    em = discord.Embed(color=0x42fc07)
    em.add_field(name='Warning', value=("You Have Been Warned -->"))
    em.add_field(name='User', value=(member))
    em.add_field(name='Reason', value=(reason))
    em.add_field(name='Moderator', value=(mod))
    em.set_footer(text="Warnings had : {}".format(n))
    await client.send_message(channel, embed=em)


@client.command(pass_context=True, hidden = True)
async def report(ctx, user: discord.Member, *, reason):
    """Reports user and sends report to Admin"""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "moderator" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    author = ctx.message.author
    server = ctx.message.server


    joined_at = user.joined_at
    user_joined = joined_at.strftime("%d %b %Y %H:%M")
    joined_on = "{}".format(user_joined)

    args = ''.join(reason)
    adminlist = []
    check = lambda r: r.name in 'Admin'

    members = server.members
    for i in members:

        role = bool(discord.utils.find(check, i.roles))

        if role is True:
            adminlist.append(i)
        else:
            pass

    colour = discord.Colour.magenta()

    description = "User Reported"
    data = discord.Embed(description=description, colour=colour)
    data.add_field(name="Report reason", value=reason)
    data.add_field(name="Report by", value=author)
    data.add_field(name="Reported user joinned this server on", value=joined_on)
    data.set_footer(text="User ID:{}"
                            "".format(user.id))

    name = str(user)
    name = " ~ ".join((name, user.nick)) if user.nick else name

    if user.avatar_url:
        data.set_author(name=name, url=user.avatar_url)
        data.set_thumbnail(url=user.avatar_url)
    else:
        data.set_author(name=name)

    for i in adminlist:
        await client.send_message(i, embed=data)
        


@client.command()
async def add(x: int, y: int = 1):
    """Adds 2 numbers together, if the 2nd number is not provided, it will add 1"""
    await client.say('answer: {}'.format(x+y))

@client.command(pass_context = True)
async def now(ctx):
    date = datetime.datetime.ctx().strftime("**Date: **%A, %B %d, %Y\n**Time: **%I:%M %p")
    embed = discord.Embed(color = embed_color)
    embed.add_field(name="Bot's System Date & Time", value=date, inline=False)
    await client.say(embed=embed)
#must import os

client.run(os.getenv('TOKEN')) 
