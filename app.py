import streamlit as st
from home import render_home
from vision_v9_4_2 import render_scraper
from ai_hub import render_ai_hub

st.set_page_config(page_title="Bifrost", layout="wide")
st.sidebar.title("🧭 Bifrost Navigation")

page = st.sidebar.radio("Go to", ["🏠 Home", "📽 vision_v9_4_2", "🧠 AI Hub"])

if page == "🏠 Home":
    render_home()
elif page == "📽 vision_v9_4_2":
    render_scraper()
elif page == "🧠 AI Hub":
    render_ai_hub()