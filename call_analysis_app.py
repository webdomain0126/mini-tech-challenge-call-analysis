"""
call_analysis_app.py

Mini Tech Challenge - Call Analysis App (Mocked for testing without Groq API)
- Simple Flask app with UI and JSON endpoint.
- Generates a 2-3 sentence summary and sentiment using a mock function.
- Prints results to console and appends to call_analysis.csv.

Usage:
  1. Create a virtualenv and install requirements: pip install -r requirements.txt
  2. Run: python call_analysis_app.py --test
  3. Or run Flask server: python call_analysis_app.py
"""

import os
import csv
from flask import Flask, request, render_template_string, jsonify

CSV_FILE = "call_analysis.csv"

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<title>Call Analysis - Mini Tech Challenge</title>
<h1>Call Analysis (Mock)</h1>
<form method="post" action="/analyze">
  <textarea name="transcript" rows="10" cols="80" placeholder="Paste transcript here...">Hi, I was trying to book a slot yesterday but the payment failed...</textarea><br>
  <button type="submit">Analyze</button>
</form>
<p>Or send JSON POST to <code>/analyze</code> with <code>{"transcript": "..."}</code></p>
"""

RESULT_HTML = """
<!doctype html>
<title>Result</title>
<h1>Result</h1>
<p><strong>Transcript:</strong></p>
<pre>{{ transcript }}</pre>
<p><strong>Summary:</strong> {{ summary }}</p>
<p><strong>Sentiment:</strong> {{ sentiment }}</p>
<p><a href="/">Back</a></p>
"""

def call_groq_summary_and_sentiment(transcript: str) -> (str, str):
    """Mock function for testing without Groq API."""
    # Generate a fake summary: first 2 sentences
    sentences = [s.strip() for s in transcript.split('.') if s.strip()]
    summary = '. '.join(sentences[:2]) + ('.' if sentences else '')

    # Fake sentiment detection
    low = transcript.lower()
    if any(w in low for w in ["angry", "frustrated", "upset", "not working", "failed"]):
        sentiment = "Negative"
    elif any(w in low for w in ["happy", "great", "thank", "thanks", "satisfied"]):
        sentiment = "Positive"
    else:
        sentiment = "Neutral"

    return summary, sentiment

def save_to_csv(transcript: str, summary: str, sentiment: str, csv_file: str = CSV_FILE):
    fieldnames = ["Transcript", "Summary", "Sentiment"]
    write_header = not os.path.exists(csv_file)
    with open(csv_file, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow({"Transcript": transcript, "Summary": summary, "Sentiment": sentiment})

@app.route('/', methods=["GET"])
def index():
    return render_template_string(INDEX_HTML)

@app.route('/analyze', methods=["POST"])
def analyze():
    transcript = request.get_json().get("transcript") if request.is_json else request.form.get("transcript")
    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400

    summary, sentiment = call_groq_summary_and_sentiment(transcript)

    # Print to console
    print("\n--- New Analysis ---")
    print("Transcript:", transcript)
    print("Summary:", summary)
    print("Sentiment:", sentiment)

    # Save to CSV
    save_to_csv(transcript, summary, sentiment)

    if request.is_json:
        return jsonify({"transcript": transcript, "summary": summary, "sentiment": sentiment})
    else:
        return render_template_string(RESULT_HTML, transcript=transcript, summary=summary, sentiment=sentiment)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Run call analysis app or test it with a sample transcript")
    parser.add_argument('--test', action='store_true', help='Run a quick local test (no server)')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    if args.test:
        sample = "Hi, I was trying to book a slot yesterday but the payment failed and I couldn't complete my booking. I got charged but the confirmation didn't show up. Can you please help?"
        print("Running test with sample transcript:\n", sample)
        s, sent = call_groq_summary_and_sentiment(sample)
        print("Summary:", s)
        print("Sentiment:", sent)
        save_to_csv(sample, s, sent)
        print(f"Transcript analyzed and saved to {CSV_FILE}")
    else:
        app.run(host=args.host, port=args.port, debug=True)

