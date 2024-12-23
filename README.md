# Habit Tracker
#### Video Demo:  https://youtu.be/k7P6Bw6olaU
#### Description:

The Habit Tracker is a Python-based project designed to help users build and maintain healthy habits through tracking and logging their daily activities. By providing a simple command-line interface, users can add habits, log progress, and review their history over a customizable time frame. It stores all user data in a single JSON file, ensuring progress is saved between sessions.

---

### Features:

1. **Add Habit**: Users can add new habits they wish to track, such as exercise, reading, or drinking water.
2. **Log Progress**: Daily progress can be recorded for each habit, allowing users to track their consistency.
3. **View History**: Users can review their progress over a specific number of days to identify trends, gaps, or patterns in their routine.
4. **Data Persistence**: All data is stored securely in a JSON file, ensuring that user habits and progress are not lost when the program is restarted.

---

### Files:

#### 1. `project.py`
This file contains the main implementation of the Habit Tracker. It includes:
- **Menu Navigation**: A command-line interface where users can select actions like adding habits, logging progress, or viewing history.
- **Core Functions**:
  - `add_habit()`: Adds a new habit to the tracking system. It prevents duplicate habits from being created.
  - `log_progress()`: Records the user's progress for a specific habit, ensuring each date is logged only once.
  - `view_history()`: Displays the user's progress over the last specified number of days in a clear and concise format.
- **Data Management**: Handles loading and saving data to a JSON file (`habit_data.json`), ensuring user data is persistent.

#### 2. `tests.py`
This file includes unit tests to ensure the functionality of the Habit Tracker:
- Tests for adding habits, logging progress, and viewing history.
- Utilizes pytest fixtures to set up and tear down temporary data files during tests, ensuring isolated and reliable results.
- Validates that duplicate habits cannot be added and that duplicate logs for the same date are prevented.

---

### Design Choices:

1. **Simplified Data Storage**:
   - All data is stored in a single JSON file (`habit_data.json`). This design was chosen to keep the project simple and easy to maintain while providing persistence and reliability.

2. **Command-Line Interface (CLI)**:
   - A CLI was chosen over a graphical interface to focus on core functionality. The program remains lightweight and easily portable while still being user-friendly.

3. **Fixtures in Testing**:
   - Pytest fixtures were used to streamline test setup and cleanup, avoiding repetitive code and ensuring each test has a clean slate.

4. **Input Validation**:
   - Minimal input validation was implemented to ensure ease of use while avoiding overly complex checks that could hinder user experience.

5. **Future-Proofing**:
   - While starting simple, the design allows for additional features like streak tracking, notifications, or analytics to be added without significant rework.

---

### Challenges and Future Improvements:

#### Challenges:
- Balancing simplicity with functionality: Deciding which features to include while keeping the project beginner-friendly and avoiding overengineering.
- Ensuring robust error handling: Safeguarding against incorrect inputs or data corruption, particularly in the JSON file.

#### Future Improvements:
- **Habit Streaks**: Implement a feature to calculate and display streaks for continuous progress, helping users stay motivated.
- **Graphical Interface**: Develop a user-friendly GUI to make the tracker accessible to a broader audience.
- **Reminders**: Add notification or reminder functionality to prompt users to log progress regularly.
- **Analytics and Insights**: Provide detailed statistics on habit performance, such as weekly trends or success rates.
- **Cloud Backup**: Enable cloud-based data storage for accessing habits and progress across devices.

---

### How to Run:

1. Clone the repository or download the `project.py` and `tests.py` files.
2. Ensure Python (3.6 or higher) and `pytest` are installed.
3. Run `project.py` to start the Habit Tracker:
   ```bash
   python project.py
