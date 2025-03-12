#!/usr/bin/env python
"""
PROJECT89 Mind Mirror Launcher
This script launches the Mind Mirror application.
"""
import os
import sys
import argparse

def main():
    """Main entry point for the application."""
    print("Starting PROJECT89 Mind Mirror...")
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="PROJECT89 Mind Mirror - Consciousness Exploration Tool")
    parser.add_argument("--performance-mode", action="store_true", help="Run in performance mode (reduced visual effects)")
    parser.add_argument("--theme", choices=["dark", "light", "cyberpunk", "quantum"], default="dark", help="Set the initial theme")
    parser.add_argument("--disable-sound", action="store_true", help="Disable sound effects")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    
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
        args.disable_sound = True
    except Exception as e:
        print(f"Warning: Issue initializing Pygame: {e}")
        print("The application will run, but sound features may not work properly.")
        args.disable_sound = True
    
    # Import and run the application
    try:
        # Try to use the new enhanced version
        from enchanted_mindmirror_new import EnchantedMindMirror
        
        print("Using enhanced MindMirror implementation...")
        
        # Create configuration dictionary
        config = {
            "performance_mode": args.performance_mode,
            "initial_theme": args.theme,
            "disable_sound": args.disable_sound,
            "debug_mode": args.debug
        }
        
        # Initialize and run the application
        import tkinter as tk
        root = tk.Tk()
        app = EnchantedMindMirror(root)
        root.mainloop()
    except ImportError:
        print("Error: Could not import the Mind Mirror application.")
        print("Attempting to use fallback implementation...")
        
        try:
            # Try the older fixed version
            from enchanted_mindmirror_fixed import EnchantedMindMirror
            app = EnchantedMindMirror()
            app.master.mainloop()
        except ImportError:
            try:
                # Try the cyberpunk version as a last resort
                from cyberpunk_mindmirror import CyberpunkMindMirror
                app = CyberpunkMindMirror()
                app.master.mainloop()
            except ImportError:
                print("Error: Could not import any Mind Mirror implementation.")
                print("Make sure 'enchanted_mindmirror_new.py', 'enchanted_mindmirror_fixed.py', or 'cyberpunk_mindmirror.py' is in the same directory.")
                sys.exit(1)
    except Exception as e:
        print(f"Error starting Mind Mirror: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 