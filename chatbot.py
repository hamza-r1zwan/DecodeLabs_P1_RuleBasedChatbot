# ============================================================
#   DecodeLabs AI Internship — Project 1
#   Rule-Based AI Chatbot
#   Architecture: IPO Model (Input → Process → Output)
# ============================================================

# ── KNOWLEDGE BASE ──────────────────────────────────────────
# Dictionary = Hash Map → O(1) lookup (not if-elif O(n) ladder)
# Each key is a cleaned user intent, value is the bot's reply.

responses = {
    # Greetings
    "hello"         : "Hello! I'm DecodeLabs Bot. How can I assist you?",
    "hi"            : "Hey there! What can I do for you today?",
    "hey"           : "Hey! Ask me anything.",

    # Identity
    "who are you"   : "I'm a Rule-Based AI Chatbot built at DecodeLabs Batch 2026.",
    "what are you"  : "I'm a deterministic logic engine — no hallucinations, pure rules.",
    "your name"     : "You can call me DecoBot.",

    # About AI / DecodeLabs
    "what is ai"    : "AI is the simulation of human intelligence by machines using logic, data, and algorithms.",
    "what is decodelabs" : "DecodeLabs is an industrial AI training platform helping interns build real-world AI projects.",

    # Small talk
    "how are you"   : "I'm running at 100% uptime! All systems nominal.",
    "what can you do": "I can answer predefined questions using rule-based logic. Ask me anything in my knowledge base!",
    "tell me a joke" : "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",

    # Help
    "help"          : "Try asking: 'what is ai', 'who are you', 'tell me a joke', or type 'quit' to exit.",

    # Farewell
    "bye"           : "Goodbye! Keep building. 🚀",
    "goodbye"       : "See you next session. Stay curious!",
    "good night"    : "Good night! Rest well, engineer.",
}

# ── FALLBACK ─────────────────────────────────────────────────
# Shown when user input doesn't match any key in the dictionary

FALLBACK = "I don't understand that yet. Type 'help' to see what I know."

# ── EXIT COMMANDS ─────────────────────────────────────────────
EXIT_COMMANDS = {"quit", "exit", "q", "bye", "goodbye"}


# ── PHASE 1: INPUT SANITIZATION FUNCTION ─────────────────────
def sanitize(raw_input: str) -> str:
    """
    Normalize raw user text:
    - Strip leading/trailing whitespace
    - Convert to lowercase
    So 'HeLLo  ' and 'hello' both become 'hello'
    """
    return raw_input.strip().lower()


# ── PHASE 2: PROCESS / INTENT MATCHING ───────────────────────
def get_response(clean_input: str) -> str:
    """
    O(1) dictionary lookup using .get()
    If key found  → return mapped response
    If key absent → return FALLBACK
    Single atomic operation: lookup + fallback combined.
    """
    return responses.get(clean_input, FALLBACK)


# ── PHASE 3: OUTPUT / MAIN LOOP ───────────────────────────────
def run_chatbot():
    """
    The Heartbeat — Infinite while loop.
    Stays alive until a Kill Command (exit/quit) is received.
    IPO cycle repeats every iteration.
    """
    print("=" * 55)
    print("   DecodeLabs AI Chatbot  |  Batch 2026")
    print("   Type 'help' to see commands. 'quit' to exit.")
    print("=" * 55)

    while True:  # ← THE INFINITE LOOP (heartbeat)

        # ── INPUT ──────────────────────────────────────────
        raw = input("\nYou: ")

        # ── SANITIZATION ───────────────────────────────────
        clean = sanitize(raw)

        # ── EXIT STRATEGY ──────────────────────────────────
        # Check kill commands BEFORE dictionary lookup
        if clean in EXIT_COMMANDS:
            print("Bot: Goodbye! Session terminated. 👋")
            break  # ← CLEAN BREAK — exits the while loop

        # ── PROCESS + OUTPUT ───────────────────────────────
        reply = get_response(clean)   # O(1) hash map lookup
        print(f"Bot: {reply}")


# ── ENTRY POINT ───────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()