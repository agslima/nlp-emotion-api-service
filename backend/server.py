"""
server.py

Flask web server for EmotionDetection application.
Provides endpoints to analyze text for emotions using Watson NLP API.
"""

import os
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(
    __name__,
    template_folder=os.path.join("..", "frontend"),
    static_folder=os.path.join("..", "frontend", "static"),
)


@app.route("/")
def home():
    """
    Render the home page (index.html).

    Returns:
        str: Rendered HTML page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_endpoint():
    """
    Analyze text for emotions using the EmotionDetection package.

    For POST requests, expects JSON payload with 'text'.
    For GET requests, expects query parameter 'textToAnalyze'.

    Returns:
        flask.Response: JSON response containing emotion scores or error message.
    """
    if request.method == "POST":
        data = request.get_json()
        text_to_analyze = data.get("text", "")
    else:  # GET request
        text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

    return response_text


if __name__ == "__main__":
    # Run the Flask server on localhost:5000
    app.run(host="0.0.0.0", port=5000)
