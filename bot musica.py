import discord
from discord.utils import get
from discord.ext import commands
from discord import FFmpegPCMAudio

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Bot online")

@client.command()
async def entrar(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send('Você não está conectado em um canal de voz')
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command()
async def sair(ctx):
    channeldc = client.voice.client_in(message.server)
    if not channeldc:
        await ctx.send('O bot não está conectado em um canal de voz')
    await channeldc.disconnect()

client.run('ODM4OTEzNzUzMTkzOTA2MTg2.YJCBUQ.8hPwVpjn5nggZq8gcwSIgG4Kn3E')