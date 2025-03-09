from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
import torch
import json

def fine_tune_model(train_data_file, model_name="llama_model"):
    # Charger le modèle et le tokenizer
    model = LlamaForCausalLM.from_pretrained(model_name)
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    
    # Charger les données de fine-tuning
    with open(train_data_file, 'r') as f:
        train_data = json.load(f)

    # Préparation des données pour le fine-tuning
    train_encodings = tokenizer([entry['prompt'] for entry in train_data], truncation=True, padding=True)
    train_labels = tokenizer([entry['response'] for entry in train_data], truncation=True, padding=True)
    
    # Définir les arguments pour le fine-tuning
    training_args = TrainingArguments(
        output_dir="./models/llama_model",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
    )
    
    # Fine-tuning du modèle
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_encodings,
        eval_dataset=train_encodings,
    )
    
    trainer.train()

    # Sauvegarder le modèle fine-tuné
    model.save_pretrained("models/llama_model")
    tokenizer.save_pretrained("models/llama_model")

