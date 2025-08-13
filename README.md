
# RecommendBot AI 📚

**AI-powered book recommendation bot that suggests books based on genre.**

RecommendBot AI is a Python desktop application built with **Tkinter** that uses **AI zero-shot classification** to detect book genres from user input and fetches real book suggestions from the **Google Books API**. Perfect for discovering books in your favorite genres!

---

## Features

- AI-powered genre detection from user input
- Fetches real book titles from Google Books API
- Supports multiple genres: action, comedy, romance, horror, fantasy, historical, adventure
- Interactive GUI built with Tkinter
- Easy-to-use and beginner-friendly

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/recommendbot-ai.git
   cd recommendbot-ai
````

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

> **Dependencies:** `transformers`, `torch`, `tkinter`, `requests`

---

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Type a message describing the type of book you like (e.g., “I like scary stories” or “I enjoy fantasy adventures”).

3. The AI will detect your preferred genre and fetch a list of recommended books.

4. Type `exit` to close the chat.

---

## Supported Genres

* Action
* Comedy
* Romance
* Horror
* Fantasy
* Historical
* Adventure

---

