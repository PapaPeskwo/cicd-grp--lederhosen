import pytest
import sys
import os

# Add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pingurl import app
from unittest.mock import patch

MIN_PERIOD = 10


@pytest.fixture
def watched_url_client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_watched_url_success(watched_url_client):
    data = {
        "activateAt": "2023-11-15T13:00:00Z",
        "force": False,
        "periodSec": 60,
        "url": "http://example.com",
    }

    with patch("pingurl.watched_urls.business.add_watched_url", return_value=1):
        response = watched_url_client.post("/watched-urls", json=data)

    assert response.status_code == 201
    assert response.json == {"message": "Watched URL added", "urlId": 1}


def test_add_watched_url_missing_parameter(watched_url_client):
    data = {
        "activateAt": "2023-11-15T13:00:00Z",
        "force": False,
        "url": "http://example.com",
    }

    response = watched_url_client.post("/watched-urls", json=data)

    assert response.status_code == 400
    assert response.json == {
        "error": "Bad request",
        "message": "Missing parameter 'periodSec'",
    }


def test_add_watched_url_invalid_url(watched_url_client):
    data = {
        "activateAt": "2023-11-15T13:00:00Z",
        "force": False,
        "periodSec": 60,
        "url": "invalid_url",
    }

    response = watched_url_client.post("/watched-urls", json=data)

    assert response.status_code == 400
    assert response.json == {
        "error": "Bad request",
        "message": "The 'url' parameter must be valid URL string.",
    }
