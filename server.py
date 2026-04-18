"""
Flask web server for Emotion Detection application.
Provides routes for emotion analysis using Watson NLP.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the index page.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """
    Handle emotion detection requests.
    Accepts both GET and POST methods.
    Returns formatted emotion analysis or error message.
    """
    if request.method == "POST":
        data = request.get_json()
        text_to_analyze = data.get("text", "")
    else:
        text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"response": "Invalid text! Please try again!"})

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
