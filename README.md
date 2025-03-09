# Bot Discord d'Assistant Médical

## Description
Ce bot Discord est conçu pour répondre aux questions médicales. Il utilise l'API Groq pour générer des réponses précises et professionnelles aux questions médicales, et offre également un système de mise en cache des réponses pour une meilleure efficacité.

## Fonctionnalités
- Répond aux questions médicales via une commande slash Discord
- Stocke les questions et réponses dans un fichier JSON pour accès rapide
- Utilise l'API Groq avec le modèle Llama3 pour générer des réponses
- Fournit des liens pertinents dans les réponses
- Ajoute des émojis pour rendre les réponses plus conviviales

## Prérequis
- Python 3.8 ou supérieur
- Un compte Discord et un bot créé sur le [portail développeur Discord](https://discord.com/developers/applications)
- Un compte Groq et une clé API

## Installation

1. Clonez ce dépôt:

git clone https://github.com/Massizelle/MedicalBot.git
cd [NOM_DU_DOSSIER]


2. Installez les dépendances:

pip install discord.py python-dotenv requests


3. Créez un fichier .env à la racine du projet avec le contenu suivant:

TOKEN=votre_token_discord_ici
GROQ_API_KEY=votre_clé_api_groq_ici


4. Créez un dossier data et un fichier JSON vide pour stocker les questions/réponses:

mkdir data
echo [] > data/faq_medical_question.json


## Configuration Discord

Pour configurer votre bot Discord:
1. Visitez le [portail développeur Discord](https://discord.com/developers/applications)
2. Créez une nouvelle application
3. Dans l'onglet "Bot", créez un bot et copiez le token
4. Activez les "Privileged Gateway Intents" (Message Content et Server Members)
5. Dans l'onglet "OAuth2" > "URL Generator", sélectionnez les scopes bot et applications.commands
6. Sélectionnez les permissions nécessaires (Send Messages, Read Messages, etc.)
7. Utilisez l'URL générée pour inviter le bot sur votre serveur

## Utilisation

1. Lancez le bot:

python main.py


2. Dans Discord, utilisez la commande slash:

/poser_une_question [votre question médicale]


## Structure du projet
- main.py: Point d'entrée du bot et configuration Discord
- answer_questions.py: Logique pour répondre aux questions via Groq ou la cache
- data/faq_medical_question.json: Cache des questions et réponses

## Personnalisation

Pour modifier le comportement du bot, vous pouvez:
- Ajuster le prompt dans la fonction answer_questions
- Modifier les paramètres de l'API Groq (température, modèle, etc.)
- Ajouter de nouvelles commandes dans main.py

## Contribution

Les contributions sont les bienvenues! N'hésitez pas à ouvrir une issue ou une pull request.

