# Offline Study Notes AI Assistant

A simple, fully offline AI tool that helps students summarize and organize their study notes using a local open-source language model (Mistral via Ollama).  
No internet required after initial setup – perfect for low-connectivity areas or exam preparation!

## Features
- Paste raw/messy notes and get clean, structured summaries with bullet points, headings, and key points  
- Local SQLite database to save all notes and summaries  
- Works completely offline  
- Two interface options:  
  - **Desktop GUI** (simple Tkinter window)  
  - **Web App** (modern browser-based interface using Streamlit – recommended for presentation)

## Technologies Used
- Python  
- Ollama + Mistral (local LLM)  
- Tkinter (Desktop GUI)  
- Streamlit (Web App)  
- SQLite (local storage)

## Setup (One-Time Only)
1. Install **Ollama** from https://ollama.com  
2. Open Command Prompt and download the model:  
(Wait for download ~4-5 GB – runs offline forever after this)  
3. Install required Python packages:  
## How to Run

### Option 1: Desktop GUI (Tkinter)
D:
cd Study-Notes-AI
python main.p
- Simple window opens  
- Paste notes and click button

### Option 2: Web App (Streamlit) – Recommended!
D:
cd Study-Notes-AI
python -m streamlit run web_app.py
- Automatically opens in your browser[](http://localhost:8501)  
- Cleaner, modern interface  
- Great for demos and presentations
## Screenshot

<img width="1918" height="1086" alt="Screenshot 2025-12-17 232320" src="https://github.com/user-attachments/assets/542c01d1-589f-4c6a-845a-8cf6849a46d0" />



## Team Members
- AKILESHWARAN S – Backend & Database  
- GOVINDAPPAGARI SAHANA – Frontend & AI Integration  
- ARUNPRABU VENKIDUSAMY – Documentation & Testing

## Future Scope
- Add quiz generation from notes  
- Export summaries to PDF  
- Note categories and search  
- Voice input  
- Fully portable .exe version

## Project for BCA MVP Submission

Thank you for checking out our project!  
We built this as a minimal viable product (MVP) – fully offline, easy to use, and ready for real students. 🚀







