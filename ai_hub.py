import streamlit as st
import json
import os

BRAIN_FILE_PATH = "brainfile/active.json"

def render_ai_hub():
    st.title("🧠 AI Hub — Multi-Agent Thinking Panel")

    st.markdown("""```markdown
This is your multi-AI command center. Select a model, load shared context (Brain File), and submit a prompt.
```""")

    # Model Selector
    model = st.selectbox("Choose your AI model", ["GPT-4 (live)", "Gemini (simulated)", "Claude (simulated)"])

    # Display shared Brain File (trimmed preview)
    st.subheader("🔍 Active Brain File Preview")
    if os.path.exists(BRAIN_FILE_PATH):
        with open(BRAIN_FILE_PATH, "r") as f:
            brain_data = json.load(f)
        st.json(brain_data, expanded=False)
    else:
        st.warning("No Brain File found at brainfile/active.json")

    # Prompt input
    st.subheader("💬 Prompt")
    user_input = st.text_area("Enter your prompt here", height=150)

    # Run the model
    if st.button("Run Model"):
        if not user_input.strip():
            st.warning("Please enter a prompt before running.")
        else:
            with st.spinner(f"Running {model}..."):
                if model == "GPT-4 (live)":
                    st.markdown("```markdown\n[Simulated GPT-4 response based on Brain File and prompt]\n```")
                elif model == "Gemini (simulated)":
                    st.markdown("```markdown\n[Simulated Gemini response]\n```")
                elif model == "Claude (simulated)":
                    st.markdown("```markdown\n[Simulated Claude response]\n```")