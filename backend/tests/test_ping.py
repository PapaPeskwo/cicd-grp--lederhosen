# tests/test_ping.py
from datetime import datetime, timedelta
from unittest.mock import patch
import pytest
import sys
import os
# Add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pingurl.ping import send_ping, send_ping_persist_data
from pingurl.models import WatchedUrl, PingData
from pingurl import persistance


def test_send_ping_success():
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=False,
        period_sec=60,
        url="http://example.com",
        url_id=1,
    )

    with patch("pingurl.ping.requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.headers = {"Date": datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")}
        mock_response.status_code = 200
        mock_response.elapsed = timedelta(seconds=1)

        ping_data = send_ping(watched_url)

    assert isinstance(ping_data, PingData)
    assert ping_data.url_id == watched_url.url_id
    assert ping_data.status_code == 200
    assert ping_data.response_time_sec.total_seconds() == 1