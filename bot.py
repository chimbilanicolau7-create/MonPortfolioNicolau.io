import discord
from discord.ext import commands
from openai import OpenAI

# TES CLÉS ICI
CLÉ_OPENAI = OpenAI(api_key
TOKEN_DISCORD = 

# CONFIGURATION
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
client_ai = OpenAI(api_key=CLÉ_OPENAI)

@bot.event
async def on_ready():
    print(f"L'ordinateur dit : Le bot {bot.user} est EN LIGNE !")

@bot.command()
async def hello(ctx):
    await ctx.send("Salut ! Je suis bien connecté.")
    bot.run(TOKEN_DISCORD)

