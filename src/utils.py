from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

# Fonction pour générer une réponse médicale
def generate_medical_response(prompt, model: LlamaForCausalLM, tokenizer: LlamaTokenizer):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(inputs["input_ids"], max_length=200, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

