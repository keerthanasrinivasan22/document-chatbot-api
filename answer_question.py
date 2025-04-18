import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def answer_question(question, context):
    prompt = f"Question: {question}\nContext: {context}\nAnswer:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are UNT Bot. Only answer questions related to UNT."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response["choices"][0]["message"]["content"].strip()
