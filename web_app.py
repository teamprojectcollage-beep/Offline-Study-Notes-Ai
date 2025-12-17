import streamlit as st
from ollama import chat  # For Ollama API
import sqlite3
from datetime import datetime

# Page config
st.set_page_config(page_title="Offline Study Notes AI Assistant", layout="wide")
st.title("📚 Offline Study Notes AI Assistant")
st.markdown("Paste your raw notes below and get an organized summary instantly (fully offline with local LLM)!")

# System prompt (same as before)
SYSTEM_PROMPT = "You are an intelligent AI study assistant for students. Help organize and summarize notes clearly. Use bullet points, headings, and simple language. Generate concise summaries, key points, important terms, or practice questions when asked. Keep responses structured and easy to revise."

# Database setup (local)
conn = sqlite3.connect('study_notes.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        user_input TEXT NOT NULL,
        ai_summary TEXT NOT NULL,
        timestamp TEXT
    )
''')
conn.commit()

# Sidebar for title
with st.sidebar:
    st.header("Note Details")
    title = st.text_input("Note Title (optional)", value="Untitled Notes")

# Main input
user_input = st.text_area("Paste your raw notes or topic here:", height=300, placeholder="e.g., Photosynthesis is the process by which plants...")

if st.button("Generate Summary / Organize Notes", type="primary"):
    if not user_input.strip():
        st.warning("Please enter some notes!")
    else:
        with st.spinner("Generating summary... (first time may take 30-60 seconds)"):
            try:
                # Call local Ollama model
                response = chat(
                    model='mistral',
                    messages=[
                        {'role': 'system', 'content': SYSTEM_PROMPT},
                        {'role': 'user', 'content': f"Summarize and organize these study notes clearly:\n\n{user_input}"}
                    ]
                )
                ai_summary = response['message']['content']
                
                # Display summary
                st.success("Summary Generated!")
                st.markdown("### AI-Generated Summary:")
                st.markdown(ai_summary)
                
                # Save to database
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute('INSERT INTO notes (title, user_input, ai_summary, timestamp) VALUES (?, ?, ?, ?)',
                               (title, user_input, ai_summary, timestamp))
                conn.commit()
                st.info("Notes saved locally!")
                
            except Exception as e:
                st.error(f"Error: {str(e)}\nMake sure Ollama is running with 'mistral' model.")

# Footer
st.markdown("---")
st.caption("Built with Streamlit + Ollama (local LLM) | Fully offline | Team: AKILESHWARAN S, GOVINDAPPAGARI SAHANA, ARUNPRABU VENKIDUSAMY")