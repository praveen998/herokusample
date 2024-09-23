from flask import Flask,request,send_file
import time
from convert_to_sound import google_text_sound

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the root URL (/)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def hello_world():
    return 'Hello, Praveen!'



@app.route('/gettextospeech',methods=['POST'])
def gettexttospeech():
    text = request.data.decode('utf-8')  # Get the raw data and decode it

    if not text:
        return {'error': 'No text provided'}, 400
    print(text)
    google_text_sound(text)
    time.sleep(0.1)
    return send_file('testtospeech.wav', mimetype='audio/wav'),200



# Run the Flask app
if __name__ == '__main__':
    app.run(port=9000)
