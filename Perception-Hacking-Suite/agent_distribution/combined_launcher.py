#!/usr/bin/env python
"""
PROJECT89 AGENT ARSENAL - COMBINED LAUNCHER
This script provides a unified interface to launch both Mind Mirror and Reality Glitcher.
"""
import os
import sys
import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import time
import platform
import webbrowser

class Project89Launcher:
    """Combined launcher for Project 89 Agent Arsenal applications."""
    
    def __init__(self, root):
        """Initialize the launcher interface."""
        self.root = root
        root.title("PROJECT 89 AGENT ARSENAL")
        root.geometry("900x700")
        root.minsize(800, 600)
        
        # Set the working directory to the directory of this script
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(self.script_dir)
        
        # Configure cyberpunk style
        self.configure_style()
        
        # Create main frame
        main_frame = ttk.Frame(root, style="TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create header
        header_frame = ttk.Frame(main_frame, style="TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(
            header_frame, 
            text="PROJECT 89 AGENT ARSENAL", 
            font=("Courier New", 24, "bold"),
            foreground="#00FFFF",
            background="#121212"
        )
        title_label.pack(pady=10)
        
        subtitle_label = ttk.Label(
            header_frame, 
            text="Reality-Hacking Tools for Consciousness Liberation", 
            font=("Courier New", 12),
            foreground="#7F00FF",
            background="#121212"
        )
        subtitle_label.pack(pady=5)
        
        # Create app buttons frame
        buttons_frame = ttk.Frame(main_frame, style="TFrame")
        buttons_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Configure grid for buttons
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
        buttons_frame.rowconfigure(0, weight=0)
        buttons_frame.rowconfigure(1, weight=0)
        buttons_frame.rowconfigure(2, weight=1)
        
        # Mind Mirror Button
        self.create_app_button(
            buttons_frame,
            "MIND MIRROR",
            "Consciousness Exploration & Neural Pattern Mapping",
            self._run_mind_mirror,
            0, 0,
            "#00FFFF"
        )
        
        # Reality Glitcher Button
        self.create_app_button(
            buttons_frame,
            "REALITY GLITCHER",
            "Reality Manipulation & Glitch Generation",
            self._run_reality_glitcher,
            0, 1,
            "#FF00FF"
        )
        
        # Create status bar
        status_frame = ttk.Frame(main_frame, style="TFrame")
        status_frame.pack(fill=tk.X, pady=10)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        status_label = ttk.Label(
            status_frame,
            textvariable=self.status_var,
            font=("Courier New", 10),
            foreground="#00FF00",
            background="#121212"
        )
        status_label.pack(side=tk.LEFT, padx=10)
        
        # Create Project 89 info box
        info_frame = ttk.Frame(main_frame, style="Dark.TFrame")
        info_frame.pack(fill=tk.X, pady=10)
        
        info_text = tk.Text(
            info_frame,
            height=10,
            background="#1A1A1A",
            foreground="#00FF00",
            font=("Courier New", 10),
            wrap=tk.WORD,
            borderwidth=0,
            highlightthickness=0
        )
        info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Insert project information
        info_text.insert(tk.END, "PROJECT 89 AGENT ARSENAL\n\n")
        info_text.insert(tk.END, "You are viewing classified Project 89 technology. These tools are designed for consciousness exploration and reality manipulation.\n\n")
        info_text.insert(tk.END, "MIND MIRROR allows you to map your consciousness states and neural patterns. It provides visualization of mental states and can export data for use with Reality Glitcher.\n\n")
        info_text.insert(tk.END, "REALITY GLITCHER uses your consciousness patterns to create custom reality glitches, allowing for manipulation of your perceived reality.\n\n")
        info_text.insert(tk.END, "WARNING: Unauthorized use is strictly prohibited.")
        
        info_text.config(state=tk.DISABLED)
        
        # Add Initialize button
        init_button = tk.Button(
            main_frame,
            text="Initialize Environment",
            font=("Courier New", 10, "bold"),
            bg="#333333",
            fg="#00FF00",
            activebackground="#444444",
            activeforeground="#00FF00",
            padx=10,
            pady=5,
            command=self._initialize_environment
        )
        init_button.pack(pady=10)
    
    def create_app_button(self, parent, title, description, command, row, col, highlight_color):
        """Create a styled application button with description."""
        button_frame = ttk.Frame(parent, style="Card.TFrame")
        button_frame.grid(row=row, column=col, padx=10, pady=10, sticky="NSEW")
        
        # Add a border
        border_frame = ttk.Frame(button_frame, style="Border.TFrame")
        border_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Add content frame
        content_frame = ttk.Frame(border_frame, style="TFrame")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add title
        title_label = ttk.Label(
            content_frame,
            text=title,
            font=("Courier New", 16, "bold"),
            foreground=highlight_color,
            background="#121212"
        )
        title_label.pack(pady=(10, 5))
        
        # Add description
        desc_label = ttk.Label(
            content_frame,
            text=description,
            font=("Courier New", 10),
            foreground="#CCCCCC",
            background="#121212",
            wraplength=300
        )
        desc_label.pack(pady=(0, 10))
        
        # Add launch button
        launch_button = tk.Button(
            content_frame,
            text="LAUNCH",
            font=("Courier New", 12, "bold"),
            bg="#333333",
            fg=highlight_color,
            activebackground="#444444",
            activeforeground=highlight_color,
            padx=20,
            pady=10,
            command=command
        )
        launch_button.pack(pady=10)
    
    def configure_style(self):
        """Configure the cyberpunk style for the UI."""
        style = ttk.Style()
        
        # Configure dark theme
        style.configure("TFrame", background="#121212")
        style.configure("Dark.TFrame", background="#0A0A0A")
        style.configure("Card.TFrame", background="#1C1C1C")
        style.configure("Border.TFrame", background="#00FFFF")
        
        style.configure("TLabel", background="#121212", foreground="#FFFFFF")
        style.configure("TButton", background="#333333", foreground="#00FFFF", 
                       font=("Courier New", 10, "bold"))
        
        # Configure the application background
        self.root.configure(background="#0A0A0A")
    
    def _initialize_environment(self):
        """Initialize the environment for proper communication between applications."""
        try:
            self.status_var.set("Initializing environment...")
            
            # Run the initialize_environment.bat script
            if platform.system() == "Windows":
                result = subprocess.run(
                    ["initialize_environment.bat"],
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
            else:
                # For non-Windows systems, run the equivalent commands
                self._ensure_directories()
            
            self.status_var.set("Environment initialized. Applications are ready.")
        except Exception as e:
            self.status_var.set(f"Error initializing environment: {str(e)}")
    
    def _ensure_directories(self):
        """Ensure all necessary directories exist."""
        # Create directories for Mind Mirror
        os.makedirs(os.path.join(self.script_dir, "MindMirror", "user_data"), exist_ok=True)
        os.makedirs(os.path.join(self.script_dir, "MindMirror", "user_data", "journal"), exist_ok=True)
        os.makedirs(os.path.join(self.script_dir, "MindMirror", "exports"), exist_ok=True)
        os.makedirs(os.path.join(self.script_dir, "MindMirror", "exports", "reality_glitcher"), exist_ok=True)
        
        # Create directories for Reality Glitcher
        os.makedirs(os.path.join(self.script_dir, "RealityGlitcher", "imports"), exist_ok=True)
    
    def _run_mind_mirror(self):
        """Run the Mind Mirror application in a separate thread."""
        threading.Thread(target=self._run_mind_mirror_thread, daemon=True).start()
    
    def _run_mind_mirror_thread(self):
        """Run the Mind Mirror application."""
        try:
            self.status_var.set("Launching Mind Mirror...")
            
            mind_mirror_dir = os.path.join(self.script_dir, "MindMirror")
            mind_mirror_script = os.path.join(mind_mirror_dir, "enchanted_mindmirror_new.py")
            
            if not os.path.exists(mind_mirror_script):
                self.status_var.set("Error: Mind Mirror script not found!")
                return
            
            # Ensure the directory exists
            self._ensure_directories()
            
            # Change to the Mind Mirror directory and run the script
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
    
    def _run_reality_glitcher(self):
        """Run the Reality Glitcher application in a separate thread."""
        threading.Thread(target=self._run_reality_glitcher_thread, daemon=True).start()
    
    def _run_reality_glitcher_thread(self):
        """Run the Reality Glitcher application."""
        try:
            self.status_var.set("Launching Reality Glitcher...")
            
            reality_glitcher_dir = os.path.join(self.script_dir, "RealityGlitcher")
            reality_glitcher_script = os.path.join(reality_glitcher_dir, "main.py")
            
            if not os.path.exists(reality_glitcher_script):
                self.status_var.set("Error: Reality Glitcher main.py not found!")
                return
            
            # Ensure the directory exists
            self._ensure_directories()
            
            # Change to the Reality Glitcher directory and run the script
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
    app = Project89Launcher(root)
    root.mainloop()

if __name__ == "__main__":
    main() 