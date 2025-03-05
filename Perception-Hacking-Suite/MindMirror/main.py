#!/usr/bin/env python
"""
PROJECT89 Mind Mirror Launcher
This script launches the Mind Mirror application.
"""
import os
import sys

def main():
    """Main entry point for the application."""
    print("Starting PROJECT89 Mind Mirror...")
    
    # Change working directory to the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check for pygame and other dependencies
    try:
        import pygame
        print("Pygame initialized successfully.")
    except ImportError:
        print("Warning: Pygame not found or could not be imported.")
        print("The application will run, but sound features will be disabled.")
    except Exception as e:
        print(f"Warning: Issue initializing Pygame: {e}")
        print("The application will run, but sound features may not work properly.")
    
    # Import and run the application
    try:
        from enchanted_mindmirror_fixed import EnchantedMindMirror
        app = EnchantedMindMirror()
        app.master.mainloop()
    except ImportError:
        print("Error: Could not import the Mind Mirror application.")
        print("Make sure 'enchanted_mindmirror_fixed.py' is in the same directory.")
        sys.exit(1)
    except Exception as e:
        print(f"Error starting Mind Mirror: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 