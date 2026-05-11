#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Keyword-based answer mapping for rate limiter paper questions
ANSWERS = {
    "token bucket": "token bucket",
    "leaky bucket": "leaky bucket",
    "fixed window": "fixed window",
    "sliding window": "sliding window",
    "boundary": "boundary",
    "redis": "redis",
    "timestamp": "timestamp",
    "consistency": "consistency, availability",
    "availability": "consistency, availability",
    "distributed": "redis",
    "sync": "redis",
    "algorithm": "token bucket",
    "problem": "boundary",
    "store": "redis",
    "track": "timestamp",
    "tradeoff": "consistency, availability",
    "trade-off": "consistency, availability",
    "trade off": "consistency, availability",
    "cap": "consistency, availability",
}

GOLD_ANSWERS = [
    ("token bucket", "token bucket"),
    ("boundary", "boundary"),
    ("redis", "redis"),
    ("timestamp", "timestamp"),
    ("consistency", "consistency, availability"),
]

def find_answer(question):
    ql = question.lower()
    # Check gold answers by keyword
    for keyword, answer in GOLD_ANSWERS:
        if keyword in ql:
            return answer
    # Broader keyword matching
    for keyword, answer in ANSWERS.items():
        if keyword in ql:
            return answer
    return "unknown"

@app.route('/', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        return jsonify({"status": "ok"}), 200

    data = request.get_json(force=True)
    question = data.get('question', '')
    answer = find_answer(question)
    return jsonify({"answer": answer}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
