from openai import OpenAI
client = OpenAI()(
    api_key="OPEN_AI_KEY"
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant, skilled in performing general tasks like alexa and google cloud."
        },
        {
            "role": "user",
            "content": "what is coding?"
        }
    ]
)

print(completion.choices[0].message.content)

