from app import app, PRICES

client = app.test_client()


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_price_known_item():
    r = client.get("/price/laptop")
    assert r.get_json()["price"] == PRICES["laptop"]


def test_price_unknown_item():
    assert client.get("/price/unicorn").status_code == 404


requirements.txt
flask==3.0.3

requirements-dev.txt
-r requirements.txt
pytest==8.3.3
