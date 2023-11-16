# tests/test_persistance.py
from datetime import datetime, timedelta
import sys
import os

# Add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pingurl.models import WatchedUrl, PingData
from pingurl.persistance import add_watched_url, get_watched_url

# Sample WatchedUrl and PingData instances for testing
sample_watched_url = WatchedUrl(
    activate_at=datetime.now(),
    force=True,
    period_sec=60,
    url="http://example.com",
)

sample_ping_data = PingData(
    pinged_at=datetime.now(),
    response_time_sec=timedelta(seconds=1),
    status_code=200,
    url_id=0,
)

def test_add_watched_url():
    url_id = add_watched_url(sample_watched_url)
    assert url_id == 0

def test_get_watched_url():
    watched_url = get_watched_url(0)
    assert watched_url == sample_watched_url
