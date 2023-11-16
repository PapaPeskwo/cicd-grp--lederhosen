from datetime import datetime, timedelta, timezone
from unittest.mock import patch, Mock
import pytest
import sys
import os

# Add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pingurl.schedule import add, remove, jobs
from pingurl.watched_urls import WatchedUrl
from pingurl.ping import send_ping_persist_data

@pytest.fixture
def sample_watched_url():
    return WatchedUrl(
        activate_at=datetime.now(timezone.utc),
        force=False,
        period_sec=60,
        url="http://example.com",
        url_id=1,
    )

@patch("pingurl.schedule.apscheduler.add_job")
@patch("pingurl.schedule.send_ping_persist_data", side_effect=send_ping_persist_data)
def test_add(mock_send_ping, mock_add_job, sample_watched_url):
    # Set the current time to be before the activation time
    with patch(
        "pingurl.schedule.datetime",
        Mock(now=Mock(return_value=datetime.now(timezone.utc) - timedelta(days=1))),
    ):
        add(sample_watched_url)

    # Check that add_job was called with the correct arguments
    mock_add_job.assert_called_once_with(
        func=mock_send_ping,
        args=[sample_watched_url.url_id],
        trigger="interval",
        seconds=sample_watched_url.period_sec,
        start_date=sample_watched_url.activate_at,
    )

@patch("pingurl.schedule.apscheduler.remove_job")
def test_remove(mock_remove_job, sample_watched_url):
    # Assume there is a job with the given url_id
    job_id = "mocked_job_id"
    jobs[sample_watched_url.url_id] = job_id

    # Check that remove_job is called with the correct job_id
    remove(sample_watched_url.url_id)
    mock_remove_job.assert_called_once_with(job_id)
