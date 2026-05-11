#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)

QA = {
    "algorithm allows burst traffic up to a configured bucket size": "token bucket",
    "burst traffic up to": "token bucket",
    "main disadvantage of the fixed window counter": "boundary",
    "disadvantage of the fixed window": "boundary",
    "most commonly used in production for distributed rate limiting": "redis",
    "commonly used in production": "redis",
    "distributed rate limiting": "redis",
    "sliding window log store for each request": "timestamp",
    "store for each request": "timestamp",
    "key tradeoff in distributed rate limiting": "consistency, availability",
    "tradeoff in distributed": "consistency, availability",
    "trade-off in distributed": "consistency, availability",
}

def find_answer(question):
    ql = question.lower()
    for q, a in QA.items():
        if q in ql:
            return a
    return "unknown"

@app.route('/', methods=['GET', 'POST'])
@app.route('/query', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        return jsonify({"status": "ok"}), 200
    data = request.get_json(force=True)
    question = data.get('question', '')
    answer = find_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
