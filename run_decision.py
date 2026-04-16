import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable before running this script.")

client = OpenAI(api_key=api_key)

prompt = """
You are an evaluation agent.

Compare 3 suppliers in China for product X based on:
- price
- reliability
- delivery time

Return a ranked list with reasoning.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You structure decisions."},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
