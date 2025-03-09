import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
from src.utils import generate_medical_response


load_dotenv()


# Configuration Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Charger le modèle Llama pré-entraîné
model_name = "models/llama_model"  # Chemin vers le modèle fine-tuné
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

# Événement pour que le bot réagisse à un message
@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith("!médical"):  # Commande pour obtenir une réponse médicale
        question = message.content[len("!médical "):].strip()  # Récupérer la question posée
        if question:
            response = generate_medical_response(question, model, tokenizer)
            await message.channel.send(f"Réponse médicale : {response}")
        else:
            await message.channel.send("Veuillez poser une question médicale après !médical.")

# Démarrage du bot avec le token
bot.run(os.getenv('DISCORD_TOKEN'))  # Remplace par ton token API Discord

