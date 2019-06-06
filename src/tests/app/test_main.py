def test_info(client):
    response = client.get('/')
    result = response.get_json()
    assert result is not None
    assert "message" in result
    assert result["message"] == "It Works"


# http://flask.pocoo.org/docs/1.0/testing/#testing-json-apis
def test_hello_greets_greetee(client):
    request_payload = {"greetee": "world"}
    response = client.post("/hello", json=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert "message" in result
    assert result['message'] == "hello world"


def test_hello_requires_greetee(client):
    request_payload = {}
    response = client.post("/hello", json=request_payload)
    result = response.get_json()

    assert response.status_code == 400
    assert result is not None
    assert "message" in result
    assert "is a required property" in result['message'][0]
