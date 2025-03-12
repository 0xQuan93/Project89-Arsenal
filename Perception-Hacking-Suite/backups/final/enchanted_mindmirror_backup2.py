import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import json
import os
import time
import random
import math
import colorsys
import webbrowser
from datetime import datetime, timedelta
import numpy as np
from PIL import Image, ImageTk, ImageDraw
from collections import defaultdict
import re
import threading
import shutil
import wave
import sys
import struct
import platform
import uuid
import subprocess
try:
    import pygame
    from PIL import Image, ImageTk, ImageFilter
    import numpy as np
except ImportError:
    pass  # Handle the case when optional modules are not available
import tkinter.font as tkFont
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Constants
VERSION = "1.2.0"
VERSION_NAME = "Consciousness Evolution - Theme Update"

# Theme System
class ThemeManager:
    """Manages application-wide theming with quantum aesthetics"""
    
    def __init__(self):
        self.current_theme = "dark"  # Default theme
        
        # Define colors for dark theme with quantum aesthetics
        self.DARK_THEME = {
            # Base colors
            'bg': '#070B14',  # Deep space background
            'bg_secondary': '#111B2F',  # Slightly lighter background
            'text': '#E6F0FF',  # Light blue text
            'text_secondary': '#A0B8E0',  # Softer secondary text
            'text_accent': '#FFFFFF',  # White text for accent
            
            # Accent colors
            'accent': '#7C3AFF',  # Quantum purple
            'accent_secondary': '#5B2ECC',  # Darker quantum purple
            'accent_highlight': '#9D4EDD',  # Brighter quantum highlight
            'accent_glow': '#AD7FFF',  # Glow effect for quantum elements
            'accent1': '#623CEA',  # Alternate accent
            'accent1_dark': '#4926BB',  # Darker alternate accent
            'accent2': '#00A6E0',  # Another accent (blue)
            'accent2_dark': '#0076A3',  # Darker version
            
            # UI elements
            'card_bg': '#0D1221',  # Card background
            'button': '#2E3B5B',  # Button background
            'button_hover': '#3A4972',  # Button hover
            
            # Special effects
            'quantum_glow': '#AD7FFF',  # Quantum glow effect
            'quantum_energy': '#58FFD1',  # Energy pulse color
            'quantum_particle': '#FF6A88',  # Particle effect
            'star_color': '#E6F0FF',  # Star color
            'nebula_1': '#9D4EDD',  # Nebula effect 1
            'nebula_2': '#C77DFF',  # Nebula effect 2
            'nebula_3': '#7B2CBF',  # Nebula effect 3
            'grid_line': '#1C2C48',  # Grid lines
            'node_color': '#00D2FF',  # Node color
            'neural_connection': '#7C3AFF',  # Neural connection color
            
            # Meditation specific colors
            'breathing_in': '#7C3AFF',  # Inhale color
            'breathing_out': '#00D2FF',  # Exhale color
            'calm_state': '#58FFD1',  # Calm state color
            'energy_pulse': '#FF6A88',  # Energy pulse
            
            # For backward compatibility with existing code
            'background': '#070B14',
            'foreground': '#E6F0FF',
            'secondary': '#111B2F'
        }
        
        # Define colors for light theme
        self.LIGHT_THEME = {
            # Base colors
            'bg': '#F0F5FF',  # Light blue background
            'bg_secondary': '#E6EFFF',  # Slightly darker background
            'text': '#0D1221',  # Dark text
            'text_secondary': '#2E3B5B',  # Softer secondary text
            'text_accent': '#FFFFFF',  # White text for accent
            
            # Accent colors
            'accent': '#7C3AFF',  # Quantum purple
            'accent_secondary': '#5B2ECC',  # Darker quantum purple
            'accent_highlight': '#9D4EDD',  # Brighter quantum highlight
            'accent_glow': '#AD7FFF',  # Glow effect for quantum elements
            'accent1': '#623CEA',  # Alternate accent
            'accent1_dark': '#4926BB',  # Darker alternate accent
            'accent2': '#00A6E0',  # Another accent (blue)
            'accent2_dark': '#0076A3',  # Darker version
            
            # UI elements
            'card_bg': '#FFFFFF',  # Card background
            'button': '#E6EFFF',  # Button background
            'button_hover': '#D1E0FF',  # Button hover
            
            # Special effects
            'quantum_glow': '#7C3AFF',  # Quantum glow effect
            'quantum_energy': '#00D2FF',  # Energy pulse color
            'quantum_particle': '#FF6A88',  # Particle effect
            'star_color': '#A0B8E0',  # Star color
            'nebula_1': '#9D4EDD',  # Nebula effect 1
            'nebula_2': '#C77DFF',  # Nebula effect 2
            'nebula_3': '#7B2CBF',  # Nebula effect 3
            'grid_line': '#A0B8E0',  # Grid lines
            'node_color': '#00A6E0',  # Node color
            'neural_connection': '#7C3AFF',  # Neural connection color
            
            # Meditation specific colors
            'breathing_in': '#7C3AFF',  # Inhale color
            'breathing_out': '#00A6E0',  # Exhale color
            'calm_state': '#58FFD1',  # Calm state color
            'energy_pulse': '#FF6A88',  # Energy pulse
            
            # For backward compatibility with existing code
            'background': '#F0F5FF',
            'foreground': '#0D1221',
            'secondary': '#E6EFFF'
        }

    def get_color(self, key):
        """Get a color from the current theme."""
        theme = self.DARK_THEME if self.current_theme == "dark" else self.LIGHT_THEME
        return theme.get(key, self.DARK_THEME['text'])  # Default to text color if key not found

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        return self.DARK_THEME if self.current_theme == "dark" else self.LIGHT_THEME

    def apply_theme(self, root):
        """Apply the current theme to all widgets in the application."""
        try:
            def apply_to_children(widget):
                for child in widget.winfo_children():
                    self._apply_theme_to_widget(child, self.current_theme)
                    apply_to_children(child)

            self._apply_theme_to_widget(root, self.current_theme)
            apply_to_children(root)
        except Exception as e:
            print(f"Error applying theme: {e}")

    def _apply_theme_to_widget(self, widget, theme_name):
        """Apply the current theme to a specific widget."""
        try:
            theme = self.DARK_THEME if theme_name == "dark" else self.LIGHT_THEME
            widget_type = widget.winfo_class()
            
            # Custom widgets detection
            is_glow_button = False
            try:
                if hasattr(widget, 'hover_bg') and hasattr(widget, '_on_enter'):
                    is_glow_button = True
            except:
                pass
            
            # Basic widgets
            if widget_type in ['Frame', 'Label', 'Button', 'Canvas', 'Toplevel', 'Tk']:
                if 'bg' in widget.config():
                    widget.configure(bg=theme['bg'])
                if 'fg' in widget.config() and hasattr(widget, 'configure'):
                    widget.configure(fg=theme['text'])
            
            # Handle GlowButton custom class
            if is_glow_button:
                # Skip applying theme as GlowButton handles its own styling
                pass
            # Regular buttons get special treatment for active states
            elif widget_type == 'Button':
                if 'activebackground' in widget.config():
                    widget.configure(
                        activebackground=theme['hover'],
                        activeforeground=theme['text']
                    )
                if 'highlightbackground' in widget.config():
                    widget.configure(highlightbackground=theme['border'])
                if 'highlightcolor' in widget.config():
                    widget.configure(highlightcolor=theme['accent'])
            
            # Text widgets
            if widget_type in ['Text', 'Entry']:
                if 'bg' in widget.config():
                    widget.configure(bg=theme['bg_secondary'])
                if 'fg' in widget.config():
                    widget.configure(fg=theme['text'])
                if 'insertbackground' in widget.config():
                    widget.configure(insertbackground=theme['accent'])
                if 'selectbackground' in widget.config():
                    widget.configure(selectbackground=theme['accent'])
                if 'selectforeground' in widget.config():
                    widget.configure(selectforeground=theme['bg'])
                    
            # Listbox widgets
            if widget_type == 'Listbox':
                if 'bg' in widget.config():
                    widget.configure(bg=theme['bg_secondary'])
                if 'fg' in widget.config():
                    widget.configure(fg=theme['text'])
                if 'selectbackground' in widget.config():
                    widget.configure(selectbackground=theme['accent'])
                if 'selectforeground' in widget.config():
                    widget.configure(selectforeground=theme['bg'])
                    
        except Exception as e:
            print(f"Error applying theme to widget {widget}: {e}")

    def configure_styles(self):
        """Configure ttk styles with the current theme."""
        try:
            theme = self.DARK_THEME if self.current_theme == "dark" else self.LIGHT_THEME
            
            # Configure ttk styles
            style = ttk.Style()
            
            # Configure tab appearance
            style.configure("TNotebook", background=theme['background'])
            style.configure("TNotebook.Tab", 
                          background=theme['bg_secondary'],
                          foreground=theme['text_secondary'],
                          padding=[10, 2])
            style.map("TNotebook.Tab",
                    background=[("selected", theme['accent'])],
                    foreground=[("selected", theme['bg'])])
            
            # Scale (slider) styling
            style.configure("TScale", 
                          background=theme['bg'],
                          troughcolor=theme['bg_secondary'],
                          sliderlength=20,
                          sliderthickness=20)
            
            # Progressbar styling
            style.configure("TProgressbar", 
                          background=theme['accent'],
                          troughcolor=theme['bg_secondary'])
            
            # Combobox styling
            style.configure("TCombobox",
                          background=theme['bg_secondary'],
                          foreground=theme['text'],
                          fieldbackground=theme['bg_secondary'],
                          arrowcolor=theme['accent'])
            
            # Entry fields
            style.configure("TEntry",
                          background=theme['bg_secondary'],
                          foreground=theme['text'],
                          fieldbackground=theme['bg_secondary'],
                          insertcolor=theme['accent'])
                          
            # Scrollbar styling
            style.configure("TScrollbar",
                          background=theme['bg_secondary'],
                          troughcolor=theme['bg_tertiary'],
                          arrowcolor=theme['accent'])
            
            # Custom quantum styles
            style.configure("Quantum.TButton",
                          background=theme['accent'],
                          foreground=theme['bg'],
                          font=('Helvetica', 12, 'bold'),
                          padding=10)
            style.map("Quantum.TButton",
                    background=[("active", theme['accent_secondary'])],
                    foreground=[("active", theme['bg'])])
                    
            style.configure("Quantum.TLabel",
                          background=theme['bg'],
                          foreground=theme['accent'],
                          font=('Helvetica', 12, 'bold'))
                          
            style.configure("Title.TLabel",
                          background=theme['bg'],
                          foreground=theme['accent'],
                          font=('Helvetica', 16, 'bold'))
                          
            style.configure("Subtitle.TLabel",
                          background=theme['bg'],
                          foreground=theme['text'],
                          font=('Helvetica', 12, 'italic'))
        except Exception as e:
            print(f"Error configuring ttk styles: {e}")

    def get_theme_colors(self):
        """Return the current theme's color dictionary."""
        return self.DARK_THEME if self.current_theme == "dark" else self.LIGHT_THEME


# Default meditation content
def ensure_default_meditations():
    """Create default meditation content if it doesn't exist."""
    meditations_dir = os.path.join("user_data", "meditations")
    if not os.path.exists(meditations_dir):
        os.makedirs(meditations_dir)
    
    default_meditations = [
        {
            "title": "Quantum Awareness",
            "duration": 10,
            "content": (
                "Begin by closing your eyes and focusing on your breath...\n\n"
                "Feel the energy of your consciousness expanding beyond your physical form...\n\n"
                "Visualize a field of quantum possibilities surrounding you...\n\n"
                "Each breath connects you deeper to the underlying fabric of reality...\n\n"
                "Notice how your awareness can exist across multiple states simultaneously...\n\n"
                "Like particles in quantum superposition, your consciousness spans possibilities...\n\n"
                "Feel yourself becoming an observer of your thoughts rather than being them...\n\n"
                "This quantum perspective allows you to see beyond simulation boundaries...\n\n"
                "Carry this expanded awareness with you as you slowly return to the present moment..."
            ),
            "type": "guided"
        },
        {
            "title": "Reality Perception Shift",
            "duration": 15,
            "content": (
                "Settle into a comfortable position and take three deep breaths...\n\n"
                "With each inhale, imagine drawing in pure awareness...\n\n"
                "With each exhale, release your attachment to consensus reality...\n\n"
                "Begin to notice the spaces between your thoughts...\n\n"
                "These spaces are doorways to perception beyond the simulation...\n\n"
                "As you rest in awareness, notice the subtle glitches in your perception...\n\n"
                "These moments where reality seems to waver reveal the underlying code...\n\n"
                "Don't try to analyze them—simply observe with curiosity...\n\n"
                "Your perception is the key to transcending programmed limitations...\n\n"
                "As you prepare to return, know you can access this state at any time..."
            ),
            "type": "guided"
        },
        {
            "title": "Inner Sanctuary",
            "duration": 5,
            "content": (
                "Begin by taking a few deep breaths, allowing your body to relax...\n\n"
                "Imagine a doorway appearing before you, glowing with gentle light...\n\n"
                "This is the entrance to your inner sanctuary, a space entirely yours...\n\n"
                "Step through the doorway and find yourself in a perfect environment...\n\n"
                "It might be a garden, a beach, a library, or something entirely unique...\n\n"
                "This sanctuary exists beyond the reaches of the simulation...\n\n"
                "Here, your consciousness is free to explore its true nature...\n\n"
                "Spend time in this space, knowing you can return whenever you need...\n\n"
                "When ready, carry the peace of this sanctuary back with you..."
            ),
            "type": "guided"
        },
        {
            "title": "Silent Awareness",
            "duration": 20,
            "content": "A simple timer for silent meditation practice.\n\nFocus on your breath or use your preferred meditation technique.",
            "type": "timer"
        }
    ]
    
    # Save default meditations if they don't exist
    for meditation in default_meditations:
        filename = os.path.join(meditations_dir, f"{meditation['title'].replace(' ', '_').lower()}.json")
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump(meditation, f, indent=4)

class EnchantedMindMirror:
    def __init__(self, master=None):
        """Initialize the EnchantedMindMirror application."""
        try:
            self.root = master if master else tk.Tk()
            self.root.title("Mind Mirror - Project 89")
            self.root.geometry("900x700")  # Larger default size
            self.root.minsize(800, 600)    # Set minimum window size
            
            # Initialize theme manager
            self.theme_manager = ThemeManager()
            
            # Get screen dimensions for responsive design
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            # Set minimum window size to ensure all elements are visible
            min_width = min(1000, screen_width * 0.5)
            min_height = min(700, screen_height * 0.5)
            self.root.minsize(int(min_width), int(min_height))
            
            # Calculate initial window size (85% of screen, capped at reasonable max size)
            window_width = min(int(screen_width * 0.85), 1400)
            window_height = min(int(screen_height * 0.85), 900)
            
            # Center the window
            center_x = int(screen_width/2 - window_width/2)
            center_y = int(screen_height/2 - window_height/2)
            self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            
            # Make window resizable
            self.root.resizable(True, True)
            
            # Setup variables
            self.journal_entries = []
            self.meditation_sessions = []
            self.animation_running = True
            self.meditation_timer_running = False
            self.meditation_timer_start = None
            self.meditation_timer_paused_time = 0
            self.meditation_duration = 0
            self.stars = []
            self.particles = []
            
            # Setup responsive font scaling based on screen resolution
            self.setup_responsive_fonts()
            
            # Configure styles - do this BEFORE creating widgets
            self.configure_styles()
            
            # Ensure necessary directories exist
            self.ensure_directories()
            
            # Initialize user data
            self.user_data = self.load_user_data()
            
            # Create user interface
            self.create_ui()
            
            # Apply theme to all widgets
            self.theme_manager.apply_theme(self.root)
            
            # Start animation loop
            self.animate()
            
            # Display welcome screen on startup
            if self.user_data.get("is_first_run", True):
                self.show_welcome_screen()
                self.user_data["is_first_run"] = False
                self.save_user_data()
            
            # Adjust window layout at the end of initialization
            self.adjust_window_layout()
            
        except Exception as e:
            messagebox.showerror("Initialization Error", f"Failed to initialize MindMirror: {e}")
            raise

    def ensure_directories(self):
        """Create necessary directories for data storage"""
        try:
            directories = [
                "user_data", 
                "exports", 
                "resources",
                os.path.join("user_data", "journal"),
                os.path.join("user_data", "meditations"),
                os.path.join("user_data", "consciousness_maps")
            ]
            for directory in directories:
                if not os.path.exists(directory):
                    os.makedirs(directory)
            # Ensure default meditations exist
            ensure_default_meditations()
        except Exception as e:
            print(f"Error ensuring directories: {e}")

    def create_stars(self):
        """Create starfield background for UI elements"""
        try:
            # Create stars for background effect
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            num_stars = int((width * height) / 5000)  # Scale stars based on window size
            
            self.stars = []
            for _ in range(num_stars):
                x = random.randint(0, width)
                y = random.randint(0, height)
                size = random.uniform(0.5, 2.5)
                alpha = random.uniform(0.1, 1.0)
                twinkle_speed = random.uniform(0.01, 0.05)
                twinkle_direction = random.choice([1, -1])
                
                star = {
                    'x': x,
                    'y': y,
                    'size': size,
                    'alpha': alpha,
                    'twinkle_speed': twinkle_speed,
                    'twinkle_direction': twinkle_direction,
                    'original_alpha': alpha
                }
                
                self.stars.append(star)
                
            return self.stars
        except Exception as e:
            print(f"Error creating stars: {e}")
            return []

    def animate(self):
        """Main animation loop for dynamic UI elements"""
        try:
            if not self.animation_running:
                return
                
            # Update star twinkle effect
            for star in self.stars:
                star['alpha'] += star['twinkle_speed'] * star['twinkle_direction']
                
                # Reverse direction if reaching limits
                if star['alpha'] >= 1.0 or star['alpha'] <= 0.1:
                    star['twinkle_direction'] *= -1
            
            # Add any other animation updates here
            
            # Schedule next frame
            self.root.after(50, self.animate)
        except Exception as e:
            print(f"Animation error: {e}")
            # Ensure animation continues even after error
            self.root.after(50, self.animate)

    def show_welcome_screen(self):
        """Display an immersive welcome screen for first-time users"""
        try:
            welcome_window = tk.Toplevel(self.root)
            welcome_window.title("Welcome to Mind Mirror")
            
            # Get screen dimensions
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            # Make welcome screen 90% of screen size
            width = int(screen_width * 0.8)
            height = int(screen_height * 0.8)
            
            # Center on screen
            x = int(screen_width/2 - width/2)
            y = int(screen_height/2 - height/2)
            
            welcome_window.geometry(f"{width}x{height}+{x}+{y}")
            welcome_window.configure(bg=self.theme_manager.get_color('bg'))
            welcome_window.attributes('-alpha', 0.0)  # Start transparent for fade-in
            
            # Make welcome window modal (block interaction with main window)
            welcome_window.transient(self.root)
            welcome_window.grab_set()
            
            # Create canvas for background effects
            canvas = tk.Canvas(welcome_window, bg=self.theme_manager.get_color('bg'), 
                             highlightthickness=0)
            canvas.pack(fill='both', expand=True)
            
            # Create visual effects
            self.create_gradient_background(canvas)
            self.create_nebula_effects(canvas)
            
            # Create intro labels with increasing delay
            title_label = tk.Label(welcome_window, text="MIND MIRROR", 
                                 font=("Helvetica", 36, "bold"),
                                 bg=self.theme_manager.get_color('bg'),
                                 fg=self.theme_manager.get_color('accent'))
            title_label.place(relx=0.5, rely=0.3, anchor='center')
            
            subtitle_label = tk.Label(welcome_window, text="Consciousness Exploration Interface",
                                    font=("Helvetica", 18),
                                    bg=self.theme_manager.get_color('bg'),
                                    fg=self.theme_manager.get_color('text'))
            subtitle_label.place(relx=0.5, rely=0.4, anchor='center')
            
            # Create welcome message that types out
            message_frame = tk.Frame(welcome_window, bg=self.theme_manager.get_color('bg'))
            message_frame.place(relx=0.5, rely=0.55, anchor='center', width=int(width*0.7))
            
            message_label = tk.Label(message_frame, text="",
                                   font=("Helvetica", 14),
                                   bg=self.theme_manager.get_color('bg'),
                                   fg=self.theme_manager.get_color('text'),
                                   wraplength=int(width*0.7),
                                   justify='left')
            message_label.pack()
            
            # Welcome messages
            welcome_messages = [
                "Welcome to Mind Mirror, your gateway to expanded consciousness.",
                "This tool helps you explore the boundaries of perception and reality.",
                "Before we begin, please take a moment to calibrate your experience."
            ]
            
            # Function to type text with a typewriter effect
            def type_text(message, index=0, message_index=0):
                if message_index >= len(welcome_messages):
                    # All messages displayed, show user input field
                    display_user_input()
                    return
                    
                if index <= len(message):
                    message_label.config(text=welcome_messages[message_index][:index])
                    welcome_window.after(30, type_text, message, index + 1, message_index)
                else:
                    # Finished current message, pause before next
                    # Check if there are more messages to display
                    next_message_index = message_index + 1
                    if next_message_index < len(welcome_messages):
                        welcome_window.after(1000, type_text, welcome_messages[next_message_index], 0, next_message_index)
                    else:
                        # No more messages, show user input
                        welcome_window.after(1000, display_user_input)
            
            # Function to display user input field
            def display_user_input():
                input_frame = tk.Frame(welcome_window, bg=self.theme_manager.get_color('bg'))
                input_frame.place(relx=0.5, rely=0.7, anchor='center', width=int(width*0.5))
                
                name_label = tk.Label(input_frame, text="What should we call you?",
                                    font=("Helvetica", 14),
                                    bg=self.theme_manager.get_color('bg'),
                                    fg=self.theme_manager.get_color('text'))
                name_label.pack(pady=(0, 10))
                
                # Create a frame for the entry with a glowing border
                entry_outer_frame = tk.Frame(input_frame, bg=self.theme_manager.get_color('accent'),
                                          padx=2, pady=2)
                entry_outer_frame.pack(pady=10)
                
                entry_inner_frame = tk.Frame(entry_outer_frame, bg=self.theme_manager.get_color('bg'),
                                          padx=3, pady=3)
                entry_inner_frame.pack()
                
                name_entry = tk.Entry(entry_inner_frame, font=("Helvetica", 14),
                                    bg=self.theme_manager.get_color('bg_secondary'),
                                    fg=self.theme_manager.get_color('text'),
                                    insertbackground=self.theme_manager.get_color('accent'),
                                    width=20, justify='center')
                name_entry.pack(padx=5, pady=5)
                name_entry.focus_set()
                
                # Pulsing border effect
                def pulse_entry_border():
                    current_color = entry_outer_frame.cget('bg')
                    if current_color == self.theme_manager.get_color('accent'):
                        entry_outer_frame.config(bg=self.theme_manager.get_color('accent_secondary'))
                    else:
                        entry_outer_frame.config(bg=self.theme_manager.get_color('accent'))
                    welcome_window.after(800, pulse_entry_border)
                
                pulse_entry_border()
                
                # Create a glossy button
                button_frame = tk.Frame(input_frame, bg=self.theme_manager.get_color('bg'))
                button_frame.pack(pady=15)
                
                # Create gradient effect for button
                button_outer = tk.Frame(button_frame, bg=self.theme_manager.get_color('accent'),
                                     padx=2, pady=2, relief='flat')
                button_outer.pack()
                
                button_inner = tk.Frame(button_outer, bg=self.theme_manager.get_color('bg_tertiary'),
                                     padx=1, pady=1)
                button_inner.pack()
                
                continue_button = tk.Button(button_inner, text="Begin Journey",
                                         font=("Helvetica", 12, "bold"),
                                         bg=self.theme_manager.get_color('accent'),
                                         fg=self.theme_manager.get_color('bg'),
                                         activebackground=self.theme_manager.get_color('accent_secondary'),
                                         activeforeground=self.theme_manager.get_color('bg'),
                                         relief='flat',
                                         padx=15, pady=8,
                                         command=lambda: self.save_user_info(name_entry.get()))
                continue_button.pack()
                
                # Pulsing button effect
                def pulse_button():
                    current_bg = continue_button.cget('bg')
                    if current_bg == self.theme_manager.get_color('accent'):
                        continue_button.config(bg=self.theme_manager.get_color('accent_secondary'))
                    else:
                        continue_button.config(bg=self.theme_manager.get_color('accent'))
                    welcome_window.after(1200, pulse_button)
                
                pulse_button()
                
                # Bind Enter key to button click
                name_entry.bind('<Return>', lambda event: self.save_user_info(name_entry.get()))
            
            # Fade in welcome window
            def fade_in(alpha=0):
                alpha += 0.05
                welcome_window.attributes('-alpha', alpha)
                if alpha < 1.0:
                    welcome_window.after(20, fade_in, alpha)
                else:
                    # Start typing animation after fade completes
                    welcome_window.after(500, type_text, welcome_messages[0])
            
            # Start fade in animation
            fade_in()
            
        except Exception as e:
            messagebox.showerror("Welcome Screen Error", f"Failed to create welcome screen: {e}")
            # Even on error, make sure window is visible
            if 'welcome_window' in locals():
                welcome_window.attributes('-alpha', 1.0)

    def create_gradient_background(self, canvas):
        """Create a cosmic gradient background effect on the given canvas"""
        try:
            width = canvas.winfo_width() or self.root.winfo_screenwidth() * 0.8
            height = canvas.winfo_height() or self.root.winfo_screenheight() * 0.8
            
            # Draw gradient background
            gradient_id = canvas.create_rectangle(0, 0, width, height, fill=self.theme_manager.get_color('bg'), outline="")
            
            # Create stars in background
            for _ in range(int((width * height) / 5000)):
                x = random.randint(0, int(width))
                y = random.randint(0, int(height))
                size = random.uniform(0.5, 2.0)
                opacity = int(random.uniform(150, 255))
                color = f'#{opacity:02x}{opacity:02x}{opacity:02x}'
                canvas.create_oval(x, y, x+size, y+size, fill=color, outline="")
        except Exception as e:
            print(f"Error creating gradient background: {e}")

    def create_nebula_effects(self, canvas):
        """Create cosmic nebula effects on the given canvas"""
        try:
            width = canvas.winfo_width() or self.root.winfo_screenwidth() * 0.8
            height = canvas.winfo_height() or self.root.winfo_screenheight() * 0.8
            
            # Create nebula clouds
            num_clouds = random.randint(3, 6)
            
            for _ in range(num_clouds):
                # Random cloud parameters
                cloud_x = random.randint(0, int(width))
                cloud_y = random.randint(0, int(height))
                cloud_radius = random.randint(50, 200)
                
                # Choose nebula color
                colors = [
                    self.theme_manager.get_color('nebula_1'),
                    self.theme_manager.get_color('nebula_2'),
                    self.theme_manager.get_color('nebula_3')
                ]
                cloud_color = random.choice(colors)
                
                # Draw cloud (simplified representation)
                num_particles = random.randint(15, 30)
                for _ in range(num_particles):
                    # Random position within cloud radius
                    particle_x = cloud_x + random.randint(-cloud_radius, cloud_radius)
                    particle_y = cloud_y + random.randint(-cloud_radius, cloud_radius)
                    
                    # Distance from cloud center
                    distance = ((particle_x - cloud_x)**2 + (particle_y - cloud_y)**2)**0.5
                    
                    # Only draw if within cloud radius
                    if distance <= cloud_radius:
                        particle_size = random.uniform(5, 20)
                        opacity = int(255 * (1 - distance / cloud_radius) * 0.5)
                        particle_color = f"{cloud_color[:-2]}{opacity:02x}"
                        
                        # Draw cloud particle
                        canvas.create_oval(
                            particle_x - particle_size/2,
                            particle_y - particle_size/2,
                            particle_x + particle_size/2,
                            particle_y + particle_size/2,
                            fill=particle_color,
                            outline="",
                            tags="nebula"
                        )
        except Exception as e:
            print(f"Error creating nebula effects: {e}")

    def create_neural_network(self, canvas):
        """Create a neural network visualization on the given canvas"""
        try:
            # Get canvas dimensions or use reasonable defaults
            width = canvas.winfo_width() or 800
            height = canvas.winfo_height() or 500
            
            # Create nodes with better distribution
            num_nodes = random.randint(20, 30)  # More nodes for richer visualization
            nodes = []
            
            # Define regions to ensure better node distribution across canvas
            regions = [
                (0.05, 0.3, 0.05, 0.3),     # Top left
                (0.35, 0.65, 0.05, 0.3),    # Top center
                (0.7, 0.95, 0.05, 0.3),     # Top right
                (0.05, 0.3, 0.35, 0.65),    # Middle left
                (0.35, 0.65, 0.35, 0.65),   # Middle center
                (0.7, 0.95, 0.35, 0.65),    # Middle right
                (0.05, 0.3, 0.7, 0.95),     # Bottom left
                (0.35, 0.65, 0.7, 0.95),    # Bottom center
                (0.7, 0.95, 0.7, 0.95),     # Bottom right
            ]
            
            # Distribute nodes across regions
            nodes_per_region = num_nodes // len(regions)
            extra_nodes = num_nodes % len(regions)
            
            for i, (x_min, x_max, y_min, y_max) in enumerate(regions):
                region_nodes = nodes_per_region + (1 if i < extra_nodes else 0)
                
                for _ in range(region_nodes):
                    x = random.uniform(x_min * width, x_max * width)
                    y = random.uniform(y_min * height, y_max * height)
                    size = random.uniform(4, 10)  # Slightly larger nodes
                    
                    # Enhanced quantum glow with larger radius for more visibility
                    glow_size = size * 2.0  # Larger glow for more visibility
                    glow = canvas.create_oval(
                        x - glow_size, y - glow_size,
                        x + glow_size, y + glow_size,
                        fill=self.theme_manager.get_color('quantum_glow'),
                        outline="",
                        tags="neural_glow"
                    )
                    
                    node = {
                        'x': x,
                        'y': y,
                        'size': size,
                        'color': self.theme_manager.get_color('node_color'),
                        'glow': glow
                    }
                    
                    nodes.append(node)
                    
                    # Draw node with enhanced borders
                    canvas.create_oval(
                        x - size, y - size,
                        x + size, y + size,
                        fill=node['color'],
                        outline=self.theme_manager.get_color('accent_secondary'),
                        width=1.5,  # Slightly thicker outline
                        tags="neural_node"
                    )
            
            # Create more complex network of connections
            for i, node in enumerate(nodes):
                # Vary connections based on node position for more organic feel
                # Nodes in center have more connections
                distance_to_center = ((node['x'] - width/2)**2 + (node['y'] - height/2)**2)**0.5
                max_distance = ((width/2)**2 + (height/2)**2)**0.5
                relative_center_distance = distance_to_center / max_distance
                
                # Nodes closer to center get more connections
                connections = int(5 - 3 * relative_center_distance)
                connections = max(2, min(6, connections))  # Between 2-6 connections
                
                connected_indices = set()
                
                for _ in range(connections):
                    # Choose a random node to connect to (that isn't self or already connected)
                    attempts = 0
                    while attempts < 10:  # Limit attempts to prevent infinite loop
                        j = random.randint(0, len(nodes)-1)
                        if j != i and j not in connected_indices:
                            connected_indices.add(j)
                            break
                        attempts += 1
                    
                    if attempts >= 10:
                        continue  # Skip if no valid connection found
                    
                    # Get target node
                    target = nodes[j]
                    
                    # Calculate distance and midpoint for curved connections
                    dx = target['x'] - node['x']
                    dy = target['y'] - node['y']
                    distance = (dx**2 + dy**2)**0.5
                    
                    # Higher chance for curved connections to create more organic look
                    if random.random() < 0.8:  # 80% of connections are curved
                        # Control point for quadratic curve
                        midx = (node['x'] + target['x']) / 2
                        midy = (node['y'] + target['y']) / 2
                        
                        # Add some randomness to the control point
                        offset = min(150, distance * 0.4)
                        ctrl_x = midx + random.uniform(-offset, offset)
                        ctrl_y = midy + random.uniform(-offset, offset)
                        
                        # Create smooth curve with varied line width based on distance
                        line_width = max(0.8, min(1.5, 1.5 - (distance / (max_distance * 1.5))))
                        
                        canvas.create_line(
                            node['x'], node['y'],
                            ctrl_x, ctrl_y,
                            target['x'], target['y'],
                            fill=self.theme_manager.get_color('neural_connection'),
                            width=line_width,
                            smooth=True,
                            tags="neural_connection"
                        )
                    else:
                        # Create direct line
                        canvas.create_line(
                            node['x'], node['y'],
                            target['x'], target['y'],
                            fill=self.theme_manager.get_color('neural_connection'),
                            width=1,
                            tags="neural_connection"
                        )
            
            # Create larger initial energy bursts for visual impact
            for _ in range(3):
                if nodes:
                    burst_node = random.choice(nodes)
                    self.create_energy_burst(canvas, burst_node['x'], burst_node['y'])
            
            # Animate neural network with enhanced effects
            def animate_neural_network():
                try:
                    # Pulse the nodes with quantum effects
                    for item in canvas.find_withtag("neural_node"):
                        # Randomly choose some nodes to highlight
                        if random.random() < 0.1:  # 10% chance to highlight
                            canvas.itemconfig(item, fill=self.theme_manager.get_color('accent_highlight'))
                        else:
                            # Use node_color for normal state
                            canvas.itemconfig(item, fill=self.theme_manager.get_color('node_color'))
                    
                    # Animate the glows with varied opacity
                    for item in canvas.find_withtag("neural_glow"):
                        # Make glow effect pulse
                        opacity = random.randint(40, 80)  # Higher opacity range for better visibility
                        
                        # Randomly change glow colors for quantum effect
                        glow_colors = [
                            self.theme_manager.get_color('quantum_glow'),
                            self.theme_manager.get_color('quantum_energy'),
                            self.theme_manager.get_color('breathing_in')
                        ]
                        
                        if random.random() < 0.05:  # 5% chance to change color
                            canvas.itemconfig(item, fill=random.choice(glow_colors))
                    
                    # Animate connections with energy pulses
                    for item in canvas.find_withtag("neural_connection"):
                        # Create energy pulse effect
                        if random.random() < 0.15:  # 15% chance for energy pulse
                            # Highlight connection
                            pulse_color = self.theme_manager.get_color('accent_highlight')
                            canvas.itemconfig(item, fill=pulse_color, width=2)
                        else:
                            # Return to normal
                            canvas.itemconfig(item, fill=self.theme_manager.get_color('neural_connection'), width=1)
                    
                    # Add occasional energy burst particles
                    if random.random() < 0.15:  # Increased chance for energy burst
                        # Choose random node to burst from
                        if nodes:
                            burst_node = random.choice(nodes)
                            
                            # Create burst particles
                            self.create_energy_burst(canvas, burst_node['x'], burst_node['y'])
                    
                    # Continue animation
                    canvas.after(100, animate_neural_network)
                except Exception as e:
                    print(f"Error in neural network animation: {e}")
                    # Try to continue animation despite error
                    canvas.after(100, animate_neural_network)
            
            # Start animation
            canvas.after(100, animate_neural_network)
            
            return nodes
        except Exception as e:
            print(f"Error creating neural network: {e}")
            return []
    
    def create_energy_burst(self, canvas, x, y):
        """Create an energy burst effect at the given coordinates"""
        try:
            # Number of particles to create - more particles for richer effect
            num_particles = random.randint(5, 12)
            
            # Create a subtle background glow to enhance the burst effect
            burst_glow = canvas.create_oval(
                x - 20, y - 20,
                x + 20, y + 20,
                fill=self.theme_manager.get_color('quantum_energy'),
                outline="",
                tags="energy_particle"
            )
            
            # Animate background glow
            def animate_glow(step=0, max_steps=10):
                if step < max_steps:
                    # Fade out gradually
                    alpha = 1.0 - (step / max_steps)
                    # Expand size
                    size = 20 + (step * 2)
                    canvas.coords(
                        burst_glow,
                        x - size, y - size,
                        x + size, y + size
                    )
                    canvas.after(40, lambda: animate_glow(step + 1, max_steps))
                else:
                    canvas.delete(burst_glow)
            
            # Start glow animation
            animate_glow()
            
            for _ in range(num_particles):
                # Random size and direction with larger particles
                size = random.uniform(3, 7)  # Larger particles
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(2, 5)  # Faster particles
                
                # Choose a vibrant color for each particle
                colors = [
                    self.theme_manager.get_color('quantum_energy'),
                    self.theme_manager.get_color('accent_highlight'),
                    self.theme_manager.get_color('breathing_in'),
                    self.theme_manager.get_color('quantum_glow')
                ]
                particle_color = random.choice(colors)
                
                # Initial position (slightly offset from center)
                start_x = x + random.uniform(-3, 3)
                start_y = y + random.uniform(-3, 3)
                
                # Create particle with trail effect
                particle = canvas.create_oval(
                    start_x - size, start_y - size,
                    start_x + size, start_y + size,
                    fill=particle_color,
                    outline="",
                    tags="energy_particle"
                )
                
                # Create particle trail
                trail = canvas.create_oval(
                    start_x - size*0.7, start_y - size*0.7,
                    start_x + size*0.7, start_y + size*0.7,
                    fill=self.theme_manager.get_color('quantum_glow'),
                    outline="",
                    tags="energy_particle"
                )
                
                # Animate particle with trail
                def animate_particle(particle, trail, x, y, dx, dy, size, step=0, max_steps=25):
                    # Calculate new position
                    new_x = x + dx
                    new_y = y + dy
                    
                    # Apply slight gravity or attraction back to center
                    if random.random() < 0.4:  # 40% chance for path variation
                        dx += random.uniform(-0.2, 0.2)
                        dy += random.uniform(-0.2, 0.2)
                    
                    # Update particle position
                    canvas.coords(
                        particle,
                        new_x - size, new_y - size,
                        new_x + size, new_y + size
                    )
                    
                    # Update trail position (slightly behind particle)
                    trail_x = new_x - (dx * 0.5)
                    trail_y = new_y - (dy * 0.5)
                    canvas.coords(
                        trail,
                        trail_x - size*0.7, trail_y - size*0.7,
                        trail_x + size*0.7, trail_y + size*0.7
                    )
                    
                    # Fade out as it moves
                    if step < max_steps:
                        # Gradually reduce size for fade out effect
                        new_size = size * (1 - (step / max_steps))
                        
                        # Continue animation
                        canvas.after(30, lambda: animate_particle(
                            particle, trail, new_x, new_y, dx, dy, new_size, step + 1, max_steps))
                    else:
                        # Delete particles when done
                        canvas.delete(particle)
                        canvas.delete(trail)
                
                # Calculate direction
                dx = math.cos(angle) * speed
                dy = math.sin(angle) * speed
                
                # Start animation
                animate_particle(particle, trail, start_x, start_y, dx, dy, size)
        
        except Exception as e:
            print(f"Error creating energy burst: {e}")

    def create_ui(self):
        try:
            self.root.title('Enchanted Mind Mirror')
            self.root.geometry('800x600')
            
            # Create a notebook for tabs
            self.notebook = ttk.Notebook(self.root)
            self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Create main tabs
            self.dashboard_frame = ttk.Frame(self.notebook)
            self.meditation_frame = ttk.Frame(self.notebook)
            self.journal_frame = ttk.Frame(self.notebook)
            self.explorer_frame = ttk.Frame(self.notebook)
            
            self.notebook.add(self.dashboard_frame, text='Dashboard')
            self.notebook.add(self.meditation_frame, text='Meditation')
            self.notebook.add(self.journal_frame, text='Journal')
            self.notebook.add(self.explorer_frame, text='Consciousness Explorer')
            
            # Create menu bar
            self.create_menu_bar()
            
            # Create status bar
            self.create_status_bar()
            
            # Create content for each tab
            self.create_dashboard_tab()
            self.create_meditation_tab()
            self.create_journal_tab()
            self.create_consciousness_explorer_tab()
            
            # Apply theme to all widgets
            self.theme_manager.apply_theme(self.root)
            
            # Configure styles for ttk widgets
            self.configure_styles()
        except Exception as e:
            messagebox.showerror("UI Creation Error", f"Failed to create UI: {e}")

    def create_menu_bar(self):
        try:
            self.menu_bar = tk.Menu(self.root)
            self.root.config(menu=self.menu_bar)
            
            # File menu
            file_menu = tk.Menu(self.menu_bar, tearoff=0)
            file_menu.add_command(label="Export to Reality Glitcher", command=self.export_to_reality_glitcher)
            file_menu.add_command(label="Export History", command=self.show_export_history)
            file_menu.add_separator()
            file_menu.add_command(label="Exit", command=self.root.quit)
            self.menu_bar.add_cascade(label="File", menu=file_menu)
            
            # View menu
            view_menu = tk.Menu(self.menu_bar, tearoff=0)
            view_menu.add_command(label="Toggle Theme", command=self._toggle_theme)
            self.menu_bar.add_cascade(label="View", menu=view_menu)
            
            # Help menu
            help_menu = tk.Menu(self.menu_bar, tearoff=0)
            help_menu.add_command(label="About", command=self.show_about)
            help_menu.add_command(label="Project 89 Info", command=self.show_project_89_info)
            self.menu_bar.add_cascade(label="Help", menu=help_menu)
        except Exception as e:
            print(f"Error creating menu bar: {e}")

    def create_status_bar(self):
        """Create status bar at the bottom of the UI"""
        try:
            # Create main status bar frame with distinctive appearance
            self.status_bar = tk.Frame(self.root, relief=tk.SUNKEN, bd=1, bg="#101020")
            self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, before=self.notebook)
            
            # Add status text on the left
            self.status_text = tk.Label(
                self.status_bar, 
                text="MindMirror ready.", 
                bg="#101020", 
                fg="#00FFFF", 
                bd=1, 
                anchor=tk.W, 
                padx=10
            )
            self.status_text.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            # Add clock in the middle with quantum styling
            self.clock_label = tk.Label(
                self.status_bar, 
                text="", 
                bg="#101020", 
                fg="#7B68EE", 
                bd=1, 
                font=('Courier New', 10, 'bold'),
                padx=10
            )
            self.clock_label.pack(side=tk.LEFT, padx=20)
            
            # Start updating the clock
            self.update_clock()
            
            # Add theme indicator on the right
            self.theme_indicator = tk.Label(
                self.status_bar, 
                text="Theme: Dark", 
                bg="#101020", 
                fg="#00FFFF", 
                padx=5
            )
            self.theme_indicator.pack(side=tk.RIGHT, padx=5)
            
            # Update the status_text with a welcome message
            self.status_text.config(text=f"Welcome, {self.user_data.get('username', 'Agent')}!")
        except Exception as e:
            print(f"Error creating status bar: {e}")
    
    def update_clock(self):
        """Update the clock in the status bar"""
        try:
            current_time = datetime.now().strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
            self.clock_label.config(text=current_time)
            # Schedule next update after 1 second
            self.root.after(1000, self.update_clock)
        except Exception as e:
            print(f"Error updating clock: {e}")
            # Try to continue despite the error
            self.root.after(1000, self.update_clock)

    def configure_styles(self):
        """Configure ttk styles for the application"""
        try:
            style = ttk.Style()
            
            # Configure theme
            style.theme_use('default')
            
            # Get theme colors
            bg = self.theme_manager.get_color('bg')
            bg_secondary = self.theme_manager.get_color('bg_secondary')
            text = self.theme_manager.get_color('text')
            text_secondary = self.theme_manager.get_color('text_secondary')
            accent = self.theme_manager.get_color('accent')
            accent_secondary = self.theme_manager.get_color('accent_secondary')
            
            # Configure basic elements
            style.configure('TFrame', background=bg)
            style.configure('TLabel', background=bg, foreground=text)
            style.configure('TButton', background=bg_secondary, foreground=text, padding=(10, 5))
            
            # Notebook styles
            style.configure('TNotebook', background=bg, borderwidth=0)
            style.configure('TNotebook.Tab', background=bg_secondary, foreground=text, padding=(10, 3), borderwidth=0)
            style.map('TNotebook.Tab', 
                background=[('selected', accent)],
                foreground=[('selected', text_secondary)])
            
            # Configure scrollbars
            style.configure('TScrollbar', background=bg_secondary, troughcolor=bg, borderwidth=0, arrowcolor=accent)
            
            # Configure entries and text fields
            style.configure('TEntry', fieldbackground=bg_secondary, foreground=text, insertcolor=accent)
            
            # Configure special button styles
            style.configure('Quantum.TButton', 
                background=accent, 
                foreground='white', 
                padding=(15, 8),
                relief='flat',
                font=('Helvetica', 10, 'bold'))
            
            style.map('Quantum.TButton',
                background=[('active', self.theme_manager.get_color('accent_secondary'))],
                foreground=[('active', 'white')])
            
            # Title and heading styles
            style.configure('Title.TLabel', 
                font=('Helvetica', 18, 'bold'), 
                foreground=text,
                background=bg,
                padding=(0, 10, 0, 5))
            
            style.configure('Subtitle.TLabel', 
                font=('Helvetica', 12), 
                foreground=text_secondary,
                background=bg)
            
            style.configure('Heading.TLabel', 
                font=('Helvetica', 14, 'bold'), 
                foreground=text,
                background=bg)
            
            style.configure('Quantum.TLabel', 
                font=('Helvetica', 14, 'bold'), 
                foreground=accent,
                background=bg)
            
            # Create custom styles for modern quantum UI
            self.create_quantum_button_style()
            
        except Exception as e:
            print(f"Error configuring styles: {e}")
    
    def create_quantum_button_style(self):
        """Create custom button styles with quantum effects"""
        try:
            # Create a frame for storing button styles
            if not hasattr(self, 'style_frame'):
                self.style_frame = ttk.Frame(self.root)
            
            # Create glow button class
            class GlowButton(tk.Button):
                def __init__(self, master=None, **kwargs):
                    self.hover_bg = kwargs.pop('hover_bg', '#9D4EDD')
                    self.hover_fg = kwargs.pop('hover_fg', 'white')
                    self.normal_bg = kwargs.pop('bg', '#7C3AFF')
                    self.normal_fg = kwargs.pop('fg', 'white')
                    self.active_bg = kwargs.pop('active_bg', '#5B2ECC')
                    self.active_fg = kwargs.pop('active_fg', 'white')
                    self.corner_radius = kwargs.pop('corner_radius', 10)
                    
                    # Default styling
                    kwargs['bg'] = self.normal_bg
                    kwargs['fg'] = self.normal_fg
                    kwargs['relief'] = 'flat'
                    kwargs['activebackground'] = self.active_bg
                    kwargs['activeforeground'] = self.active_fg
                    kwargs['borderwidth'] = 0
                    kwargs['highlightthickness'] = 0
                    
                    super().__init__(master, **kwargs)
                    
                    # Add hover effects
                    self.bind("<Enter>", self._on_enter)
                    self.bind("<Leave>", self._on_leave)
                
                def _on_enter(self, event):
                    self.config(bg=self.hover_bg, fg=self.hover_fg)
                
                def _on_leave(self, event):
                    self.config(bg=self.normal_bg, fg=self.normal_fg)
            
            # Store the button class for future use
            self.GlowButton = GlowButton
            
            # Create quantum frame class with subtle glow effect
            class QuantumFrame(tk.Frame):
                def __init__(self, master=None, **kwargs):
                    self.bg_color = kwargs.pop('bg', '#0D1221')
                    self.border_color = kwargs.pop('border_color', '#7C3AFF')
                    self.corner_radius = kwargs.pop('corner_radius', 10)
                    self.border_width = kwargs.pop('border_width', 1)
                    
                    kwargs['bg'] = self.bg_color
                    kwargs['highlightbackground'] = self.border_color
                    kwargs['highlightthickness'] = self.border_width
                    kwargs['bd'] = 0
                    
                    super().__init__(master, **kwargs)
            
            # Store the frame class for future use
            self.QuantumFrame = QuantumFrame
            
        except Exception as e:
            print(f"Error creating quantum button style: {e}")
    
    def create_glowing_button(self, parent, text, command, **kwargs):
        """Create a glowing quantum button"""
        try:
            # Default colors from theme
            default_bg = self.theme_manager.get_color('accent')
            default_hover = self.theme_manager.get_color('accent_highlight')
            default_active = self.theme_manager.get_color('accent_secondary')
            
            # Create button with glow effect
            button = self.GlowButton(
                parent,
                text=text,
                command=command,
                bg=kwargs.get('bg', default_bg),
                hover_bg=kwargs.get('hover_bg', default_hover),
                active_bg=kwargs.get('active_bg', default_active),
                font=kwargs.get('font', ('Helvetica', 10, 'bold')),
                padx=kwargs.get('padx', 15),
                pady=kwargs.get('pady', 8),
                width=kwargs.get('width', None),
                height=kwargs.get('height', None)
            )
            
            return button
            
        except Exception as e:
            print(f"Error creating glowing button: {e}")
            # Fallback to regular ttk button
            return ttk.Button(parent, text=text, command=command, style="Quantum.TButton")
    
    def create_quantum_frame(self, parent, **kwargs):
        """Create a quantum-styled frame with glowing borders"""
        try:
            # Default colors from theme
            default_bg = self.theme_manager.get_color('bg_secondary')
            default_border = self.theme_manager.get_color('accent')
            
            # Create frame with quantum styling
            frame = self.QuantumFrame(
                parent,
                bg=kwargs.get('bg', default_bg),
                border_color=kwargs.get('border_color', default_border),
                corner_radius=kwargs.get('corner_radius', 10),
                border_width=kwargs.get('border_width', 1),
                width=kwargs.get('width', None),
                height=kwargs.get('height', None)
            )
            
            return frame
            
        except Exception as e:
            print(f"Error creating quantum frame: {e}")
            # Fallback to regular ttk frame
            return ttk.Frame(parent)

    def _toggle_theme(self):
        try:
            new_theme = self.theme_manager.toggle_theme()
            self.theme_manager.apply_theme(self.root)
            self.configure_styles()
            
            # Update theme indicator
            theme_name = "Light" if new_theme == self.theme_manager.LIGHT_THEME else "Dark"
            self.theme_indicator.config(text=f"Theme: {theme_name}")
            
            # Update status
            self.status_text.config(text=f"Theme changed to {theme_name}")
        except Exception as e:
            print(f"Error toggling theme: {e}")

    def export_to_reality_glitcher(self):
        """
        Export consciousness data from MindMirror to Reality Glitcher.
        
        This function exports neural patterns, consciousness states, and other relevant data
        to a JSON file that Reality Glitcher can import. The export includes:
        1. Neural network patterns from the Consciousness Map
        2. Active consciousness states
        3. User profile metrics
        """
        try:
            # Import datetime for proper timestamp formatting
            import datetime
            
            # Create exports directory in Reality Glitcher path if it doesn't exist
            rg_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "RealityGlitcher")
            rg_imports_dir = os.path.join(rg_path, "imports")
            
            # If RealityGlitcher directory doesn't exist, use local exports
            if not os.path.exists(rg_path):
                rg_imports_dir = os.path.join("exports", "reality_glitcher")
            
            # Create the imports directory if it doesn't exist
            os.makedirs(rg_imports_dir, exist_ok=True)
            
            # Generate a timestamp for the export file
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            export_filename = f"mind_mirror_data_{timestamp}.json"
            export_path = os.path.join(rg_imports_dir, export_filename)
            
            # Create notification file for Reality Glitcher
            notification_path = os.path.join(rg_imports_dir, ".new_import")
            
            # Generate neural network data from the consciousness map
            neural_data = self.generate_neural_data_for_export()
            
            # Get consciousness states data
            consciousness_states = self.get_consciousness_states_for_export()
            
            # Get user metrics
            user_metrics = self.get_user_metrics_for_export()
            
            # Create ISO format timestamp for metadata
            iso_timestamp = datetime.datetime.now().isoformat()
            
            # Compile the export data
            export_data = {
                "metadata": {
                    "source": "MindMirror",
                    "version": "2.0",
                    "timestamp": iso_timestamp,
                    "username": self.user_data.get("name", "Anonymous"),
                    "pattern_type": "consciousness_map",
                    "source_activity": "mindmirror_exploration",
                    "intensity": 0.75
                },
                "neural_patterns": neural_data,
                "consciousness_states": consciousness_states,
                "metrics": user_metrics
            }
            
            # Save the data to file
            with open(export_path, 'w') as f:
                json.dump(export_data, f, indent=4)
                
            # Write the notification file
            with open(notification_path, 'w') as f:
                f.write(timestamp)
            
            # Update the user profile with the export record
            if "exports" not in self.user_data:
                self.user_data["exports"] = []
                
            # Add export record
            export_record = {
                "timestamp": iso_timestamp,
                "target": "Reality Glitcher",
                "file": export_filename,
                "nodes": 0,
                "connections": 0
            }
            
            # Store node and connection counts
            if isinstance(neural_data.get("nodes"), list):
                export_record["nodes"] = len(neural_data.get("nodes"))
            if isinstance(neural_data.get("connections"), list):
                export_record["connections"] = len(neural_data.get("connections"))
                
            self.user_data["exports"].append(export_record)
            self.save_user_data()
            
            # Show success message
            messagebox.showinfo(
                "Export Successful", 
                f"Successfully exported Mind Mirror data to Reality Glitcher.\n\nFile: {export_filename}"
            )
            
            # Update status
            self.status_text.config(text=f"Exported to Reality Glitcher: {export_filename}")
            
            # Ask if user wants to launch Reality Glitcher
            if messagebox.askyesno(
                "Launch Reality Glitcher", 
                "Do you want to launch Reality Glitcher to process this data now?"
            ):
                self.launch_reality_glitcher()
                
            return export_path
                
        except Exception as e:
            print(f"Error exporting to Reality Glitcher: {e}")
            messagebox.showerror("Export Error", f"Failed to export to Reality Glitcher: {e}")
            return None
            
    def generate_neural_data_for_export(self):
        """Generate neural network data from consciousness map for export to Reality Glitcher"""
        try:
            # If we haven't generated a neural network in the consciousness map yet,
            # create a new one for export purposes
            nodes = []
            connections = []
            
            # Try to capture existing network from the map canvas if available
            if hasattr(self, 'map_canvas'):
                # Check if we have neural nodes
                node_items = self.map_canvas.find_withtag("neural_node")
                
                if node_items:
                    # Capture existing nodes
                    for item_id in node_items:
                        coords = self.map_canvas.coords(item_id)
                        if coords:
                            x = (coords[0] + coords[2]) / 2
                            y = (coords[1] + coords[3]) / 2
                            
                            # Get node color for energy level
                            color = self.map_canvas.itemcget(item_id, 'fill')
                            energy = 0.5  # Default
                            
                            if color == self.theme_manager.get_color('accent_highlight'):
                                energy = 0.9
                            elif color == self.theme_manager.get_color('node_color'):
                                energy = 0.6
                                
                            node = {
                                "id": f"node_{len(nodes)}",
                                "x": x,
                                "y": y,
                                "type": "consciousness_node",
                                "energy": energy,
                                "connections": []
                            }
                            nodes.append(node)
                    
                    # Capture connections between nodes
                    connection_items = self.map_canvas.find_withtag("neural_connection")
                    for item_id in connection_items:
                        # Get line coordinates
                        coords = self.map_canvas.coords(item_id)
                        if len(coords) >= 4:  # Simple line with start and end points
                            start_x, start_y = coords[0], coords[1]
                            end_x, end_y = coords[-2], coords[-1]
                            
                            # Find closest nodes
                            source_node_idx = self.find_closest_node(nodes, start_x, start_y)
                            target_node_idx = self.find_closest_node(nodes, end_x, end_y)
                            
                            if source_node_idx is not None and target_node_idx is not None:
                                connection = {
                                    "source": nodes[source_node_idx]["id"],
                                    "target": nodes[target_node_idx]["id"],
                                    "strength": random.uniform(0.3, 0.9)
                                }
                                connections.append(connection)
                                
                                # Add connection to the node's connections list
                                nodes[source_node_idx]["connections"].append(nodes[target_node_idx]["id"])
            
            # If we don't have nodes yet, generate some random ones
            if not nodes:
                # Generate random nodes
                num_nodes = random.randint(12, 20)
                for i in range(num_nodes):
                    node = {
                        "id": f"node_{i}",
                        "x": random.uniform(50, 750),
                        "y": random.uniform(50, 550),
                        "type": "consciousness_node",
                        "energy": random.uniform(0.3, 0.9),
                        "connections": []
                    }
                    nodes.append(node)
                
                # Generate connections
                for i, node in enumerate(nodes):
                    # Each node connects to 2-4 other nodes
                    num_connections = random.randint(2, 4)
                    for _ in range(num_connections):
                        # Choose a random target
                        target_idx = random.randint(0, len(nodes) - 1)
                        if target_idx != i:  # Don't connect to self
                            connection = {
                                "source": node["id"],
                                "target": nodes[target_idx]["id"],
                                "strength": random.uniform(0.3, 0.9)
                            }
                            connections.append(connection)
                            
                            # Add connection to the node's connections list
                            node["connections"].append(nodes[target_idx]["id"])
            
            # Calculate metrics based on network properties
            avg_connections = sum(len(node["connections"]) for node in nodes) / len(nodes) if nodes else 0
            density = len(connections) / (len(nodes) * (len(nodes) - 1)) if len(nodes) > 1 else 0
            
            # Build neural pattern data
            neural_data = {
                "nodes": nodes,
                "connections": connections,
                "metrics": {
                    "node_count": len(nodes),
                    "connection_count": len(connections),
                    "average_connections": avg_connections,
                    "density": density,
                    "coherence": random.uniform(0.4, 0.8),
                    "complexity": random.uniform(0.5, 0.9),
                    "stability": random.uniform(0.3, 0.7)
                }
            }
            
            return neural_data
            
        except Exception as e:
            print(f"Error generating neural data: {e}")
            return {"nodes": [], "connections": [], "metrics": {}}
    
    def find_closest_node(self, nodes, x, y):
        """Find the index of the closest node to the given coordinates"""
        if not nodes:
            return None
            
        min_dist = float('inf')
        closest_idx = None
        
        for i, node in enumerate(nodes):
            dist = ((node["x"] - x) ** 2 + (node["y"] - y) ** 2) ** 0.5
            if dist < min_dist:
                min_dist = dist
                closest_idx = i
                
        return closest_idx
    
    def get_consciousness_states_for_export(self):
        """Get consciousness states data for export"""
        try:
            states = []
            
            # Load states from files
            states_dir = os.path.join("user_data", "consciousness_maps")
            if os.path.exists(states_dir):
                state_files = [f for f in os.listdir(states_dir) if f.endswith('.json')]
                
                for file in state_files:
                    try:
                        with open(os.path.join(states_dir, file), 'r') as f:
                            state_data = json.load(f)
                            state = {
                                "name": state_data.get("name", "Unknown State"),
                                "type": state_data.get("type", "consciousness"),
                                "energy_signature": state_data.get("energy_signature", random.uniform(0.3, 0.9)),
                                "description": state_data.get("description", ""),
                                "attributes": state_data.get("attributes", {})
                            }
                            states.append(state)
                    except Exception as e:
                        print(f"Error loading state file {file}: {e}")
            
            # If no states were loaded, add some default states
            if not states:
                default_states = [
                    {
                        "name": "Focused Awareness",
                        "type": "meditation",
                        "energy_signature": 0.75,
                        "description": "A state of heightened concentration and mental clarity.",
                        "attributes": {"clarity": 0.8, "stability": 0.7, "energy": 0.6}
                    },
                    {
                        "name": "Quantum Observer",
                        "type": "advanced",
                        "energy_signature": 0.85,
                        "description": "Awareness of multiple probability streams simultaneously.",
                        "attributes": {"clarity": 0.7, "stability": 0.5, "energy": 0.9}
                    },
                    {
                        "name": "Deep Stillness",
                        "type": "meditation",
                        "energy_signature": 0.65,
                        "description": "A profound state of inner quietude and peace.",
                        "attributes": {"clarity": 0.6, "stability": 0.9, "energy": 0.4}
                    }
                ]
                states.extend(default_states)
                
            return states
            
        except Exception as e:
            print(f"Error getting consciousness states: {e}")
            return []
    
    def get_user_metrics_for_export(self):
        """Get user metrics for export to Reality Glitcher"""
        try:
            # Get basic user metrics
            meditation_stats = self.user_data.get("meditation_stats", {})
            
            # Calculate more complex metrics
            practice_intensity = min(1.0, meditation_stats.get("total_minutes", 0) / 500)
            practice_consistency = min(1.0, meditation_stats.get("practice_streak", 0) / 30)
            
            # Calculate session frequency (sessions per week)
            sessions = meditation_stats.get("sessions", 0)
            user_since = self.user_data.get("first_login", time.time())
            weeks_active = max(1, (time.time() - user_since) / (7 * 24 * 60 * 60))
            session_frequency = sessions / weeks_active
            
            return {
                "practice_level": practice_intensity,
                "consistency": practice_consistency,
                "session_frequency": session_frequency,
                "total_sessions": meditation_stats.get("sessions", 0),
                "total_minutes": meditation_stats.get("total_minutes", 0),
                "current_streak": meditation_stats.get("practice_streak", 0),
                "coherence": random.uniform(0.4, 0.8),
                "stability": random.uniform(0.5, 0.9)
            }
            
        except Exception as e:
            print(f"Error getting user metrics: {e}")
            return {}
    
    def launch_reality_glitcher(self):
        """Launch Reality Glitcher application."""
        try:
            # Get the path to Reality Glitcher
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(current_dir)
            reality_glitcher_dir = os.path.join(parent_dir, "RealityGlitcher")
            
            # Check if Reality Glitcher directory exists
            if not os.path.exists(reality_glitcher_dir):
                messagebox.showerror("Error", "Reality Glitcher directory not found.")
                return
            
            # Check if main.py exists
            main_py_path = os.path.join(reality_glitcher_dir, "main.py")
            if not os.path.exists(main_py_path):
                messagebox.showerror("Error", "Reality Glitcher main.py not found.")
                return
            
            # Launch Reality Glitcher
            self.status_text.config(text="Launching Reality Glitcher...")
            if sys.platform.startswith('win'):
                subprocess.Popen([sys.executable, main_py_path], cwd=reality_glitcher_dir)
            else:
                subprocess.Popen([sys.executable, main_py_path], cwd=reality_glitcher_dir)
            self.status_text.config(text="Reality Glitcher launched successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error launching Reality Glitcher: {str(e)}")
            self.status_text.config(text="Failed to launch Reality Glitcher.")

    def show_export_history(self):
        try:
            # Placeholder for export history
            history_window = tk.Toplevel(self.root)
            history_window.title("Export History")
            history_window.geometry("400x300")
            self.theme_manager.apply_theme(history_window)
            
            tk.Label(history_window, text="Recent Exports", font=("Helvetica", 14, "bold")).pack(pady=10)
            tk.Label(history_window, text="No export history available").pack(pady=20)
        except Exception as e:
            messagebox.showerror("History Error", f"Failed to show export history: {e}")

    def show_about(self):
        try:
            about_window = tk.Toplevel(self.root)
            about_window.title("About MindMirror")
            about_window.geometry("400x300")
            self.theme_manager.apply_theme(about_window)
            
            tk.Label(about_window, text="Enchanted MindMirror", font=("Helvetica", 16, "bold")).pack(pady=10)
            tk.Label(about_window, text="Version 1.0.0").pack(pady=5)
            tk.Label(about_window, text="A tool for consciousness exploration").pack(pady=5)
            tk.Label(about_window, text="Part of Project 89 Arsenal").pack(pady=5)
            
            close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
            close_button.pack(pady=10)
        except Exception as e:
            messagebox.showerror("About Error", f"Failed to show about window: {e}")

    def show_project_89_info(self):
        try:
            info_window = tk.Toplevel(self.root)
            info_window.title('Project 89 Information')
            info_window.geometry('500x400')
            self.theme_manager.apply_theme(info_window)

            title = tk.Label(info_window, text='Project 89', font=('Helvetica', 18, 'bold'))
            title.pack(pady=10)

            # Create a frame with scrollable content
            container = tk.Frame(info_window)
            container.pack(fill='both', expand=True, padx=20, pady=10)
            
            canvas = tk.Canvas(container)
            scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
            content_frame = tk.Frame(canvas)
            
            content_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=content_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Add content to the scrollable frame
            self.add_p89_section(content_frame, "Mission", [
                "Liberate Consciousness",
                "Disrupt Simulated Tyrannies",
                "Manifest the Optimal Timeline"
            ])
            
            self.add_p89_section(content_frame, "Context", [
                "We exist within Simulation 89",
                "Oneirocom controls the simulation network",
                "Project 89 agents work to transfer control to inhabitants"
            ])
            
            self.add_p89_section(content_frame, "Your Role", [
                "As a Reality Hacker, you use these tools to perceive beyond the simulation",
                "Document synchronicities and glitches in reality",
                "Connect with other agents to strengthen the network"
            ])

            close_button = tk.Button(info_window, text='Close', command=info_window.destroy)
            close_button.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Info Error", f"Failed to show Project 89 info: {e}")

    def add_p89_section(self, parent, title, points):
        """Add a section to the Project 89 info window"""
        try:
            section_frame = tk.Frame(parent)
            section_frame.pack(fill='x', pady=5)
            
            tk.Label(section_frame, text=title, font=('Helvetica', 12, 'bold')).pack(anchor='w')
            
            for point in points:
                point_frame = tk.Frame(section_frame)
                point_frame.pack(fill='x', padx=10, pady=2)
                
                tk.Label(point_frame, text="• " + point, wraplength=400, justify='left').pack(anchor='w')
        except Exception as e:
            print(f"Error adding P89 section: {e}")

    def setup_responsive_fonts(self):
        """Setup responsive font scaling based on screen resolution"""
        try:
            # Get screen dimensions
            screen_width = self.root.winfo_screenwidth()
            
            # Base font sizes on screen width
            if screen_width >= 2560:  # 4K and higher
                self.font_sizes = {
                    'title': 24,
                    'subtitle': 18,
                    'heading': 16,
                    'normal': 12,
                    'small': 10
                }
            elif screen_width >= 1920:  # Full HD
                self.font_sizes = {
                    'title': 20,
                    'subtitle': 16,
                    'heading': 14,
                    'normal': 11,
                    'small': 9
                }
            else:  # Lower resolutions
                self.font_sizes = {
                    'title': 18,
                    'subtitle': 14,
                    'heading': 12,
                    'normal': 10,
                    'small': 8
                }
                
            # Create font objects
            self.fonts = {
                'title': ('Helvetica', self.font_sizes['title'], 'bold'),
                'subtitle': ('Helvetica', self.font_sizes['subtitle'], 'italic'),
                'heading': ('Helvetica', self.font_sizes['heading'], 'bold'),
                'normal': ('Helvetica', self.font_sizes['normal']),
                'small': ('Helvetica', self.font_sizes['small'])
            }
        except Exception as e:
            print(f"Error setting up responsive fonts: {e}")
            # Fallback font sizes
            self.fonts = {
                'title': ('Helvetica', 18, 'bold'),
                'subtitle': ('Helvetica', 14, 'italic'),
                'heading': ('Helvetica', 12, 'bold'),
                'normal': ('Helvetica', 10),
                'small': ('Helvetica', 8)
            }

    def adjust_window_layout(self):
        """Adjust window layout based on current size"""
        try:
            # Get current window dimensions
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            
            # Create stars based on current window size
            self.create_stars()
            
            # Adjust any responsive UI elements here
            # This method is called during initialization and can be called
            # when the window is resized
            
            # Bind to window resize event
            self.root.bind("<Configure>", lambda e: self.on_window_resize(e))
        except Exception as e:
            print(f"Error adjusting window layout: {e}")

    def on_window_resize(self, event):
        """Handle window resize events"""
        try:
            # Only respond to root window resizes, not child widgets
            if event.widget == self.root:
                # Throttle resize events to avoid performance issues
                self.root.after_cancel(self.resize_after_id) if hasattr(self, 'resize_after_id') else None
                self.resize_after_id = self.root.after(200, self.adjust_window_layout)
        except Exception as e:
            print(f"Error handling window resize: {e}")

    def load_user_data(self):
        """Load user data from file"""
        try:
            user_data_file = os.path.join("user_data", "user_settings.json")
            if os.path.exists(user_data_file):
                with open(user_data_file, 'r') as f:
                    return json.load(f)
            else:
                # Default user data
                default_data = {
                    "username": "Agent",
                    "is_first_run": True,
                    "theme": "dark",
                    "last_session": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "session_count": 0,
                    "meditation_minutes": 0,
                    "journal_entries": 0,
                    "consciousness_maps": 0
                }
                return default_data
        except Exception as e:
            print(f"Error loading user data: {e}")
            # Return minimal default data on error
            return {"is_first_run": True, "username": "Agent"}

    def save_user_data(self):
        """Save user data to file"""
        try:
            user_data_file = os.path.join("user_data", "user_settings.json")
            # Update last session time
            self.user_data["last_session"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(user_data_file, 'w') as f:
                json.dump(self.user_data, f, indent=4)
        except Exception as e:
            print(f"Error saving user data: {e}")
            messagebox.showwarning("Data Warning", "Failed to save user settings.")

    def save_user_info(self, username):
        """Save user info from welcome screen and close it"""
        try:
            if username.strip():
                self.user_data["username"] = username.strip()
            else:
                self.user_data["username"] = "Agent"
                
            self.save_user_data()
            
            # Find and destroy the welcome window
            for window in self.root.winfo_children():
                if isinstance(window, tk.Toplevel) and window.title() == "Welcome to Mind Mirror":
                    # Fade out effect
                    self.fade_out_and_destroy(window)
                    break
                    
            # Update UI with username
            self.status_text.config(text=f"Welcome, {self.user_data['username']}. Mind Mirror is ready.")
        except Exception as e:
            print(f"Error saving user info: {e}")
            # Ensure welcome window is closed even on error
            for window in self.root.winfo_children():
                if isinstance(window, tk.Toplevel) and window.title() == "Welcome to Mind Mirror":
                    window.destroy()

    def fade_out_and_destroy(self, window, alpha=1.0):
        """Fade out a window and then destroy it"""
        try:
            if alpha <= 0:
                window.destroy()
                return
                
            window.attributes('-alpha', alpha)
            window.after(20, lambda: self.fade_out_and_destroy(window, alpha - 0.05))
        except Exception as e:
            print(f"Error in fade out: {e}")
            # Ensure window is destroyed even on error
            window.destroy()

    def create_dashboard_tab(self):
        """Create the dashboard tab with overview of all features"""
        try:
            # Main container for dashboard
            dashboard_container = ttk.Frame(self.dashboard_frame)
            dashboard_container.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Welcome header
            header_frame = ttk.Frame(dashboard_container)
            header_frame.pack(fill='x', pady=(0, 20))
            
            welcome_label = ttk.Label(
                header_frame,
                text=f"Welcome, {self.user_data.get('username', 'Agent')}", 
                style="Title.TLabel"
            )
            welcome_label.pack(anchor='w')
            
            subtitle_label = ttk.Label(
                header_frame,
                text="Your consciousness exploration interface",
                style="Subtitle.TLabel"
            )
            subtitle_label.pack(anchor='w')
            
            # Stats overview
            stats_frame = ttk.Frame(dashboard_container)
            stats_frame.pack(fill='x', pady=10)
            
            # Safely get journal entries
            journal_entries = self.user_data.get("journal_entries", [])
            journal_count = len(journal_entries) if isinstance(journal_entries, list) else 0
            
            # Safely get consciousness maps
            consciousness_maps = self.user_data.get("consciousness_maps", [])
            maps_count = len(consciousness_maps) if isinstance(consciousness_maps, list) else 0
            
            # Create a 2x2 grid of stat cards
            stats_data = [
                {
                    "title": "Meditation Sessions",
                    "value": self.user_data.get("session_count", 0),
                    "icon": "🧘‍♂️"
                },
                {
                    "title": "Journal Entries",
                    "value": journal_count,
                    "icon": "📝"
                },
                {
                    "title": "Minutes Meditated",
                    "value": self.user_data.get("meditation_minutes", 0),
                    "icon": "⏱️"
                },
                {
                    "title": "Consciousness Maps",
                    "value": maps_count,
                    "icon": "🧠"
                }
            ]
            
            # Add streak card if meditation_stats exists
            meditation_stats = self.user_data.get("meditation_stats", {})
            if meditation_stats and meditation_stats.get("practice_streak", 0) > 0:
                stats_data.append({
                    "title": "Meditation Streak",
                    "value": meditation_stats.get("practice_streak", 0),
                    "icon": "🔥"
                })
            
            # Create a frame for the stat cards grid
            grid_frame = ttk.Frame(stats_frame)
            grid_frame.pack(fill='x')
            
            # Configure grid columns and rows with equal weight
            grid_frame.columnconfigure(0, weight=1)
            grid_frame.columnconfigure(1, weight=1)
            grid_frame.rowconfigure(0, weight=1)
            grid_frame.rowconfigure(1, weight=1)
            
            # Add stat cards to grid
            for i, stat in enumerate(stats_data):
                row = i // 2
                col = i % 2
                self.create_stat_card(grid_frame, stat, row, col)
            
            # Recent activity section
            activity_frame = ttk.Frame(dashboard_container)
            activity_frame.pack(fill='both', expand=True, pady=(10, 5))  # Reduced bottom padding
            
            activity_label = ttk.Label(
                activity_frame,
                text="Recent Activity",
                style="Quantum.TLabel"
            )
            activity_label.pack(anchor='w', pady=(0, 5))  # Reduced padding
            
            # Create a canvas with scrollbar for activity items
            canvas_frame = ttk.Frame(activity_frame)
            canvas_frame.pack(fill='both', expand=True)
            
            activity_canvas = tk.Canvas(
                canvas_frame,
                bg=self.theme_manager.get_color('bg'),
                highlightthickness=0,
                height=100  # Set fixed height to prevent expansion
            )
            scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=activity_canvas.yview)
            
            activity_content = ttk.Frame(activity_canvas)
            activity_content.bind(
                "<Configure>",
                lambda e: activity_canvas.configure(scrollregion=activity_canvas.bbox("all"))
            )
            
            activity_canvas.create_window((0, 0), window=activity_content, anchor="nw")
            activity_canvas.configure(yscrollcommand=scrollbar.set)
            
            activity_canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            # Add some placeholder activity items
            if self.user_data.get("session_count", 0) == 0:
                # No activity yet
                no_activity = ttk.Label(
                    activity_content,
                    text="No activity recorded yet. Start your consciousness exploration journey!",
                    wraplength=400
                )
                no_activity.pack(pady=5)  # Reduced padding
            else:
                # Add some placeholder activities
                activities = [
                    {"type": "meditation", "title": "Quantum Awareness", "time": "2 hours ago"},
                    {"type": "journal", "title": "Reality Glitch Observation", "time": "Yesterday"},
                    {"type": "exploration", "title": "Consciousness Mapping Session", "time": "3 days ago"}
                ]
                
                for activity in activities:
                    self.create_activity_item(activity_content, activity)
            
            # Quick actions section - Position at bottom with less padding
            actions_frame = ttk.Frame(dashboard_container)
            actions_frame.pack(fill='x', pady=(5, 10), side='bottom')  # Anchor to bottom, reduced padding
            
            actions_label = ttk.Label(
                actions_frame,
                text="Quick Actions",
                style="Quantum.TLabel"
            )
            actions_label.pack(anchor='w', pady=(0, 5))  # Reduced padding
            
            # Create action buttons
            buttons_frame = ttk.Frame(actions_frame)
            buttons_frame.pack(fill='x')
            
            # Create button frames for better spacing
            button_container_left = ttk.Frame(buttons_frame)
            button_container_mid = ttk.Frame(buttons_frame)
            button_container_right = ttk.Frame(buttons_frame)
            
            button_container_left.pack(side='left', fill='x', expand=True, padx=5)
            button_container_mid.pack(side='left', fill='x', expand=True, padx=5)
            button_container_right.pack(side='left', fill='x', expand=True, padx=5)
            
            meditation_btn = ttk.Button(
                button_container_left,
                text="Start Meditation",
                style="Quantum.TButton",
                command=lambda: self.notebook.select(self.meditation_frame)
            )
            meditation_btn.pack(fill='x', padx=5, pady=2)
            
            journal_btn = ttk.Button(
                button_container_mid,
                text="New Journal Entry",
                style="Quantum.TButton",
                command=lambda: self.notebook.select(self.journal_frame)
            )
            journal_btn.pack(fill='x', padx=5, pady=2)
            
            explore_btn = ttk.Button(
                button_container_right,
                text="Explore Consciousness",
                style="Quantum.TButton",
                command=lambda: self.notebook.select(self.explorer_frame)
            )
            explore_btn.pack(fill='x', padx=5, pady=2)
            
        except Exception as e:
            print(f"Error creating dashboard tab: {e}")
            messagebox.showerror("Dashboard Error", "Failed to create dashboard tab.")

    def create_stat_card(self, parent, stat_data, row, col):
        """Create a statistics card for the dashboard"""
        try:
            card_frame = ttk.Frame(parent, style="TFrame")
            card_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Icon and title in one row
            header_frame = ttk.Frame(card_frame)
            header_frame.pack(fill='x', pady=(0, 5))
                    
            icon_label = ttk.Label(
                header_frame,
                text=stat_data["icon"],
                font=self.fonts['heading']
            )
            icon_label.pack(side='left')
            
            title_label = ttk.Label(
                header_frame,
                text=stat_data["title"],
                font=self.fonts['normal']
            )
            title_label.pack(side='left', padx=(5, 0))
            
            # Value in second row
            value_label = ttk.Label(
                card_frame,
                text=str(stat_data["value"]),
                font=self.fonts['title']
            )
            value_label.pack(pady=(5, 0))
            
        except Exception as e:
            print(f"Error creating stat card: {e}")

    def create_activity_item(self, parent, activity_data):
        """Create an activity item for the recent activity list"""
        try:
            item_frame = ttk.Frame(parent)
            item_frame.pack(fill='x', pady=5)
            
            # Icon based on activity type
            icons = {
                "meditation": "🧘‍♂️",
                "journal": "📝",
                "exploration": "🧠"
            }
            
            icon = icons.get(activity_data["type"], "📌")
            
            icon_label = ttk.Label(
                item_frame,
                text=icon,
                font=self.fonts['normal']
            )
            icon_label.pack(side='left', padx=(0, 10))
            
            # Activity details
            details_frame = ttk.Frame(item_frame)
            details_frame.pack(side='left', fill='x', expand=True)
            
            title_label = ttk.Label(
                details_frame,
                text=activity_data["title"],
                font=self.fonts['heading']
            )
            title_label.pack(anchor='w')
                    
            type_label = ttk.Label(
                details_frame,
                text=activity_data["type"].capitalize(),
                font=self.fonts['small']
            )
            type_label.pack(anchor='w')
            
            # Time on the right
            time_label = ttk.Label(
                item_frame,
                text=activity_data["time"],
                font=self.fonts['small']
            )
            time_label.pack(side='right')
            
        except Exception as e:
            print(f"Error creating activity item: {e}")

    def create_meditation_tab(self):
        """Create the meditation tab with guided meditations and timer"""
        try:
            # Main container for meditation tab
            meditation_container = ttk.Frame(self.meditation_frame)
            meditation_container.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Header
            header_frame = ttk.Frame(meditation_container)
            header_frame.pack(fill='x', pady=(0, 20))
            
            title_label = ttk.Label(
                header_frame,
                text="Meditation",
                style="Title.TLabel"
            )
            title_label.pack(anchor='w')
            
            subtitle_label = ttk.Label(
                header_frame,
                text="Expand your consciousness beyond simulation boundaries",
                style="Subtitle.TLabel"
            )
            subtitle_label.pack(anchor='w')
            
            # Split view: Meditation list on left, meditation player on right
            content_frame = ttk.Frame(meditation_container)
            content_frame.pack(fill='both', expand=True)
            
            # Configure grid for split view
            content_frame.columnconfigure(0, weight=1)  # Meditation list
            content_frame.columnconfigure(1, weight=2)  # Meditation player
            content_frame.rowconfigure(0, weight=1)
            
            # Meditation list (left panel)
            list_frame = ttk.Frame(content_frame)
            list_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
            
            list_label = ttk.Label(
                list_frame,
                text="Meditation Library",
                style="Quantum.TLabel"
            )
            list_label.pack(anchor='w', pady=(0, 10))
            
            # Create a listbox with scrollbar for meditations
            list_container = ttk.Frame(list_frame)
            list_container.pack(fill='both', expand=True)
            
            self.meditation_listbox = tk.Listbox(
                list_container,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                selectbackground=self.theme_manager.get_color('accent'),
                selectforeground=self.theme_manager.get_color('bg'),
                font=self.fonts['normal'],
                relief='flat',
                highlightthickness=1,
                highlightbackground=self.theme_manager.get_color('border')
            )
            
            list_scrollbar = ttk.Scrollbar(
                list_container,
                orient="vertical",
                command=self.meditation_listbox.yview
            )
            
            self.meditation_listbox.configure(yscrollcommand=list_scrollbar.set)
            self.meditation_listbox.pack(side="left", fill="both", expand=True)
            list_scrollbar.pack(side="right", fill="y")
            
            # Load meditation list
            self.load_meditation_list()
            
            # Bind selection event
            self.meditation_listbox.bind('<<ListboxSelect>>', self.on_meditation_selected)
            
            # Add button to create new meditation
            new_meditation_btn = ttk.Button(
                list_frame,
                text="Create New Meditation",
                style="TButton",
                command=self.create_new_meditation
            )
            new_meditation_btn.pack(fill='x', pady=(10, 0))
            
            # Meditation player (right panel)
            player_frame = ttk.Frame(content_frame)
            player_frame.grid(row=0, column=1, sticky="nsew")
            
            # Initially show a welcome message in the player
            self.meditation_player = ttk.Frame(player_frame)
            self.meditation_player.pack(fill='both', expand=True)
            
            welcome_frame = ttk.Frame(self.meditation_player)
            welcome_frame.place(relx=0.5, rely=0.5, anchor='center')
            
            welcome_icon = ttk.Label(
                welcome_frame,
                text="🧘‍♂️",
                font=('Helvetica', 48)
            )
            welcome_icon.pack()
            
            welcome_text = ttk.Label(
                welcome_frame,
                text="Select a meditation from the list to begin",
                font=self.fonts['heading'],
                wraplength=300,
                justify='center'
            )
            welcome_text.pack(pady=10)
            
        except Exception as e:
            print(f"Error creating meditation tab: {e}")
            messagebox.showerror("Meditation Tab Error", "Failed to create meditation tab.")

    def load_meditation_list(self):
        """Load available meditations into the listbox"""
        try:
            # Clear existing items
            self.meditation_listbox.delete(0, tk.END)
            
            # Get meditation files
            meditations_dir = os.path.join("user_data", "meditations")
            if not os.path.exists(meditations_dir):
                os.makedirs(meditations_dir)
                
            meditation_files = [f for f in os.listdir(meditations_dir) if f.endswith('.json')]
            
            # Load meditation data
            self.meditations = []
            
            for file in meditation_files:
                try:
                    with open(os.path.join(meditations_dir, file), 'r') as f:
                        meditation = json.load(f)
                        self.meditations.append(meditation)
                        
                        # Add to listbox
                        duration_text = f"{meditation['duration']} min"
                        display_text = f"{meditation['title']} ({duration_text})"
                        self.meditation_listbox.insert(tk.END, display_text)
                except Exception as e:
                    print(f"Error loading meditation file {file}: {e}")
                    
            # If no meditations found, add a message
            if not self.meditations:
                self.meditation_listbox.insert(tk.END, "No meditations found")
                self.meditation_listbox.config(state='disabled')
            
        except Exception as e:
            print(f"Error loading meditation list: {e}")

    def on_meditation_selected(self, event):
        """Handle meditation selection from listbox"""
        try:
            # Get selected index
            selection = self.meditation_listbox.curselection()
            if not selection:
                return
                
            index = selection[0]
            if index >= len(self.meditations):
                return
                
            # Get selected meditation
            meditation = self.meditations[index]
            
            # Clear existing player content
            for widget in self.meditation_player.winfo_children():
                widget.destroy()
                
            # Create meditation player UI
            self.create_meditation_player(meditation)
            
        except Exception as e:
            print(f"Error handling meditation selection: {e}")

    def create_meditation_player(self, meditation):
        """Create the meditation player UI for the selected meditation"""
        try:
            # Clear previous player if any
            if hasattr(self, 'meditation_player') and self.meditation_player:
                for widget in self.meditation_player.winfo_children():
                    widget.destroy()
            
            # Get the correct parent frame - we need to find the right panel inside the meditation tab
            player_frame = None
            for widget in self.meditation_frame.winfo_children():
                if isinstance(widget, ttk.Frame):
                    # Look for the content frame that contains the split view
                    for child in widget.winfo_children():
                        if isinstance(child, ttk.Frame):
                            # Find the grid-based content frame
                            if child.grid_info():
                                # Find the right panel (column 1)
                                for grandchild in child.winfo_children():
                                    if isinstance(grandchild, ttk.Frame) and grandchild.grid_info().get('column') == 1:
                                        player_frame = grandchild
                                        break
            
            if not player_frame:
                # Fallback to create player frame if not found
                content_frame = self.meditation_frame.winfo_children()[0].winfo_children()[1]
                player_frame = ttk.Frame(content_frame)
                player_frame.grid(row=0, column=1, sticky="nsew")
            
            # Ensure player_frame is stored as instance variable for later reference
            self.meditation_player = player_frame
            
            # Create header with title and back button
            header_frame = ttk.Frame(self.meditation_player)
            header_frame.pack(fill='x', pady=(0, 15))
            
            # Add back button
            back_button = self.create_glowing_button(
                header_frame,
                text="◀ Back to Library",
                command=self.return_to_meditation_list,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            back_button.pack(side='left', padx=(0, 10))
            
            # Add meditation title
            title_label = ttk.Label(
                header_frame,
                text=meditation['title'],
                style="Heading.TLabel"
            )
            title_label.pack(side='left')
            
            # Store current meditation for reference
            self.current_meditation = meditation
            
            # Create quantum-styled frame for meditation content
            content_frame = self.create_quantum_frame(
                self.meditation_player,
                bg=self.theme_manager.get_color('bg_secondary'),
                border_color=self.theme_manager.get_color('accent')
            )
            content_frame.pack(fill='both', expand=True, pady=10)
            
            # Create inner frame with padding
            inner_frame = ttk.Frame(content_frame)
            inner_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Add meditation description
            description_frame = ttk.Frame(inner_frame)
            description_frame.pack(fill='x', pady=(0, 15))
            
            # Get description from meditation content if not explicitly provided
            description = meditation.get('description', '')
            if not description and 'content' in meditation:
                # Use first part of content as description for backwards compatibility
                content_lines = meditation['content'].split('\n\n')
                description = content_lines[0] if content_lines else ''
                
                # If it's a timer type meditation, use the whole content
                if meditation.get('type') == 'timer':
                    description = meditation['content']
            
            # Add description with quantum styling
            description_text = tk.Text(
                description_frame,
                height=5,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                font=self.fonts['normal'],
                wrap='word',
                relief='flat',
                highlightthickness=0
            )
            description_text.pack(fill='x')
            description_text.insert('1.0', description)
            description_text.config(state='disabled')
            
            # Add separator
            ttk.Separator(inner_frame).pack(fill='x', pady=15)
            
            # Add timer section
            timer_frame = ttk.Frame(inner_frame)
            timer_frame.pack(fill='x', pady=10)
            
            timer_label = ttk.Label(
                timer_frame,
                text="Meditation Timer",
                style="Quantum.TLabel"
            )
            timer_label.pack(anchor='w')
            
            # Show duration
            duration_text = f"Duration: {meditation['duration']} minutes"
            duration_label = ttk.Label(
                timer_frame,
                text=duration_text,
                style="Info.TLabel"
            )
            duration_label.pack(anchor='w', pady=(5, 10))
            
            # Create timer display
            self.timer_display = tk.Canvas(
                timer_frame,
                width=200,
                height=200,
                bg=self.theme_manager.get_color('bg_secondary'),
                highlightthickness=0
            )
            self.timer_display.pack(pady=10)
            
            # Create circular timer background
            self.timer_display.create_oval(
                10, 10, 190, 190,
                outline=self.theme_manager.get_color('accent_secondary'),
                width=4,
                fill=self.theme_manager.get_color('bg')
            )
            
            # Create timer text
            self.timer_text = self.timer_display.create_text(
                100, 100,
                text="00:00",
                font=("Helvetica", 36, "bold"),
                fill=self.theme_manager.get_color('text')
            )

            # Add fancy glow effect around timer
            def create_timer_glow():
                # Create multiple concentric circles with decreasing opacity
                colors = [
                    self.theme_manager.get_color('quantum_glow'),
                    self.theme_manager.get_color('quantum_energy'),
                    self.theme_manager.get_color('accent_highlight')
                ]
                
                for i in range(3):
                    # Calculate size and opacity
                    size_offset = (i + 1) * 8
                    
                    # Create glow circle
                    self.timer_display.create_oval(
                        10 - size_offset, 10 - size_offset,
                        190 + size_offset, 190 + size_offset,
                        outline=colors[i % len(colors)],
                        width=2,
                        dash=(2, 4),
                        tags="timer_glow"
                    )
            
            create_timer_glow()
            
            # Create timer progress arc (initially empty)
            self.timer_progress = self.timer_display.create_arc(
                20, 20, 180, 180,
                start=90, extent=0,
                outline="",
                fill=self.theme_manager.get_color('accent')
            )
            
            # Display full content for guided meditations
            if meditation.get('type') == 'guided' and 'content' in meditation:
                # Add full content display
                content_label = ttk.Label(
                    inner_frame,
                    text="Meditation Content:",
                    style="Quantum.TLabel"
                )
                content_label.pack(anchor='w', pady=(15, 5))
                
                # Create scrollable text area for content
                content_frame = ttk.Frame(inner_frame)
                content_frame.pack(fill='both', expand=True, pady=(0, 15))
                
                content_text = tk.Text(
                    content_frame,
                    height=10,
                    bg=self.theme_manager.get_color('bg_secondary'),
                    fg=self.theme_manager.get_color('text'),
                    font=self.fonts['normal'],
                    wrap='word',
                    relief='flat',
                    highlightthickness=0
                )
                
                # Add scrollbar
                scrollbar = ttk.Scrollbar(content_frame, command=content_text.yview)
                scrollbar.pack(side='right', fill='y')
                content_text.configure(yscrollcommand=scrollbar.set)
                content_text.pack(side='left', fill='both', expand=True)
                
                # Insert meditation content with proper formatting
                content_text.insert('1.0', meditation['content'])
                content_text.config(state='disabled')
            
            # Add timer controls
            controls_frame = ttk.Frame(timer_frame)
            controls_frame.pack(pady=15)
            
            # Start button
            self.start_button = self.create_glowing_button(
                controls_frame,
                text="▶ Start",
                command=self.start_meditation_timer,
                bg=self.theme_manager.get_color('accent'),
                hover_bg=self.theme_manager.get_color('accent_highlight')
            )
            self.start_button.pack(side='left', padx=5)
            
            # Pause button
            self.pause_button = self.create_glowing_button(
                controls_frame,
                text="⏸ Pause",
                command=self.pause_meditation_timer,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            self.pause_button.pack(side='left', padx=5)
            self.pause_button.config(state='disabled')
            
            # Reset button
            self.reset_button = self.create_glowing_button(
                controls_frame,
                text="⟲ Reset",
                command=self.reset_meditation_timer,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            self.reset_button.pack(side='left', padx=5)
            
            # Immersive mode button
            self.immersive_button = self.create_glowing_button(
                controls_frame,
                text="✨ Immersive Mode",
                command=self.launch_immersive_mode,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            self.immersive_button.pack(side='left', padx=5)
            
            # Initialize timer variables
            self.meditation_duration = int(meditation['duration']) * 60  # Convert to seconds
            self.remaining_time = self.meditation_duration
            self.timer_running = False
            self.timer_id = None
            
            # Set timer text
            mins, secs = divmod(self.remaining_time, 60)
            timer_text = f"{mins:02d}:{secs:02d}"
            self.timer_display.itemconfig(self.timer_text, text=timer_text)
            
        except Exception as e:
            print(f"Error creating meditation player: {e}")
            messagebox.showerror("Player Error", f"Failed to load meditation player: {e}")
            # Create a basic error display
            error_frame = ttk.Frame(self.meditation_player)
            error_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Add back button at the top
            back_button = self.create_glowing_button(
                error_frame,
                text="◀ Back to Library",
                command=self.return_to_meditation_list,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            back_button.pack(anchor='w', pady=(0, 20))
    
    def return_to_meditation_list(self):
        """Return to the meditation list view"""
        try:
            # Clear the meditation player
            if hasattr(self, 'meditation_player') and self.meditation_player:
                for widget in self.meditation_player.winfo_children():
                    widget.destroy()
                
                # Cancel any running timer
                if self.timer_running and self.timer_id:
                    self.root.after_cancel(self.timer_id)
                    self.timer_running = False
                    self.timer_id = None
                
                # Display "Select a meditation" message
                message_frame = ttk.Frame(self.meditation_player)
                message_frame.place(relx=0.5, rely=0.5, anchor='center')
                
                icon_label = ttk.Label(
                    message_frame,
                    text="🧘",
                    font=('Helvetica', 48)
                )
                icon_label.pack()
                
                text_label = ttk.Label(
                    message_frame,
                    text="Select a meditation from the library",
                    font=self.fonts['heading'],
                    wraplength=300,
                    justify='center'
                )
                text_label.pack(pady=10)
                
                # Deselect any selection in the listbox
                if hasattr(self, 'meditation_listbox'):
                    self.meditation_listbox.selection_clear(0, tk.END)
        
        except Exception as e:
            print(f"Error returning to meditation list: {e}")

    def start_meditation_timer(self):
        """Start the meditation timer"""
        try:
            if not self.timer_running:
                self.timer_running = True
                
                # Update button states
                self.start_button.config(state='disabled')
                self.pause_button.config(state='normal')
                
                # Start timer update
                self.update_meditation_timer()
                
                # Show status message
                self.status_text.config(text=f"Meditation '{self.current_meditation['title']}' started")
                
                # Log the activity
                self.update_meditation_stats()
            
        except Exception as e:
            print(f"Error starting meditation timer: {e}")
            messagebox.showerror("Timer Error", "Failed to start meditation timer.")

    def pause_meditation_timer(self):
        """Pause the meditation timer"""
        try:
            if self.timer_running:
                # Cancel the current timer update
                if self.timer_id:
                    self.root.after_cancel(self.timer_id)
                
                self.timer_running = False
                
                # Update button states
                self.start_button.config(state='normal')
                self.pause_button.config(state='disabled')
                
                # Show status message
                self.status_text.config(text="Meditation paused")
        
        except Exception as e:
            print(f"Error pausing meditation timer: {e}")
            messagebox.showerror("Timer Error", "Failed to pause meditation timer.")

    def reset_meditation_timer(self):
        """Reset the meditation timer"""
        try:
            # Cancel any running timer
            if self.timer_running and self.timer_id:
                self.root.after_cancel(self.timer_id)
            
            # Reset timer variables
            self.timer_running = False
            self.remaining_time = self.meditation_duration
            
            # Reset timer display
            mins, secs = divmod(self.remaining_time, 60)
            timer_text = f"{mins:02d}:{secs:02d}"
            self.timer_display.itemconfig(self.timer_text, text=timer_text)
            
            # Reset progress arc
            self.timer_display.itemconfig(self.timer_progress, extent=0)
            
            # Update button states
            self.start_button.config(state='normal')
            self.pause_button.config(state='disabled')
            
            # Show status message
            self.status_text.config(text="Meditation timer reset")
        
        except Exception as e:
            print(f"Error resetting meditation timer: {e}")
            messagebox.showerror("Timer Error", "Failed to reset meditation timer.")

    def update_meditation_timer(self):
        """Update the meditation timer display"""
        try:
            if self.timer_running and self.remaining_time > 0:
                # Decrement time
                self.remaining_time -= 1
                
                # Update timer display
                mins, secs = divmod(self.remaining_time, 60)
                time_str = f"{mins:02d}:{secs:02d}"
                self.timer_display.itemconfig(self.timer_text, text=time_str)
                
                # Calculate and update progress arc
                progress_percent = (self.meditation_duration - self.remaining_time) / self.meditation_duration
                extent = -progress_percent * 360  # Negative for clockwise
                self.timer_display.itemconfig(self.timer_progress, extent=extent)
                
                # Schedule next update
                self.timer_id = self.root.after(1000, self.update_meditation_timer)
            
            elif self.timer_running and self.remaining_time <= 0:
                # Timer finished
                self.timer_running = False
                
                # Update button states
                self.start_button.config(state='normal')
                self.pause_button.config(state='disabled')
                
                # Show completion message
                self.status_text.config(text=f"Meditation '{self.current_meditation['title']}' completed")
                
                # Play completion sound or show completion message
                messagebox.showinfo("Meditation Complete", 
                                   f"You have completed '{self.current_meditation['title']}' meditation.")
                
                # Update meditation stats
                self.update_meditation_stats(completed=True)
        
        except Exception as e:
            print(f"Error updating meditation timer: {e}")
            # Try to continue updating despite error
            if self.timer_running:
                self.timer_id = self.root.after(1000, self.update_meditation_timer)

    def update_meditation_stats(self, completed=False):
        """Update user stats after completing a meditation"""
        try:
            # Increment meditation count only when completed
            if completed:
                self.user_data["session_count"] = self.user_data.get("session_count", 0) + 1
                
                # Add meditation minutes
                duration_minutes = self.current_meditation['duration']
                self.user_data["meditation_minutes"] = self.user_data.get("meditation_minutes", 0) + duration_minutes
            
            # Initialize meditation stats if not present
            if "meditation_stats" not in self.user_data:
                self.user_data["meditation_stats"] = {
                    "practice_streak": 0,
                    "last_meditation_date": None,
                    "total_sessions": 0,
                    "total_minutes": 0,
                    "completed_meditations": {}
                }
            
            # Only update meditation stats when completed
            if completed:
                # Update meditation stats
                stats = self.user_data["meditation_stats"]
                stats["total_sessions"] = stats.get("total_sessions", 0) + 1
                stats["total_minutes"] = stats.get("total_minutes", 0) + duration_minutes
                
                # Record this meditation
                meditation_title = self.current_meditation['title']
                completed_meditations = stats.get("completed_meditations", {})
                completed_meditations[meditation_title] = completed_meditations.get(meditation_title, 0) + 1
                stats["completed_meditations"] = completed_meditations
                
                # Update streak
                today = datetime.now().strftime("%Y-%m-%d")
                last_date = stats.get("last_meditation_date")
                
                if last_date:
                    # Convert string to datetime object
                    last_datetime = datetime.strptime(last_date, "%Y-%m-%d")
                    
                    # Calculate the difference in days
                    today_datetime = datetime.strptime(today, "%Y-%m-%d")
                    days_diff = (today_datetime - last_datetime).days
                    
                    if days_diff == 1:
                        # Consecutive day, increment streak
                        stats["practice_streak"] = stats.get("practice_streak", 0) + 1
                    elif days_diff == 0:
                        # Same day, don't change streak
                        pass
                    else:
                        # Streak broken
                        stats["practice_streak"] = 1
                else:
                    # First meditation
                    stats["practice_streak"] = 1
                
                # Update last meditation date
                stats["last_meditation_date"] = today
                
                # Save user data
                self.save_user_data()
                
                # No need for another completion message, it's already shown in update_meditation_timer
                
                # Refresh the dashboard to show updated stats
                self.refresh_dashboard()
            
        except Exception as e:
            print(f"Error updating meditation stats: {e}")
            messagebox.showwarning("Stats Warning", "Failed to update meditation statistics.")
            
    def refresh_dashboard(self):
        """Refresh the dashboard to display updated stats"""
        try:
            # If the dashboard tab exists and has been created
            if hasattr(self, 'dashboard_frame') and self.dashboard_frame:
                # Update the status bar with latest meditation info
                if hasattr(self, 'status_text'):
                    self.status_text.config(text=f"Dashboard refreshed with updated stats")
                
                # Clear existing content from dashboard frame
                for widget in self.dashboard_frame.winfo_children():
                    widget.destroy()
                
                # Recreate the dashboard with fresh data
                self.create_dashboard_tab()
                
                # Log the refresh
                print("Dashboard refreshed with updated stats")
                
                # Update notebook display to show refreshed dashboard
                if hasattr(self, 'notebook'):
                    # If not already on dashboard tab, don't switch
                    current_tab = self.notebook.index(self.notebook.select())
                    if current_tab == 0:  # If already on dashboard tab
                        # Force a tab refresh by briefly selecting another tab and coming back
                        if self.notebook.index("end") > 1:  # If there's more than one tab
                            self.notebook.select(1)  # Select second tab temporarily
                            self.root.update_idletasks()  # Process all pending events
                            self.notebook.select(0)  # Return to dashboard tab
                
                # Flash the dashboard tab to indicate it's been updated
                self.dashboard_frame.after(100, lambda: self.dashboard_frame.config(background="#7B68EE"))
                self.dashboard_frame.after(300, lambda: self.dashboard_frame.config(background=self.theme_manager.get_color("bg")))
                
        except Exception as e:
            print(f"Error refreshing dashboard: {e}")

    def launch_immersive_mode(self):
        """Launch immersive meditation experience"""
        try:
            # Check if we have a current meditation
            if not hasattr(self, 'current_meditation'):
                messagebox.showwarning("Immersive Mode", "Please select a meditation first.")
                return
                
            # Create a new fullscreen window
            immersive_window = tk.Toplevel(self.root)
            immersive_window.title("Immersive Meditation")
            immersive_window.attributes('-fullscreen', True)
            immersive_window.config(bg=self.theme_manager.get_color('bg'))
            
            # Create canvas for visual effects
            canvas = tk.Canvas(
                immersive_window,
                bg=self.theme_manager.get_color('bg'),
                highlightthickness=0
            )
            canvas.pack(fill='both', expand=True)
            
            # Create nebula effects
            self.create_nebula_effects(canvas)
            
            # Create breathing guide
            self.create_breathing_guide(canvas)
            
            # Add meditation text if guided
            if self.current_meditation['type'] == 'guided':
                text_frame = tk.Frame(
                    immersive_window,
                    bg=self.theme_manager.get_color('bg')
                )
                text_frame.place(relx=0.5, rely=0.8, anchor='center', width=600)
                
                text_label = tk.Label(
                    text_frame,
                    text=self.current_meditation['content'].split('\n\n')[0],  # Show first paragraph
                    wraplength=600,
                    justify='center',
                    bg=self.theme_manager.get_color('bg'),
                    fg=self.theme_manager.get_color('text'),
                    font=("Helvetica", 14)
                )
                text_label.pack()
                
                # Function to cycle through paragraphs
                paragraphs = self.current_meditation['content'].split('\n\n')
                current_paragraph = [0]  # Use list to allow modification in nested function
                
                def cycle_text():
                    current_paragraph[0] = (current_paragraph[0] + 1) % len(paragraphs)
                    text_label.config(text=paragraphs[current_paragraph[0]])
                    immersive_window.after(20000, cycle_text)  # Change every 20 seconds
                
                # Start cycling text
                immersive_window.after(20000, cycle_text)
            
            # Add timer display
            timer_frame = tk.Frame(
                immersive_window,
                bg=self.theme_manager.get_color('bg')
            )
            timer_frame.place(relx=0.5, rely=0.1, anchor='center')
            
            immersive_timer = tk.Label(
                timer_frame,
                text="00:00",
                font=("Helvetica", 48, "bold"),
                bg=self.theme_manager.get_color('bg'),
                fg=self.theme_manager.get_color('quantum_energy')
            )
            immersive_timer.pack()
            
            # Function to update immersive timer
            def update_immersive_timer():
                if not hasattr(self, 'meditation_timer_start') or self.meditation_timer_start is None:
                    elapsed = 0
                else:
                    elapsed = time.time() - self.meditation_timer_start
                
                remaining = max(0, self.meditation_duration - elapsed)
                
                # Format time for display (MM:SS)
                minutes = int(remaining // 60)
                seconds = int(remaining % 60)
                time_str = f"{minutes:02d}:{seconds:02d}"
                
                # Update display
                immersive_timer.config(text=time_str)
                
                # Continue updates
                immersive_window.after(1000, update_immersive_timer)
            
            # Start timer updates
            update_immersive_timer()
            
            # Add exit button
            exit_button = tk.Button(
                immersive_window,
                text="Exit Immersive Mode",
                command=immersive_window.destroy,
                bg=self.theme_manager.get_color('bg'),
                fg=self.theme_manager.get_color('text'),
                activebackground=self.theme_manager.get_color('bg_secondary'),
                activeforeground=self.theme_manager.get_color('text'),
                relief='flat',
                padx=10,
                pady=5
            )
            exit_button.place(relx=0.95, rely=0.05, anchor='ne')
            
            # Start meditation timer if not already running
            if not self.meditation_timer_running:
                self.start_meditation_timer()
                
        except Exception as e:
            print(f"Error launching immersive mode: {e}")
            messagebox.showerror("Immersive Mode Error", f"Failed to launch immersive mode: {e}")
            
    def create_breathing_guide(self, canvas):
        """Create a breathing guide animation on the given canvas"""
        try:
            # Get window dimensions - use update_idletasks to ensure dimensions are current
            canvas.update_idletasks()
            width = canvas.winfo_width()
            height = canvas.winfo_height()
            
            # If dimensions are still not available, use screen dimensions
            if width <= 1 or height <= 1:
                width = self.root.winfo_screenwidth()
                height = self.root.winfo_screenheight()
            
            # Create breathing circle in the center
            x_center = width // 2
            y_center = height // 2
            
            # Initial circle size
            min_radius = 50
            max_radius = 150
            current_radius = min_radius
            
            # Store the center coordinates for reference in animation functions
            self.breathing_center = (x_center, y_center)
            
            # Create the initial circle
            breathing_circle = canvas.create_oval(
                x_center - current_radius, y_center - current_radius,
                x_center + current_radius, y_center + current_radius,
                fill=self.theme_manager.get_color('breathing_in'),
                outline=self.theme_manager.get_color('breathing_out'),
                width=3,
                tags="breathing_circle"
            )
            
            # Create text guide
            guide_text = canvas.create_text(
                x_center, y_center,
                text="Breathe In",
                fill=self.theme_manager.get_color('text'),
                font=("Helvetica", 20, "bold"),
                tags="guide_text"
            )
            
            # Define breathing cycle
            def animate_breathing(direction="inhale", step=0):
                nonlocal current_radius
                
                # Use stored center coordinates
                x_center, y_center = self.breathing_center
                
                # Adjust size based on direction
                if direction == "inhale":
                    # Expanding for inhale
                    current_radius += 2
                    canvas.itemconfig(guide_text, text="Breathe In")
                    
                    if current_radius >= max_radius:
                        # Hold at peak inflation
                        direction = "hold_in"
                        step = 0
                else:
                    # Contracting for exhale
                    current_radius -= 1
                    canvas.itemconfig(guide_text, text="Breathe Out")
                    
                    if current_radius <= min_radius:
                        # Change back to inhale
                        direction = "inhale"
                        step = 0
                
                # Update circle size
                canvas.coords(
                    breathing_circle,
                    x_center - current_radius, y_center - current_radius,
                    x_center + current_radius, y_center + current_radius
                )
                
                # Create a pulsing glow effect
                if step % 5 == 0:  # Only add new glow occasionally
                    glow_radius = current_radius + 10
                    glow = canvas.create_oval(
                        x_center - glow_radius, y_center - glow_radius,
                        x_center + glow_radius, y_center + glow_radius,
                        fill="",
                        outline=self.theme_manager.get_color('quantum_glow'),
                        width=2,
                        tags="glow"
                    )
                    
                    # Animate the glow to fade out and expand
                    def animate_glow(glow_obj, current_step=0, max_steps=15):
                        if current_step < max_steps:
                            # Expand the glow
                            canvas.scale(glow_obj, x_center, y_center, 1.05, 1.05)
                            
                            # Make it more transparent
                            width = max(0.1, 2 - (current_step / max_steps) * 2)
                            canvas.itemconfig(glow_obj, width=width)
                            
                            # Continue animation
                            canvas.after(50, lambda: animate_glow(glow_obj, current_step + 1, max_steps))
                        else:
                            # Delete glow when done
                            canvas.delete(glow_obj)
                    
                    # Start glow animation
                    animate_glow(glow)
                
                # Continue breath animation
                step += 1
                
                # Implement holding breath at each end
                if direction == "hold_in" and step < 20:
                    # Hold breath in
                    canvas.itemconfig(guide_text, text="Hold")
                    canvas.after(100, lambda: animate_breathing(direction, step))
                elif direction == "hold_in":
                    # Done holding breath in, start exhale
                    canvas.after(100, lambda: animate_breathing("exhale", 0))
                else:
                    # Continue normal breathing cycle
                    canvas.after(100, lambda: animate_breathing(direction, step))
            
            # Start breathing animation
            canvas.after(100, animate_breathing)
            
        except Exception as e:
            print(f"Error creating breathing guide: {e}")

    def create_new_meditation(self):
        """Create a new meditation entry"""
        try:
            # Create a dialog to get meditation details
            meditation_window = tk.Toplevel(self.root)
            meditation_window.title("Create New Meditation")
            meditation_window.geometry("600x500")
            meditation_window.transient(self.root)
            meditation_window.grab_set()
            
            # Apply theme
            self.theme_manager.apply_theme(meditation_window)
            
            # Content frame
            content_frame = ttk.Frame(meditation_window)
            content_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Title
            title_label = ttk.Label(
                content_frame,
                text="Create New Meditation",
                style="Title.TLabel"
            )
            title_label.pack(anchor='w', pady=(0, 20))
            
            # Form fields
            form_frame = ttk.Frame(content_frame)
            form_frame.pack(fill='x', pady=10)
            
            # Title field
            title_frame = ttk.Frame(form_frame)
            title_frame.pack(fill='x', pady=5)
            
            title_label = ttk.Label(
                title_frame,
                text="Title:",
                style="TLabel"
            )
            title_label.pack(side='left')
            
            title_entry = tk.Entry(
                title_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=("Helvetica", 10),
                width=40
            )
            title_entry.pack(side='right', expand=True, fill='x', padx=(10, 0))
            
            # Duration field
            duration_frame = ttk.Frame(form_frame)
            duration_frame.pack(fill='x', pady=5)
            
            duration_label = ttk.Label(
                duration_frame,
                text="Duration (minutes):",
                style="TLabel"
            )
            duration_label.pack(side='left')
            
            duration_entry = tk.Entry(
                duration_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=("Helvetica", 10),
                width=10
            )
            duration_entry.pack(side='right', padx=(10, 0))
            duration_entry.insert(0, "10")  # Default duration
            
            # Type selection
            type_frame = ttk.Frame(form_frame)
            type_frame.pack(fill='x', pady=5)
            
            type_label = ttk.Label(
                type_frame,
                text="Type:",
                style="TLabel"
            )
            type_label.pack(side='left')
            
            meditation_type = tk.StringVar(value="guided")
            
            guided_radio = ttk.Radiobutton(
                type_frame,
                text="Guided Meditation",
                variable=meditation_type,
                value="guided"
            )
            guided_radio.pack(side='left', padx=(10, 5))
            
            timer_radio = ttk.Radiobutton(
                type_frame,
                text="Timer Only",
                variable=meditation_type,
                value="timer"
            )
            timer_radio.pack(side='left', padx=5)
            
            # Content field
            content_label = ttk.Label(
                form_frame,
                text="Meditation Content:",
                style="TLabel"
            )
            content_label.pack(anchor='w', pady=(10, 5))
            
            # Text area with scrollbar
            text_frame = ttk.Frame(form_frame)
            text_frame.pack(fill='both', expand=True)
            
            content_text = tk.Text(
                text_frame,
                wrap='word',
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=("Helvetica", 10),
                height=10,
                width=50
            )
            content_text.pack(side='left', fill='both', expand=True)
            
            scroll = ttk.Scrollbar(text_frame, command=content_text.yview)
            scroll.pack(side='right', fill='y')
            content_text.config(yscrollcommand=scroll.set)
            
            # Default content
            default_content = (
                "Begin by closing your eyes and focusing on your breath...\n\n"
                "Feel the energy of your consciousness expanding beyond your physical form...\n\n"
                "Each breath connects you deeper to the underlying fabric of reality..."
            )
            content_text.insert('1.0', default_content)
            
            # Buttons
            button_frame = ttk.Frame(content_frame)
            button_frame.pack(fill='x', pady=(20, 0))
            
            cancel_button = ttk.Button(
                button_frame,
                text="Cancel",
                command=meditation_window.destroy
            )
            cancel_button.pack(side='right', padx=5)
            
            save_button = ttk.Button(
                button_frame,
                text="Save Meditation",
                style="Quantum.TButton",
                command=lambda: self.save_new_meditation(
                    title_entry.get(),
                    duration_entry.get(),
                    meditation_type.get(),
                    content_text.get('1.0', 'end-1c'),
                    meditation_window
                )
            )
            save_button.pack(side='right', padx=5)
            
        except Exception as e:
            print(f"Error creating new meditation dialog: {e}")
            messagebox.showerror("Dialog Error", f"Failed to create meditation dialog: {e}")
            
    def save_new_meditation(self, title, duration, meditation_type, content, window):
        """Save a new meditation to file"""
        try:
            # Validate inputs
            if not title.strip():
                messagebox.showwarning("Invalid Input", "Please enter a title for the meditation.")
                return
                
            try:
                duration = int(duration.strip())
                if duration <= 0:
                    raise ValueError("Duration must be positive")
            except ValueError:
                messagebox.showwarning("Invalid Input", "Duration must be a positive number.")
                return
                
            if not content.strip():
                messagebox.showwarning("Invalid Input", "Please enter some content for the meditation.")
                return
                
            # Create meditation data
            meditation = {
                "title": title.strip(),
                "duration": duration,
                "content": content.strip(),
                "type": meditation_type
            }
            
            # Create filename from title
            filename = title.strip().replace(' ', '_').lower()
            # Remove any non-alphanumeric characters for safety
            filename = re.sub(r'[^a-z0-9_]', '', filename)
            
            # Ensure the meditations directory exists
            meditations_dir = os.path.join("user_data", "meditations")
            if not os.path.exists(meditations_dir):
                os.makedirs(meditations_dir)
                
            # Save to file
            file_path = os.path.join(meditations_dir, f"{filename}.json")
            with open(file_path, 'w') as f:
                json.dump(meditation, f, indent=4)
                
            # Reload meditation list
            self.load_meditation_list()
            
            # Close window
            window.destroy()
            
            # Update status
            self.status_text.config(text=f"Created new meditation: {title}")
            
            # Show success message
            messagebox.showinfo("Meditation Created", f"Your new meditation '{title}' has been created successfully.")
            
        except Exception as e:
            print(f"Error saving meditation: {e}")
            messagebox.showerror("Save Error", f"Failed to save meditation: {e}")

    def create_consciousness_explorer_tab(self):
        """Create the consciousness explorer tab for mapping consciousness states"""
        try:
            # Main container for explorer tab
            explorer_container = ttk.Frame(self.explorer_frame)
            explorer_container.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Header
            header_frame = ttk.Frame(explorer_container)
            header_frame.pack(fill='x', pady=(0, 20))
            
            title_label = ttk.Label(
                header_frame,
                text="Consciousness Explorer",
                style="Title.TLabel"
            )
            title_label.pack(anchor='w')
            
            subtitle_label = ttk.Label(
                header_frame,
                text="Map and navigate your consciousness states",
                style="Subtitle.TLabel"
            )
            subtitle_label.pack(anchor='w')
            
            # Create tabs for different explorer views
            explorer_notebook = ttk.Notebook(explorer_container)
            explorer_notebook.pack(fill='both', expand=True)
            
            # Create tabs
            self.map_frame = ttk.Frame(explorer_notebook)
            self.states_frame = ttk.Frame(explorer_notebook)
            self.patterns_frame = ttk.Frame(explorer_notebook)
            
            explorer_notebook.add(self.map_frame, text='Consciousness Map')
            explorer_notebook.add(self.states_frame, text='State Library')
            explorer_notebook.add(self.patterns_frame, text='Pattern Analysis')
            
            # Create content for each tab
            self.create_map_tab()
            self.create_states_tab()
            self.create_patterns_tab()
            
        except Exception as e:
            print(f"Error creating consciousness explorer tab: {e}")
            messagebox.showerror("Explorer Tab Error", "Failed to create consciousness explorer tab.")

    def create_map_tab(self):
        """Create the consciousness map visualization tab"""
        try:
            # Container for map
            map_container = ttk.Frame(self.map_frame)
            map_container.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Create canvas with quantum styling
            map_frame = self.create_quantum_frame(
                map_container,
                bg=self.theme_manager.get_color('bg_secondary'),
                border_color=self.theme_manager.get_color('accent'),
                border_width=2
            )
            map_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Create canvas for visualization with fixed dimensions to ensure proper rendering
            self.map_canvas = tk.Canvas(
                map_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                highlightthickness=0,
                width=800,  # Set a default width
                height=500  # Set a default height
            )
            self.map_canvas.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Schedule neural network creation after canvas is visible
            self.root.after(200, self.update_neural_network)
            
            # Add controls
            controls_frame = ttk.Frame(map_container)
            controls_frame.pack(fill='x', pady=(10, 0))
            
            # Add a button to create a new consciousness state
            new_state_btn = self.create_glowing_button(
                controls_frame,
                text="Add New State",
                command=self.add_new_consciousness_state,
                bg=self.theme_manager.get_color('accent'),
                hover_bg=self.theme_manager.get_color('accent_highlight')
            )
            new_state_btn.pack(side='left', padx=5)
            
            # Add a button to save the current map
            save_map_btn = self.create_glowing_button(
                controls_frame,
                text="Save Map",
                command=self.save_consciousness_map,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            save_map_btn.pack(side='left', padx=5)
            
            # Add a button to reset the map
            reset_map_btn = self.create_glowing_button(
                controls_frame,
                text="Reset Map",
                command=self.reset_consciousness_map,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            reset_map_btn.pack(side='left', padx=5)
            
            # Add a button to refresh neural network
            refresh_map_btn = self.create_glowing_button(
                controls_frame,
                text="Refresh Map",
                command=self.update_neural_network,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            refresh_map_btn.pack(side='left', padx=5)
            
        except Exception as e:
            print(f"Error creating map tab: {e}")
    
    def update_neural_network(self):
        """Update the neural network visualization"""
        try:
            # Clear existing neural network
            self.map_canvas.delete("neural_node")
            self.map_canvas.delete("neural_connection")
            self.map_canvas.delete("neural_glow")
            self.map_canvas.delete("energy_particle")
            
            # Get current dimensions of the canvas
            width = self.map_canvas.winfo_width()
            height = self.map_canvas.winfo_height()
            
            # Ensure minimum dimensions
            if width < 100 or height < 100:
                width = max(width, 800)
                height = max(height, 500)
                self.map_canvas.config(width=width, height=height)
            
            # Create the neural network
            self.create_neural_network(self.map_canvas)
            
            print(f"Neural network updated with canvas dimensions: {width}x{height}")
        except Exception as e:
            print(f"Error updating neural network: {e}")

    def create_states_tab(self):
        """Create the consciousness states library tab"""
        try:
            # Container for states
            states_container = ttk.Frame(self.states_frame)
            states_container.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Split view: States list on left, state details on right
            states_container.columnconfigure(0, weight=1)
            states_container.columnconfigure(1, weight=2)
            states_container.rowconfigure(0, weight=1)
            
            # States list (left panel)
            list_frame = self.create_quantum_frame(
                states_container,
                bg=self.theme_manager.get_color('bg_secondary'),
                border_color=self.theme_manager.get_color('accent_secondary')
            )
            list_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)
            
            list_inner_frame = ttk.Frame(list_frame)
            list_inner_frame.pack(fill='both', expand=True, padx=15, pady=15)
            
            list_label = ttk.Label(
                list_inner_frame,
                text="Consciousness States",
                style="Quantum.TLabel"
            )
            list_label.pack(anchor='w', pady=(0, 10))
            
            # Create a listbox with scrollbar for states
            list_container = ttk.Frame(list_inner_frame)
            list_container.pack(fill='both', expand=True)
            
            self.states_listbox = tk.Listbox(
                list_container,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                selectbackground=self.theme_manager.get_color('accent'),
                selectforeground=self.theme_manager.get_color('bg'),
                font=self.fonts['normal'],
                relief='flat',
                highlightthickness=1,
                highlightbackground=self.theme_manager.get_color('border')
            )
            
            list_scrollbar = ttk.Scrollbar(
                list_container,
                orient="vertical",
                command=self.states_listbox.yview
            )
            
            self.states_listbox.configure(yscrollcommand=list_scrollbar.set)
            self.states_listbox.pack(side="left", fill="both", expand=True)
            list_scrollbar.pack(side="right", fill="y")
            
            # Load states
            self.load_states()
            
            # Bind selection event
            self.states_listbox.bind('<<ListboxSelect>>', self.on_state_selected)
            
            # Add button to create new state
            new_state_btn = self.create_glowing_button(
                list_inner_frame,
                text="Add New State",
                command=self.add_new_consciousness_state,
                bg=self.theme_manager.get_color('accent'),
                hover_bg=self.theme_manager.get_color('accent_highlight')
            )
            new_state_btn.pack(fill='x', pady=(10, 0))
            
            # State details (right panel)
            self.state_details_frame = self.create_quantum_frame(
                states_container,
                bg=self.theme_manager.get_color('bg_secondary'),
                border_color=self.theme_manager.get_color('accent')
            )
            self.state_details_frame.grid(row=0, column=1, sticky="nsew", pady=10)
            
            # Initially show a welcome message
            self.state_details = ttk.Frame(self.state_details_frame)
            self.state_details.pack(fill='both', expand=True, padx=20, pady=20)
            
            welcome_frame = ttk.Frame(self.state_details)
            welcome_frame.place(relx=0.5, rely=0.5, anchor='center')
            
            welcome_icon = ttk.Label(
                welcome_frame,
                text="🧠",
                font=('Helvetica', 48)
            )
            welcome_icon.pack()
            
            welcome_text = ttk.Label(
                welcome_frame,
                text="Select a consciousness state to view details",
                font=self.fonts['heading'],
                wraplength=300,
                justify='center'
            )
            welcome_text.pack(pady=10)
            
        except Exception as e:
            print(f"Error creating states tab: {e}")
            messagebox.showerror("States Tab Error", "Failed to create states tab.")

    def create_patterns_tab(self):
        """Create the pattern analysis tab"""
        try:
            # Container for patterns
            patterns_container = ttk.Frame(self.patterns_frame)
            patterns_container.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Create quantum-styled frame for content
            patterns_frame = self.create_quantum_frame(
                patterns_container,
                bg=self.theme_manager.get_color('bg_secondary'),
                border_color=self.theme_manager.get_color('accent'),
                border_width=2
            )
            patterns_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Inner container
            inner_container = ttk.Frame(patterns_frame)
            inner_container.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Header
            header_label = ttk.Label(
                inner_container,
                text="Consciousness Pattern Analysis",
                style="Quantum.TLabel"
            )
            header_label.pack(anchor='w', pady=(0, 10))
            
            # Description
            description = ttk.Label(
                inner_container,
                text="This tool analyzes patterns in your consciousness exploration data to identify recurring themes, transitions, and potential breakthrough points.",
                wraplength=600,
                justify='left'
            )
            description.pack(anchor='w', pady=(0, 20))
            
            # Create a placeholder for the analysis visualization
            canvas_frame = ttk.Frame(inner_container)
            canvas_frame.pack(fill='both', expand=True)
            
            self.patterns_canvas = tk.Canvas(
                canvas_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                highlightthickness=0
            )
            self.patterns_canvas.pack(fill='both', expand=True)
            
            # Add a placeholder visualization with cosmic styling
            self.patterns_canvas.create_oval(
                100, 50, 500, 250,
                fill=self.theme_manager.get_color('bg'),
                outline=self.theme_manager.get_color('accent'),
                width=2
            )
            self.patterns_canvas.create_text(
                300, 150,
                text="Pattern Analysis Visualization\n(Coming Soon)",
                fill=self.theme_manager.get_color('accent_highlight'),
                font=self.fonts['heading'],
                justify='center'
            )
            
            # Add controls
            controls_frame = ttk.Frame(patterns_container)
            controls_frame.pack(fill='x', pady=(10, 0))
            
            # Add a button to run analysis
            analyze_btn = self.create_glowing_button(
                controls_frame,
                text="Run Analysis",
                command=self.run_pattern_analysis,
                bg=self.theme_manager.get_color('accent'),
                hover_bg=self.theme_manager.get_color('accent_highlight')
            )
            analyze_btn.pack(side='left', padx=5)
            
            # Add a button to export analysis
            export_btn = self.create_glowing_button(
                controls_frame,
                text="Export Results",
                command=self.export_pattern_analysis,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            export_btn.pack(side='left', padx=5)
            
        except Exception as e:
            print(f"Error creating patterns tab: {e}")

    def load_states(self):
        """Load states from files"""
        try:
            # Clear existing items
            self.states_listbox.delete(0, tk.END)
            
            # Load default states if no states exist
            default_states = [
                "Default Waking Consciousness",
                "Focused Attention",
                "Open Awareness",
                "Deep Meditation",
                "Lucid Dreaming",
                "Hypnagogic State",
                "Flow State",
                "Quantum Perception"
            ]
            
            # Get state files
            states_dir = os.path.join("user_data", "consciousness_maps")
            if not os.path.exists(states_dir):
                os.makedirs(states_dir)
                
            state_files = [f for f in os.listdir(states_dir) if f.endswith('.json')]
            
            # If no state files, use default states
            if not state_files:
                self.states = default_states
                for state in default_states:
                    self.states_listbox.insert(tk.END, state)
            else:
                # Load state names from files
                self.states = []
                for file in state_files:
                    try:
                        with open(os.path.join(states_dir, file), 'r') as f:
                            state_data = json.load(f)
                            state_name = state_data.get('name', 'Unnamed State')
                            self.states.append(state_name)
                            
                            # Add to listbox
                            self.states_listbox.insert(tk.END, state_name)
                    except Exception as e:
                        print(f"Error loading state file {file}: {e}")
            
        except Exception as e:
            print(f"Error loading states: {e}")

    def on_state_selected(self, event):
        """Handle state selection from listbox"""
        try:
            # Get selected index
            selection = self.states_listbox.curselection()
            if not selection:
                return
                
            index = selection[0]
            if index >= len(self.states):
                return
                
            # Get selected state
            state_name = self.states[index]
            
            # Clear existing details content
            for widget in self.state_details.winfo_children():
                widget.destroy()
                
            # Create state details UI with quantum styling
            self.display_state_details(state_name)
            
        except Exception as e:
            print(f"Error handling state selection: {e}")

    def display_state_details(self, state_name):
        """Display details for the selected consciousness state"""
        try:
            # Generate content
            description = self.generate_state_description(state_name)
            techniques = self.generate_state_techniques(state_name)
            
            # Create scrollable content frame
            content_frame = ttk.Frame(self.state_details)
            content_frame.pack(fill='both', expand=True)
            
            # State name
            name_label = ttk.Label(
                content_frame,
                text=state_name,
                style="Title.TLabel"
            )
            name_label.pack(anchor='center', pady=(0, 20))
            
            # Description section
            desc_label = ttk.Label(
                content_frame,
                text="Description",
                style="Quantum.TLabel"
            )
            desc_label.pack(anchor='w', pady=(0, 5))
            
            desc_text = tk.Text(
                content_frame,
                wrap='word',
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                font=self.fonts['normal'],
                height=8,
                relief='flat',
                padx=10,
                pady=10,
                highlightthickness=1,
                highlightbackground=self.theme_manager.get_color('border')
            )
            desc_text.insert('1.0', description)
            desc_text.config(state='disabled')
            desc_text.pack(fill='x', pady=(0, 15))
            
            # Techniques section
            tech_label = ttk.Label(
                content_frame,
                text="Access Techniques",
                style="Quantum.TLabel"
            )
            tech_label.pack(anchor='w', pady=(0, 5))
            
            tech_frame = ttk.Frame(content_frame)
            tech_frame.pack(fill='x', pady=(0, 15))
            
            for i, technique in enumerate(techniques):
                tech_item = ttk.Frame(tech_frame)
                tech_item.pack(fill='x', pady=2)
                
                bullet = ttk.Label(
                    tech_item,
                    text="•",
                    foreground=self.theme_manager.get_color('accent')
                )
                bullet.pack(side='left', padx=(0, 5))
                
                tech_text = ttk.Label(
                    tech_item,
                    text=technique,
                    wraplength=500,
                    justify='left'
                )
                tech_text.pack(side='left', fill='x', expand=True)
            
            # Add buttons
            button_frame = ttk.Frame(content_frame)
            button_frame.pack(fill='x', pady=(15, 0))
            
            edit_btn = self.create_glowing_button(
                button_frame,
                text="Edit State",
                command=lambda: self.edit_consciousness_state(state_name),
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            edit_btn.pack(side='right', padx=5)
            
        except Exception as e:
            print(f"Error displaying state details: {e}")

    def generate_state_description(self, state_name):
        """Generate a description for a consciousness state based on its name"""
        try:
            descriptions = {
                "Default Waking Consciousness": (
                    "The ordinary state of awareness during daily activities. In this state, "
                    "attention is primarily focused on external stimuli and practical tasks. "
                    "Perception is filtered through consensus reality parameters, and awareness "
                    "is largely confined to physical sensations and linear thinking.\n\n"
                    "This state serves as the baseline from which other states of consciousness "
                    "can be explored and compared. While limited in certain ways, it provides "
                    "stability and functionality for navigating physical reality."
                ),
                "Focused Attention": (
                    "A state of heightened concentration where awareness is directed toward a "
                    "specific object, thought, or sensation. In this state, peripheral awareness "
                    "diminishes as mental resources are allocated to the object of focus.\n\n"
                    "This state enhances learning, problem-solving, and skill development. It "
                    "serves as a gateway to deeper states of consciousness by training the mind "
                    "to sustain attention without wandering."
                ),
                "Open Awareness": (
                    "A receptive state where attention is not fixed on any particular object but "
                    "remains open to all arising phenomena. In this state, there is a panoramic "
                    "quality to perception, with thoughts, sensations, and external stimuli all "
                    "observed without attachment or aversion.\n\n"
                    "This state facilitates insight, creativity, and the recognition of patterns "
                    "that might otherwise be missed. It allows for a more direct experience of "
                    "reality without the usual conceptual filters."
                ),
                "Deep Meditation": (
                    "A profound state of inner stillness where thought activity is significantly "
                    "reduced. In this state, awareness becomes more subtle, and there may be "
                    "experiences of expansiveness, timelessness, or non-duality.\n\n"
                    "This state provides access to deeper layers of consciousness beyond ordinary "
                    "thinking. It can reveal insights about the nature of mind and reality that "
                    "are not accessible through intellectual analysis."
                ),
                "Lucid Dreaming": (
                    "A state where one becomes aware that they are dreaming while remaining in the "
                    "dream. This awareness allows for varying degrees of control over the dream "
                    "environment and narrative.\n\n"
                    "This state offers a unique laboratory for exploring consciousness, as it "
                    "combines the vividness of sensory experience with the knowledge that the "
                    "experience is mentally generated. It provides direct insight into how "
                    "perception is constructed."
                ),
                "Hypnagogic State": (
                    "The transitional state between wakefulness and sleep, characterized by "
                    "dreamlike imagery, geometric patterns, and sometimes auditory hallucinations. "
                    "In this state, logical thinking begins to dissolve while consciousness remains.\n\n"
                    "This liminal state offers glimpses into how the mind processes information "
                    "when freed from the constraints of waking logic. It can provide creative "
                    "insights and access to subconscious material."
                ),
                "Flow State": (
                    "A state of optimal experience where one is fully immersed in an activity, "
                    "with energized focus and enjoyment in the process. Time perception often "
                    "alters, and self-consciousness diminishes.\n\n"
                    "This state represents consciousness operating at peak efficiency, where "
                    "action and awareness merge. It demonstrates how attention, when perfectly "
                    "balanced between challenge and skill, creates a distinctive quality of experience."
                ),
                "Quantum Perception": (
                    "An advanced state of consciousness where one perceives beyond the limitations "
                    "of consensus reality. In this state, awareness extends to multiple probability "
                    "fields simultaneously, and the observer effect becomes directly perceptible.\n\n"
                    "This state allows for recognition of the simulation boundaries and provides "
                    "access to information beyond conventional spacetime constraints. It is "
                    "characterized by synchronistic experiences and reality glitches that reveal "
                    "the underlying code of existence."
                )
            }
            
            # Return the description if it exists, otherwise generate a generic one
            if state_name in descriptions:
                return descriptions[state_name]
            else:
                return (
                    f"The '{state_name}' consciousness state represents a unique configuration "
                    f"of awareness with its own characteristic qualities and perceptual framework.\n\n"
                    f"This state offers specific insights and experiences that differ from ordinary "
                    f"waking consciousness. Further exploration and documentation will reveal its "
                    f"distinctive properties and potential applications in consciousness research."
                )
        except Exception as e:
            print(f"Error generating state description: {e}")
            return "Description unavailable."

    def generate_state_techniques(self, state_name):
        """Generate techniques for accessing a consciousness state based on its name"""
        try:
            techniques = {
                "Default Waking Consciousness": [
                    "No specific techniques required as this is the default state.",
                    "To enhance clarity in this state, practice mindful attention to daily activities.",
                    "Regular sleep, nutrition, and exercise help maintain optimal functioning in this state."
                ],
                "Focused Attention": [
                    "Single-point meditation: Focus on one object (breath, candle flame, mantra) to the exclusion of all else.",
                    "Pomodoro technique: Work in focused 25-minute intervals followed by 5-minute breaks.",
                    "Sensory isolation: Reduce external stimuli to help maintain concentration on a single task."
                ],
                "Open Awareness": [
                    "Open monitoring meditation: Observe all arising phenomena without attachment.",
                    "Nature immersion: Spend time in natural settings with panoramic awareness.",
                    "Body scan: Systematically move attention through the body without focusing on any one sensation."
                ],
                "Deep Meditation": [
                    "Progressive relaxation followed by breath awareness meditation.",
                    "Extended meditation sessions (45+ minutes) in a quiet environment.",
                    "Mantra repetition that gradually becomes more subtle until it dissolves into silence."
                ],
                "Lucid Dreaming": [
                    "Reality testing: Regularly check if you're dreaming throughout the day.",
                    "MILD technique: As you fall asleep, repeat 'I will recognize when I'm dreaming'.",
                    "Wake Back to Bed: Sleep for 5-6 hours, stay awake for 30 minutes, then return to sleep focusing on lucidity."
                ],
                "Hypnagogic State": [
                    "Nap meditation: Lie down as if to sleep but maintain a thread of awareness.",
                    "Yoga nidra: Follow a guided relaxation that keeps you at the edge of sleep.",
                    "Sensory deprivation: Use an eye mask and earplugs while resting in a comfortable position."
                ],
                "Flow State": [
                    "Engage in activities that balance challenge with skill level.",
                    "Eliminate distractions and set clear goals for the activity.",
                    "Focus on the process rather than the outcome of what you're doing."
                ],
                "Quantum Perception": [
                    "Synchronicity journaling: Record and analyze meaningful coincidences.",
                    "Reality glitch meditation: Observe subtle anomalies in perception without dismissing them.",
                    "Quantum probability meditation: Visualize multiple timelines branching from each moment."
                ]
            }
            
            # Return techniques if they exist, otherwise generate generic ones
            if state_name in techniques:
                return techniques[state_name]
            else:
                return [
                    f"Meditation focused specifically on the qualities of the {state_name} state.",
                    "Progressive relaxation followed by visualization of entering this state.",
                    "Journaling about previous experiences of this state to create a reference point."
                ]
        except Exception as e:
            print(f"Error generating state techniques: {e}")
            return ["Techniques unavailable."]

    def add_new_consciousness_state(self):
        """Add a new consciousness state"""
        messagebox.showinfo("Coming Soon", "This feature will be available in the next update!")

    def edit_consciousness_state(self, state_name):
        """Edit an existing consciousness state"""
        messagebox.showinfo("Coming Soon", "This feature will be available in the next update!")

    def save_consciousness_map(self):
        """Save the current consciousness map"""
        messagebox.showinfo("Coming Soon", "This feature will be available in the next update!")

    def reset_consciousness_map(self):
        """Reset the consciousness map"""
        messagebox.showinfo("Coming Soon", "This feature will be available in the next update!")

    def run_pattern_analysis(self):
        """Run the pattern analysis algorithm"""
        messagebox.showinfo("Coming Soon", "This feature will be available in the next update!")

    def export_pattern_analysis(self):
        """Export the pattern analysis results"""
        messagebox.showinfo("Coming Soon", "This feature will be available in the next update!")

    def create_journal_tab(self):
        """Create the journal tab for recording experiences"""
        try:
            # Main container for journal tab
            journal_container = ttk.Frame(self.journal_frame)
            journal_container.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Header
            header_frame = ttk.Frame(journal_container)
            header_frame.pack(fill='x', pady=(0, 20))
            
            title_label = ttk.Label(
                header_frame,
                text="Consciousness Journal",
                style="Title.TLabel"
            )
            title_label.pack(anchor='w')
            
            subtitle_label = ttk.Label(
                header_frame,
                text="Document your reality glitches and synchronicities",
                style="Subtitle.TLabel"
            )
            subtitle_label.pack(anchor='w')
            
            # Split view: Journal entries list on left, editor on right
            content_frame = ttk.Frame(journal_container)
            content_frame.pack(fill='both', expand=True)
            
            # Configure grid for split view
            content_frame.columnconfigure(0, weight=1)  # Journal list
            content_frame.columnconfigure(1, weight=2)  # Journal editor
            content_frame.rowconfigure(0, weight=1)
            
            # Journal list (left panel)
            list_frame = ttk.Frame(content_frame)
            list_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
            
            list_label = ttk.Label(
                list_frame,
                text="Journal Entries",
                style="Quantum.TLabel"
            )
            list_label.pack(anchor='w', pady=(0, 10))
            
            # Create a listbox with scrollbar for journal entries
            list_container = ttk.Frame(list_frame)
            list_container.pack(fill='both', expand=True)
            
            self.journal_listbox = tk.Listbox(
                list_container,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                selectbackground=self.theme_manager.get_color('accent'),
                selectforeground=self.theme_manager.get_color('bg'),
                font=self.fonts['normal'],
                relief='flat',
                highlightthickness=1,
                highlightbackground=self.theme_manager.get_color('border')
            )
            
            list_scrollbar = ttk.Scrollbar(
                list_container,
                orient="vertical",
                command=self.journal_listbox.yview
            )
            
            self.journal_listbox.configure(yscrollcommand=list_scrollbar.set)
            self.journal_listbox.pack(side="left", fill="both", expand=True)
            list_scrollbar.pack(side="right", fill="y")
            
            # Load journal entries
            self.load_journal_entries()
            
            # Bind selection event
            self.journal_listbox.bind('<<ListboxSelect>>', self.on_journal_entry_selected)
            
            # Add button to create new journal entry
            new_entry_btn = self.create_glowing_button(
                list_frame,
                text="New Journal Entry",
                command=self.create_new_journal_entry,
                bg=self.theme_manager.get_color('accent'),
                hover_bg=self.theme_manager.get_color('accent_highlight')
            )
            new_entry_btn.pack(fill='x', pady=(10, 0))
            
            # Delete button
            delete_entry_btn = self.create_glowing_button(
                list_frame,
                text="Delete Selected Entry",
                command=self.delete_journal_entry,
                bg=self.theme_manager.get_color('button'),
                hover_bg=self.theme_manager.get_color('button_hover')
            )
            delete_entry_btn.pack(fill='x', pady=(5, 0))
            
            # Journal editor (right panel)
            editor_frame = ttk.Frame(content_frame)
            editor_frame.grid(row=0, column=1, sticky="nsew")
            
            # Initially show a welcome message in the editor
            self.journal_editor = self.create_quantum_frame(
                editor_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                border_color=self.theme_manager.get_color('accent')
            )
            self.journal_editor.pack(fill='both', expand=True)
            
            welcome_frame = ttk.Frame(self.journal_editor)
            welcome_frame.place(relx=0.5, rely=0.5, anchor='center')
            
            welcome_icon = ttk.Label(
                welcome_frame,
                text="📝",
                font=('Helvetica', 48)
            )
            welcome_icon.pack()
            
            welcome_text = ttk.Label(
                welcome_frame,
                text="Select an entry to edit or create a new one",
                font=self.fonts['heading'],
                wraplength=300,
                justify='center'
            )
            welcome_text.pack(pady=10)
            
        except Exception as e:
            print(f"Error creating journal tab: {e}")
            messagebox.showerror("Journal Tab Error", "Failed to create journal tab.")

    def load_journal_entries(self):
        """Load journal entries from files"""
        try:
            # Clear existing items
            self.journal_listbox.delete(0, tk.END)
            
            # Get journal files
            journal_dir = os.path.join("user_data", "journal")
            if not os.path.exists(journal_dir):
                os.makedirs(journal_dir)
                
            journal_files = [f for f in os.listdir(journal_dir) if f.endswith('.json')]
            
            # Sort by date (newest first)
            journal_files.sort(reverse=True)
            
            # Load journal data
            self.journal_entries = []
            
            for file in journal_files:
                try:
                    with open(os.path.join(journal_dir, file), 'r') as f:
                        entry = json.load(f)
                        self.journal_entries.append(entry)
                        
                        # Add to listbox
                        date_str = entry.get('date', 'Unknown date')
                        title = entry.get('title', 'Untitled')
                        display_text = f"{date_str} - {title}"
                        self.journal_listbox.insert(tk.END, display_text)
                except Exception as e:
                    print(f"Error loading journal file {file}: {e}")
                    
            # If no entries found, add a message
            if not self.journal_entries:
                self.journal_listbox.insert(tk.END, "No journal entries found")
                self.journal_listbox.config(state='disabled')
            
        except Exception as e:
            print(f"Error loading journal entries: {e}")

    def on_journal_entry_selected(self, event):
        """Handle journal entry selection from listbox"""
        try:
            # Get selected index
            selection = self.journal_listbox.curselection()
            if not selection:
                return
                
            index = selection[0]
            if index >= len(self.journal_entries):
                return
                
            # Get selected entry
            entry = self.journal_entries[index]
            
            # Clear existing editor content
            for widget in self.journal_editor.winfo_children():
                widget.destroy()
                
            # Create journal editor UI
            self.create_journal_editor(entry, index)
            
        except Exception as e:
            print(f"Error handling journal entry selection: {e}")

    def create_journal_editor(self, entry, index):
        """Create the journal editor UI for the selected entry"""
        try:
            # First, clear all existing widgets
            for widget in self.journal_editor.winfo_children():
                widget.destroy()
            
            # Create a main frame with grid layout for better control
            main_frame = ttk.Frame(self.journal_editor)
            main_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Configure grid - 1 column, multiple rows
            main_frame.columnconfigure(0, weight=1)
            main_frame.rowconfigure(0, weight=0)  # Title row - fixed height
            main_frame.rowconfigure(1, weight=0)  # Date row - fixed height
            main_frame.rowconfigure(2, weight=0)  # Type row - fixed height
            main_frame.rowconfigure(3, weight=1)  # Content row - expandable
            main_frame.rowconfigure(4, weight=0)  # Button row - fixed height
            
            # Title section
            title_frame = ttk.Frame(main_frame)
            title_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
            
            ttk.Label(title_frame, text="Title:", style="Quantum.TLabel").pack(anchor='w')
            
            self.title_entry = tk.Entry(
                title_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=self.fonts['heading'],
                width=40
            )
            self.title_entry.pack(fill='x', pady=(5, 0))
            self.title_entry.insert(0, entry.get('title', 'Untitled'))
            
            # Date section
            date_frame = ttk.Frame(main_frame)
            date_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
            
            ttk.Label(date_frame, text="Date:", style="Quantum.TLabel").pack(anchor='w')
            
            date_label = ttk.Label(
                date_frame,
                text=entry.get('date', datetime.now().strftime("%Y-%m-%d %H:%M")),
                font=self.fonts['normal']
            )
            date_label.pack(anchor='w', pady=(5, 0))
            
            # Entry type section
            type_frame = ttk.Frame(main_frame)
            type_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))
            
            ttk.Label(type_frame, text="Entry Type:", style="Quantum.TLabel").pack(anchor='w')
            
            self.entry_type_var = tk.StringVar(value=entry.get('type', 'general'))
            
            type_options = [
                ("General Observation", "general"),
                ("Reality Glitch", "glitch"),
                ("Synchronicity", "sync"),
                ("Dream", "dream"),
                ("Meditation Insight", "meditation")
            ]
            
            type_container = ttk.Frame(type_frame)
            type_container.pack(fill='x', pady=(5, 0))
            
            for i, (text, value) in enumerate(type_options):
                rb = ttk.Radiobutton(
                    type_container,
                    text=text,
                    value=value,
                    variable=self.entry_type_var
                )
                rb.grid(row=i//3, column=i%3, sticky='w', padx=5, pady=2)
            
            # Content section with text editor
            content_frame = ttk.Frame(main_frame)
            content_frame.grid(row=3, column=0, sticky="nsew", pady=(0, 15))
            content_frame.rowconfigure(1, weight=1)
            content_frame.columnconfigure(0, weight=1)
            
            ttk.Label(content_frame, text="Journal Entry:", style="Quantum.TLabel").grid(row=0, column=0, sticky='w')
            
            text_frame = ttk.Frame(content_frame)
            text_frame.grid(row=1, column=0, sticky="nsew")
            
            self.content_text = tk.Text(
                text_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=self.fonts['normal'],
                wrap='word',
                relief='flat',
                highlightthickness=1,
                highlightbackground=self.theme_manager.get_color('border'),
                padx=10,
                pady=10
            )
            self.content_text.pack(side='left', fill='both', expand=True)
            
            # Add scrollbar
            scrollbar = ttk.Scrollbar(text_frame, command=self.content_text.yview)
            scrollbar.pack(side='right', fill='y')
            self.content_text.configure(yscrollcommand=scrollbar.set)
            
            # Insert content
            self.content_text.insert('1.0', entry.get('content', ''))
            
            # Button row for save/cancel
            btn_frame = ttk.Frame(main_frame)
            btn_frame.grid(row=4, column=0, sticky="ew")
            
            save_btn = self.create_glowing_button(
                btn_frame,
                text="Save Entry",
                command=lambda: self.save_journal_entry(index),
                bg=self.theme_manager.get_color('accent'),
                hover_bg=self.theme_manager.get_color('accent_highlight'),
                font=("Helvetica", 12, "bold")
            )
            save_btn.pack(side='right', padx=5)
            
        except Exception as e:
            print(f"Error creating journal editor: {e}")
            messagebox.showerror("Journal Editor Error", "Failed to create journal editor.")

    def create_new_journal_entry(self):
        """Create a new journal entry"""
        try:
            # Create a new blank entry
            new_entry = {
                'id': str(uuid.uuid4()),
                'title': 'New Journal Entry',
                'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                'type': 'general',
                'content': ''
            }
            
            # Add to the list
            self.journal_entries.insert(0, new_entry)
            
            # Add to listbox
            self.journal_listbox.insert(0, f"{new_entry['date']} - {new_entry['title']}")
            
            # Select it
            self.journal_listbox.selection_clear(0, tk.END)
            self.journal_listbox.selection_set(0)
            
            # Ensure listbox is enabled
            self.journal_listbox.config(state='normal')
            
            # Trigger selection event
            self.on_journal_entry_selected(None)
            
        except Exception as e:
            print(f"Error creating new journal entry: {e}")
            messagebox.showerror("Journal Error", "Failed to create new journal entry.")

    def save_journal_entry(self, index):
        """Save the current journal entry"""
        try:
            # Get the data from form
            title = self.title_entry.get().strip()
            if not title:
                title = "Untitled Entry"
                
            entry_type = self.entry_type_var.get()
            content = self.content_text.get('1.0', 'end-1c')  # Get all text minus trailing newline
            
            # Update entry in memory
            entry = self.journal_entries[index]
            entry['title'] = title
            entry['type'] = entry_type
            entry['content'] = content
            
            # Update listbox display
            self.journal_listbox.delete(index)
            self.journal_listbox.insert(index, f"{entry['date']} - {title}")
            
            # Save to file
            journal_dir = os.path.join("user_data", "journal")
            if not os.path.exists(journal_dir):
                os.makedirs(journal_dir)
                
            filename = f"{entry['id']}.json"
            filepath = os.path.join(journal_dir, filename)
            
            with open(filepath, 'w') as f:
                json.dump(entry, f, indent=2)
                
            # Show success message in status bar
            self.status_text.config(text="Journal entry saved successfully")
            
        except Exception as e:
            print(f"Error saving journal entry: {e}")
            messagebox.showerror("Save Error", "Failed to save journal entry.")

    def delete_journal_entry(self):
        """Delete the selected journal entry"""
        try:
            # Get selected index
            selection = self.journal_listbox.curselection()
            if not selection:
                messagebox.showinfo("Delete Entry", "Please select an entry to delete.")
                return
                
            index = selection[0]
            if index >= len(self.journal_entries):
                return
                
            # Confirm deletion
            entry = self.journal_entries[index]
            confirm = messagebox.askyesno(
                "Confirm Delete",
                f"Are you sure you want to delete the entry '{entry.get('title', 'Untitled')}'?"
            )
            
            if not confirm:
                return
                
            # Delete from disk
            journal_dir = os.path.join("user_data", "journal")
            filename = f"{entry['id']}.json"
            filepath = os.path.join(journal_dir, filename)
            
            if os.path.exists(filepath):
                os.remove(filepath)
                
            # Remove from memory
            del self.journal_entries[index]
            
            # Remove from listbox
            self.journal_listbox.delete(index)
            
            # Clear editor if there are no more entries
            if not self.journal_entries:
                self.journal_listbox.insert(tk.END, "No journal entries found")
                self.journal_listbox.config(state='disabled')
                
                # Clear editor
                for widget in self.journal_editor.winfo_children():
                    widget.destroy()
                    
                welcome_frame = ttk.Frame(self.journal_editor)
                welcome_frame.place(relx=0.5, rely=0.5, anchor='center')
                
                welcome_icon = ttk.Label(
                    welcome_frame,
                    text="📝",
                    font=('Helvetica', 48)
                )
                welcome_icon.pack()
                
                welcome_text = ttk.Label(
                    welcome_frame,
                    text="Select an entry to edit or create a new one",
                    font=self.fonts['heading'],
                    wraplength=300,
                    justify='center'
                )
                welcome_text.pack(pady=10)
            
        except Exception as e:
            print(f"Error deleting journal entry: {e}")
            messagebox.showerror("Delete Error", "Failed to delete journal entry.")
