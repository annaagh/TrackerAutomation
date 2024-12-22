import cv2
import csv

def draw_cross(frame, center, size=10, color=(0, 255, 0), thickness=2):
    """Draws a cross at the specified center coordinates."""
    x, y = center
    cv2.line(frame, (x - size, y), (x + size, y), color, thickness)
    cv2.line(frame, (x, y - size), (x, y + size), color, thickness)

def tracker(video_path, bbox_func=None, output_csv="tracker_output.csv", test_mode=False):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Read the first frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read video frame.")
        return

    # Get the initial bounding box
    if bbox_func:
        bbox = bbox_func()
    else:
        # Let the user select the region to track
        bbox = cv2.selectROI("Select Region", frame, fromCenter=False, showCrosshair=True)
        cv2.destroyWindow("Select Region")

    # Initialize the tracker
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)

    # Open a CSV file to save the output
    with open(output_csv, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the header
        csv_writer.writerow(["frame_index", "x", "y", "width", "height"])

        frame_index = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                print("End of video.")
                break

            # Update the tracker
            success, bbox = tracker.update(frame)

            if success:
                # Extract bounding box details
                x, y, w, h = map(int, bbox)

                # Save bounding box to CSV
                csv_writer.writerow([frame_index, x, y, w, h])

                if not test_mode:
                    print(f"Tracker Coords (Frame {frame_index}): ", (x, y, w, h))
                    # Draw a cross at the center of the bounding box
                    center = (x + w // 2, y + h // 2)
                    draw_cross(frame, center)

            if not test_mode:
                # Display the result
                cv2.imshow("Tracking", frame)

                # Exit on ESC key
                if cv2.waitKey(1) & 0xFF == 27:
                    break

            frame_index += 1

    # Cleanup
    cap.release()
    if not test_mode:
        cv2.destroyAllWindows()
    print(f"Tracking data saved to {output_csv}")

if __name__ == "__main__":
    def mock_bbox_func():
        """Mock bounding box for test mode."""
        return (642, 262, 95, 183)  # Replace with your test values

    video_path = "data/video_input_028sec.mp4"  # Replace with the path to your video file
    tracker(video_path, mock_bbox_func, test_mode=False)
    # tracker(video_path, bbox_func=mock_bbox_func, test_mode=True, output_csv="test_mode_output.csv")
