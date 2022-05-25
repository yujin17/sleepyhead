import discord
from discord.ext.commands import Bot

TOKEN = 'OTc5MTAwMTY4NzkwMDk4MDAw.GHB8dv.6YjaRN_aldy0eCAj6eGbjTyPbFvcv4iz35ylhg'

intents = discord.Intents.default()

# !로 시작하면 명령어로 인식
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')

# !hello 명령어 처리
@bot.command()
async def hello(ctx):
  await ctx.reply('Hi, there!')

# !bye 명령어 처리
@bot.command()
async def bye(ctx):
  await ctx.reply('See you later!')

@bot.command()
async def talk(ctx, arg1, arg2):
  await ctx.reply('{} talks to {}.'.format(arg1, arg2))



bot.run(TOKEN)