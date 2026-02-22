from openai import OpenAI

client = OpenAI()

print("Memory Chatbot started... (type 'exit' to stop)")

# Define personality ONCE
messages = [
    {"role": "system", "content": """
You are a technical interviewer.
When the user claims a skill, you must respond ONLY with one technical question.
Do not praise.
Do not explain.
Be direct.
"""}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot ended.")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3
        )

        reply = response.choices[0].message.content
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})

        # Limit memory
        if len(messages) > 7:
            messages = [messages[0]] + messages[-6:]

    except Exception as e:
        print("Error:", e)