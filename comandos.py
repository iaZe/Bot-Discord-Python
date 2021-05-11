from discord.ext import commands
import random
import os
import discord

bot = commands.Bot(command_prefix='!')

                # EVENTS

@bot.event # bot online
async def on_ready():
    print('Online e roteando')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} Está conectado no discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Olá {member.name}, seja bem-vindo!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    resposta = ['Não respondo a isso','Sim','As vezes','Não','Claro','NUNCA!','Um dia talvez','A resposta está dentro de ti','Mais ou menos','Uma Bosta','Podia ser pior']
    if message.content == '?':
        response = random.choice(respostas)
        await message.channel.send(respostas)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'feliz aniversario' in message.content.lower():
        await message.channel.send('Feliz aniversário 🎈🎉')

                # COMMANDS

@bot.command()
async def ola(ctx):
    await ctx.send(f'Olá {ctx.author}, como você está?')

@bot.command()
async def dado(ctx):
    numr = random.randint(1,6)
    await ctx.send(numr)

bot.run('ODM4OTEzNzUzMTkzOTA2MTg2.YJCBUQ.8hPwVpjn5nggZq8gcwSIgG4Kn3E')


@client.command(name='entrar')
async def entrar(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
            await voice.move_to(channel)
    else:
            voice = await channel.connect()
    source = FFmpegPCMAudio('1.m4a')
    player = voice.play(source)