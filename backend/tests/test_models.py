import pytest
from datetime import datetime, timedelta
import sys
import os

# Add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pingurl.models import WatchedUrl, PingData


# Test WatchedUrl class
def test_watched_url_valid():
    activate_at = datetime(2023, 1, 1)
    force = True
    period_sec = 60
    url = "https://example.com"
    url_id = 1

    watched_url = WatchedUrl(activate_at, force, period_sec, url, url_id)

    assert watched_url.activate_at == activate_at
    assert watched_url.force == force
    assert watched_url.period_sec == period_sec
    assert watched_url.url == url
    assert watched_url.url_id == url_id


def test_watched_url_invalid_url():
    # Test that WatchedUrl raises ValueError for an invalid URL
    with pytest.raises(ValueError):
        WatchedUrl(datetime.now(), True, 60, "invalid_url")


# Test PingData class
def test_ping_data_ok():
    pinged_at = datetime(2023, 1, 1)
    response_time_sec = timedelta(seconds=1)
    status_code = 200
    url_id = 1

    ping_data = PingData(pinged_at, response_time_sec, status_code, url_id)

    assert ping_data.ok()


def test_ping_data_not_ok():
    ping_data = PingData(datetime.now(), timedelta(seconds=1), 404, 1)

    assert not ping_data.ok() 
