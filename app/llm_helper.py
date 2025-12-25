import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_reason(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional product support assistant. "
                        "Be clear, polite, and policy-aware. Do not promise approvals."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=150
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OpenAI error:", str(e))
        return None
