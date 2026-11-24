import tiktoken

encoding = tiktoken.get_encoding("o200k_harmony")

# ids = encoding.encode("123456789101112")
# print(len(ids), ids, [encoding.decode([i]) for i in ids])

from dotenv import load_dotenv

load_dotenv()

from groq import Groq

client = Groq()  # reads GROQ_API_KEY from the environment
# system = {"role": "system", "content": "You are FinCoach, a personal finance assistant. Reply in one short sentence."}

# first = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[system, {"role": "user", "content": "My monthly take-home is ₹1,20,000."}],
# )
# print(first.choices[0].message.content)

# history = [
#     system,
#     {"role": "user", "content": "My monthly take-home is ₹1,20,000."},
#     {"role": "user", "content": "What is my monthly take-home?"},
# ]

# total_tokens = 0
# for message in history:
#     print("encoding: ", len(encoding.encode(message.get("content"))))
#     total_tokens += len(encoding.encode(message.get("content")))
# print("Total tokens sent: ", total_tokens)

# response = client.chat.completions.create(model="openai/gpt-oss-120b", messages=history)
# print(response.choices[0].message.content)
# print(response.usage.prompt_tokens, "tokens the model read")

# def ask(messages, **settings):
#     response = client.chat.completions.create(model="openai/gpt-oss-120b", messages=messages, **settings)
#     return response.choices[0].message.content

# print(ask([{"role": "user", "content": "In one sentence, what does a customer support ticket record?"}], **{"temperature": 0}))

# structured = """You sort customer support tickets for an online shop.

# Categories:
# - billing: payments, charges, refunds
# - shipping: parcels, delivery, damaged boxes
# - other: anything else

# Reply with one line of JSON and nothing else, like this:
# {"category": "shipping", "priority": 3}
# priority is 1 (can wait) to 5 (urgent)."""

# conversation = [{"role": "system", "content": structured}]
# for turn in range(40):
#     conversation.append({"role": "user", "content": f"Ticket {turn}: my parcel has not arrived yet"})
#     conversation.append({"role": "assistant", "content": '{"category": "shipping", "priority": 3}'})

# def count_tokens(messages):
#     return sum(len(encoding.encode(message["content"])) for message in messages)

# def trim(messages, budget):
#     system, rest = messages[:1], messages[1:]

#     while rest and count_tokens(system + rest) > budget:
#         rest = rest[1:]

#     return system + rest


# print(f"Conversation: {len(conversation)}, message tokens: {count_tokens(conversation)}")

# short = trim(conversation, 480)
# print(f"{len(short)} messages, {count_tokens(short)}, tokens")
# print(f"Oldest: {short[1]['content']}")

system = {"role": "system", "content": "You are FinCoach, a personal finance assistant. Reply in one short sentence."}

turns = [
    "My monthly take-home is ₹1,20,000.",
    "My expenses are ₹60,000 a month.",
    "What is the most important thing I should do this month?",
    "Suggest the best fund that I can invest these 30k"
]
history = [system]
for turn in turns:
    history.append({"role": "user", "content": turn})
    response = client.chat.completions.create(model="openai/gpt-oss-120b", messages=history)
    history.append({"role": "assistant", "content": response.choices[0].message.content})
    print(f"###### turn: {turn}, assisstant: {response.choices[0].message.content}")
    print(len(history), "messages,", response.usage.prompt_tokens, "tokens sent")