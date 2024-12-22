import csv

def read_csv(file_path):
    """Reads a CSV file and returns the data as a list of dictionaries."""
    data = []
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append({
                "frame_index": int(row["frame_index"]),
                "x": int(row["x"]),
                "y": int(row["y"]),
                "width": int(row["width"]),
                "height": int(row["height"])
            })
    return data

def calculate_iou(box1, box2):
    """
    Calculates Intersection over Union (IoU) between two bounding boxes.
    Each box is a dictionary with keys: x, y, width, height.
    """
    x1_min = box1["x"]
    y1_min = box1["y"]
    x1_max = x1_min + box1["width"]
    y1_max = y1_min + box1["height"]

    x2_min = box2["x"]
    y2_min = box2["y"]
    x2_max = x2_min + box2["width"]
    y2_max = y2_min + box2["height"]

    # Calculate intersection
    inter_x_min = max(x1_min, x2_min)
    inter_y_min = max(y1_min, y2_min)
    inter_x_max = min(x1_max, x2_max)
    inter_y_max = min(y1_max, y2_max)

    if inter_x_min < inter_x_max and inter_y_min < inter_y_max:
        intersection = (inter_x_max - inter_x_min) * (inter_y_max - inter_y_min)
    else:
        intersection = 0

    # Calculate areas
    area1 = box1["width"] * box1["height"]
    area2 = box2["width"] * box2["height"]

    # Calculate union
    union = area1 + area2 - intersection

    # IoU
    return intersection / union if union > 0 else 0