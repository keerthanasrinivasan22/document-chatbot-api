from flask import Flask, request, jsonify
from retrieve_section import retrieve_relevant_section
from answer_question import answer_question

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get("question", "")

    document = retrieve_relevant_section(question)

    if document:
        answer = answer_question(question, document)
    else:
        answer = "I'm a UNT-specific bot. I can only help with UNT-related topics."

    return jsonify({"answer": answer})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  # This is required for Render
