# 🤖 Rule-Based AI Chatbot — DecodeLabs Project 1

**Batch:** 2026 | **Powered by:** DecodeLabs  
**Track:** Artificial Intelligence | **Milestone:** Project 1

## 📌 Overview
A rule-based AI chatbot built using pure Python control flow and dictionary-based intent matching. No machine learning — just deterministic logic, demonstrating the foundational architecture of AI guardrail systems.

## 🏗️ Architecture: IPO Model
- **Input** → Sanitization (`.strip().lower()`)
- **Process** → Hash Map lookup (`dict.get()`) — O(1) complexity
- **Output** → Response generation with fallback handling

## ✅ Features
- Continuous `while` loop (heartbeat)
- Input sanitization (case & whitespace handling)
- Dictionary knowledge base with 15+ intents
- O(1) lookup via `.get()` — avoids if-elif O(n) ladder
- Fallback response for unknown inputs
- Clean exit strategy

## 🚀 How to Run
```bash
py chatbot.py
```

## 🛠️ Tech Stack
- Python 3.x
- Pure standard library (no dependencies)

## 👨‍💻 Author
**Hamza Rizwan** — AI Intern, DecodeLabs Batch 2026  
[LinkedIn](https://linkedin.com/in/hamza-rizwan-339bb7297) | [GitHub](https://github.com/hamza-r1zwan)