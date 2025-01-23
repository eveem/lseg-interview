# from flask import Flask, render_template
# from aws_lambda_powertools.event_handler import api_gateway
# from aws_lambda_powertools.logging import Logger

# app = Flask(__name__)

# dogs = [
#     { "name": "Lunar", "image": "lunar.jpg" },
#     { "name": "Solar", "image": "solar.jpg" },
#     { "name": "Stellar", "image": "stellar.jpg" },
# ]

# current_dog_index = 0
# logger = Logger()

# @app.route("/")
# def home():
#     global current_dog_index
#     dog = dogs[current_dog_index]
#     current_dog_index = (current_dog_index + 1) % len(dogs)
#     return render_template("index.html", dog_name=dog["name"], dog_image=dog["image"])

# def lambda_handler(event, context):
#     handler = api_gateway.ApiGatewayHandler()
#     logger.info(f"Received event: {event}")
#     return handler.handle(event, context)

from flask import Flask, jsonify
from aws_lambda_wsgi import response

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

# AWS Lambda function handler
def lambda_handler(event, context):
    return response(app, event, context)
