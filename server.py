""" Executing this function initiates the application of emotional 
detection to be executed over a Flask channel and deployed on
localhost:5000  
"""

# Importing libraries and functions 
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app:
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """This Function recieves text from the HTML interface and runs
       emotion detection over it using emotion_detector() function.
       The output returned shows the different emotions - and their 
       scores - for the provided text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to emotion_detector function and store response
    response = emotion_detector(text_to_analyze)

    # Extract the different emotions from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if user has submitted blank input, or another invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # return a formatted string with the emotions and scores using f-string
    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main 
       application page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    """This function executes the flask app and deploys it on 
       localhost:5000
    """
    app.run(host="0.0.0.0", port=5000, debug=True)