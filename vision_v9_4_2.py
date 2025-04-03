import streamlit as st
import subprocess
import os

def render_scraper():
    st.title("📽 vision_v9.4.2 — Smart Video Scraper")

    st.markdown("""```markdown
Paste a YouTube URL below and trigger the smart scraper (vision_v9.4.2).
This will generate a Brain File with understanding score, glossary, and timeline.
```""")

    url = st.text_input("YouTube URL")

    if st.button("Run vision_v9.4.2"):
        if url:
            with st.spinner("Running vision_v9.4.2..."):
                # Run the real scraper script with the given URL
                result = subprocess.run(["python3", "vision_v9.4.2.py", url], capture_output=True, text=True)

            # Show output
            st.success("Scraper finished.")
            st.markdown("```shell\n" + result.stdout + "\n```")
            if result.stderr:
                st.error("Errors:")
                st.markdown("```shell\n" + result.stderr + "\n```")
        else:
            st.warning("Please enter a YouTube URL before running.")