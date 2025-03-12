#!/usr/bin/env python
"""
PROJECT89 AGENT ARSENAL - LAUNCH SCRIPT
This is the main entry point for the Project 89 Agent Arsenal.
It initializes the environment and launches the combined launcher.
"""
import os
import sys
import subprocess
import platform

def main():
    """Initialize the environment and launch the combined launcher."""
    # Get the current directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("===================================")
    print("PROJECT 89 AGENT ARSENAL LAUNCHER")
    print("===================================")
    print("Initializing environment...")
    
    # Initialize the environment
    if platform.system() == "Windows":
        # On Windows, run the BAT script
        try:
            subprocess.run(
                ["initialize_environment.bat"],
                shell=True,
                check=True
            )
        except subprocess.CalledProcessError:
            print("Warning: Failed to run initialize_environment.bat")
            print("Attempting to initialize environment directly...")
            ensure_directories()
    else:
        # On other platforms, use Python to create directories
        ensure_directories()
    
    print("Environment initialized.")
    print("Launching Project 89 Agent Arsenal...")
    
    # Launch the combined launcher
    if os.path.exists(os.path.join(script_dir, "combined_launcher.py")):
        # Use subprocess to run the launcher
        subprocess.run([sys.executable, "combined_launcher.py"])
    else:
        print("Error: Combined launcher not found!")
        print("Please ensure combined_launcher.py exists in the distribution package.")
        input("Press Enter to exit...")
        sys.exit(1)

def ensure_directories():
    """Ensure that all necessary directories exist."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create directories for Mind Mirror
    os.makedirs(os.path.join(script_dir, "MindMirror", "user_data"), exist_ok=True)
    os.makedirs(os.path.join(script_dir, "MindMirror", "user_data", "journal"), exist_ok=True)
    os.makedirs(os.path.join(script_dir, "MindMirror", "exports"), exist_ok=True)
    os.makedirs(os.path.join(script_dir, "MindMirror", "exports", "reality_glitcher"), exist_ok=True)
    
    # Create directories for Reality Glitcher
    os.makedirs(os.path.join(script_dir, "RealityGlitcher", "imports"), exist_ok=True)
    
    # Copy any existing exports to imports directory
    mm_exports = os.path.join(script_dir, "MindMirror", "exports", "reality_glitcher")
    rg_imports = os.path.join(script_dir, "RealityGlitcher", "imports")
    
    if os.path.exists(mm_exports):
        for filename in os.listdir(mm_exports):
            if filename.endswith(".json"):
                src = os.path.join(mm_exports, filename)
                dst = os.path.join(rg_imports, filename)
                if not os.path.exists(dst):
                    try:
                        import shutil
                        shutil.copy2(src, dst)
                        print(f"Copied: {filename}")
                    except Exception as e:
                        print(f"Failed to copy {filename}: {e}")
    
    # Create notification file for Reality Glitcher if Mind Mirror exported data
    import glob
    if glob.glob(os.path.join(mm_exports, "*.json")):
        import time
        with open(os.path.join(rg_imports, ".new_import"), "w") as f:
            f.write(time.strftime("%Y%m%d_%H%M%S"))
        print("Notification created for Reality Glitcher about available imports")

if __name__ == "__main__":
    main() 