import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def verify_dashboard():
    """Verify the dashboard data and user stats"""
    # Path to user data
    user_data_file = os.path.join('user_data', 'user_data.json')
    
    # Check if file exists
    if os.path.exists(user_data_file):
        # Load existing data
        try:
            with open(user_data_file, 'r') as f:
                user_data = json.load(f)
            
            # Get relevant stats
            username = user_data.get('username', 'Unknown')
            session_count = user_data.get('session_count', 0)
            meditation_minutes = user_data.get('meditation_minutes', 0)
            meditation_stats = user_data.get('meditation_stats', {})
            
            streak = meditation_stats.get('practice_streak', 0)
            last_date = meditation_stats.get('last_meditation_date', 'None')
            total_sessions = meditation_stats.get('total_sessions', 0)
            
            # Print verification info
            print("\n✨ DASHBOARD VERIFICATION ✨")
            print("===========================")
            print(f"Username: {username}")
            print(f"Session Count: {session_count}")
            print(f"Meditation Minutes: {meditation_minutes}")
            print(f"Practice Streak: {streak}")
            print(f"Last Meditation Date: {last_date}")
            print(f"Total Sessions: {total_sessions}")
            
            # Compare with today's date
            today = datetime.now().strftime("%Y-%m-%d")
            if last_date == today:
                print("\n✅ Last meditation date is today - Dashboard should show current streak")
            else:
                print(f"\n❓ Last meditation date ({last_date}) is not today ({today})")
                print("   Dashboard may not show the most current streak")
            
            # Check if user data and meditation stats are consistent
            if session_count == total_sessions:
                print("✅ Session count matches total sessions - Data is consistent")
            else:
                print(f"❌ Data inconsistency: session_count ({session_count}) ≠ total_sessions ({total_sessions})")
            
            # Create summary
            print("\n📊 DASHBOARD SUMMARY 📊")
            print("=====================")
            print("The dashboard should display:")
            print(f"- Welcome message for {username}")
            print(f"- Session count: {session_count}")
            print(f"- Meditation minutes: {meditation_minutes}")
            if streak > 0:
                print(f"- Meditation streak: {streak} 🔥")
            else:
                print("- No streak card (streak is 0)")
            
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("User data file not found")

if __name__ == "__main__":
    verify_dashboard() 