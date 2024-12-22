# TrackerAutomation
Opencv object tracker automation

Install dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Run Tests

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
