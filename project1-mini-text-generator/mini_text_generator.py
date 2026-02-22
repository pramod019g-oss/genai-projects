import random

# Training data
data = [
    "I love AI",
    "I love coding",
    "I love Python",
    "AI is powerful",
    "Python is powerful",
    "Coding is fun"
]

# Build word relationship model
model = {}

for sentence in data:
    words = sentence.split()
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]

        if word not in model:
            model[word] = []

        model[word].append(next_word)

# Generate text
def generate_text(start_word, length=5):
    current_word = start_word
    result = [current_word]

    for _ in range(length):
        if current_word in model:
            next_word = random.choice(model[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break

    return " ".join(result)

# Run program
while True:
    user_input = input("Enter a starting word (or type 'exit'): ")

    if user_input.lower() == "exit":
        break

    print("Generated:", generate_text(user_input))