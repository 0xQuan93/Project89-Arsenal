# REDIRECT TO FIXED VERSION
# This file is kept for reference but the fixed version should be used instead

import os
import sys

print("Redirecting to fixed version of Mind Mirror...")
print("Please use 'enchanted_mindmirror_fixed.py' directly in the future.")
print("-" * 60)

# Execute the fixed version
if __name__ == "__main__":
    try:
        # Change working directory to the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        
        # Run the fixed version
        os.system(f"{sys.executable} enchanted_mindmirror_fixed.py")
    except Exception as e:
        print(f"Error redirecting: {e}")
        print("Please run 'enchanted_mindmirror_fixed.py' directly.")