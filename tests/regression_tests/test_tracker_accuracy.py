"""
Tests the tracker's accuracy by comparing tracker output with ground truth.
Passes if IoU for all frames meets the threshold.
"""
import pytest
import os
from main import tracker
from tests.test_utils import read_csv, calculate_iou

# Testing data
test_video_path = "tests/data/video_input_028sec.mp4"
tracker_tmp_output_path = "tests/data/tracker_tmp_output.csv"
right_output_path = "tests/data/test_accuracy_right_output.csv"

def mock_bbox_func():
    return (642, 262, 95, 183)

@pytest.mark.parametrize("tracker_output_csv, right_csv, iou_threshold", [
    (tracker_tmp_output_path, right_output_path, 0.5),  # Example file paths
])
def test_tracker_accuracy(tracker_output_csv, right_csv, iou_threshold):
    try:
        tracker(test_video_path, mock_bbox_func, test_mode=True, output_csv=tracker_output_csv)
        tracker_data = read_csv(tracker_output_csv)
        right_data = read_csv(right_csv)

        assert len(tracker_data) == len(right_data),\
            "Mismatch in number of frames between tracker output and ground truth."

        total_frames = len(tracker_data)
        passed_frames = 0

        for tracker_box, right_box in zip(tracker_data, right_data):
            iou = calculate_iou(tracker_box, right_box)
            if iou >= iou_threshold:
                passed_frames += 1

        accuracy = passed_frames / total_frames
        print(f"Accuracy: {accuracy * 100:.2f}%")

        assert accuracy == 1, f"Tracker accuracy ({accuracy:.2f})."
    finally:
        if os.path.exists(tracker_output_csv):
            os.remove(tracker_output_csv)
