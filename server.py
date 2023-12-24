from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('__name__')

@app.route('/emotionDetector')
def emot_detection():
    text_to_analyze = request.args.get('text_to_analyze')
    response = emotion_detector(text_to_analyze)
    if response != None:
        a = response['anger']
        d = response['disgust']
        f = response['fear']
        j = response['joy']
        s = response['sadness']
        de = response['dominant_emotion']
        return f"For the given statement, the system response is 'anger': {a}, 'disgust': {d}, 'fear': {f}, 'joy': {j} and 'sadness': {s}. The dominant emotion is {de}."
    else:
        return "Invalid text! Please try again!."

@app.route('/')
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)