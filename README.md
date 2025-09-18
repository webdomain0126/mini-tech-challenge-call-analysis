📌 Project Overview

This is my submission for the Mini Tech Challenge.
The project is a Python application that processes customer call transcripts using the Groq API.

It can:

✅ Summarize a conversation in 2–3 sentences.

✅ Extract the customer’s sentiment (Positive / Neutral / Negative).

✅ Print the original transcript, summary, and sentiment.

✅ Save the results into a .csv file → Transcript | Summary | Sentiment.

⚙️ Features

Simple command-line interface to run test transcripts.

Uses Groq API for summarization and sentiment analysis.

Auto-generates call_analysis.csv with structured output.

Easy to extend for batch transcript processing.

🗂️ Project Structure
├── call_analysis_app.py    # Main Python script
├── call_analysis.csv       # Output file (auto-generated)
├── requirements.txt        # Dependencies
└── README.md               # Documentation

🚀 How to Run

Clone this repository:

git clone https://github.com/yourusername/mini-tech-challenge-call-analysis.git
cd mini-tech-challenge-call-analysis


Install dependencies:

pip install -r requirements.txt


Run the script with a sample transcript:

python call_analysis_app.py --test


Output:

Transcript, summary, and sentiment will be printed in the terminal.

Results will also be saved in call_analysis.csv.

📊 Example

Input:

Hi, I was trying to book a slot yesterday but the payment failed and I couldn't complete my booking.


Output (Terminal + CSV):

Transcript → "Hi, I was trying to book a slot yesterday but the payment failed…"

Summary → "Customer faced a payment failure while booking a slot."

Sentiment → "Negative"

🎥 Video Demo

A 4–5 minute video (recorded using OBS Studio) explains:

My approach to solving the challenge.

Step-by-step walkthrough of the code.

Running the script successfully.

Opening the generated .csv file.

👉 Watch the Video Demo here 

📂 Deliverables

Python Script: GitHub Repo Link

Video Recording: Google Drive Video Link  https://drive.google.com/file/d/1LGDQHkeF2jkw6nCzeqZ3yx1V35N9JbDV/view?usp=sharing

✨ Developed by Taslima Akhter
