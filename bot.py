import os
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event # bot online
async def on_ready():
    print('INICIANDO \n 1/1 \nONLINE')

@bot.event
async def on_member_join(member):
  canal = client.get_channel(767201786095861760)
  regras = client.get_channel(755166845044129844)
  msg = "Bem Vindo {}\n leia as {}".format(member.mention, regras.mention)
  await channel.send(msg) 

        # COMMANDS

@bot.command()
async def ola(ctx):
    await ctx.send(f'Olรก {ctx.author}, como vocรช estรก?')

@bot.command()
@commands.has_role('๐๐๐๐๐๐๐๐ ๐๐ข๐ก๐๐')
async def opa(ctx):
    await ctx.send(f'Olรก ADEMIR, vocรช estรก tรฃo bonito hoje!')

@bot.command()
async def dado(ctx):
    numr = random.randint(1,6)
    await ctx.send(numr)

bot.run('TOKEN')
