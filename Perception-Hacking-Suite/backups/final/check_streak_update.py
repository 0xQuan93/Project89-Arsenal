import json
import os
from datetime import datetime

def check_streak_update():
    # Path to user data
    user_data_file = os.path.join('user_data', 'user_data.json')

    # Check if file exists
    if os.path.exists(user_data_file):
        # Load existing data
        try:
            with open(user_data_file, 'r') as f:
                user_data = json.load(f)
            
            # Check current streak
            meditation_stats = user_data.get('meditation_stats', {})
            current_streak = meditation_stats.get('practice_streak', 0)
            last_date = meditation_stats.get('last_meditation_date')
            
            print("\n✨ STREAK TEST RESULTS ✨")
            print("========================")
            print(f"Current streak: {current_streak}")
            print(f"Last meditation date: {last_date}")
            today = datetime.now().strftime("%Y-%m-%d")
            
            if last_date == today and current_streak > 0:
                print("✅ SUCCESS: Streak has been updated! The streak function is working correctly.")
                print(f"Streak incremented to {current_streak} and last meditation date updated to today.")
            else:
                print("❌ FAILURE: Streak may not be updating correctly.")
                if last_date != today:
                    print(f"Last meditation date ({last_date}) was not updated to today ({today}).")
                if current_streak == 0:
                    print("Streak is still at 0.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("User data file not found")

if __name__ == "__main__":
    check_streak_update() 