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
try:
    import pygame
    from PIL import Image, ImageTk, ImageFilter
    import numpy as np
except ImportError:
    pass  # Handle the case when optional modules are not available

# Constants
VERSION = "1.2.0"
VERSION_NAME = "Consciousness Evolution - Theme Update"

# Theme System
class ThemeManager:
    """Manages application-wide theming with quantum aesthetics"""
    
    def __init__(self):
        self.current_theme = "dark"  # Default theme
        self.DARK_THEME = {
            'bg': '#070B14',  # Deep space background
            'bg_gradient_start': '#0D1221',  # Top gradient color
            'bg_gradient_end': '#0A0E19',  # Bottom gradient color
            'bg_secondary': '#111B2F',  # Neural void
            'bg_tertiary': '#172338',  # Deeper background for contrast
            'text': '#E6F0FF',  # Ethereal text
            'text_secondary': '#A0B8E0',  # Mystic text
            'accent': '#7C3AFF',  # Quantum purple - more vibrant
            'accent_secondary': '#A96FFF',  # Energy pulse
            'accent_tertiary': '#C094FF',  # Subtle accent
            'success': '#00FFB2',  # Neural green - brighter
            'success_glow': '#00FFB2',  # Success glow (removed alpha)
            'warning': '#FFCC00',  # Cosmic gold - brighter
            'warning_glow': '#FFCC00',  # Warning glow (removed alpha)
            'error': '#FF3A6A',  # Reality glitch
            'error_glow': '#FF3A6A',  # Error glow (removed alpha)
            'info': '#00D2FF',  # Quantum stream - brighter
            'info_glow': '#00D2FF',  # Info glow (removed alpha)
            'border': '#1C2C48',  # Dark matter
            'hover': '#243A61',  # Quantum field
            'active': '#2C4678',  # Energy field
            'disabled': '#1A2133',  # Void state
            'highlight': '#3457A0',  # Quantum highlight
            'glow': '#7C3AFF',  # Quantum glow effect - stronger
            'quantum_effect': '#7C3AFF',  # Subtle quantum effect (removed alpha)
            'star_color': '#E6F0FF',  # Star color for dark theme
            'nebula_1': '#9D4EDD',  # Nebula effect 1
            'nebula_2': '#C77DFF',  # Nebula effect 2
            'nebula_3': '#7B2CBF',  # Nebula effect 3
            'grid_line': '#1C2C48',  # Grid lines (removed alpha channel)
            'node_color': '#00D2FF',  # Node color
            'neural_connection': '#7C3AFF',  # Neural connection color (removed alpha)
            # For backward compatibility with existing code
            'background': '#070B14',
            'foreground': '#E6F0FF',
            'secondary': '#111B2F'
        }
        
        self.LIGHT_THEME = {
            'bg': '#F0F5FF',  # Ethereal light
            'bg_gradient_start': '#FFFFFF',  # Top gradient
            'bg_gradient_end': '#F0F5FF',  # Bottom gradient
            'bg_secondary': '#E6EFFF',  # Quantum mist
            'bg_tertiary': '#D6E5FF',  # Deeper background for contrast
            'text': '#0D1221',  # Deep thought
            'text_secondary': '#2D3C61',  # Mystic dark
            'accent': '#7C3AFF',  # Quantum pulse - same as dark for continuity
            'accent_secondary': '#A96FFF',  # Energy wave
            'accent_tertiary': '#C094FF',  # Subtle accent
            'success': '#00CC8F',  # Life force
            'success_glow': '#00CC8F',  # Success glow (removed alpha)
            'warning': '#FFA800',  # Solar energy
            'warning_glow': '#FFA800',  # Warning glow (removed alpha)
            'error': '#FF2B55',  # Reality break
            'error_glow': '#FF2B55',  # Error glow (removed alpha)
            'info': '#00A6E0',  # Info stream
            'info_glow': '#00A6E0',  # Info glow (removed alpha)
            'border': '#D6E5FF',  # Quantum boundary
            'hover': '#E6EFFF',  # Light field
            'active': '#D6E5FF',  # Energy pulse
            'disabled': '#E6EFFF',  # Void state
            'highlight': '#D6E5FF',  # Quantum highlight
            'glow': '#7C3AFF',  # Quantum glow effect (removed alpha)
            'quantum_effect': '#7C3AFF',  # Subtle quantum effect (removed alpha)
            'star_color': '#7C3AFF',  # Star color for light theme
            'nebula_1': '#9D4EDD',  # Nebula effect 1 (removed alpha)
            'nebula_2': '#C77DFF',  # Nebula effect 2 (removed alpha)
            'nebula_3': '#7B2CBF',  # Nebula effect 3 (removed alpha)
            'grid_line': '#A0B8E0',  # Grid lines (removed alpha)
            'node_color': '#00A6E0',  # Node color
            'neural_connection': '#7C3AFF',  # Neural connection color (removed alpha)
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
            
            # Basic widgets
            if widget_type in ['Frame', 'Label', 'Button', 'Canvas', 'Toplevel', 'Tk']:
                if 'bg' in widget.config():
                    widget.configure(bg=theme['bg'])
                if 'fg' in widget.config() and hasattr(widget, 'configure'):
                    widget.configure(fg=theme['text'])
            
            # Buttons get special treatment for active states
            if widget_type == 'Button':
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
            height = canvas.winfo_height() or 600
            
            # Create nodes
            num_nodes = random.randint(10, 20)
            nodes = []
            
            for _ in range(num_nodes):
                x = random.randint(int(width * 0.1), int(width * 0.9))
                y = random.randint(int(height * 0.1), int(height * 0.9))
                size = random.uniform(4, 8)
                
                node = {
                    'x': x,
                    'y': y,
                    'size': size,
                    'color': self.theme_manager.get_color('accent')  # Use accent without alpha
                }
                
                nodes.append(node)
                
                # Draw node
                canvas.create_oval(
                    x - size, y - size,
                    x + size, y + size,
                    fill=node['color'],
                    outline=self.theme_manager.get_color('accent_secondary'),
                    width=1,
                    tags="neural_node"
                )
            
            # Create connections between nodes
            for i, node in enumerate(nodes):
                # Each node connects to 1-3 other nodes
                connections = random.randint(1, 3)
                connected_indices = set()
                
                for _ in range(connections):
                    # Choose a random node to connect to (that isn't self or already connected)
                    while True:
                        j = random.randint(0, num_nodes-1)
                        if j != i and j not in connected_indices:
                            connected_indices.add(j)
                            break
                    
                    # Draw connection
                    line_id = canvas.create_line(
                        node['x'], node['y'],
                        nodes[j]['x'], nodes[j]['y'],
                        fill=self.theme_manager.get_color('neural_connection'),
                        width=1,
                        tags="neural_connection"
                    )
            
            # Animate neural network
            def animate_neural_network():
                # Pulse the nodes
                for item in canvas.find_withtag("neural_node"):
                    current_fill = canvas.itemcget(item, "fill")
                    if current_fill == self.theme_manager.get_color('accent'):
                        new_fill = self.theme_manager.get_color('accent_secondary')
                    else:
                        new_fill = self.theme_manager.get_color('accent')
                    canvas.itemconfig(item, fill=new_fill)
                
                # Animate connections
                for item in canvas.find_withtag("neural_connection"):
                    # Randomly choose some connections to highlight
                    if random.random() < 0.2:  # 20% chance to highlight a connection
                        canvas.itemconfig(item, fill=self.theme_manager.get_color('accent'), width=2)
                    else:
                        # Use a solid color instead of one with alpha (44 extension)
                        canvas.itemconfig(item, fill=self.theme_manager.get_color('neural_connection'), width=1)
                
                canvas.after(500, animate_neural_network)
            
            # Start animation
            canvas.after(500, animate_neural_network)
            
            return nodes
        except Exception as e:
            print(f"Error creating neural network: {e}")
            return []

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
        try:
            self.status_bar = tk.Frame(self.root, relief=tk.SUNKEN, bd=1)
            self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
            
            self.status_text = tk.Label(self.status_bar, text="MindMirror ready.")
            self.status_text.pack(side=tk.LEFT)
            
            self.theme_indicator = tk.Label(self.status_bar, text="Theme: Dark")
            self.theme_indicator.pack(side=tk.RIGHT, padx=5)
        except Exception as e:
            print(f"Error creating status bar: {e}")

    def configure_styles(self):
        try:
            theme = self.theme_manager.get_theme_colors()
            
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
        try:
            # Placeholder for export functionality
            messagebox.showinfo("Export", "Exporting to Reality Glitcher. This feature is not fully implemented yet.")
            self.status_text.config(text="Exported to Reality Glitcher")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export: {e}")

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
            activity_frame.pack(fill='both', expand=True, pady=(20, 10))

            activity_label = ttk.Label(
                activity_frame,
                text="Recent Activity",
                style="Quantum.TLabel"
            )
            activity_label.pack(anchor='w', pady=(0, 10))
            
            # Create a canvas with scrollbar for activity items
            canvas_frame = ttk.Frame(activity_frame)
            canvas_frame.pack(fill='both', expand=True)
            
            activity_canvas = tk.Canvas(
                canvas_frame,
                bg=self.theme_manager.get_color('bg'),
                highlightthickness=0
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
                no_activity.pack(pady=10)
            else:
                # Add some placeholder activities
                activities = [
                    {"type": "meditation", "title": "Quantum Awareness", "time": "2 hours ago"},
                    {"type": "journal", "title": "Reality Glitch Observation", "time": "Yesterday"},
                    {"type": "exploration", "title": "Consciousness Mapping Session", "time": "3 days ago"}
                ]
                
                for activity in activities:
                    self.create_activity_item(activity_content, activity)
            
            # Quick actions section
            actions_frame = ttk.Frame(dashboard_container)
            actions_frame.pack(fill='x', pady=20)
            
            actions_label = ttk.Label(
                actions_frame,
                text="Quick Actions",
                style="Quantum.TLabel"
            )
            actions_label.pack(anchor='w', pady=(0, 10))
            
            # Create action buttons
            buttons_frame = ttk.Frame(actions_frame)
            buttons_frame.pack(fill='x')
            
            meditation_btn = ttk.Button(
                buttons_frame,
                text="Start Meditation",
                style="Quantum.TButton",
                command=lambda: self.notebook.select(self.meditation_frame)
            )
            meditation_btn.pack(side='left', padx=5)
            
            journal_btn = ttk.Button(
                buttons_frame,
                text="New Journal Entry",
                style="Quantum.TButton",
                command=lambda: self.notebook.select(self.journal_frame)
            )
            journal_btn.pack(side='left', padx=5)
            
            explore_btn = ttk.Button(
                buttons_frame,
                text="Explore Consciousness",
                style="Quantum.TButton",
                command=lambda: self.notebook.select(self.explorer_frame)
            )
            explore_btn.pack(side='left', padx=5)
            
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
            # Header with title and duration
            header_frame = ttk.Frame(self.meditation_player)
            header_frame.pack(fill='x', pady=(0, 20))
            
            title_label = ttk.Label(
                header_frame,
                text=meditation['title'],
                style="Title.TLabel"
            )
            title_label.pack(anchor='w')
            
            duration_label = ttk.Label(
                header_frame,
                text=f"Duration: {meditation['duration']} minutes",
                style="Subtitle.TLabel"
            )
            duration_label.pack(anchor='w')
            
            # Meditation content
            content_frame = ttk.Frame(self.meditation_player)
            content_frame.pack(fill='both', expand=True)
            
            # Different UI based on meditation type
            if meditation['type'] == 'guided':
                # Guided meditation shows text content
                content_container = ttk.Frame(content_frame)
                content_container.pack(fill='both', expand=True)
                
                # Create text widget with scrollbar
                text_container = ttk.Frame(content_container)
                text_container.pack(fill='both', expand=True, pady=(0, 20))
                
                content_text = tk.Text(
                    text_container,
                    wrap='word',
                    bg=self.theme_manager.get_color('bg_secondary'),
                    fg=self.theme_manager.get_color('text'),
                    font=self.fonts['normal'],
                    relief='flat',
                    highlightthickness=1,
                    highlightbackground=self.theme_manager.get_color('border'),
                    padx=10,
                    pady=10
                )
                
                text_scrollbar = ttk.Scrollbar(
                    text_container,
                    orient="vertical",
                    command=content_text.yview
                )
                
                content_text.configure(yscrollcommand=text_scrollbar.set)
                content_text.pack(side="left", fill="both", expand=True)
                text_scrollbar.pack(side="right", fill="y")
                
                # Insert meditation content
                content_text.insert('1.0', meditation['content'])
                content_text.config(state='disabled')  # Make read-only
                
            else:  # Timer meditation
                # Timer meditation shows a simple description
                description_label = ttk.Label(
                    content_frame,
                    text=meditation['content'],
                    wraplength=400,
                    justify='center'
                )
                description_label.pack(pady=20)
            
            # Timer display
            timer_frame = ttk.Frame(self.meditation_player)
            timer_frame.pack(fill='x', pady=20)
            
            self.timer_label = ttk.Label(
                timer_frame,
                text=f"{meditation['duration']}:00",
                font=('Helvetica', 48, 'bold'),
                foreground=self.theme_manager.get_color('accent')
            )
            self.timer_label.pack()
            
            # Control buttons
            controls_frame = ttk.Frame(self.meditation_player)
            controls_frame.pack(fill='x', pady=(0, 20))
            
            # Store meditation duration for timer
            self.meditation_duration = meditation['duration'] * 60  # Convert to seconds
            
            # Create buttons with proper spacing
            button_frame = ttk.Frame(controls_frame)
            button_frame.pack()
            
            start_button = ttk.Button(
                button_frame,
                text="Start",
                style="Quantum.TButton",
                command=self.start_meditation_timer
            )
            start_button.pack(side='left', padx=5)
            
            pause_button = ttk.Button(
                button_frame,
                text="Pause",
                style="TButton",
                command=self.pause_meditation_timer
            )
            pause_button.pack(side='left', padx=5)
            
            reset_button = ttk.Button(
                button_frame,
                text="Reset",
                style="TButton",
                command=self.reset_meditation_timer
            )
            reset_button.pack(side='left', padx=5)
            
        except Exception as e:
            print(f"Error creating meditation player: {e}")

    def start_meditation_timer(self):
        """Start the meditation timer"""
        try:
            if not self.meditation_timer_running:
                # If timer was paused, resume from paused time
                if self.meditation_timer_paused_time > 0:
                    self.meditation_timer_start = time.time() - self.meditation_timer_paused_time
                    self.meditation_timer_paused_time = 0
                else:
                    # Start fresh timer
                    self.meditation_timer_start = time.time()
                
                self.meditation_timer_running = True
                self.update_meditation_timer()
                
                # Update status
                self.status_text.config(text="Meditation in progress...")
        except Exception as e:
            print(f"Error starting meditation timer: {e}")

    def pause_meditation_timer(self):
        """Pause the meditation timer"""
        try:
            if self.meditation_timer_running:
                # Calculate elapsed time and store it
                elapsed = time.time() - self.meditation_timer_start
                self.meditation_timer_paused_time = elapsed
                self.meditation_timer_running = False
                
                # Update status
                self.status_text.config(text="Meditation paused")
        except Exception as e:
            print(f"Error pausing meditation timer: {e}")

    def reset_meditation_timer(self):
        """Reset the meditation timer"""
        try:
            self.meditation_timer_running = False
            self.meditation_timer_start = None
            self.meditation_timer_paused_time = 0
            
            # Reset timer display
            minutes = self.meditation_duration // 60
            seconds = 0
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            
            # Update status
            self.status_text.config(text="Meditation reset")
        except Exception as e:
            print(f"Error resetting meditation timer: {e}")

    def update_meditation_timer(self):
        """Update the meditation timer display"""
        try:
            if not self.meditation_timer_running:
                return
                
            # Calculate elapsed time
            elapsed = time.time() - self.meditation_timer_start
            remaining = max(0, self.meditation_duration - elapsed)
            
            # Update timer display
            minutes = int(remaining // 60)
            seconds = int(remaining % 60)
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            
            # Check if timer has finished
            if remaining <= 0:
                self.meditation_timer_running = False
                self.meditation_timer_start = None
                self.meditation_timer_paused_time = 0
                
                # Update basic user stats
                self.user_data["meditation_minutes"] = self.user_data.get("meditation_minutes", 0) + (self.meditation_duration // 60)
                self.user_data["session_count"] = self.user_data.get("session_count", 0) + 1
                
                # Initialize meditation_stats if it doesn't exist
                if "meditation_stats" not in self.user_data:
                    self.user_data["meditation_stats"] = {
                        "sessions": 0,
                        "total_minutes": 0,
                        "practice_streak": 0,
                        "last_meditation": None
                    }
                
                # Update meditation stats
                meditation_stats = self.user_data["meditation_stats"]
                meditation_stats["sessions"] = meditation_stats.get("sessions", 0) + 1
                meditation_stats["total_minutes"] = meditation_stats.get("total_minutes", 0) + (self.meditation_duration // 60)
                
                # Update streak
                today = datetime.now().strftime("%Y-%m-%d")
                last_date = meditation_stats.get("last_meditation", None)
                
                if last_date != today:
                    # Check if last meditation was yesterday
                    if last_date:
                        try:
                            last_date_obj = datetime.strptime(last_date, "%Y-%m-%d")
                            today_obj = datetime.strptime(today, "%Y-%m-%d")
                            days_diff = (today_obj - last_date_obj).days
                            
                            if days_diff == 1:  # Consecutive day
                                meditation_stats["practice_streak"] = meditation_stats.get("practice_streak", 0) + 1
                            elif days_diff > 1:  # Streak broken
                                meditation_stats["practice_streak"] = 1
                        except ValueError:
                            # If date parsing fails, just set streak to 1
                            meditation_stats["practice_streak"] = 1
                    else:
                        # First meditation
                        meditation_stats["practice_streak"] = 1
                    
                    meditation_stats["last_meditation"] = today
                
                # Save updated data
                self.save_user_data()
                
                # Show completion message with streak info
                streak = meditation_stats.get("practice_streak", 0)
                streak_message = f"Your meditation session has completed.\nCurrent streak: {streak} day{'s' if streak != 1 else ''}!"
                messagebox.showinfo("Meditation Complete", streak_message)
                self.status_text.config(text="Meditation complete")
                return
            
            # Continue updating timer
            self.root.after(1000, self.update_meditation_timer)
        except Exception as e:
            print(f"Error updating meditation timer: {e}")
            # Ensure timer continues even after error
            self.root.after(1000, self.update_meditation_timer)

    def create_new_meditation(self):
        """Create a new meditation"""
        try:
            # Create dialog window
            dialog = tk.Toplevel(self.root)
            dialog.title("Create New Meditation")
            dialog.geometry("500x600")
            dialog.configure(bg=self.theme_manager.get_color('bg'))
            
            # Make dialog modal
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Apply theme
            self.theme_manager.apply_theme(dialog)
            
            # Create form
            form_frame = ttk.Frame(dialog)
            form_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Title
            title_label = ttk.Label(
                form_frame,
                text="Create New Meditation",
                style="Title.TLabel"
            )
            title_label.pack(anchor='w', pady=(0, 20))
            
            # Meditation title
            title_frame = ttk.Frame(form_frame)
            title_frame.pack(fill='x', pady=10)
            
            ttk.Label(title_frame, text="Title:").pack(anchor='w')
            
            title_entry = tk.Entry(
                title_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=self.fonts['normal'],
                width=40
            )
            title_entry.pack(fill='x', pady=(5, 0))
            
            # Duration
            duration_frame = ttk.Frame(form_frame)
            duration_frame.pack(fill='x', pady=10)
            
            ttk.Label(duration_frame, text="Duration (minutes):").pack(anchor='w')
            
            duration_var = tk.StringVar(value="10")
            duration_options = [str(i) for i in range(1, 61)]
            
            duration_dropdown = ttk.Combobox(
                duration_frame,
                textvariable=duration_var,
                values=duration_options,
                state="readonly",
                width=5
            )
            duration_dropdown.pack(anchor='w', pady=(5, 0))
            
            # Meditation type
            type_frame = ttk.Frame(form_frame)
            type_frame.pack(fill='x', pady=10)
            
            ttk.Label(type_frame, text="Type:").pack(anchor='w')
            
            type_var = tk.StringVar(value="guided")
            
            guided_radio = ttk.Radiobutton(
                type_frame,
                text="Guided Meditation",
                variable=type_var,
                value="guided"
            )
            guided_radio.pack(anchor='w', pady=(5, 0))
            
            timer_radio = ttk.Radiobutton(
                type_frame,
                text="Timer Only",
                variable=type_var,
                value="timer"
            )
            timer_radio.pack(anchor='w')
            
            # Content
            content_frame = ttk.Frame(form_frame)
            content_frame.pack(fill='both', expand=True, pady=10)
            
            ttk.Label(content_frame, text="Content:").pack(anchor='w')
            
            content_text = tk.Text(
                content_frame,
                wrap='word',
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=self.fonts['normal'],
                height=10
            )
            content_text.pack(fill='both', expand=True, pady=(5, 0))
            
            # Buttons
            button_frame = ttk.Frame(form_frame)
            button_frame.pack(fill='x', pady=(20, 0))
            
            cancel_button = ttk.Button(
                button_frame,
                text="Cancel",
                command=dialog.destroy
            )
            cancel_button.pack(side='right', padx=5)
            
            save_button = ttk.Button(
                button_frame,
                text="Save",
                style="Quantum.TButton",
                command=lambda: self.save_new_meditation(
                    title_entry.get(),
                    int(duration_var.get()),
                    type_var.get(),
                    content_text.get('1.0', 'end-1c'),
                    dialog
                )
            )
            save_button.pack(side='right', padx=5)
            
        except Exception as e:
            print(f"Error creating new meditation dialog: {e}")
            messagebox.showerror("Error", "Failed to create new meditation dialog.")

    def save_new_meditation(self, title, duration, meditation_type, content, dialog):
        """Save a new meditation to file"""
        try:
            # Validate inputs
            if not title.strip():
                messagebox.showerror("Error", "Please enter a title for the meditation.")
                return
                
            if meditation_type == "guided" and not content.strip():
                messagebox.showerror("Error", "Please enter content for the guided meditation.")
                return
                
            # Create meditation data
            meditation = {
                "title": title.strip(),
                "duration": duration,
                "type": meditation_type,
                "content": content.strip() if meditation_type == "guided" else "A simple timer for silent meditation practice."
            }
            
            # Save to file
            filename = title.strip().replace(' ', '_').lower()
            file_path = os.path.join("user_data", "meditations", f"{filename}.json")
            
            with open(file_path, 'w') as f:
                json.dump(meditation, f, indent=4)
                
            # Close dialog
            dialog.destroy()
            
            # Reload meditation list
            self.load_meditation_list()
            
            # Update status
            self.status_text.config(text=f"Created new meditation: {title}")
            
        except Exception as e:
            print(f"Error saving new meditation: {e}")
            messagebox.showerror("Error", "Failed to save new meditation.")

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
            new_entry_btn = ttk.Button(
                list_frame,
                text="New Journal Entry",
                style="Quantum.TButton",
                command=self.create_new_journal_entry
            )
            new_entry_btn.pack(fill='x', pady=(10, 0))
            
            # Delete button
            delete_entry_btn = ttk.Button(
                list_frame,
                text="Delete Selected Entry",
                style="TButton",
                command=self.delete_journal_entry
            )
            delete_entry_btn.pack(fill='x', pady=(5, 0))
            
            # Journal editor (right panel)
            editor_frame = ttk.Frame(content_frame)
            editor_frame.grid(row=0, column=1, sticky="nsew")
            
            # Initially show a welcome message in the editor
            self.journal_editor = ttk.Frame(editor_frame)
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
            main_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
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
            
            ttk.Label(title_frame, text="Title:").pack(anchor='w')
            
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
            
            ttk.Label(date_frame, text="Date:").pack(anchor='w')
            
            date_label = ttk.Label(
                date_frame,
                text=entry.get('date', datetime.now().strftime("%Y-%m-%d %H:%M")),
                font=self.fonts['normal']
            )
            date_label.pack(anchor='w', pady=(5, 0))
            
            # Entry type section
            type_frame = ttk.Frame(main_frame)
            type_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))
            
            ttk.Label(type_frame, text="Entry Type:").pack(anchor='w')
            
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
            
            # Use grid for radio buttons to ensure they're all visible
            for i, (text, value) in enumerate(type_options):
                ttk.Radiobutton(
                    type_container,
                    text=text,
                    variable=self.entry_type_var,
                    value=value
                ).grid(row=i//3, column=i%3, sticky="w", padx=5, pady=2)
            
            # Content section
            content_frame = ttk.Frame(main_frame)
            content_frame.grid(row=3, column=0, sticky="nsew", pady=(0, 10))
            
            ttk.Label(content_frame, text="Content:").pack(anchor='w')
            
            # Create text widget with scrollbar
            text_container = ttk.Frame(content_frame)
            text_container.pack(fill='both', expand=True, pady=(5, 0))
            
            self.content_text = tk.Text(
                text_container,
                wrap='word',
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=self.fonts['normal'],
                relief='flat',
                highlightthickness=1,
                highlightbackground=self.theme_manager.get_color('border'),
                padx=10,
                pady=10,
                height=10  # Set a fixed height to ensure button is visible
            )
            
            text_scrollbar = ttk.Scrollbar(
                text_container,
                orient="vertical",
                command=self.content_text.yview
            )
            
            self.content_text.configure(yscrollcommand=text_scrollbar.set)
            self.content_text.pack(side="left", fill="both", expand=True)
            text_scrollbar.pack(side="right", fill="y")
            
            # Insert content
            self.content_text.insert('1.0', entry.get('content', ''))
            
            # Button section - GUARANTEED TO BE VISIBLE with grid layout
            button_frame = ttk.Frame(main_frame, height=50)  # Fixed height
            button_frame.grid(row=4, column=0, sticky="ew", pady=(10, 0))
            
            # Force the frame to maintain its size
            button_frame.pack_propagate(False)
            
            # Create a very prominent save button
            save_button = tk.Button(
                button_frame,
                text="💾 SAVE JOURNAL ENTRY",
                bg=self.theme_manager.get_color('accent'),
                fg=self.theme_manager.get_color('bg'),
                font=('Helvetica', 12, 'bold'),
                relief='raised',
                borderwidth=3,
                padx=20,
                pady=8,
                command=lambda: self.save_journal_entry(index)
            )
            save_button.pack(side='right', padx=10, pady=5)
            
            # Add a warning label
            warning_label = tk.Label(
                button_frame,
                text="⚠️ Click to save your changes!",
                fg=self.theme_manager.get_color('warning'),
                bg=self.theme_manager.get_color('bg'),
                font=('Helvetica', 11)
            )
            warning_label.pack(side='left', padx=10, pady=5)
            
        except Exception as e:
            print(f"Error creating journal editor: {e}")
            messagebox.showerror("Editor Error", f"Failed to create journal editor: {e}")

    def create_new_journal_entry(self):
        """Create a new journal entry"""
        try:
            # Create a new entry with default values
            new_entry = {
                'title': 'New Journal Entry',
                'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
                'type': 'general',
                'content': ''
            }
            
            # Add to journal entries list
            self.journal_entries.insert(0, new_entry)
            
            # Add to listbox
            display_text = f"{new_entry['date']} - {new_entry['title']}"
            self.journal_listbox.insert(0, display_text)
            
            # Select the new entry
            self.journal_listbox.selection_clear(0, tk.END)
            self.journal_listbox.selection_set(0)
            self.journal_listbox.activate(0)
            
            # Enable listbox if it was disabled
            self.journal_listbox.config(state='normal')
            
            # Show editor for new entry
            self.on_journal_entry_selected(None)
            
            # Update user stats
            self.user_data["journal_entries"] = self.user_data.get("journal_entries", 0) + 1
            self.save_user_data()
            
        except Exception as e:
            print(f"Error creating new journal entry: {e}")
            messagebox.showerror("Error", "Failed to create new journal entry.")

    def save_journal_entry(self, index):
        """Save the current journal entry"""
        try:
            # Get entry data from editor
            title = self.title_entry.get().strip() or "Untitled"
            entry_type = self.entry_type_var.get()
            content = self.content_text.get('1.0', 'end-1c')
            
            # Update entry in list
            self.journal_entries[index]['title'] = title
            self.journal_entries[index]['type'] = entry_type
            self.journal_entries[index]['content'] = content
            
            # Update listbox display
            date_str = self.journal_entries[index]['date']
            display_text = f"{date_str} - {title}"
            self.journal_listbox.delete(index)
            self.journal_listbox.insert(index, display_text)
            self.journal_listbox.selection_set(index)
            
            # Save to file
            filename = f"{date_str.replace(':', '-').replace(' ', '_')}_{title.replace(' ', '_')[:20]}.json"
            file_path = os.path.join("user_data", "journal", filename)
            
            with open(file_path, 'w') as f:
                json.dump(self.journal_entries[index], f, indent=4)
                
            # Update status
            self.status_text.config(text=f"Saved journal entry: {title}")
            
        except Exception as e:
            print(f"Error saving journal entry: {e}")
            messagebox.showerror("Error", "Failed to save journal entry.")

    def delete_journal_entry(self):
        """Delete the selected journal entry"""
        try:
            # Get selected index
            selection = self.journal_listbox.curselection()
            if not selection:
                messagebox.showinfo("Info", "Please select an entry to delete.")
                return
                
            index = selection[0]
            if index >= len(self.journal_entries):
                return
                
            # Confirm deletion
            entry_title = self.journal_entries[index].get('title', 'Untitled')
            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete the entry '{entry_title}'?"
            )
            
            if not confirm:
                return
                
            # Get filename to delete
            date_str = self.journal_entries[index]['date']
            filename = f"{date_str.replace(':', '-').replace(' ', '_')}_{entry_title.replace(' ', '_')[:20]}.json"
            file_path = os.path.join("user_data", "journal", filename)
            
            # Delete file if it exists
            if os.path.exists(file_path):
                os.remove(file_path)
                
            # Remove from list and listbox
            self.journal_entries.pop(index)
            self.journal_listbox.delete(index)
            
            # Clear editor
            for widget in self.journal_editor.winfo_children():
                widget.destroy()
                
            # Show welcome message if no entries left
            if not self.journal_entries:
                self.journal_listbox.insert(0, "No journal entries found")
                self.journal_listbox.config(state='disabled')
                
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
                    text="Create a new journal entry to begin",
                    font=self.fonts['heading'],
                    wraplength=300,
                    justify='center'
                )
                welcome_text.pack(pady=10)
                
            # Update user stats
            self.user_data["journal_entries"] = max(0, self.user_data.get("journal_entries", 0) - 1)
            self.save_user_data()
            
            # Update status
            self.status_text.config(text=f"Deleted journal entry: {entry_title}")
            
        except Exception as e:
            print(f"Error deleting journal entry: {e}")
            messagebox.showerror("Error", "Failed to delete journal entry.")

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
            
            # Create canvas for visualization
            self.map_canvas = tk.Canvas(
                map_container,
                bg=self.theme_manager.get_color('bg'),
                highlightthickness=0
            )
            self.map_canvas.pack(fill='both', expand=True)
            
            # Create neural network visualization
            self.create_neural_network(self.map_canvas)
            
            # Add controls
            controls_frame = ttk.Frame(map_container)
            controls_frame.pack(fill='x', pady=(10, 0))
            
            # Add a button to create a new consciousness state
            new_state_btn = ttk.Button(
                controls_frame,
                text="Add New State",
                style="Quantum.TButton",
                command=self.add_new_consciousness_state
            )
            new_state_btn.pack(side='left', padx=5)
            
            # Add a button to save the current map
            save_map_btn = ttk.Button(
                controls_frame,
                text="Save Map",
                style="TButton",
                command=self.save_consciousness_map
            )
            save_map_btn.pack(side='left', padx=5)
            
            # Add a button to reset the map
            reset_map_btn = ttk.Button(
                controls_frame,
                text="Reset Map",
                style="TButton",
                command=self.reset_consciousness_map
            )
            reset_map_btn.pack(side='left', padx=5)
            
        except Exception as e:
            print(f"Error creating map tab: {e}")

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
            list_frame = ttk.Frame(states_container)
            list_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
            
            list_label = ttk.Label(
                list_frame,
                text="Consciousness States",
                style="Quantum.TLabel"
            )
            list_label.pack(anchor='w', pady=(0, 10))
            
            # Create a listbox with scrollbar for states
            list_container = ttk.Frame(list_frame)
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
            new_state_btn = ttk.Button(
                list_frame,
                text="Add New State",
                style="TButton",
                command=self.add_new_consciousness_state
            )
            new_state_btn.pack(fill='x', pady=(10, 0))
            
            # State details (right panel)
            self.state_details = ttk.Frame(self.states_frame)
            self.state_details.pack(fill='both', expand=True)
            
            # Initially show a welcome message
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

    def load_states(self):
        """Load states from files"""
        try:
            # Clear existing items
            self.states_listbox.delete(0, tk.END)
            
            # Get state files
            states_dir = os.path.join("user_data", "consciousness_maps")
            if not os.path.exists(states_dir):
                os.makedirs(states_dir)
                
            state_files = [f for f in os.listdir(states_dir) if f.endswith('.txt')]
            
            # Load state names
            self.states = []
            
            for file in state_files:
                try:
                    with open(os.path.join(states_dir, file), 'r') as f:
                        state_name = f.readline().strip()
                        self.states.append(state_name)
                        
                        # Add to listbox
                        self.states_listbox.insert(tk.END, state_name)
                except Exception as e:
                    print(f"Error loading state file {file}: {e}")
                    
            # If no states found, add a message
            if not self.states:
                self.states_listbox.insert(tk.END, "No states found")
                self.states_listbox.config(state='disabled')
            
        except Exception as e:
            print(f"Error loading states: {e}")

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
        try:
            # Create dialog window
            dialog = tk.Toplevel(self.root)
            dialog.title("Create New Consciousness State")
            dialog.geometry("500x600")
            dialog.configure(bg=self.theme_manager.get_color('bg'))
            
            # Make dialog modal
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Apply theme
            self.theme_manager.apply_theme(dialog)
            
            # Create form
            form_frame = ttk.Frame(dialog)
            form_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Title
            title_label = ttk.Label(
                form_frame,
                text="Create New Consciousness State",
                style="Title.TLabel"
            )
            title_label.pack(anchor='w', pady=(0, 20))
            
            # State name
            name_frame = ttk.Frame(form_frame)
            name_frame.pack(fill='x', pady=10)
            
            ttk.Label(name_frame, text="State Name:").pack(anchor='w')
            
            self.state_name_entry = tk.Entry(
                name_frame,
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=self.fonts['normal'],
                width=40
            )
            self.state_name_entry.pack(fill='x', pady=(5, 0))
            
            # Description
            description_frame = ttk.Frame(form_frame)
            description_frame.pack(fill='x', pady=10)
            
            ttk.Label(description_frame, text="Description:").pack(anchor='w')
            
            self.description_text = tk.Text(
                description_frame,
                wrap='word',
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=self.fonts['normal'],
                height=10
            )
            self.description_text.pack(fill='both', expand=True, pady=(5, 0))
            
            # Techniques
            techniques_frame = ttk.Frame(form_frame)
            techniques_frame.pack(fill='x', pady=10)
            
            ttk.Label(techniques_frame, text="Techniques:").pack(anchor='w')
            
            self.techniques_text = tk.Text(
                techniques_frame,
                wrap='word',
                bg=self.theme_manager.get_color('bg_secondary'),
                fg=self.theme_manager.get_color('text'),
                insertbackground=self.theme_manager.get_color('accent'),
                font=self.fonts['normal'],
                height=10
            )
            self.techniques_text.pack(fill='both', expand=True, pady=(5, 0))
            
            # Buttons
            button_frame = ttk.Frame(form_frame)
            button_frame.pack(fill='x', pady=(20, 0))
            
            cancel_button = ttk.Button(
                button_frame,
                text="Cancel",
                command=dialog.destroy
            )
            cancel_button.pack(side='right', padx=5)
            
            save_button = ttk.Button(
                button_frame,
                text="Save",
                style="Quantum.TButton",
                command=lambda: self.save_new_consciousness_state(
                    self.state_name_entry.get(),
                    self.description_text.get('1.0', 'end-1c'),
                    self.techniques_text.get('1.0', 'end-1c'),
                    dialog
                )
            )
            save_button.pack(side='right', padx=5)
            
        except Exception as e:
            print(f"Error creating new consciousness state dialog: {e}")
            messagebox.showerror("Error", "Failed to create new consciousness state dialog.")

    def save_new_consciousness_state(self, name, description, techniques, dialog):
        """Save a new consciousness state"""
        try:
            # Validate inputs
            if not name.strip():
                messagebox.showerror("Error", "Please enter a name for the state.")
                return
                
            if not description.strip():
                messagebox.showerror("Error", "Please enter a description for the state.")
                return
                
            if not techniques.strip():
                messagebox.showerror("Error", "Please enter some techniques for the state.")
                return
                
            # Create state data
            state = {
                "name": name.strip(),
                "description": description.strip(),
                "techniques": techniques.strip()
            }
            
            # Save to file
            filename = name.strip().replace(' ', '_').lower()
            file_path = os.path.join("user_data", "consciousness_maps", f"{filename}.txt")
            
            with open(file_path, 'w') as f:
                f.write(f"{name.strip()}\n")
                f.write(description.strip() + "\n")
                f.write(techniques.strip())
                
            # Close dialog
            dialog.destroy()
            
            # Reload states
            self.load_states()
            
            # Update status
            self.status_text.config(text=f"Created new consciousness state: {name}")
            
        except Exception as e:
            print(f"Error saving new consciousness state: {e}")
            messagebox.showerror("Error", "Failed to save new consciousness state.")

    def save_consciousness_map(self):
        """Save the current consciousness map"""
        try:
            # Get current map data
            map_data = self.get_map_data()
            
            # Save to file
            filename = "consciousness_map.json"
            file_path = os.path.join("user_data", "consciousness_maps", filename)
            
            with open(file_path, 'w') as f:
                json.dump(map_data, f, indent=4)
                
            # Update status
            self.status_text.config(text="Consciousness map saved")
        except Exception as e:
            print(f"Error saving consciousness map: {e}")
            messagebox.showerror("Error", "Failed to save consciousness map.")

    def reset_consciousness_map(self):
        """Reset the consciousness map"""
        try:
            # Clear existing map data
            self.clear_map_data()
            
            # Update status
            self.status_text.config(text="Consciousness map reset")
        except Exception as e:
            print(f"Error resetting consciousness map: {e}")
            messagebox.showerror("Error", "Failed to reset consciousness map.")

    def get_map_data(self):
        """Get the current map data"""
        try:
            map_data = {
                "nodes": self.get_nodes(),
                "connections": self.get_connections()
            }
            return map_data
        except Exception as e:
            print(f"Error getting map data: {e}")
            return {}

    def get_nodes(self):
        """Get the current nodes"""
        try:
            nodes = []
            for item in self.map_canvas.find_withtag("neural_node"):
                x = self.map_canvas.coords(item)[0]
                y = self.map_canvas.coords(item)[1]
                size = self.map_canvas.itemcget(item, "width")
                color = self.map_canvas.itemcget(item, "fill")
                nodes.append({
                    "id": item,
                    "x": x,
                    "y": y,
                    "size": size,
                    "color": color
                })
            return nodes
        except Exception as e:
            print(f"Error getting nodes: {e}")
            return []

    def get_connections(self):
        """Get the current connections"""
        try:
            connections = []
            for item in self.map_canvas.find_withtag("neural_connection"):
                start = self.map_canvas.coords(item)[0]
                end = self.map_canvas.coords(item)[2]
                color = self.map_canvas.itemcget(item, "fill")
                connections.append({
                    "start": start,
                    "end": end,
                    "color": color
                })
            return connections
        except Exception as e:
            print(f"Error getting connections: {e}")
            return []

    def clear_map_data(self):
        """Clear the map data"""
        try:
            # Clear all nodes and connections
            self.map_canvas.delete("neural_node")
            self.map_canvas.delete("neural_connection")
            
            # Clear state list
            self.states_listbox.delete(0, tk.END)
            
            # Clear state details
            for widget in self.state_details.winfo_children():
                widget.destroy()
            
            # Clear map canvas
            self.map_canvas.delete("all")
            
            # Clear neural network
            self.clear_neural_network()
            
            # Clear user data
            self.user_data["consciousness_maps"] = 0
            self.save_user_data()
            
            # Update status
            self.status_text.config(text="Consciousness map cleared")
        except Exception as e:
            print(f"Error clearing map data: {e}")
            messagebox.showerror("Error", "Failed to clear map data.")

    def clear_neural_network(self):
        """Clear the neural network"""
        try:
            # Clear all nodes and connections
            self.map_canvas.delete("neural_node")
            self.map_canvas.delete("neural_connection")
            
            # Clear state list
            self.states_listbox.delete(0, tk.END)
            
            # Clear state details
            for widget in self.state_details.winfo_children():
                widget.destroy()
            
            # Clear map canvas
            self.map_canvas.delete("all")
            
            # Remove recursive call that would cause infinite recursion
            # self.clear_neural_network()
            
            # Clear user data
            self.user_data["consciousness_maps"] = 0
            self.save_user_data()
            
            # Update status
            self.status_text.config(text="Neural network cleared")
        except Exception as e:
            print(f"Error clearing neural network: {e}")
            messagebox.showerror("Error", "Failed to clear neural network.")

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
            
            # Clear existing state details
            for widget in self.state_details.winfo_children():
                widget.destroy()
                
            # Create state details UI
            self.create_state_details(state_name, index)
            
        except Exception as e:
            print(f"Error handling state selection: {e}")

    def create_state_details(self, state_name, index=None):
        """Create the details view for a selected consciousness state"""
        try:
            # Header with state name
            header_frame = ttk.Frame(self.state_details)
            header_frame.pack(fill='x', pady=(0, 10))
            
            state_label = ttk.Label(
                header_frame,
                text=state_name,
                style="Title.TLabel"
            )
            state_label.pack(anchor='w')
            
            # Description
            description_frame = ttk.Frame(self.state_details)
            description_frame.pack(fill='x', pady=10)
            
            description_label = ttk.Label(
                description_frame,
                text=self.generate_state_description(state_name),
                style="Subtitle.TLabel"
            )
            description_label.pack(anchor='w')
            
            # Techniques
            techniques_frame = ttk.Frame(self.state_details)
            techniques_frame.pack(fill='x', pady=10)
            
            for technique in self.generate_state_techniques(state_name):
                technique_label = ttk.Label(
                    techniques_frame,
                    text=technique,
                    style="Quantum.TLabel"
                )
                technique_label.pack(anchor='w')
            
            # Add to state list
            if index is not None:
                self.states_listbox.selection_set(index)
        except Exception as e:
            print(f"Error creating state details: {e}")
            messagebox.showerror("Error", "Failed to create state details.")

    def create_patterns_tab(self):
        """Create the pattern analysis tab"""
        try:
            # Container for patterns
            patterns_container = ttk.Frame(self.patterns_frame)
            patterns_container.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Header
            header_label = ttk.Label(
                patterns_container,
                text="Consciousness Pattern Analysis",
                style="Quantum.TLabel"
            )
            header_label.pack(anchor='w', pady=(0, 10))
            
            # Description
            description = ttk.Label(
                patterns_container,
                text="This tool analyzes patterns in your consciousness exploration data to identify recurring themes, transitions, and potential breakthrough points.",
                wraplength=600,
                justify='left'
            )
            description.pack(anchor='w', pady=(0, 20))
            
            # Create a placeholder for the analysis visualization
            canvas_frame = ttk.Frame(patterns_container)
            canvas_frame.pack(fill='both', expand=True)
            
            self.patterns_canvas = tk.Canvas(
                canvas_frame,
                bg=self.theme_manager.get_color('bg'),
                highlightthickness=0
            )
            self.patterns_canvas.pack(fill='both', expand=True)
            
            # Add a placeholder visualization
            self.patterns_canvas.create_text(
                300, 150,
                text="Pattern Analysis Visualization\n(Coming Soon)",
                fill=self.theme_manager.get_color('text_secondary'),
                font=self.fonts['heading'],
                justify='center'
            )
            
            # Add controls
            controls_frame = ttk.Frame(patterns_container)
            controls_frame.pack(fill='x', pady=(10, 0))
            
            # Add a button to run analysis
            analyze_btn = ttk.Button(
                controls_frame,
                text="Run Analysis",
                style="Quantum.TButton",
                command=self.run_pattern_analysis
            )
            analyze_btn.pack(side='left', padx=5)
            
            # Add a button to export analysis
            export_btn = ttk.Button(
                controls_frame,
                text="Export Results",
                style="TButton",
                command=self.export_pattern_analysis
            )
            export_btn.pack(side='left', padx=5)
            
        except Exception as e:
            print(f"Error creating patterns tab: {e}")

    def run_pattern_analysis(self):
        """Run analysis on consciousness patterns"""
        try:
            # Show a loading message
            self.patterns_canvas.delete("all")
            self.patterns_canvas.create_text(
                300, 150,
                text="Analyzing consciousness patterns...",
                fill=self.theme_manager.get_color('text'),
                font=self.fonts['heading'],
                justify='center',
                tags="loading"
            )
            
            # Schedule the actual analysis to allow UI to update
            self.root.after(1000, self.perform_pattern_analysis)
            
        except Exception as e:
            print(f"Error starting pattern analysis: {e}")
            messagebox.showerror("Analysis Error", "Failed to start pattern analysis.")

    def perform_pattern_analysis(self):
        """Perform the actual pattern analysis"""
        try:
            # Clear canvas
            self.patterns_canvas.delete("all")
            
            # Create a simple visualization
            width = self.patterns_canvas.winfo_width() or 600
            height = self.patterns_canvas.winfo_height() or 400
            
            # Draw a grid
            for i in range(0, width, 50):
                self.patterns_canvas.create_line(
                    i, 0, i, height,
                    fill=self.theme_manager.get_color('grid_line'),
                    tags="grid"
                )
                
            for i in range(0, height, 50):
                self.patterns_canvas.create_line(
                    0, i, width, i,
                    fill=self.theme_manager.get_color('grid_line'),
                    tags="grid"
                )
            
            # Draw some random data points
            for _ in range(20):
                x = random.randint(50, width - 50)
                y = random.randint(50, height - 50)
                size = random.randint(5, 15)
                
                self.patterns_canvas.create_oval(
                    x - size, y - size,
                    x + size, y + size,
                    fill=self.theme_manager.get_color('accent'),
                    outline="",
                    tags="data"
                )
            
            # Draw some connections between points
            points = self.patterns_canvas.find_withtag("data")
            for i in range(len(points)):
                # Connect to 1-3 other points
                connections = random.randint(1, 3)
                for _ in range(connections):
                    j = random.randint(0, len(points) - 1)
                    if i != j:
                        # Get coordinates of both points
                        x1, y1, x2, y2 = self.patterns_canvas.coords(points[i])
                        x3, y3, x4, y4 = self.patterns_canvas.coords(points[j])
                        
                        # Calculate center points
                        cx1 = (x1 + x2) / 2
                        cy1 = (y1 + y2) / 2
                        cx2 = (x3 + x4) / 2
                        cy2 = (y3 + y4) / 2
                        
                        # Draw connection
                        self.patterns_canvas.create_line(
                            cx1, cy1, cx2, cy2,
                            fill=self.theme_manager.get_color('neural_connection'),
                            width=1,
                            tags="connection"
                        )
            
            # Add some labels
            self.patterns_canvas.create_text(
                width / 2, 30,
                text="Consciousness Pattern Analysis",
                fill=self.theme_manager.get_color('accent'),
                font=self.fonts['heading'],
                tags="label"
            )
            
            self.patterns_canvas.create_text(
                width / 2, height - 20,
                text="Patterns detected: 7 | Synchronicity index: High | Quantum coherence: 68%",
                fill=self.theme_manager.get_color('text_secondary'),
                font=self.fonts['normal'],
                tags="label"
            )
            
            # Update status
            self.status_text.config(text="Pattern analysis complete")
            
        except Exception as e:
            print(f"Error performing pattern analysis: {e}")
            self.patterns_canvas.delete("all")
            self.patterns_canvas.create_text(
                300, 150,
                text=f"Analysis error: {e}",
                fill=self.theme_manager.get_color('error'),
                font=self.fonts['normal'],
                justify='center'
            )

    def export_pattern_analysis(self):
        """Export the pattern analysis results"""
        try:
            # Create directory if it doesn't exist
            exports_dir = os.path.join("exports")
            if not os.path.exists(exports_dir):
                os.makedirs(exports_dir)
                
            # Create a timestamp for the filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"pattern_analysis_{timestamp}.txt"
            file_path = os.path.join(exports_dir, filename)
            
            # Create export data
            export_data = (
                "CONSCIOUSNESS PATTERN ANALYSIS\n"
                "==============================\n\n"
                f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"User: {self.user_data.get('username', 'Agent')}\n\n"
                "ANALYSIS RESULTS:\n"
                "----------------\n"
                "Patterns detected: 7\n"
                "Synchronicity index: High\n"
                "Quantum coherence: 68%\n"
                "Reality glitch frequency: 3.2 per day\n\n"
                "INTERPRETATION:\n"
                "-------------\n"
                "The analysis indicates a significant increase in consciousness expansion\n"
                "compared to baseline measurements. Synchronicity patterns suggest active\n"
                "engagement with quantum probability fields, potentially indicating\n"
                "increased awareness of simulation parameters.\n\n"
                "RECOMMENDATIONS:\n"
                "---------------\n"
                "1. Continue regular meditation practice with focus on quantum perception\n"
                "2. Document reality glitches with increased detail\n"
                "3. Explore the 'Lucid Dreaming' state for further consciousness expansion\n"
                "4. Consider connecting with other Project 89 agents to compare patterns\n\n"
                "NOTE: This analysis is generated for research purposes within Project 89.\n"
                "Individual results may vary based on consciousness development and\n"
                "simulation parameters in your local reality sector."
            )
            
            # Save to file
            with open(file_path, 'w') as f:
                f.write(export_data)
                
            # Update status
            self.status_text.config(text=f"Exported pattern analysis: {filename}")
            
            # Show confirmation
            messagebox.showinfo(
                "Export Complete", 
                f"Pattern analysis has been exported to:\n{file_path}"
            )
            
        except Exception as e:
            print(f"Error exporting pattern analysis: {e}")
            messagebox.showerror("Export Error", "Failed to export pattern analysis.")


if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = EnchantedMindMirror(root)
        root.mainloop()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
            