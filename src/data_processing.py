import pandas as pd
import json
from sklearn.model_selection import train_test_split

# Fonction pour nettoyer les données médicales
def clean_data(input_file):
    # Charger les données
    df = pd.read_csv(input_file)
    
    # Suppression des doublons et des données erronées
    df.drop_duplicates(inplace=True)
    df = df.dropna(subset=['question', 'answer'])
    
    # Sauvegarder les données nettoyées
    df.to_json('data/cleaned_medical_data.json', orient='records', lines=True)
    return df

# Fonction pour structurer les données pour le fine-tuning
def structure_data_for_finetuning(df):
    # Structurer les données dans un format adapté au fine-tuning (ex. format de paires question/réponse)
    training_data = [{"prompt": row["question"], "response": row["answer"]} for index, row in df.iterrows()]
    
    with open('data/structured_finetuning_data.json', 'w') as f:
        json.dump(training_data, f)

# Fonction pour diviser les données en ensembles d'entraînement et de test
def split_data(input_file):
    df = pd.read_json(input_file)
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
    
    train_data.to_json('data/train_data.json', orient='records', lines=True)
    test_data.to_json('data/test_data.json', orient='records', lines=True)

