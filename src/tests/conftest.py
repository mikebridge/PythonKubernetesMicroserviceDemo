import pytest
from app import main


# http://flask.pocoo.org/docs/1.0/testing/
@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    client = main.app.test_client()
    yield client


@pytest.fixture()
def create_valid_greeting_request():
    """
    Helper function for creating a correctly-structured
    json request
    """
    def _create_valid_greeting_request(greetee="fixture"):
        return {
            "greetee": greetee
        }
    return _create_valid_greeting_request
