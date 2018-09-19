import pkgutil
import sys
import asyncio
import timeit
import time
import discord
from discord.ext import commands
import os
import zipfile
import hashlib
import datetime
import multiprocessing
import logging
from pkgutil import extend_path
import json
from discord.ext.commands import errors
# for async .

is_owner = lambda ctx: ctx.message.author.id == '320256494132002817'
#@client.command(pass_context=true)
#@commands.check(is_owner)



#async def........
# for rewrite you can simply do @commands.is_owner()




now = datetime.datetime.now()
tm1 = "%d" %now.year
tm2 = "%d" %now.month
tm3 = "%d" %now.hour
tm4 = "%d" %now.minute
tm5 = "%d" %now.second
fix1 = (str(int(tm3)-6))
timestampdate = "Year: "+tm1+" Month: "+tm2+" Hour: "+tm3+" Minute: "+tm4+" Second: "+tm5
GMT4 = "Year: "+tm1+" Month: "+tm2+" Hour: "+fix1+" Minute: "+tm4+" Second: "+tm5
gap = "                                                                                                                                                          "
Fri= 'hello dude'
print(timestampdate)
Client = commands.Bot(command_prefix='...')
###############
###############
###My Modules###
from Variables import Variable


from Token.Token import token1
###############
###############

'''t1= type=0#Playing
t2= type=1#Streaming
t3= type=2#Listening to
t4= type=3#Watching
'''
async def status_task():
	while True:
		await Client.change_presence(game=discord.Game(name='... Prefix is ...',type=1))
		await asyncio.sleep(10) 
		await Client.change_presence(game=discord.Game(name='With New codes', type=1))
		await asyncio.sleep(10)
		await Client.change_presence(game=discord.Game(name='OverLord', type=3))
		await asyncio.sleep(10)
		await Client.change_presence(game=discord.Game(name=str(len(Client.servers))+' Severs', type=3))
		await asyncio.sleep(20)
		


def Owner_is(ctx):
	return ctx.message.author.id == ' 320256494132002817'
	


@Client.event
async def on_ready():
	Client.loop.create_task(status_task())
	print("Logged in as:")
	print(Client.user.name)
	print("ID:"+" "+Client.user.id)
	print("Ready to use:")
	print(" ")
	print("Use this to invite your bot")
	print(Variable.invite)


@Client.event
async def on_message(message):
	
	###############################
    mcu = message.content.upper().startswith
    sm = Client.send_message
    mc = message.channel
    UserId = message.author.id
    
    
    
    
    
    ###############################
    
    
    
    
    
    
    
    
    
    #print(message.author.id)
    await Client.process_commands(message)
    if message.author == Client.user :
        return
    
    
    
    elif mcu("#HERE"):   	
    	await sm(mc, "<@%s> What can i do for you?" % (UserId))
    	return
 
    	
    	   	
    	   	   	
    	   	   	   	
    	   	   	   	   	
    	   	   	   	   	   	
    	   	   	   	   	   	   	
    	   	   	   	   	   	   	   	   	
    elif mcu('#START'):
        await sm(mc, 'Type #ME 4 times.')
        X = 4
        D = 4
        for i in range(X):
        	msg = await Client.wait_for_message(author=message.author, content='me')
        	fmt = '{} left to go...'
        	#await Client.send_message(message.channel, fmt.format(i+i))
        	D = D-1
        	await sm(mc,D)
        	if D is not 0:
        		await sm(mc, 'Good job!')
        		
        	elif D == 0:
        		if D is 0:
        			await sm(mc, 'Nicely Done')
        		
        		
        		
        		
        		
        		
        		
        		
    elif  mcu("RECORD"):
    	args = message.content()
    	await 	sm(mc, "%s" % (args)  (UserId))
    	return
    
    
    
    
    
    
    elif mcu("HELP"):
        embed=discord.Embed(title="Information and Commands", description=" ", colour =909999)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/364142374420611084/381822867265814529/thumb-1920-777881.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/364142374420611084/381822867265814529/thumb-1920-777881.png")
        embed.add_field(name="Created By", value="JSB or Lord Vile", inline=True)
        embed.add_field(name="Friends", value=Fri, inline=True)
        embed.add_field(name="--------------------------------------------------------------", value="------------------------------------------------------------", inline=False)
        embed.add_field(name="Commands", value="------------------------------------------------------------"+gap+"------------------------------------------------------------", inline=True)
        embed.add_field(name="Misc", value="?"+gap+"Ping"+gap+"Hi"+gap+"Good and you?"+gap+"Bot Invite"+gap+"Community Invite"+gap+"#here", inline=True)
        await sm(message.author, embed=embed)
        await sm(message.channel, embed=embed)
        return
	









#if (message.author.id !== 'A user ID') return;
@Client.command()
async def  ping():
	await Client.say('Pong')
	return

	
@Client.command()
async def LogOut():
	Client.say('closing connections')
	await asyncio.sleep(10)
	await Client.logout
	Client.close
	return 
	
	

@Client.command(pass_context= True,hidden=True)
async def cool():
	await Client.say('You are cool indeed')
	
	
@Client.command(pass_context= True,hidden=True)
async def StatusChange(*args):
	output = ' '
	for word in args:
		output += word
		output += ' '
		await Client.say(output)
		os.chdir('..')
		cwdu = os.getcwd()
		print(cwdu)
	try:
		w = open(cwdu+'/Status/'+'Status21.py','w+')
		w.write(output)
		w.close
	except:
		print('error')
	pass

	
#@Client.command()
			
				
@Client.command(pass_context= True)
async def clean(ctx, amount=100):
	channel = ctx.message.channel
	messages = [ ]
	async for message in Client.logs_from(channel, limit=int(amount)):
		messages.append(message)
		
		
		
		
@Client.command(pass_context= True)
async def ping_ms(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await Client.send_typing(channel)
	t2 = time.perf_counter
	await Client.say("Pong: Latency {}ms".format(round((t2-t1)*1000)))


	
	
@Client.command()
@commands.check(is_owner)
async def greet(user: discord.User=None):
	if not user:
		await Client.say("Hello generic!")
	else:
		await Client.say('Hello {}!'.format(user))
		await Client.say("Your id is {}!".format(user.id))
	

@Client.command(pass_context= True,hidden=True)
async def member(ctx, member : discord.Member = None):
	"""Retrieves information about a member of the guild."""
	channel = ctx.message.channel
	Client.send_typing(channel)
	member = member or ctx.author
	e = discord.Embed(type='rich', color=member.color)
	
	e.add_field(name='Name', value=str(member))
	e.add_field(name='ID', value=member.id)
	e.add_field(name='Nickname', value=member.nick)
	e.add_field(name='Bot Created' if member.bot else 'User Joined Discord', value=member.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
	e.add_field(name='Joined Guild', value=member.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
	e.add_field(name='Color', value=str(member.color).upper())
	e.add_field(name='Status and Game', value='%s, playing %s' % (str(member.status).title(), member.game), inline=False)
	roles = sorted(member.roles)[1:]
	roles.reverse()
	e.add_field(name='Roles', value=', '.join(role.name for role in roles) or 'None', inline=False)
	await Client.say(embed=e)	
	
	
@Client.command(pass_context= True,hidden=True)
async def m_Info(ctx, user: discord.Member = None):
	
	em = discord.Embed(type='rich', color=user.color)
	em.add_field(name='Name', value=str(user))

	em.add_field(name='User ID', value=user.id, inline=True)
	em.add_field(name='Nick', value=user.nick, inline=True)
	em.add_field(name='Status', value=user.status, inline=True)
	em.add_field(name='Game', value=user.game, inline=True)
	roles = sorted(user.roles)[1:]
	roles.reverse()
	em.add_field(name='Highest Role', value=''.join(role.name for role in roles) or 'None',inline=True)
	em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
	em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
	em.add_field(name='TimeStamp GMT +02:00:',value=timestampdate)
	em.add_field(name='TimeStamp GMT -04:00:',value=GMT4)
	await Client.say(embed=em)
	


@Client.command(pass_context= True,hidden=True)
async def ctime(ctx):
	emn=discord.Embed(title="Information and Commands", description=" ", colour =909999)
	emn.add_field(name='Year', value="%d" %now.year)
	emn.add_field(name='Month', value="%d" %now.month)
	emn.add_field(name='Day', value="%d" %now.day)
	emn.add_field(name='Hour', value="%d" %now.hour)
	emn.add_field(name='Minutes', value="%d" %now.minute)
	
	await Client.say(embed=emn)
	
	

@Client.command(pass_context= True,hidden=True)
async def ci(ctx):
	channel = ctx.message.channel
	a = "{}".format(ctx.message.channel.id)
	print(a)
  

@Client.command(pass_context=True, hidden=True)
async def sendC(ctx, msg: str):
	await Client.send_message(Client.get_channel("490600507287666719"), msg)
 
    
@Client.command(pass_context=True, hidden=True)
async def e1(ctx, *,msg: str):	
	msg2 = msg
	ID, msg1 = msg2.split(' ', 1)
	await Client.say(ID)
	await Client.say(msg1)
	await Client.send_message(Client.get_channel(""+ID+""), msg1)





@Client.command(pass_context = True)
async def ch(ctx,user: discord.Member = None):
	channel1 = ctx.message.channel
	roles = sorted(user.roles)[1:]
	roles.reverse()
	roles1 = ' '.join(role.name for role in roles) or 'None'
	TopR , waste= roles1.split(' ', 1)
	await Client.send_message(channel1,TopR)




@Client.command(pass_context = True)
async def info(ctx):
	
		await Client.say(len(Client.servers))







@Client.command(pass_context = True)
async def kick(ctx, user: discord.User = None):
		
	 A = '{}'.format(user)
	 channel = ctx.message.channel
	 rem = await Client.send_message(channel, 'Do you want to kick '+str(A))
	 msg = await Client.send_message(channel,'No 👎/Yes 👍')
	 
	 res = await Client.wait_for_reaction(['👍', '👎'], message=msg)
	 
	 Confirm = '{0.reaction.emoji}'.format(res)
	 if Confirm == '👎':
	 	exit
	 try:
	 	if Confirm == '👍':
	 		msg3 = await Client.send_message(channel,str(user)+' has been kicked')
	 		#await Client.kick(user)
	 		
	 		
	 except errors.DiscordException:
	 	Client.say('Unknow user')
	 	Client.say('PermissionError')
	 await Client.delete_message(msg)
	 await.Client.delete_message(rem)
	 

@Client.command(pass_context = True)
async def ban(ctx, user: discord.User = None):
		
	 A = '{}'.format(user)
	 channel = ctx.message.channel
	 await Client.send_message(channel, 'Do you want to ban '+str(A))
	 msg = await Client.say('No 👎/Yes 👍')
	 
	 res = await Client.wait_for_reaction(['👍', '👎'], message=msg)
	 
	 Confirm = '{0.reaction.emoji}'.format(res)
	 if Confirm == '👎':
	 	exit
	 try:
	 	if Confirm == '👍':
	 		await Client.ban(user)
	 except errors.DiscordException:
	 	Client.say('Unknow user')
	 	Client.say('PermissionError')



@Client.command(pass_context = True)
async def re(ctx):
	channel = ctx.message.channel
	msg = await Client.send_message(channel,'Y / N')
	await Client.add_reaction(msg, '👍')
	await Client.add_reaction(msg, '👎')
	
	
	
	
@Client.command(pass_context = True)
async def re1(ctx):
	channel = ctx.message.channel
	msg = await Client.send_message(channel, 'React with thumbs up or thumbs down.')
	res = await Client.wait_for_reaction(['👍', '👎'], message=msg)
	await Client.send_message(channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))


Client.run('MzgxMDkyMTg1NDE3ODQyNjg4.DngUqQ.hllju1PnCHKXautnryEIDA2o3Zk')