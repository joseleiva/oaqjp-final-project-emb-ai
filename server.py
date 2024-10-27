"""
Server for Emotion detection
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Main function for Emotion Analysis
    """
    text_to_analize = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analize)
    if output['dominant_emotion']:
        return f"""
For the given statement, the system response is 
    'anger': {output['anger']}, 
    'disgust': {output['disgust']}, 
    'fear': {output['fear']}, 
    'joy': {output['joy']} and 
    'sadness': {output['sadness']}. 
    The dominant emotion is {output['dominant_emotion']}.
"""
    return "Invalid text! Please try again!"
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
