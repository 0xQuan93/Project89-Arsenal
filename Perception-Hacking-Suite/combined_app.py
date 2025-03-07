#!/usr/bin/env python
"""
PROJECT89 Perception-Hacking Suite Launcher
This script provides a unified interface to launch both Mind Mirror and Reality Glitcher.
"""
import os
import sys
import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import time

class CombinedLauncher:
    """Combined launcher for Mind Mirror and Reality Glitcher applications."""
    
    def __init__(self, root):
        """Initialize the launcher interface."""
        self.root = root
        root.title("PROJECT89 Perception-Hacking Suite")
        root.geometry("800x600")
        root.minsize(800, 600)
        
        # Set the working directory to the directory of this script
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(self.script_dir)
        
        # Configure dark cyberpunk style
        self.configure_style()
        
        # Create main frame
        main_frame = ttk.Frame(root, style="TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        header_frame = ttk.Frame(main_frame, style="TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(
            header_frame, 
            text="PROJECT89 PERCEPTION-HACKING SUITE", 
            font=("Courier New", 24, "bold"),
            foreground="#00FFFF",
            background="#121212"
        )
        title_label.pack(pady=10)
        
        subtitle_label = ttk.Label(
            header_frame, 
            text="Reality manipulation toolkit for awakened agents", 
            font=("Courier New", 12),
            foreground="#7F00FF",
            background="#121212"
        )
        subtitle_label.pack(pady=5)
        
        # Create app buttons frame
        buttons_frame = ttk.Frame(main_frame, style="TFrame")
        buttons_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Mind Mirror button
        mind_mirror_frame = ttk.Frame(buttons_frame, style="Card.TFrame")
        mind_mirror_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=50)
        
        mind_mirror_title = ttk.Label(
            mind_mirror_frame, 
            text="MIND MIRROR", 
            font=("Courier New", 18, "bold"),
            foreground="#00FFFF",
            background="#1A1A1A"
        )
        mind_mirror_title.pack(pady=(20, 10))
        
        mind_mirror_desc = ttk.Label(
            mind_mirror_frame, 
            text="Neural pattern visualization and consciousness exploration tool",
            font=("Courier New", 12),
            foreground="#FFFFFF",
            background="#1A1A1A",
            wraplength=700
        )
        mind_mirror_desc.pack(pady=10)
        
        mind_mirror_button = ttk.Button(
            mind_mirror_frame, 
            text="LAUNCH MIND MIRROR",
            style="Launch.TButton",
            command=self.launch_mind_mirror
        )
        mind_mirror_button.pack(pady=20)
        
        # Reality Glitcher button
        reality_glitcher_frame = ttk.Frame(buttons_frame, style="Card.TFrame")
        reality_glitcher_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=50)
        
        reality_glitcher_title = ttk.Label(
            reality_glitcher_frame, 
            text="REALITY GLITCHER", 
            font=("Courier New", 18, "bold"),
            foreground="#7F00FF",
            background="#1A1A1A"
        )
        reality_glitcher_title.pack(pady=(20, 10))
        
        reality_glitcher_desc = ttk.Label(
            reality_glitcher_frame, 
            text="Perception manipulation interface for altering reality stability",
            font=("Courier New", 12),
            foreground="#FFFFFF",
            background="#1A1A1A",
            wraplength=700
        )
        reality_glitcher_desc.pack(pady=10)
        
        reality_glitcher_button = ttk.Button(
            reality_glitcher_frame, 
            text="LAUNCH REALITY GLITCHER",
            style="Launch.TButton",
            command=self.launch_reality_glitcher
        )
        reality_glitcher_button.pack(pady=20)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready. Choose an application to launch.")
        status_bar = ttk.Label(
            main_frame, 
            textvariable=self.status_var,
            font=("Courier New", 10),
            foreground="#AAAAAA",
            background="#121212"
        )
        status_bar.pack(fill=tk.X, pady=(20, 0), anchor=tk.S)
        
        # Create footer
        footer_frame = ttk.Frame(main_frame, style="TFrame")
        footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        footer_text = ttk.Label(
            footer_frame, 
            text="PROJECT89 - For the liberation of consciousness",
            font=("Courier New", 10),
            foreground="#555555",
            background="#121212"
        )
        footer_text.pack(side=tk.RIGHT)
    
    def configure_style(self):
        """Configure the cyberpunk style for the application."""
        style = ttk.Style()
        
        # Configure colors
        bg_color = "#121212"
        card_bg = "#1A1A1A"
        accent_color = "#00FFFF"
        secondary_accent = "#7F00FF"
        
        # Configure the root window
        self.root.configure(bg=bg_color)
        
        # Configure styles
        style.configure("TFrame", background=bg_color)
        style.configure("Card.TFrame", background=card_bg, relief=tk.RAISED)
        
        # Configure button styles
        style.configure(
            "Launch.TButton",
            font=("Courier New", 12, "bold"),
            background="#00AAAA",
            foreground="#FFFFFF",
            padding=10
        )
        
        # Try to set the button hover effect (may not work on all platforms)
        try:
            style.map(
                "Launch.TButton",
                background=[("active", "#00CCCC")],
                foreground=[("active", "#FFFFFF")]
            )
        except Exception:
            # If the hover effect fails, just continue
            pass
    
    def launch_mind_mirror(self):
        """Launch the Mind Mirror application."""
        self.status_var.set("Launching Mind Mirror...")
        self.root.update()
        
        # Launch in a separate thread to keep the UI responsive
        threading.Thread(target=self._run_mind_mirror, daemon=True).start()
    
    def _run_mind_mirror(self):
        """Run the Mind Mirror application in a separate thread."""
        try:
            mind_mirror_dir = os.path.join(self.script_dir, "MindMirror")
            mind_mirror_script = os.path.join(mind_mirror_dir, "main.py")
            
            if not os.path.exists(mind_mirror_script):
                self.status_var.set("Error: Mind Mirror main.py not found!")
                return
            
            os.chdir(mind_mirror_dir)
            result = subprocess.run([sys.executable, mind_mirror_script], 
                                  stdout=subprocess.PIPE, 
                                  stderr=subprocess.PIPE,
                                  text=True)
            
            if result.returncode != 0:
                self.status_var.set(f"Mind Mirror exited with error: {result.returncode}")
                print("STDOUT:", result.stdout)
                print("STDERR:", result.stderr)
            else:
                self.status_var.set("Mind Mirror closed successfully.")
        except Exception as e:
            self.status_var.set(f"Error launching Mind Mirror: {e}")
            print(f"Error launching Mind Mirror: {e}")
        finally:
            # Return to the original directory
            os.chdir(self.script_dir)
    
    def launch_reality_glitcher(self):
        """Launch the Reality Glitcher application."""
        self.status_var.set("Launching Reality Glitcher...")
        self.root.update()
        
        # Launch in a separate thread to keep the UI responsive
        threading.Thread(target=self._run_reality_glitcher, daemon=True).start()
    
    def _run_reality_glitcher(self):
        """Run the Reality Glitcher application in a separate thread."""
        try:
            reality_glitcher_dir = os.path.join(self.script_dir, "RealityGlitcher")
            reality_glitcher_script = os.path.join(reality_glitcher_dir, "main.py")
            
            if not os.path.exists(reality_glitcher_script):
                self.status_var.set("Error: Reality Glitcher main.py not found!")
                return
            
            os.chdir(reality_glitcher_dir)
            result = subprocess.run([sys.executable, reality_glitcher_script], 
                                  stdout=subprocess.PIPE, 
                                  stderr=subprocess.PIPE,
                                  text=True)
            
            if result.returncode != 0:
                self.status_var.set(f"Reality Glitcher exited with error: {result.returncode}")
                print("STDOUT:", result.stdout)
                print("STDERR:", result.stderr)
            else:
                self.status_var.set("Reality Glitcher closed successfully.")
        except Exception as e:
            self.status_var.set(f"Error launching Reality Glitcher: {e}")
            print(f"Error launching Reality Glitcher: {e}")
        finally:
            # Return to the original directory
            os.chdir(self.script_dir)

def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = CombinedLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main() 