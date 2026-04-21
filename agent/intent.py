def classify_intent(user_input: str) -> str:
    text = user_input.lower()

    # 🔥 HIGH INTENT FIRST (important)
    high_intent_words = ["buy", "subscribe", "start", "try", "sign up", "interested", "want"]

    if any(word in text for word in high_intent_words):
        return "high_intent"

    # Greeting
    greeting_words = ["hi", "hello", "hey"]
    if any(word in text for word in greeting_words):
        return "greeting"

    # Default → query
    return "query"