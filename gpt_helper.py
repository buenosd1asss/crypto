import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

def ask_gpt(data):
    if "error" in data:
        return f"Ошибка: {data['error']}"

    prompt = f"""
Crypto: {data['name']}
Price: ${data['price']}
Market Cap: ${data['market_cap']}
Rank: {data['rank']}
News: {data['news']}

Summarize this cryptocurrency's current status.
"""

    response = requests.post(
        "https://api-inference.huggingface.co/models/google/flan-t5-small",
        headers={"Authorization": f"Bearer {HF_API_KEY}"},
        json={"inputs": prompt}
    )

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"AI error: {response.text}"
