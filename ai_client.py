import os

from groq import Groq

import settings

client = Groq(
    # This is the default and can be omitted
    api_key="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"
)

def get_ai_response(user_input: str):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": settings.ROLE
                },
                {
                    "role": "user",
                    "content": settings.PROMPT + user_input,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        print(settings.PROMPT + user_input)
        return chat_completion.choices[0].message.content
    except:
        return "Error"