from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the root URL (/)
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask app
if __name__ == '__main__':
    app.run(port=9000)
