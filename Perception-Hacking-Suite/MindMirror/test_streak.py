import json
import os
from datetime import datetime, timedelta

def test_streak():
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
            
            print(f'Current streak: {current_streak}')
            print(f'Last meditation date: {last_date}')
            
            # Simulate a meditation from yesterday to test streak calculation
            if meditation_stats:
                yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
                meditation_stats['last_meditation_date'] = yesterday
                user_data['meditation_stats'] = meditation_stats
                
                # Save modified data
                with open(user_data_file, 'w') as f:
                    json.dump(user_data, f, indent=4)
                
                print(f'Updated last meditation date to: {yesterday} for streak testing')
                print('Now run meditation to check if streak increments')
            else:
                print('No meditation stats found')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print('User data file not found')

if __name__ == "__main__":
    test_streak() 