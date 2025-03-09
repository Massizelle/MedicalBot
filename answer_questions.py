import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GROQ_API_KEY')

# Fonction pour lire le fichier JSON et vérifier si la question existe
def get_answer_from_json(question):
    try:
        # Charger le fichier JSON
        with open('data/faq_medical_question.json', 'r', encoding='utf-8') as f:
            faq_data = json.load(f)
        
        # Chercher la question dans les données JSON
        for item in faq_data:
            if item['question'].strip().lower() == question.strip().lower():
                return item['answer']  # Retourner la réponse associée
    except FileNotFoundError:
        return None  # Si le fichier n'existe pas, retourne None

# Fonction pour enregistrer une nouvelle question et réponse dans le fichier JSON
def save_question_answer(question, answer):
    # Nettoyer la réponse pour enlever les sauts de ligne et autres caractères indésirables
    clean_answer = answer.replace("\n", " ").replace("\r", " ").strip()

    # Ajouter une virgule à la fin de la réponse si nécessaire
    if not clean_answer.endswith(','):
        clean_answer += ','

    # Charger les données existantes du fichier JSON
    try:
        with open('data/faq_medical_question.json', 'r', encoding='utf-8') as f:
            faq_data = json.load(f)
    except FileNotFoundError:
        faq_data = []  # Créer une liste vide si le fichier n'existe pas

    # Ajouter la nouvelle question et réponse
    faq_data.append({'question': question, 'answer': clean_answer})

    # Sauvegarder les données dans le fichier JSON
    with open('data/faq_medical_question.json', 'w', encoding='utf-8') as f:
        json.dump(faq_data, f, ensure_ascii=False, indent=4)

# Fonction principale pour répondre aux questions
def answer_questions(content):
    # Chercher la réponse dans le fichier JSON
    answer = get_answer_from_json(content)
    
    if answer:  # Si la réponse est trouvée dans le JSON, on la renvoie
        return answer
    
    # Si la question n'existe pas, on demande à l'API GROQ (Llama) de répondre
    prompt = """
    Tu es un assistant médical. Tu réponds uniquement à des questions médicales. Si une question hors sujet est posée, 
    réponds que tu réponds uniquement aux questions médicales et n'aborde pas d'autres sujets. 
    Pour chaque réponse médicale, fournit un ou deux liens pertinents de pages web concernant la maladie. Réponds de manière claire, précise, et professionnelle.
    Exemple : 
    Si un utilisateur demande 'Quels sont les symptômes de la grippe ?', tu répondras :
    'Les symptômes de la grippe incluent de la fièvre, des frissons, des douleurs musculaires, une toux sèche, et plus encore. 
    Tu peux consulter plus de détails sur la grippe ici : [Lien vers page sur la grippe] et [Autre lien pertinent].'
    
    Si la question est hors sujet, tu réponds :
    'Désolé, je réponds uniquement aux questions médicales. Veuillez poser une question liée à la santé.' 
    Respecte ce format et répond uniquement avec des informations médicales. 
    Je veux aussi que tu sois très gentil, et que tu ajoutes des émojis liés au sujet et à ta réponse.
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt + content}],
        "temperature": 0.7
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)
    
    # Extraire la réponse du modèle Llama
    answer = response.json()["choices"][0]["message"]["content"]

    # Enregistrer la nouvelle question et réponse dans le fichier JSON
    save_question_answer(content, answer)
    
    return answer
