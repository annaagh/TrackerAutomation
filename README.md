# TrackerAutomation

**TrackerAutomation** is a project that automates object tracking using OpenCV. It includes tools and tests for evaluating the accuracy of object trackers.


## Installation

Follow the steps below to set up the environment and install dependencies:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/annaagh/TrackerAutomation.git
   cd TrackerAutomation

2. Install dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Run Tests

   Run All Tests: To run all tests in the tests directory
   ```
   pytest
   ```
   Run Specific Test File: To run tests in a specific test file, provide the path to the file:
   ```
   pytest tests/smoke/test_tracker.py
   ```
   
   Run Tests with a Specific Mark or Test Case: To run tests that are marked with a specific label, use the -m option:
   ```
   pytest -m "smoke"
   ```
