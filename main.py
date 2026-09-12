import os
from groq import Groq

os.environ["API_KEY"] = input("Enter your Groq API key: ")
print(
    "Key loaded:",
    "Yes" if os.environ.get("API_KEY") else "No"
)

client = Groq(
    api_key=os.environ.get("API_KEY")
)
print("Groq client created successfully!")
MODEL = "openai/gpt-oss-120b"
print("Model:", MODEL)

def ask_llm(user_prompt, system_prompt=None, temperature=0.7, model=MODEL):
    messages = []

    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })

    messages.append({
        "role": "user",
        "content": user_prompt
    })

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )

    return response
result = ask_llm(
    "Brief in 5 lines about Python with numbered points."
)
print(result.choices[0].message.content)
