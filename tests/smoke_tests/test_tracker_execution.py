"""
Smoke test to verify tracker work without exception. with a mock video.
Use mock video with a moving square.
"""

import pytest
from main import tracker
from tests.fixtures.tracker_fixtures import create_mock_video

def mock_bbox_func():
    return (20, 20, 30, 30)

def test_tracker_execution(create_mock_video):
    try:
        tracker(create_mock_video, mock_bbox_func)
        assert True
    except Exception as e:
        pytest.fail(f"Tracker initialization failed: {e}")
