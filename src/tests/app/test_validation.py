import pytest
from flask import Flask, request

from app.validation import validate_greeting

app = Flask(__name__)


@pytest.mark.parametrize("params", [
    {"greetee": 1},
    {"greetee": ["array"]}
])
def test_invalid_types_are_rejected(params, create_valid_greeting_request):
    json_input = create_valid_greeting_request(**params)
    with app.test_request_context('/', json=json_input):
        errors = validate_greeting(request)
        assert errors is not None


@pytest.mark.parametrize("required_parm_name", ["greetee"])
def test_missing_required_params_is_rejected(required_parm_name, create_valid_greeting_request):
    json_input = create_valid_greeting_request()
    del json_input[required_parm_name]
    with app.test_request_context('/', json=json_input):
        errors = validate_greeting(request)
        assert errors is not None


def test_valid_greetee_is_accepted(create_valid_greeting_request):
    json_input = create_valid_greeting_request(greetee="Tester")
    with app.test_request_context('/', json=json_input):
        errors = validate_greeting(request)
        assert errors is None
