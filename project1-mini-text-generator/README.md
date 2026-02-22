# Mini Text Generator (Tiny GPT Concept)

## 📌 Project Overview
This project demonstrates the basic idea behind how Large Language Models (LLMs) generate text.

It uses simple word pattern learning to predict the next word in a sentence.

---

## 🧠 Concept Behind the Project

The program:

1. Takes small training sentences.
2. Learns word-to-word relationships.
3. Predicts the next word based on learned patterns.
4. Generates text step-by-step.

This simulates the core idea of how models like GPT work — predicting the next token repeatedly.

---

## ⚙️ How It Works

- Splits sentences into words.
- Builds a dictionary mapping:
  - Current word → Possible next words
- Randomly selects a next word.
- Repeats generation for a fixed length.

---

