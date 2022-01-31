import asyncio
import random
import discord
from discord.errors import NotFound
from discord.ext import commands
from discord.ext.commands import Bot

IDME=None

client = commands.Bot(command_prefix = ";", case_insensitive = True, intents=discord.Intents.all())
client.remove_command("help")

##HELP
@client.command()
async def help(ctx):
  await ctx.channel.purge(limit=1)
  embed = discord.Embed(
      title=("Antes dos comandos deve haver um ;"),
      description=('**- dado "numero maximo"** - retorna um numero aleatório de 1 ao numero dado \n **- vote "titulo" "pergunta"** - Adiciona as reações ✅ e ❎ na mensagem \n **- options "pergunta" "opção 1" "opção 2" "opção 3" "opção 4" "opção 5"** - cria uma votação entre as opções dadas, o minimo são duas opções \n **- diga "texto"** - o bot repete o texto escrito \n **- embed "titulo" "texto"** - o bot manda uma mensagem bonitinha com o titulo e texto dados \n **- sendpersonal "@membro" "texto"** - manda o texto no privado do membro marcado \n **- clear "numero"** - apaga a quantidades de mensagens dadas naquele chat \n **- reaction "titulo" "texto"** - manda uma embed e adicona 🖐 a ela \n\n **Lembrando que frases devem estar entre "" e você pode marcar canais, pessoas ou cargos em qualquer comando.** \n **Divirta-se usando este bot e fique a vontade para dar sugestões de comandos novos também!**'),
      colour=discord.Color.blue()
      )
  await ctx.send(embed=embed)

##ALEATÓRIO
@client.command()
async def dado(ctx, numero=None):
  if numero==None:
    message = await ctx.send('Você deve informar o número máximo após o comando **exemplo [dado 6]**')
  else:
    variavel = random.randint(1,int(numero))
    embed = discord.Embed(
      title=("Pensando..."),
      description=(f'O número é {variavel}'),
      colour=discord.Color.blue()
    )
    await ctx.send(embed=embed)

## VOTAÇÕES
@client.command()
async def vote(ctx, question=None, txt=None):
  if question==None or txt==None:
    await ctx.send('Você deve dar o titulo e o texto da mensagem exemplo **[vote "titulo" "texto"]**')
  else:
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
      title=question,
      description=txt,
      colour=discord.Color.blue()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')

@client.command()
async def options(ctx, question=None, option1=None, option2=None, option3=None, option4=None, option5=None):
  if question==None or option1==None or option2==None:
    message = await ctx.send('Você deve adicionar pelo menos duas opções **exemplo [options "pergunta" "opção 1" "opção 2"]**')
  elif option3==None:
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
      title=('Favor votar...'),
      description=(f" \n{question} \n\n**1️⃣ = {option1}**\n**2️⃣ = {option2}**"),
      colour=discord.Color.blue()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
  elif option4==None:
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
      title=('Favor votar...'),
      description=(f" \n{question} \n\n**1️⃣ = {option1}**\n**2️⃣ = {option2}**\n**3️⃣ = {option3}**"),
      colour=discord.Color.blue()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
  elif option5==None:
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
      title=('Favor votar...'),
      description=(f" \n{question} \n\n**1️⃣ = {option1}**\n**2️⃣ = {option2}**\n**3️⃣ = {option3}**\n**4️⃣ = {option4}**"),
      colour=discord.Color.blue()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
    await message.add_reaction('4️⃣')
  else:
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
      title=('Favor votar...'),
      description=(f" \n{question} \n\n**1️⃣ = {option1}**\n**2️⃣ = {option2}**\n**3️⃣ = {option3}**\n**4️⃣ = {option4}**\n**5️⃣ = {option5}**"),
      colour=discord.Color.blue()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
    await message.add_reaction('4️⃣')
    await message.add_reaction('5️⃣')

##MENSAGENS DIRETAS
@client.command()
async def diga(ctx, txt=None):
  if txt==None:
    await ctx.send('Você deve informar o texto também **exemplo [diga "texto"]**')
  else:
    await ctx.channel.purge(limit=1)
    messsage = await ctx.send(f'{txt}')

@client.command()
async def desculpa(ctx):
  messsage = await ctx.send('Eu te perdoo, amigo!')

@client.command()
async def bosta(ctx, member: discord.Member):
  await ctx.channel.purge(limit=1)
  messsage = await ctx.send(f'{member} você foi marcado como bosta suprema💩')

@client.command()
async def embed(ctx, message=None, txt=None):
  if message==None or txt==None:
    await ctx.send('Você precisa informar o titulo e o texto **exemplo [embed "titulo" "texto"]**')
  else:
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title=message,
        description=txt,
        colour=discord.Color.blue()
        )
    await ctx.send(embed=embed)

@client.command()
async def sendpersonal(ctx, member: discord.Member=None, *, message=None):
  if member==None or message==None:
    await ctx.send('Você deve informar o nome da pessoa e a mensagem **exemplo[sendpersonal @membro "texto"]**')
  else:
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
      title=f"Olá!",
      description=f"{message}",
      colour=discord.Color.blue()
      )
    await member.send(embed=embed)

##DELETAR MENSAGENS
@client.command()
async def clear(ctx, number=None):
  if number==None:
    await ctx.send('Você deve informar também a quantidade de mensagens a serem apagadas **exemplo[clear 12]**')
  else:
    await ctx.channel.purge(limit= int(number)+1)
  
##COMANDOS NÃO FINALIZADOS
##CARGO POR REAÇÃO
@client.command()
async def reaction(ctx, message=None, txt=None):
  if message==None or txt==None:
    await ctx.send('Você deve informar o titulo e o texto a serem ditos **exemplo [reaction "titulo" "texto"]**')
  else:
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
      title=message,
      description=txt,
      colour=discord.Color.blue()
      )
    message = await ctx.send(embed=embed)
    await message.add_reaction('🖐')

@client.event
async def on_raw_reaction_add(payload):
  if payload.message_id == (898920068237385778):
    guild = client.get_guild(895655835236175902)
    member = guild.get_member(payload.user_id)
  if payload.emoji.name == '🖐':
    cargo = discord.utils.get(guild.roles, name="Mudae-chan")
    await member.add_roles(cargo)

client.run('ODk2NzU4NDcwMzMyNzg0NzIw.YWLxaA.loJW8rFWsvG5HLGbPv-tazbEtvc')