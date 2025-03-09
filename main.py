import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


from answer_questions import answer_questions

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
    
# @bot.hybrid_command(name="dire_coucou", description="Dit coucou", with_app_command=True)
# async def dire_coucou(ctx: commands.Context):
#     await ctx.send("Coucou ! 😊")

    
@bot.hybrid_command(name="poser_une_question", description="Poser une question médicale au bot", with_app_command=True)
async def answer(ctx: commands.Context, *, content: str):
    await ctx.defer()  # This defers the interaction response, preventing a timeout

    answer_message = answer_questions(content)
    await ctx.send(answer_message)




# Lancer le bot
bot.run(TOKEN)

