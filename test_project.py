import pytest
import os
import json
import project
from datetime import datetime


@pytest.fixture
def temp_data_file():
    temp_file = "temp_habit_data.json"
    if os.path.exists(temp_file):
        os.remove(temp_file)
    project.DATA_FILE = temp_file
    yield temp_file
    if os.path.exists(temp_file):
        os.remove(temp_file)


def test_add_habit(temp_data_file):
    project.save_data({})
    project.add_habit("Test Habit")
    data = project.load_data()
    assert "Test Habit" in data
    project.add_habit("Test Habit")
    data = project.load_data()
    assert len(data) == 1


def test_log_progress(temp_data_file):
    project.save_data({"Exercise": []})
    project.log_progress("Exercise")

    data = project.load_data()
    today = datetime.now().strftime("%Y-%m-%d")
    assert today in data["Exercise"]
    project.log_progress("Exercise")

    data = project.load_data()
    assert len(data["Exercise"]) == 1



def test_view_history(capsys, temp_data_file):
    today = "2024-11-30"
    project.save_data({"Exercise": [today]})
    project.view_history(days=7)
    captured = capsys.readouterr()
    assert "Exercise: 1 days" in captured.out


def test_streak_calculation(temp_data_file):
    today = "2024-11-30"
    yesterday = "2024-11-29"
    project.save_data({"Exercise": [today, yesterday]})
    streak = project.calculate_streak("Exercise")
    assert streak == 2




