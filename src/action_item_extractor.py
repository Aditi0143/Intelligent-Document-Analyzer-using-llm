from transformers import pipeline

# Use smaller model
generator = pipeline("text2text-generation", model="google/flan-t5-small")

def extract_action_items(text):
    prompt = f"Extract action items with tasks, assigned persons, and deadlines from this text:\n{text}"
    output = generator(prompt, max_length=128, do_sample=False)[0]['generated_text']
    return output
