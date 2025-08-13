import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline
import requests

# 🧠 AI for genre classification
classifier = pipeline("zero-shot-classification")
possible_genres = ["action", "comedy", "romance", "horror", "fantasy", "historical", "adventure"]

# 📚 Function to search real books from Google Books API
def search_books_google(genre):
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}&langRestrict=en&maxResults=5"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        try:
            titles = [book["volumeInfo"]["title"] for book in data.get("items", [])]
            return titles if titles else ["(No suitable books found)"]
        except:
            return ["(Error reading API response)"]
    else:
        return ["(Error connecting to Google Books)"]

# 🗨️ Main function that responds in the GUI
def send_message():
    message = user_input.get()

    if message.strip() == "":
        return

    chat.insert(tk.END, f"You: {message}\n")
    user_input.delete(0, tk.END)

    if message.lower() == "exit":
        chat.insert(tk.END, "RecommendBot: Goodbye! 📚🎬\n")
        return

    # 🧠 AI detects genre
    result = classifier(message, possible_genres)
    detected_genre = result["labels"][0]

    # 📚 Search real books on Google Books for the detected genre
    books = search_books_google(detected_genre)
    response = f"Recommended books ({detected_genre.title()}): {', '.join(books)}"
    chat.insert(tk.END, f"RecommendBot: {response}\n")

# 🖼️ Graphical interface
window = tk.Tk()
window.title("RecommendBot AI 📚")

chat = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
chat.pack(padx=10, pady=10)
chat.insert(tk.END, "RecommendBot: Hi! Tell me what type of book you like.\n")

user_input = tk.Entry(window, width=50)
user_input.pack(padx=10, pady=5)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

window.mainloop()


