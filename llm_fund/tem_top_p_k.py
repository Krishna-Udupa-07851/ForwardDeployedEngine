from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()  # reads GROQ_API_KEY from the environment
# prompt = [{"role": "user", "content": "Suggest a name for a small online shop that sells tea. Reply with the name only."}]

# for temperature in (0, 1):
#     names = []
#     for _ in range(3):
#         response = client.chat.completions.create(
#             model="openai/gpt-oss-120b", messages=prompt, temperature=temperature
#         )
#         names.append(response.choices[0].message.content)
#     print(temperature, names)

# import math


# def softmax(scores):
#     exps = {word: math.exp(score) for word, score in scores.items()}
#     total = sum(exps.values())
#     return {word: e / total for word, e in exps.items()}

# # made-up scores for the word after "The cat sat on the"
# scores = {"mat": 4.0, "floor": 3.1, "sofa": 2.6, "roof": 1.2, "moon": -1.5}

# # for temperature in (0.2, 1.0, 1.8, 0.5, 3):
# #     probs = softmax({word: score / temperature for word, score in scores.items()})
# #     print(temperature, {word: round(p, 2) for word, p in probs.items()})

# probs = softmax(scores)
# ranked = sorted(probs, key=probs.get, reverse=True)  # likeliest first

# kept1, total1 = [], 0.0
# for word in ranked:
#     if total1 >= 0.5:
#         break
#     kept1.append(word)
#     total1 += probs[word]

# kept2, total2 = [], 0
# for word in ranked:
#     if total2 >= 0.9:
#         break
#     kept2.append(word)
#     total2 += probs[word]

# print("top_p=0.5 keeps", kept1, "holding", round(total1, 3))
# print("top_k=2 keeps", ranked[:2])
# print("top_p=0.9 keeps", kept2, "holding", round(total2, 3))
# print("top_k=2 keeps", ranked[:2])

for model in client.models.list().data:
    if model.id == "openai/gpt-oss-120b":
        print(model)
        print("###############", model.supported_features)
        print(model.supported_sampling_parameters)