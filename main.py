import discord, os, asyncio, requests, json
from discord.ext import commands
from discord.ext.forms import Form
from discord.utils import get
from discord import activity

intents = intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents = intents)
msg_id = None
msg2_id = None
msg3_id = None
msg4_id = None
msg5_id = None
#instagram = "https://discord.com/api/webhooks/1062248203484942336/snIwTurP0g3wZsA-2RzBzEIoQ8T-vc31XTKkJuSByqXpEMkYyiG3r7A02mJ2V19Vu2ky"
#@bot.event
#async def teste(ctx, message):
#    if bot.user.mentioned_in(message):
#        await message.channel.send("You can type `!vx help` for more info")

@bot.event
async def on_ready():
    print('Pronto pra fuder :D')

@bot.event
async def on_member_join(member):    
	role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956591370329)
	channel = bot.get_channel(1001218957358944377)  
	em = discord.Embed(
		title = "Bem Vindo(a)",
		description = f"Seja bem-vindo {member.mention}! Você acabou de entrar no discord do **Rede New LiFe**, aqui você poderá se interagir com os jogadores, conversar sobre suas coisas favoritas e muito mais! Se identifique agora mesmo em: <#1062169632460517446>. ",
		color = discord.Color.blue()
	)
	em.set_author(name=member.name, icon_url=member.avatar.url)
	em.add_field(name="<:rnl_shield:1062551142938189854> ID do Usuário", value=f"`{member.id}`", inline=True)
	em.add_field(name="<:rnl_computador:1062550538803224666> Visite nosso site!", value=f"[Site](https://google.com)", inline=True)
	em.add_field(name="<:rnl_insta:1062550389649584190> Siga no Instagram!", value=f"[@redenewlife](https://www.instagram.com/redenewlifesamp)", inline=True)
	em.add_field(name="<:rnl_twitter:1062550455319806023> Siga no Twitter!", value=f"[@redenewlife](https://twitter.com/redenewlifesamp)", inline=True)
	em.add_field(name="<:rnl_youtube:1062550630809481217> Inscreva-se em nosso canal!!", value=f"[@RedeNewLife](https://www.youtube.com/@redenewlife2474)", inline=True)
	em.set_footer(text='Rede New Life [SA-MP: PC/Android] • © Todos os direitos reservados.')
	em.set_thumbnail(url=member.avatar.url)
	await channel.send(f"{member.mention}")
	await channel.send(embed=em)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1001218957358944378)
    embed = discord.Embed(
        title = "Até a Proxima!",
        description = f"{member.name} Saiu do nosso servidor, espero que volte em breve...",
        color = discord.Color.blue()
    )
    embed.set_author(name=member.name + "#" + member.discriminator, icon_url=member.avatar.url)
    embed.set_footer(text=f'{member.id}')
    embed.set_thumbnail(url=member.avatar.url)
    await member.add_roles(role)
    await channel.send(embed=embed)

@bot.command()
async def criarevento(ctx):
	async def to_int(ctx, msg: discord.Message):
		try:
			return int(msg.content)
		except Exception as e:
			return False

	form = forms.Form(ctx, 'Title')
	form.add_question('Give me an invite link!', 'invite')
	form.add_question('Mention a Channel', 'channel')
	form.add_question('Ping a User!', 'member')
	form.add_question('Give me a number!', 'number')
	form.add_question('How are you?', 'feels')
	form.edit_and_delete(True)
	form.set_timeout(60)
	await form.set_color("#7289DA")
    
	result = await form.start()
    
	embed=discord.Embed(title="Data", description=f"Invite: {result.invite.guild}\nChannel: {result.channel.mention}\nMember: {result.member.mention}\nNumber: `{result.number}`\n Feels: `{result.feels}`")
	await ctx.send(embed=embed)
   
@bot.command()
async def exposicao32318(ctx):
    await ctx.send("EXPOSIÇÕES\nCanal destinado para players vinculados compartilharem suas artes.\n<a:rnl_20:1062537621663924254>  - Artes;\n<a:rnl_20:1062537621663924254>  - Avatar, sign e fanbar;\n<a:rnl_21:1062537867919884288> - Enviar mensagens (Chat)\n\n@everyone // @here")
    
@bot.command()
async def identifique32318(ctx):
	botmsg = await ctx.send("*Gênero:*\n<@&1001218956452974637>\n<@&1001218956452974636>")
	await botmsg.add_reaction("👦")
	await botmsg.add_reaction("👩‍🦰")
    
	with open('Data/reactrole.json') as json_file:
		data = json.load(json_file)
		new_react_role = {
			'mensagem_id':botmsg.id
		}
		data.append(new_react_role)
	with open('Data/reactrole.json', 'w') as j:
		json.dump(data, j, indent=4)
 
	global msg_id
	msg_id = botmsg.id
     
	botmsg2 = await ctx.send("*Plataforma:*\n<@&1001218956452974634>\n<@&1001218956452974635>")
	await botmsg2.add_reaction("📱")
	await botmsg2.add_reaction("💻")
	
	global msg2_id
	msg2_id = botmsg2.id
	
	botmsg3 = await ctx.send("*Idade:*\n<@&1001218956452974633>\n<@&1001218956452974632>")
	await botmsg3.add_reaction("🔒")
	await botmsg3.add_reaction("🔓")
	
	global msg3_id
	msg3_id = botmsg3.id
	
	botmsg4 = await ctx.send("*Região:*\n<@&1001218956431986736>\n<@&1001218956431986735>\n<@&1001218956431986734>\n<@&1001218956431986733>\n<@&1001218956431986732>\n<@&1001218956431986731>")
	await botmsg4.add_reaction("🌳")
	await botmsg4.add_reaction("🔥")
	await botmsg4.add_reaction("🤠")
	await botmsg4.add_reaction("🌧️")
	await botmsg4.add_reaction("❄️")
	await botmsg4.add_reaction("🌎")
	
	global msg4_id
	msg4_id = botmsg4.id
	
	botmsg5 = await ctx.send("*TAGs de PING:*\n<@&1001218956431986729>\n<@&1001218956431986728>\n<@&1001218956411027606>\n<@&1001218956411027605>\n<@&1001218956411027603>\n<@&1001218956411027604>\n<@&1062597998099574784> \n<@&1062484750629097602>")
	await botmsg5.add_reaction("🎉")
	await botmsg5.add_reaction("📢")
	await botmsg5.add_reaction("🍀")
	await botmsg5.add_reaction("✅")
	await botmsg5.add_reaction("⚙️")
	await botmsg5.add_reaction("🆕")
	await botmsg5.add_reaction("📝")
	await botmsg5.add_reaction("📷")
	
	global msg5_id
	msg5_id = botmsg5.id
    
@bot.event
async def on_reaction_add(reaction, user):
	if user.bot:
		pass
	else:
		msg = reaction.message
		if reaction.emoji == "👦" and msg.id == msg_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974637)
			await user.add_roles(role)

		if reaction.emoji == "👩‍🦰" and msg.id == msg_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974636)
			await user.add_roles(role)
			
		if reaction.emoji == "📱" and msg.id == msg2_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974634)
			await user.add_roles(role)

		if reaction.emoji == "💻" and msg.id == msg2_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974635)
			await user.add_roles(role)
			
		if reaction.emoji == "🔓" and msg.id == msg3_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974633)
			await user.add_roles(role)

		if reaction.emoji == "🔒" and msg.id == msg3_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974632)
			await user.add_roles(role)
			
		if reaction.emoji == "🌳" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986736)
			await user.add_roles(role)

		if reaction.emoji == "🔥" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986735)
			await user.add_roles(role)
		
		if reaction.emoji == "🤠" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986734)
			await user.add_roles(role)

		if reaction.emoji == "🌧️" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986733)
			await user.add_roles(role)
		
		if reaction.emoji == "❄️" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986732)
			await user.add_roles(role)

		if reaction.emoji == "🌎" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974631)
			await user.add_roles(role)
			
		if reaction.emoji == "🎉" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986729)
			await user.add_roles(role)

		if reaction.emoji == "📢" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986728)
			await user.add_roles(role)
		
		if reaction.emoji == "🍀" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956411027606)
			await user.add_roles(role)

		if reaction.emoji == "✅" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956411027605)
			await user.add_roles(role)
		
		if reaction.emoji == "⚙️" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956411027603)
			await user.add_roles(role)

		if reaction.emoji == "🆕" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956411027604)
			await user.add_roles(role)
			
		if reaction.emoji == "📝" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1062597998099574784)
			await user.add_roles(role)
			
		if reaction.emoji == "📷" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1062484750629097602)
			await user.add_roles(role)
			
@bot.event
async def on_reaction_remove(reaction, user):
	if user.bot:
		pass
	else:
		msg = reaction.message
		if reaction.emoji == "👦" and msg.id == msg_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974637)
			await user.remove_roles(role)

		if reaction.emoji == "👩‍🦰" and msg.id == msg_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974636)
			await user.remove_roles(role)
			
		if reaction.emoji == "📱" and msg.id == msg2_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974634)
			await user.remove_roles(role)

		if reaction.emoji == "💻" and msg.id == msg2_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974635)
			await user.remove_roles(role)
			
		if reaction.emoji == "🔓" and msg.id == msg3_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974633)
			await user.remove_roles(role)

		if reaction.emoji == "🔒" and msg.id == msg3_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974632)
			await user.remove_roles(role)
			
		if reaction.emoji == "🌳" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986736)
			await user.remove_roles(role)

		if reaction.emoji == "🔥" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986735)
			await user.remove_roles(role)
		
		if reaction.emoji == "🤠" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986734)
			await user.remove_roles(role)

		if reaction.emoji == "🌧️" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986733)
			await user.remove_roles(role)
		
		if reaction.emoji == "❄️" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986732)
			await user.remove_roles(role)

		if reaction.emoji == "🌎" and msg.id == msg4_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956452974631)
			await user.remove_roles(role)
			
		if reaction.emoji == "🎉" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986729)
			await user.remove_roles(role)

		if reaction.emoji == "📢" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956431986728)
			await user.remove_roles(role)
		
		if reaction.emoji == "🍀" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956411027606)
			await user.remove_roles(role)

		if reaction.emoji == "✅" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956411027605)
			await user.remove_roles(role)
		
		if reaction.emoji == "⚙️" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956411027603)
			await user.remove_roles(role)

		if reaction.emoji == "🆕" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1001218956411027604)
			await user.remove_roles(role)
			
		if reaction.emoji == "📝" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1062597998099574784)
			await user.remove_roles(role)
			
		if reaction.emoji == "📷" and msg.id == msg5_id:
			role = discord.utils.get(bot.get_guild(user.guild.id).roles, id=1062484750629097602)
			await user.remove_roles(role)
#===================================================================================
     
bot.run('NzYwNjgwOTQxMTkzNTI3Mzg3.G7DQvG.2MTzEobt_ogU5nhgc_bWcIhZwk2eDiT1ym5aE0')