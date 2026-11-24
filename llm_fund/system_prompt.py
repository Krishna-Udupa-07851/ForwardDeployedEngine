structured = """
You sort customer support tickets for an online shop.

Reply with one line of JSON and nothing else, like this:
{"category": "shipping", "priority": 3}
priority is 1 (can wait) to 5 (urgent).

Categories:
- billing: payments, charges, refunds
- shipping: parcels, delivery, damaged boxes
- other: account changes, cancelling an order, anything else

"""

examples = [
    {"role": "user", "content": "Where is my delivery? It is a week late"},
    {"role": "assistant", "content": '{"category": "shipping", "priority": 3}'},
    {"role": "user", "content": "The delivery driver demanded extra cash for shipping at my door"},
    {"role": "assistant", "content": '{"category": "billing", "priority": 5}'},
    {"role": "user", "content": "You took money from my card two times"},
    {"role": "assistant", "content": '{"category": "billing", "priority": 4}'},
    
    {"role": "user", "content": "Can I change the email on my account?"},
    {"role": "assistant", "content": '{"category": "other", "priority": 2}'},
    
]


from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

tickets = [
    ("I was charged twice for one order", "billing"),
    ("My parcel has not arrived", "shipping"),
    ("Can I get a refund for the blue mug?", "billing"),
    ("How do I change my password?", "other"),
    ("The parcel arrived but the box was crushed", "shipping"),
    ("The courier asked me to pay a delivery fee at the door", "billing"),
    ("I want to cancel my order before it ships", "other"),
]


def ask(messages, **settings):
    response = client.chat.completions.create(model="openai/gpt-oss-120b", messages=messages, **settings)
    return response.choices[0].message.content

for text, expected in tickets:
    answer = ask([ *examples, {"role": "user", "content": text}])
    print(f"{expected:9} {answer}")