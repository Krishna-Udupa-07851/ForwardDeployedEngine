from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

prompt = [{"role": "user", "content": "Write a 3 paragraph apology to a customer whose parcel is late."}]

response = client.chat.completions.create(
    model="openai/gpt-oss-120b", messages=prompt, max_completion_tokens=100, reasoning_effort="medium"
)
choice = response.choices[0]
print(choice.finish_reason, repr(choice.message.content))
print("#########", response.usage.completion_tokens_details.reasoning_tokens)