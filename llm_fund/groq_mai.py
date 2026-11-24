from importlib.metadata import version
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# print("##########", version('groq'))

client = Groq()
# response = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[{"role": "user", "content": "Reply with single word: Ready"}],
#     )
# print(response.choices[0].message.content)
# print(response.model)

# for model in client.models.list().data:
#     print(model.id)

# models = {model.id: model for model in client.models.list().data}

# for name in ["openai/gpt-oss-20b", "openai/gpt-oss-120b"]:
#     model = models[name]
#     print(name, "| made by", model.owned_by, "| weights:", model.hugging_face_id)

# questions = [{"role": "user", "content": "In one sentence what is a refund?"}]

# for name in ["openai/gpt-oss-20b", "openai/gpt-oss-120b"]:
#     response = client.chat.completions.create(model=name, messages=questions)
#     print(name)
#     print(" ", response.choices[0].message.content)

"""Assign 1"""
# models = [model for model in client.models.list().data if model.id in ["openai/gpt-oss-20b", "openai/gpt-oss-120b"]]
# for model in models:
#     print(model.id, ":", model.context_window)

"""Assign 2: Give a complex question to the 20B and 120B models and compare the answers"""

# question = """A baker makes 6 trays of cookies, with 8 cookies on each tray. After selling 17 cookies, how many cookies are left? Show the two calculation steps briefly."""

# answers = {}
# for model_name in ["openai/gpt-oss-20b", "openai/gpt-oss-120b"]:
#     response = client.chat.completions.create(
#         model=model_name,
#         messages=[{"role": "user", "content": question}],
#     )
#     answer = response.choices[0].message.content
#     answers[model_name] = answer
#     print(f"\n--- {model_name} ---\n{answer}")


"""Assign 3""" 
# print(sorted(model.id for model in client.models.list().data))

for prompt in [
    "What is the refund policy of Brightcart, the online shop? Answer in two sentences.",
    "Write the refund section of Brightcart's help page in two sentences.",
]:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
    )
    print(prompt)
    print("  ->", response.choices[0].message.content)