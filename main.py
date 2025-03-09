import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime, timedelta
import asyncio



load_dotenv()

# Vérifier si le token est bien chargé
TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    raise ValueError("Le token du bot n'est pas défini. Vérifiez votre fichier .env.")

# Configurer les intents
intents = discord.Intents.default()
intents.message_content = True  # Autorisation de lire les messages
intents.members = True  # Autorisation d'accéder aux membres du serveur

# Créer le bot
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"Le bot {bot.user.name} est en ligne !")
    await bot.tree.sync()
    
    
    
    
    # Commandes 
    
@bot.hybrid_command(name="dire_coucou", description="Dit coucou", with_app_command=True)
async def dire_coucou(ctx: commands.Context):
    await ctx.send("Coucou ! 😊")
    
# @bot.hybrid_command(name="news", description="Récupère les dernières actualités crypto", with_app_command=True)
# async def news(ctx: commands.Context):
#     news_message = get_crypto_news()
#     await ctx.send(news_message)




# Lancer le bot
bot.run(TOKEN)

