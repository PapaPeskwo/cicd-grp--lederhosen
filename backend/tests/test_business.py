from datetime import datetime, timedelta
import pytest
from unittest.mock import Mock
import sys
import os
# Add the root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pingurl.models import WatchedUrl
from pingurl import business


@pytest.fixture
def mock_send_ping(mocker):
    return mocker.patch('pingurl.business.send_ping', return_value=Mock(ok=lambda: True))


def test_add_watched_url_success(mocker, mock_send_ping):
    # Mock the dependencies
    mocker.patch('pingurl.business.persistance.add_watched_url', return_value=123)
    mocker.patch('pingurl.business.persistance.add_ping_data')
    mocker.patch('pingurl.business.schedule.add')

    # Create a WatchedUrl instance
    watched_url = WatchedUrl(
        activate_at=datetime.now(),
        force=True,
        period_sec=60,
        url='http://example.com',
    )

    # Call the function
    result = business.add_watched_url(watched_url)

    # Assertions
    assert result == 123
    mock_send_ping.assert_called_once_with(watched_url)
    business.persistance.add_watched_url.assert_called_once_with(watched_url)
    business.persistance.add_ping_data.assert_called_once()
    business.schedule.add.assert_called_once_with(watched_url)


def test_delete_watched_url(mocker):
    # Mock the dependencies
    mocker.patch('pingurl.business.schedule.remove')
    mocker.patch('pingurl.business.persistance.delete_watched_url')

    # Call the function
    business.delete_watched_url(123)

    # Assertions
    business.schedule.remove.assert_called_once_with(123)
    business.persistance.delete_watched_url.assert_called_once_with(123)
