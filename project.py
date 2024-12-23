import json
from datetime import datetime, timedelta

DATA_FILE = "habit_data.json"

def main():
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Log Progress")
        print("3. View Habit History")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            habit = input("Enter habit name: ")
            add_habit(habit)
        elif choice == "2":
            habit = input("Enter habit name: ")
            log_progress(habit)
        elif choice == "3":
            days = int(input("Enter number of days to view: "))
            view_history(days)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def add_habit(habit):
    data = load_data()
    if habit in data:
        print(f"Habit '{habit}' already exists.")
    else:
        data[habit] = []
        save_data(data)
        print(f"Habit '{habit}' added!")

def log_progress(habit):
    data = load_data()
    if habit not in data:
        print(f"Habit '{habit}' not found.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    if today in data[habit]:
        print(f"Progress for '{habit}' already logged today.")
    else:
        data[habit].append(today)
        save_data(data)
        print(f"Progress for '{habit}' logged!")

def view_history(days):
    data = load_data()
    start_date = datetime.now() - timedelta(days=days)
    print(f"History for the last {days} days:")

    for habit, dates in data.items():
        count = sum(datetime.strptime(d, "%Y-%m-%d") >= start_date for d in dates)
        print(f"{habit}: {count} days")

def calculate_streak(habit_name):
    data = load_data()
    if habit_name not in data or not data[habit_name]:
        return 0
    today = datetime.now().strftime("%Y-%m-%d")
    streak = 0
    current_date = today
    while current_date in data[habit_name]:
        streak += 1
        current_date = (datetime.strptime(current_date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    return streak

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()



