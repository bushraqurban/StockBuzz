# 📈 StockBuzz - Financial News Sentiment Analyzer

StockBuzz is a web application that analyzes the **sentiment of financial news articles** using the FinBERT model. It helps users understand the market mood surrounding specific keywords like "apple", "gold", or "tech stocks".

> ⚠️ This app is for educational purposes only. It does **not provide financial advice**.

---

## 🎓 About This Project

It demonstrates the integration of:

- NLP models (FinBERT)
- Real-time news data (NewsAPI)
- Web development using Flask

---

## 🚀 Features

- 🔍 Search for financial news using keywords
- 📅 Choose from predefined or custom date ranges (within the past 30 days)
- 💬 See sentiment analysis (positive / neutral / negative)
---

## 🧠 How It Works

1. User inputs a **keyword** and a **date range**
2. The app queries the **NewsAPI** for relevant articles
3. Content is analyzed with **FinBERT**, a sentiment classification model trained on financial data
4. Results are displayed with a visual summary of each article's sentiment

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bushraqurban/stockbuzz.git
   cd stockbuzz


2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your NewsAPI key**:
   Create a file named `API_KEY` (no extension) and paste your API key inside:

   ```
   YOUR_NEWS_API_KEY_HERE
   ```

5. **Run the app**:

   ```bash
   python app.py
   ```

   Visit `http://127.0.0.1:5000` in your browser.

---

## 📁 Project Structure

```
stockbuzz/
│
├── templates/
│   ├── index.html
│   ├── results.html
│   └── about.html
│
├── static/
│   ├── style.css
│   └── images/
│       └── logo.png
│
├── API_KEY              # <-- Add Your NewsAPI key
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🛡 Disclaimer

This application is for **demonstration and educational** use only.
It provides sentiment analysis as **one aspect** of financial news and **should not be used for investment decisions**.

---

## 📬 Contact

Feel free to reach out if you'd like to contribute or collaborate!

---
