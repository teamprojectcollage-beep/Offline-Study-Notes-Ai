import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3
import ollama  # pip install ollama
from datetime import datetime

# System prompt for the study assistant
SYSTEM_PROMPT = "You are an intelligent AI study assistant for students. Help organize and summarize notes clearly. Use bullet points, headings, and simple language. Generate concise summaries, key points, important terms, or practice questions when asked. Keep responses structured and easy to revise."

# Database setup (local file)
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

def generate_summary():
    title = title_entry.get().strip()
    user_input = input_text.get("1.0", tk.END).strip()
    
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter your notes or topic.")
        return
    
    if not title:
        title = "Untitled Notes"
    
    try:
        # Generate summary using local LLM (Mistral)
        response = ollama.chat(
            model='mistral',
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': f"Summarize and organize these study notes clearly:\n\n{user_input}"}
            ]
        )
        ai_summary = response['message']['content']
        
        # Display the summary
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, ai_summary)
        output_text.config(state=tk.DISABLED)
        
        # Save to database
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('INSERT INTO notes (title, user_input, ai_summary, timestamp) VALUES (?, ?, ?, ?)',
                       (title, user_input, ai_summary, timestamp))
        conn.commit()
        
        messagebox.showinfo("Success", "Summary generated and saved successfully!")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate summary:\n{str(e)}\n\nMake sure Ollama is running and 'mistral' model is downloaded.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Offline Study Notes AI Assistant")
root.geometry("800x700")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Note Title:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
title_entry = tk.Entry(root, width=70, font=("Arial", 11))
title_entry.pack()

tk.Label(root, text="Paste your raw notes or topic here:", font=("Arial", 12), bg="#f0f0f0").pack(pady=(20,5))
input_text = scrolledtext.ScrolledText(root, height=10, width=90, font=("Arial", 11))
input_text.pack(padx=20)

submit_button = tk.Button(root, text="Generate Summary / Organize Notes", command=generate_summary,
                          bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), pady=10)
submit_button.pack(pady=20)

tk.Label(root, text="AI-Generated Summary:", font=("Arial", 12), bg="#f0f0f0").pack(pady=(20,5))
output_text = scrolledtext.ScrolledText(root, height=15, width=90, font=("Arial", 11), state=tk.DISABLED)
output_text.pack(padx=20)

root.mainloop()

# Close database when app closes
conn.close()