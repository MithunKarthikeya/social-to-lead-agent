from agent.intent import classify_intent
from agent.rag import retrieve_answer
from agent.state import AgentState
from agent.tools import mock_lead_capture

state = AgentState()

print("🤖 AutoStream Assistant Ready!")

while True:
    user_input = input("\nUser: ")

    # ✅ Exit option
    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye! 👋")
        break

    # 🔥 If already in lead flow, continue it
    if state.stage != "start":
        
        if state.stage == "ask_name":
            state.name = user_input
            print("Agent: Got it! What's your email?")
            state.stage = "ask_email"

        elif state.stage == "ask_email":
            state.email = user_input
            print("Agent: Which platform do you create on? (YouTube, Instagram, etc.)")
            state.stage = "ask_platform"

        elif state.stage == "ask_platform":
            state.platform = user_input

            # ✅ Call tool ONLY after all data
            mock_lead_capture(state.name, state.email, state.platform)

            print("Agent: You're all set! We'll reach out soon 🎉")

            # Reset state (optional)
            state.stage = "start"
            state.name = None
            state.email = None
            state.platform = None

        continue  # skip rest of loop

    # 🔍 Detect intent
    intent = classify_intent(user_input)
    state.intent = intent

    # 😊 Greeting
    if intent == "greeting":
        print("Agent: Hi! 👋 I'm your AutoStream assistant. I can help with pricing, features, or getting you started.")

    # 📊 Query → RAG
    elif intent == "query":
        response = retrieve_answer(user_input)
        print(f"Agent: {response}")

    # 🚀 High Intent → Start Lead Flow
    elif intent == "high_intent":
        print("Agent: Great! Let's get you started 🚀")
        print("Agent: What's your name?")
        state.stage = "ask_name"