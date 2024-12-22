import cv2
import pytest
import os
import numpy as np


@pytest.fixture()
def create_mock_video(tmp_path, width=640, height=480, num_frames=50, square_size=50, speed=5):
    """
    Creates a mock video with a moving square.

    Parameters:
        tmp_path (str): Path to save the video.
        width (int): Width of the video frames.
        height (int): Height of the video frames.
        num_frames (int): Number of frames in the video.
        square_size (int): Size of the square (pixels).
        speed (int): Pixels the square moves per frame.
    """
    video_path = os.path.join(tmp_path,"test_video.avi")
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(video_path, fourcc, 30.0, (width, height))

    center_x = width // 2
    center_y = height // 2
    radius = min(width, height) // 4  # Define a movement radius

    for frame_idx in range(num_frames):
        frame = np.zeros((height, width, 3), dtype=np.uint8)

        # Calculate the square's position in a circular motion
        angle = (frame_idx * speed) % 360  # Angle in degrees
        radian = np.deg2rad(angle)

        x_offset = int(radius * np.cos(radian))
        y_offset = int(radius * np.sin(radian))

        x_start = center_x + x_offset - square_size // 2
        y_start = center_y + y_offset - square_size // 2
        x_end = x_start + square_size
        y_end = y_start + square_size

        # Draw the moving square
        cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (255, 255, 255), -1)

        out.write(frame)

    out.release()
    # print(f"Mock video created at {video_path}")
    return str(video_path)