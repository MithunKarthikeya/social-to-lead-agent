import json

def load_knowledge():
    with open("data/knowledge.json") as f:
        return json.load(f)

def retrieve_answer(query: str):
    kb = load_knowledge()
    query = query.lower()

    # 🔥 Better keyword matching
    if any(word in query for word in ["price", "pricing", "plan", "cost"]):
        return f"""
📊 AutoStream Pricing:

Basic Plan:
- $29/month
- 10 videos/month
- 720p resolution

Pro Plan:
- $79/month
- Unlimited videos
- 4K resolution
- AI captions
"""

    if "refund" in query:
        return kb["policies"]["refund"]

    if "support" in query:
        return kb["policies"]["support"]

    return "I can help you with pricing, plans, or features!"