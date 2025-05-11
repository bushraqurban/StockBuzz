from flask import Flask, render_template, request
from transformers import pipeline
from datetime import datetime, timedelta
import requests

app = Flask(__name__)
pipe = pipeline("text-classification", model="ProsusAI/finbert")

# Load API key
with open('API_KEY') as f:
    API_KEY = f.read().strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form.get('keyword', '').strip()
        range_option = request.form.get('range')
        custom_date = request.form.get('custom_date')

        # Validate keyword
        if not keyword:
            return render_template('index.html', error="Keyword is required.")

        try:
            if range_option == 'custom' and custom_date:
                start_date = datetime.strptime(custom_date, '%Y-%m-%d')
                if (datetime.now() - start_date).days > 30:
                    return render_template('index.html', error="Sorry, custom date cannot be more than 30 days in the past.")
                date = start_date.strftime('%Y-%m-%d')
            elif range_option:
                days = int(range_option)
                if days > 30:
                    return render_template('index.html', error="You can only analyze news from the past 30 days.")
                date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
            else:
                return render_template('index.html', error="Date selection is required.")
        except ValueError:
            return render_template('index.html', error="Invalid date format.")

        url = 'https://newsapi.org/v2/everything'
        params = {
            'q': keyword,
            'from': date,
            'sortBy': 'popularity',
            'apiKey': API_KEY
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return render_template('index.html', error="Unable to connect to the news service. Please check your internet connection.")

        articles = response.json().get('articles', [])
        if not articles:
            return render_template('index.html', error="No articles found. Try a different keyword or a more recent date.")

        results = []
        total_score = 0
        count = 0

        for article in articles:
            title = article.get('title') or ""
            description = article.get('description') or ""
            content = article.get('content') or ""

            if keyword.lower() in (title + description).lower():
                if content:
                    sentiment = pipe(content[:512])[0]
                else:
                    sentiment = {'label': 'neutral', 'score': 0.0}

                score = sentiment['score'] if sentiment['label'] == 'positive' else \
                        -sentiment['score'] if sentiment['label'] == 'negative' else 0

                total_score += score
                count += 1
                results.append({
                    'title': title,
                    'url': article.get('url'),
                    'description': description,
                    'sentiment': sentiment['label'],
                    'score': round(sentiment['score'], 2)
                })

        if not results:
            return render_template('index.html', error="Insufficient data for analysis.")

        final_score = total_score / count
        overall = "Positive" if final_score > 0.15 else "Negative" if final_score < -0.15 else "Neutral"

        return render_template('results.html', results=results, keyword=keyword,
                               final_score=round(final_score, 2), overall=overall)

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
