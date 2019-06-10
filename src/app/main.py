from flask import Flask, jsonify, request

from app.invalid_usage import InvalidUsage
from app.validation import validate_greeting
from mypkg.greetings import say_hello_to

app = Flask(__name__)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/")
def index() -> str:
    return jsonify({"message": "It Works"})


@app.route("/hello", methods=['POST'])
def hello() -> str:
    errors = validate_greeting(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)
    greetee = request.json.get("greetee", None)
    response = {"message": say_hello_to(greetee)}
    return jsonify(response)


# These two lines are used only while developing.
# In production this code will be run as a module.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

