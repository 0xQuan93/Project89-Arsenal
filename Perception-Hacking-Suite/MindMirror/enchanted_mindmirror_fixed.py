import tkinter as tk
from tkinter import ttk, messagebox
import os
import json
import random
import time
import math
from datetime import datetime, timedelta
import pygame
from PIL import Image, ImageTk, ImageFilter
import numpy as np
import threading
import uuid

# Constants
VERSION = "1.0"
VERSION_NAME = "Cosmic Consciousness"

# Color palette
COSMIC_BLUE = "#0A1128"
MYSTICAL_PURPLE = "#7B2CBF"
AMBIENT_TEAL = "#4CC9F0"
MIND_GOLD = "#F7B801"
DEEP_THOUGHT = "#023E8A"
PEARL_WHITE = "#EEF4ED"
NEURAL_GREEN = "#39A776"
ATTENTION_RED = "#E63946"
COSMIC_INDIGO = "#170B5A"
ENERGY_CYAN = "#38FFE8"
ETHEREAL_PINK = "#FF7ECE"
COSMIC_GOLD = "#FFD700"
MIND_GREEN = "#218380"

def ensure_default_meditations():
    """Create default meditation files if none exist"""
    meditation_dir = "resources/meditations"
    
    if not os.path.exists(meditation_dir):
        os.makedirs(meditation_dir, exist_ok=True)
    
    default_meditations = {
        "cosmic_consciousness.txt": """Cosmic Consciousness Meditation

Find a comfortable position and close your eyes. Begin by taking deep breaths, in through your nose and out through your mouth.

With each breath, feel yourself becoming more relaxed, more at ease. Feel the weight of your body against the surface below you.

Now, visualize a point of light at the center of your being. With each breath, this light grows brighter and expands outward.

As the light expands, it begins to dissolve the boundaries of your physical body. Your consciousness starts to extend beyond your physical form.

Imagine your awareness extending outward, first filling the room around you, then the building, then the surrounding area.

Continue to expand your consciousness outward, encompassing your city, your country, the entire planet.

Feel your consciousness expanding further, out into space, embracing the planets, the solar system, the galaxy.

Your consciousness now extends throughout the universe, connecting with all forms of existence, all patterns of energy and matter.

You are one with the cosmic consciousness, the universal mind that permeates all of existence.

Remain in this state of expanded awareness, feeling the interconnectedness of all things.

When you are ready, slowly begin to bring your awareness back to your physical form, while maintaining a sense of connection with the greater cosmos.

Take a deep breath, and when you're ready, open your eyes, bringing this expanded awareness back into your daily life.""",

        "neural_pattern_exploration.txt": """Neural Pattern Exploration

Sit comfortably and close your eyes. Take several deep breaths, allowing your body to relax and your mind to become calm.

Now, bring your attention to your thoughts. Simply observe them as they arise, without judgment or attachment.

Visualize your thoughts as neural patterns, networks of light forming and dissolving within your mind.

As you observe these patterns, notice how they connect and interact with each other, forming complex networks of association and meaning.

Some patterns may appear bright and well-defined, representing clear and established thought patterns. Others may appear fainter, representing emerging or fading thoughts.

Without trying to change anything, simply observe the natural flow of these neural patterns. Notice how some thoughts trigger others, creating chains of association.

Now, imagine you can zoom out, seeing the entire landscape of your neural patterns from a distance. Observe the overall structure and organization of your thought patterns.

From this perspective, notice any areas of particular activity or density. These may represent areas of focus or concern in your life.

Now, bring your attention to the spaces between the neural patterns - the gaps of silence between thoughts. Allow yourself to rest in these spaces of pure awareness.

As you prepare to end this meditation, know that you can return to this perspective anytime, observing your thoughts as neural patterns from a place of calm awareness.

Take a deep breath, and when you're ready, gently open your eyes, carrying this awareness with you.""",

        "reality_perception.txt": """Reality Perception Meditation

Find a comfortable seated position and close your eyes. Take a few deep breaths, allowing your body to relax and your mind to settle.

Begin by bringing awareness to your immediate sensory experience - the sounds around you, the sensations in your body, the rhythm of your breath.

Now, consider that what you perceive as reality is actually your brain's interpretation of sensory input. Your perception is not reality itself, but your mind's construction of reality.

Imagine your consciousness as a field of awareness, receiving and interpreting signals from your environment.

Consider how your beliefs, expectations, and past experiences shape how you interpret these signals, creating your unique perception of reality.

Now, imagine temporarily letting go of your filters and interpretations. Imagine experiencing reality more directly, with fewer preconceptions.

As you sit in this space of open awareness, notice how reality might appear different when approached with fewer filters and judgments.

Recognize that everyone experiences their own constructed version of reality, shaped by their unique perspectives and experiences.

As you prepare to end this meditation, consider how you might carry this awareness of constructed perception into your daily life, approaching your experiences with more openness and flexibility.

Take a deep breath, and when you're ready, gently open your eyes, carrying this understanding with you."""
    }
    
    # Write default meditation files
    for filename, content in default_meditations.items():
        file_path = os.path.join(meditation_dir, filename)
        if not os.path.exists(file_path):
            try:
                with open(file_path, "w") as f:
                    f.write(content)
                print(f"Created default meditation: {filename}")
            except Exception as e:
                print(f"Error creating default meditation {filename}: {e}")

class EnchantedMindMirror:
    def __init__(self):
        # Initialize the main Tkinter window
        self.master = tk.Tk()
        self.master.title("PROJECT89: ENCHANTED MIND MIRROR")
        self.master.geometry("1200x800")
        self.master.minsize(1000, 700)
        self.master.configure(bg=COSMIC_BLUE)
        
        # Set up fonts
        self.title_font = ("Helvetica", 24, "bold")
        self.subtitle_font = ("Helvetica", 18)
        self.normal_font = ("Helvetica", 12)
        self.small_font = ("Helvetica", 10)
        
        # Initialize pygame mixer for sounds
        try:
            pygame.mixer.init()
            self.pygame_available = True
        except Exception as e:
            print(f"Warning: Could not initialize pygame mixer: {e}")
            print("Sound functionality will be disabled.")
            self.pygame_available = False
        self.ambient_playing = False
        
        # Create directories for resources
        self.ensure_directories()
        
        # Load or create default meditations
        ensure_default_meditations()
        
        # User data
        self.user_data = {
            "name": None,
            "journal_entries": [],
            "beliefs": [],
            "insights": [],
            "meditation_stats": {
                "sessions": 0,
                "total_minutes": 0,
                "last_meditation": None,
                "practice_streak": 0
            }
        }
        self.load_user_data()
        
        # Use grid layout for better control of positioning (replaces the main_container frame)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        # Create main UI frame directly in the window
        self.main_container = tk.Frame(self.master, bg=COSMIC_BLUE)
        self.main_container.grid(row=0, column=0, sticky="nsew")  # Position at top
        
        # Configure main container for grid layout
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)
        
        # Create stars for background directly in the main container
        self.background_canvas = tk.Canvas(self.main_container, bg=COSMIC_BLUE, highlightthickness=0)
        self.background_canvas.grid(row=0, column=0, sticky="nsew")  # Fill the space completely
        
        # Create stars for the background
        self.star_objects = []
        self.stars = []
        self.create_stars()
        
        # Start the star animation
        self.animate()
        
        # Check if user exists, if not show welcome screen
        if self.user_data["name"] is None:
            self.show_welcome_screen()
        else:
            self.create_ui()
            
    def ensure_directories(self):
        """Create necessary directories for the application"""
        directories = [
            "resources",
            "resources/sounds",
            "resources/images",
            "resources/fonts",
            "resources/meditations",
            "resources/journal",
            "user_data"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def create_stars(self):
        """Create a starfield for the cosmic background"""
        self.stars = []
        for i in range(200):
            x = random.randint(0, 1200)
            y = random.randint(0, 800)
            size = random.uniform(0.5, 3.0)
            brightness = random.uniform(0.7, 1.0)
            
            # Calculate RGB values based on brightness
            r = int(220 * brightness)
            g = int(220 * brightness)
            b = int(255 * brightness)
            
            star = {
                "x": x,
                "y": y,
                "size": size,
                "color": (r, g, b),
                "twinkle_speed": random.uniform(0.5, 3.0),
                "twinkle_offset": random.uniform(0, 2 * math.pi)
            }
            
            self.stars.append(star)
    
    def animate(self):
        """Animate the cosmic background with twinkling stars"""
        # Clear previous star objects
        for star_obj in self.star_objects:
            self.background_canvas.delete(star_obj)
        self.star_objects = []
        
        # Current time for animation
        t = time.time()
        
        # Draw each star with twinkling effect
        for star in self.stars:
            x, y = star["x"], star["y"]
            
            # Calculate twinkle factor
            twinkle = 0.3 + 0.7 * (0.5 + 0.5 * math.sin(t * star["twinkle_speed"] + star["twinkle_offset"]))
            
            # Draw the star
            r, g, b = star["color"]
            color = f"#{int(r * twinkle):02x}{int(g * twinkle):02x}{int(b * twinkle):02x}"
            
            star_obj = self.background_canvas.create_oval(
                x - star["size"], y - star["size"],
                x + star["size"], y + star["size"],
                fill=color, outline=""
            )
            
            self.star_objects.append(star_obj)
        
        # Continue animation
        self.master.after(50, self.animate)
    
    def show_welcome_screen(self):
        """Display the welcome screen to collect user information"""
        # Create a welcome frame directly on the root window (not in a canvas)
        self.welcome_frame = tk.Frame(self.master, bg=COSMIC_BLUE)
        self.welcome_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=500)
        
        # Title label
        title_label = tk.Label(
            self.welcome_frame, 
            text="Welcome to the Enchanted Mind Mirror",
            font=self.title_font,
            fg=MYSTICAL_PURPLE,
            bg=COSMIC_BLUE
        )
        title_label.pack(pady=(40, 30))
        
        # Description
        desc_text = "A journey into the depths of your consciousness awaits.\nThis tool will help you explore your mind, expand your awareness,\nand discover new dimensions of self-understanding."
        desc_label = tk.Label(
            self.welcome_frame,
            text=desc_text,
            font=self.normal_font,
            fg="white",
            bg=COSMIC_BLUE,
            justify="center"
        )
        desc_label.pack(pady=(0, 30))
        
        # Name entry frame
        name_frame = tk.Frame(self.welcome_frame, bg=COSMIC_BLUE)
        name_frame.pack(pady=20)
        
        name_label = tk.Label(
            name_frame,
            text="What shall we call you, explorer?",
            font=("Helvetica", 14),
            fg="white",
            bg=COSMIC_BLUE
        )
        name_label.pack(side=tk.TOP, pady=(0, 10))
        
        self.name_entry = tk.Entry(name_frame, width=30, font=self.normal_font)
        self.name_entry.pack(side=tk.TOP)
        
        # Start button
        start_button = tk.Button(
            self.welcome_frame,
            text="Begin the Journey",
            command=self.save_user_info,
            bg=MYSTICAL_PURPLE,
            fg="white",
            font=self.normal_font,
            padx=20,
            pady=8
        )
        start_button.pack(pady=(30, 0))
        
        # Add a quote
        quote_label = tk.Label(
            self.welcome_frame,
            text="\"The mind is like a mirror; it gathers dust while it reflects.\" — Zen proverb",
            font=("Georgia", 10, "italic"),
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        quote_label.pack(pady=(40, 0))
    
    def save_user_info(self):
        """Save user information from welcome screen"""
        name = self.name_entry.get().strip()
        if name:
            self.user_data["name"] = name
            self.save_user_data()
            self.welcome_frame.destroy()
            self.create_ui()
        else:
            messagebox.showwarning("Input Required", "Please enter your name to continue.")
    
    def create_ui(self):
        """Create the main user interface with tabs"""
        # Create a menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        
        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.master.quit)
        
        # Export menu
        export_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Export", menu=export_menu)
        export_menu.add_command(label="Export to Reality Glitcher", command=self.integrate_with_reality_glitcher)
        export_menu.add_command(label="Export to File", command=self.export_to_custom_location)
        export_menu.add_separator()
        export_menu.add_command(label="View Export History", command=self.show_export_history)
        
        # Integration menu
        integration_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Integration", menu=integration_menu)
        integration_menu.add_command(label="Connect with Project89 Tools", command=self.show_integration_options)
        
        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Version Info", command=lambda: messagebox.showinfo("Version", f"Mind Mirror {VERSION} ({VERSION_NAME})"))
        
        # Use grid layout for placing UI elements
        # Configure main_container for placing UI elements
        self.main_container.grid_rowconfigure(0, weight=1)  # Row for tab control
        self.main_container.grid_rowconfigure(1, weight=0)  # Row for status bar (smaller)
        self.main_container.grid_columnconfigure(0, weight=1)
        
        # Main tab control - placed at the top with no padding
        self.tab_control = ttk.Notebook(self.main_container)
        self.tab_control.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        
        # Apply custom styling to tabs - simpler style with minimal padding
        style = ttk.Style()
        style.configure("TNotebook", background=COSMIC_BLUE)
        style.configure("TNotebook.Tab", 
                       background=DEEP_THOUGHT, 
                       foreground=PEARL_WHITE, 
                       padding=[10, 2],  # Very minimal vertical padding
                       font=('Helvetica', 10))
        style.map("TNotebook.Tab", 
                 background=[("selected", MYSTICAL_PURPLE)],
                 foreground=[("selected", MIND_GOLD)])

        # Create tab frames using a consistent frame with a content container
        self.dashboard_tab = self.create_tab_container("Dashboard") 
        self.neural_patterns_tab = self.create_tab_container("Neural Patterns")
        self.consciousness_tab = self.create_tab_container("Consciousness Explorer")
        self.mind_tools_tab = self.create_tab_container("Mind Tools")
        
        # Add tabs to notebook
        self.tab_control.add(self.dashboard_tab, text="Dashboard")
        self.tab_control.add(self.neural_patterns_tab, text="Neural Patterns")
        self.tab_control.add(self.consciousness_tab, text="Consciousness Explorer")
        self.tab_control.add(self.mind_tools_tab, text="Mind Tools")
        
        # Add a callback for tab changes
        self.tab_control.bind("<<NotebookTabChanged>>", self.on_tab_change)
        
        # Create content for dashboard tab
        self.create_dashboard_tab()
        
        # Create content for neural patterns tab
        self.create_neural_patterns_tab()
        
        # Add content for other tabs
        self.create_placeholder_tabs()
        
        # Create status bar
        self.create_status_bar()
    
    def create_tab_container(self, title):
        """Creates a consistent container frame for each tab with proper spacing"""
        tab = tk.Frame(self.tab_control, bg=COSMIC_BLUE)
        
        # Configure the tab's grid
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_rowconfigure(1, weight=1)
        
        # Return the tab frame
        return tab
    
    def create_dashboard_tab(self):
        """Create the dashboard tab content"""
        # Clear any existing content
        for widget in self.dashboard_tab.winfo_children():
            widget.destroy()
        
        # Configure grid
        self.dashboard_tab.grid_columnconfigure(0, weight=1)
        
        # Welcome header - place at the very top with zero padding
        header_frame = tk.Frame(self.dashboard_tab, bg=COSMIC_BLUE)
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 5))
        
        welcome_text = f"Welcome back, {self.user_data['name']}"
        welcome_label = tk.Label(
            header_frame,
            text=welcome_text,
            font=self.title_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        welcome_label.pack(pady=(0, 0))  # No padding
        
        subtitle = "Your consciousness exploration dashboard"
        subtitle_label = tk.Label(
            header_frame,
            text=subtitle,
            font=("Helvetica", 14),
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        subtitle_label.pack(pady=(2, 0))  # Minimal padding
        
        # Main dashboard content
        content_frame = tk.Frame(self.dashboard_tab, bg=COSMIC_BLUE)
        content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=5)
        self.dashboard_tab.grid_rowconfigure(1, weight=1)  # Make content expandable
        
        # Left side - Stats and streak
        left_frame = tk.Frame(content_frame, bg=COSMIC_BLUE, width=300)  # Set fixed width
        left_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 20))
        left_frame.pack_propagate(False)  # Prevent shrinking
        
        # Practice streak
        streak_frame = tk.Frame(left_frame, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        streak_frame.pack(fill="x", pady=10, ipady=20)  # Increased internal padding
        
        streak_label = tk.Label(
            streak_frame,
            text="PRACTICE STREAK",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT
        )
        streak_label.pack(pady=(20, 10))  # Increased padding
        
        streak_count = tk.Label(
            streak_frame,
            text=str(self.user_data["meditation_stats"]["practice_streak"]),
            font=("Helvetica", 60, "bold"),  # Increased font size
            fg=MIND_GOLD,
            bg=DEEP_THOUGHT
        )
        streak_count.pack()
        
        streak_text = tk.Label(
            streak_frame,
            text="days in a row",
            font=self.small_font,
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT
        )
        streak_text.pack(pady=(5, 20))  # Increased padding
        
        # Right side - Recommendations
        right_frame = tk.Frame(content_frame, bg=COSMIC_BLUE)
        right_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=(20, 0))
        
        recommendations_label = tk.Label(
            right_frame,
            text="RECOMMENDED PRACTICES",
            font=self.subtitle_font,
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        recommendations_label.pack(anchor="w", pady=(0, 20))  # Increased bottom padding
        
        # Define recommendations with associated actions
        recommendations = [
            {
                "title": "Begin Your Meditation Practice",
                "description": "Regular meditation enhances self-awareness. Start with short sessions to build your practice.",
                "button_text": "Start Meditation",
                "command": lambda: self.tab_control.select(self.consciousness_tab)
            },
            {
                "title": "Record Your Insights",
                "description": "Journaling enhances reflection and consolidates insights. Document your inner journey.",
                "button_text": "Open Journal",
                "command": lambda: self.tab_control.select(self.mind_tools_tab)
            },
            {
                "title": "Explore Neural Patterns",
                "description": "Visualize how your thoughts connect to reveal deeper cognitive patterns.",
                "button_text": "View Patterns",
                "command": lambda: self.tab_control.select(self.neural_patterns_tab)
            }
        ]
        
        for rec in recommendations:
            rec_frame = tk.Frame(right_frame, bg=MYSTICAL_PURPLE, bd=1, relief=tk.RAISED)
            rec_frame.pack(fill="x", pady=10, ipady=10)  # Increased padding
            
            title = tk.Label(
                rec_frame,
                text=rec["title"],
                font=("Helvetica", 14, "bold"),
                fg=MIND_GOLD,
                bg=MYSTICAL_PURPLE,
                anchor="w"
            )
            title.pack(fill="x", padx=15, pady=(10, 5))  # Increased padding
            
            desc = tk.Label(
                rec_frame,
                text=rec["description"],
                font=self.small_font,
                fg=PEARL_WHITE,
                bg=MYSTICAL_PURPLE,
                anchor="w",
                justify="left",
                wraplength=380
            )
            desc.pack(fill="x", padx=15, pady=(0, 10))  # Increased padding
            
            button_frame = tk.Frame(rec_frame, bg=MYSTICAL_PURPLE)  # New frame for button alignment
            button_frame.pack(fill="x", padx=15, pady=(0, 10))
            
            button = tk.Button(
                button_frame,
                text=rec["button_text"],
                font=self.small_font,
                bg=COSMIC_BLUE,
                fg=PEARL_WHITE,
                bd=0,
                padx=10,  # Added padding to button
                pady=5,   # Added padding to button
                command=rec["command"],
                activebackground=AMBIENT_TEAL,  # Highlighted color when clicked
                activeforeground=PEARL_WHITE,  # Text color when clicked
                cursor="hand2"  # Hand cursor when hovering
            )
            button.pack(side=tk.RIGHT)  # Aligned to right
    
    def create_neural_patterns_tab(self):
        """Create the neural patterns visualization tab"""
        # Header frame
        header = tk.Frame(self.neural_patterns_tab, bg=COSMIC_BLUE)
        header.pack(fill="x", pady=(5, 5))  # Minimal top padding
        
        title = tk.Label(
            header,
            text="Neural Pattern Visualization",
            font=self.title_font,
            fg=NEURAL_GREEN,
            bg=COSMIC_BLUE
        )
        title.pack()
        
        description = tk.Label(
            header,
            text="Explore the interconnected patterns of your thoughts and consciousness.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        description.pack(pady=(5, 5))  # Minimal padding
        
        # Main content frame
        pattern_frame = tk.Frame(self.neural_patterns_tab, bg=COSMIC_INDIGO)
        pattern_frame.pack(fill="both", expand=True, padx=20, pady=(5, 10))  # Reduced padding
        
        # Visualization canvas
        self.pattern_canvas = tk.Canvas(
            pattern_frame,
            bg=COSMIC_INDIGO,
            highlightthickness=0,
            width=800,
            height=400
        )
        self.pattern_canvas.pack(pady=20, fill="both", expand=True)
        
        # Controls frame
        controls = tk.Frame(self.neural_patterns_tab, bg=COSMIC_BLUE)
        controls.pack(fill="x", padx=30, pady=20)
        
        # Pattern type selector
        pattern_type_frame = tk.Frame(controls, bg=COSMIC_BLUE)
        pattern_type_frame.pack(side=tk.LEFT, padx=10)
        
        pattern_label = tk.Label(
            pattern_type_frame,
            text="Pattern Type:",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        pattern_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.pattern_type = tk.StringVar(value="web")
        
        web_rb = tk.Radiobutton(
            pattern_type_frame,
            text="Neural Web",
            variable=self.pattern_type,
            value="web",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            selectcolor=COSMIC_INDIGO
        )
        web_rb.pack(side=tk.LEFT, padx=5)
        
        stream_rb = tk.Radiobutton(
            pattern_type_frame,
            text="Thought Stream",
            variable=self.pattern_type,
            value="stream",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            selectcolor=COSMIC_INDIGO
        )
        stream_rb.pack(side=tk.LEFT, padx=5)
        
        cloud_rb = tk.Radiobutton(
            pattern_type_frame,
            text="Concept Cloud",
            variable=self.pattern_type,
            value="cloud",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            selectcolor=COSMIC_INDIGO
        )
        cloud_rb.pack(side=tk.LEFT, padx=5)
        
        # Visualization button
        generate_btn = tk.Button(
            controls,
            text="Generate Pattern",
            font=self.normal_font,
            bg=MYSTICAL_PURPLE,
            fg=PEARL_WHITE,
            command=self.generate_neural_pattern
        )
        generate_btn.pack(side=tk.RIGHT, padx=10)
        
        # Initial pattern generation
        self.generate_neural_pattern()
    
    def create_status_bar(self):
        """Create status bar at the bottom of the application"""
        status_bar = tk.Frame(self.main_container, bg=DEEP_THOUGHT, height=25)
        status_bar.grid(row=1, column=0, sticky="ew")
        
        # Version info
        version_label = tk.Label(
            status_bar,
            text=f"Mind Mirror {VERSION} | {VERSION_NAME}",
            font=("Helvetica", 8),
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT
        )
        version_label.pack(side=tk.LEFT, padx=10)
        
        # Connection status
        self.connection_status = tk.Label(
            status_bar,
            text="Ready",
            font=("Helvetica", 8),
            fg=NEURAL_GREEN,
            bg=DEEP_THOUGHT
        )
        self.connection_status.pack(side=tk.RIGHT, padx=10)
    
    def show_integration_options(self):
        """Show integration options with other Project89 tools"""
        integration_window = tk.Toplevel(self.master)
        integration_window.title("Project89 Integration")
        integration_window.geometry("500x300")
        integration_window.configure(bg=COSMIC_BLUE)
        
        # Header
        header = tk.Label(
            integration_window,
            text="Perception-Hacking Suite Integration",
            font=self.title_font,
            fg=ENERGY_CYAN,
            bg=COSMIC_BLUE
        )
        header.pack(pady=(20, 10))
        
        description = tk.Label(
            integration_window,
            text="Connect Mind Mirror with other Project89 tools for enhanced perception exploration.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=450,
            justify=tk.CENTER
        )
        description.pack(pady=(0, 20))
        
        # Integration options
        tools_frame = tk.Frame(integration_window, bg=COSMIC_BLUE)
        tools_frame.pack(fill="both", expand=True, padx=20)
        
        # Reality Glitcher integration
        rg_frame = tk.Frame(tools_frame, bg=MYSTICAL_PURPLE, bd=1, relief=tk.RAISED)
        rg_frame.pack(fill="x", pady=5)
        
        rg_label = tk.Label(
            rg_frame,
            text="Reality Glitcher",
            font=self.subtitle_font,
            fg=ENERGY_CYAN,
            bg=MYSTICAL_PURPLE
        )
        rg_label.pack(anchor="w", padx=10, pady=(5, 0))
        
        rg_desc = tk.Label(
            rg_frame,
            text="Export your neural patterns to create targeted perception glitches.",
            font=self.small_font,
            fg=PEARL_WHITE,
            bg=MYSTICAL_PURPLE,
            justify=tk.LEFT,
            wraplength=450
        )
        rg_desc.pack(anchor="w", padx=10, pady=(0, 5))
        
        rg_btn = tk.Button(
            rg_frame,
            text="Connect with Reality Glitcher",
            font=self.small_font,
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            command=self.integrate_with_reality_glitcher
        )
        rg_btn.pack(anchor="e", padx=10, pady=5)
        
        # Close button
        close_btn = tk.Button(
            integration_window,
            text="Close",
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            command=integration_window.destroy
        )
        close_btn.pack(pady=20)
    
    def integrate_with_reality_glitcher(self):
        """Handle integration with Reality Glitcher"""
        # First check if Reality Glitcher exists in the Perception-Hacking Suite
        reality_glitcher_path = "../RealityGlitcher"
        
        if not os.path.exists(reality_glitcher_path):
            messagebox.showinfo(
                "Reality Glitcher Not Found",
                "Could not locate Reality Glitcher in the Perception-Hacking Suite directory.\n\n"
                "Make sure it's installed properly."
            )
            return
            
        # Create a progress window
        progress_window = tk.Toplevel(self.master)
        progress_window.title("Connecting to Reality Glitcher")
        progress_window.geometry("450x350")
        progress_window.configure(bg=COSMIC_BLUE)
        progress_window.resizable(False, False)
        progress_window.grab_set()  # Make the window modal
        
        # Center the window
        self._center_window(progress_window)
        
        # Progress content
        header = tk.Label(
            progress_window,
            text="Neural Pattern Export",
            font=self.title_font,
            fg=ENERGY_CYAN,
            bg=COSMIC_BLUE
        )
        header.pack(pady=(20, 10))
        
        # Status icon - will be updated based on success/failure
        status_frame = tk.Frame(progress_window, bg=COSMIC_BLUE)
        status_frame.pack(pady=10)
        
        status_canvas = tk.Canvas(
            status_frame, 
            width=60, 
            height=60, 
            bg=COSMIC_BLUE,
            highlightthickness=0
        )
        status_canvas.pack()
        
        # Initial blue circle as status indicator
        status_indicator = status_canvas.create_oval(5, 5, 55, 55, fill=AMBIENT_TEAL, outline="")
        
        # Generate neural pattern data for export
        neural_data = self.generate_export_data()
        
        # Show progress information
        status_label = tk.Label(
            progress_window,
            text="Initializing...",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=400
        )
        status_label.pack(pady=10)
        
        # Create progress indicator
        progress_frame = tk.Frame(progress_window, bg=COSMIC_BLUE)
        progress_frame.pack(pady=10)
        
        progress = ttk.Progressbar(
            progress_frame,
            orient="horizontal",
            length=300,
            mode="determinate"
        )
        progress.pack()
        
        # Details text area
        details_text = tk.Text(
            progress_window,
            height=5,
            width=50,
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            font=self.small_font,
            wrap=tk.WORD
        )
        details_text.pack(pady=10, padx=20, fill=tk.X)
        
        # Insert initial status message
        details_text.insert(tk.END, "Beginning integration with Reality Glitcher...\n")
        
        # Add close button (initially disabled)
        close_button = tk.Button(
            progress_window,
            text="Close",
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            command=progress_window.destroy,
            state=tk.DISABLED
        )
        close_button.pack(pady=20)
        
        # Run integration in the background
        def perform_integration():
            # Setup export paths
            imports_path = os.path.join(reality_glitcher_path, "imports")
            os.makedirs(imports_path, exist_ok=True)
            
            export_path = os.path.join(imports_path, "mind_mirror_data.json")
            
            # Mark with timestamp to avoid conflicts
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            export_path = os.path.join(imports_path, f"mind_mirror_data_{timestamp}.json")
            
            # Export metadata info
            export_info = {
                "exported_at": datetime.now().isoformat(),
                "source": "Mind Mirror",
                "version": VERSION,
                "nodes": len(neural_data["neural_patterns"]["nodes"]),
                "connections": len(neural_data["neural_patterns"]["connections"]),
                "user": self.user_data["name"]
            }
            
            # Update UI for each step
            steps = [
                "Generating neural pattern data",
                "Processing consciousness data",
                "Formatting for Reality Glitcher",
                "Establishing connection",
                "Transferring neural patterns"
            ]
            
            # Simulate steps with actual work between them
            for i, step in enumerate(steps):
                # Update progress
                progress["value"] = (i + 1) * 20
                status_label.config(text=step)
                
                # Do actual work for each step
                if i == 0:
                    # Generate data already done before this loop
                    details_text.insert(tk.END, f"✓ Neural pattern data generated: {len(neural_data['neural_patterns']['nodes'])} nodes\n")
                    progress_window.update()
                    time.sleep(0.5)
                elif i == 1:
                    # Add consciousness level info
                    details_text.insert(tk.END, f"✓ Consciousness level: {neural_data['metadata']['consciousness_level']:.2f}\n")
                    progress_window.update()
                    time.sleep(0.7)
                elif i == 2:
                    # Nothing to do, data already formatted
                    details_text.insert(tk.END, "✓ Data formatted for Reality Glitcher\n")
                    progress_window.update()
                    time.sleep(0.5)
                elif i == 3:
                    # Create directories if needed
                    try:
                        os.makedirs(imports_path, exist_ok=True)
                        details_text.insert(tk.END, f"✓ Connection established with Reality Glitcher\n")
                    except Exception as e:
                        details_text.insert(tk.END, f"✗ Error creating directories: {str(e)}\n")
                    progress_window.update()
                    time.sleep(0.8)
                elif i == 4:
                    # Actually export the data
                    try:
                        success, message = self.export_data_to_file(
                            neural_data, 
                            export_path, 
                            "Neural pattern data"
                        )
                        if success:
                            details_text.insert(tk.END, f"✓ Transfer complete! Data saved to Reality Glitcher.\n")
                            
                            # Also create a metadata file for RG to know what was imported
                            meta_path = os.path.join(imports_path, f"meta_{timestamp}.json")
                            with open(meta_path, "w") as f:
                                json.dump(export_info, f, indent=2)
                                
                            # Create a notification file for Reality Glitcher
                            notification_path = os.path.join(imports_path, ".new_import")
                            with open(notification_path, "w") as f:
                                f.write(timestamp)
                        else:
                            details_text.insert(tk.END, f"✗ Error: {message}\n")
                    except Exception as e:
                        details_text.insert(tk.END, f"✗ Error exporting data: {str(e)}\n")
                    progress_window.update()
            
            # Determine final status
            try:
                if os.path.exists(export_path):
                    # Success
                    status_canvas.itemconfig(status_indicator, fill=NEURAL_GREEN)
                    status_label.config(text="Integration Complete!", fg=NEURAL_GREEN)
                    
                    # Record this export in user data
                    if "exports" not in self.user_data:
                        self.user_data["exports"] = []
                        
                    self.user_data["exports"].append({
                        "timestamp": datetime.now().isoformat(),
                        "target": "Reality Glitcher",
                        "file": os.path.basename(export_path),
                        "nodes": len(neural_data["neural_patterns"]["nodes"]),
                        "connections": len(neural_data["neural_patterns"]["connections"])
                    })
                    self.save_user_data()
                    
                    # Show success message
                    messagebox.showinfo(
                        "Export Complete",
                        "Neural patterns have been successfully exported to Reality Glitcher!\n\n"
                        "You can now use these patterns in your Reality Glitcher experiments."
                    )
                else:
                    # Failure
                    status_canvas.itemconfig(status_indicator, fill=ATTENTION_RED)
                    status_label.config(text="Integration Failed", fg=ATTENTION_RED)
            except Exception as e:
                # Failure
                status_canvas.itemconfig(status_indicator, fill=ATTENTION_RED)
                status_label.config(text=f"Error: {str(e)}", fg=ATTENTION_RED)
                
            # Enable close button
            close_button.config(state=tk.NORMAL)
        
        # Start integration process in a separate thread to keep UI responsive
        threading.Thread(target=perform_integration, daemon=True).start()

    def _center_window(self, window):
        """Center a window on the screen"""
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")
        
    def generate_export_data(self):
        """Generate neural pattern data for export to Reality Glitcher"""
        # Create sample data structure that Reality Glitcher would understand
        export_data = {
            "source": "Mind Mirror",
            "version": VERSION,
            "version_name": VERSION_NAME,
            "timestamp": datetime.now().isoformat(),
            "user": self.user_data["name"],
            "neural_patterns": {
                "nodes": [],
                "connections": [],
                "metrics": self._generate_neural_metrics()
            },
            "metadata": {
                "pattern_type": "thought_web",
                "consciousness_level": random.uniform(0.7, 0.9),
                "color_scheme": "cosmic",
                "energy_signature": "alpha_theta_blend",
                "export_id": f"mm_export_{int(time.time())}",
                "session_duration": self._calculate_session_duration()
            }
        }
        
        # Generate nodes from user data - more comprehensive approach
        node_sources = []
        
        # Add beliefs if available
        if "beliefs" in self.user_data and self.user_data["beliefs"]:
            for belief in self.user_data["beliefs"]:
                node_sources.append({
                    "label": belief["belief"][:30], 
                    "type": "belief",
                    "strength": random.uniform(0.7, 1.0)
                })
        
        # Add journal insights if available
        if "journal_entries" in self.user_data and self.user_data["journal_entries"]:
            for entry in self.user_data["journal_entries"][:5]:  # Limit to 5 entries
                keywords = self._extract_keywords(entry.get("content", ""))
                for keyword in keywords[:2]:  # Take top 2 keywords
                    node_sources.append({
                        "label": keyword,
                        "type": "insight",
                        "strength": random.uniform(0.6, 0.9)
                    })
        
        # Add any specific insights recorded
        for insight in self.user_data.get("insights", []):
            node_sources.append({
                "label": insight,
                "type": "direct_insight",
                "strength": random.uniform(0.8, 1.0)
            })
        
        # Add base consciousness concepts
        consciousness_concepts = [
            "Perception", "Consciousness", "Reality", "Mind", "Time", "Space", 
            "Self", "Awareness", "Memory", "Identity", "Dream", "Existence"
        ]
        
        for concept in consciousness_concepts:
            node_sources.append({
                "label": concept,
                "type": "concept",
                "strength": random.uniform(0.5, 0.8)
            })
        
        # Ensure we don't have duplicate labels
        unique_nodes = {}
        for source in node_sources:
            if source["label"] not in unique_nodes:
                unique_nodes[source["label"]] = source
        
        # Generate nodes with positions in a network layout
        nodes = list(unique_nodes.values())
        random.shuffle(nodes)  # Randomize order
        nodes = nodes[:15]  # Limit to 15 nodes for visualization clarity
        
        # Generate positions using a simple force-directed layout simulation
        positions = self._generate_network_positions(len(nodes))
        
        # Create the final node objects
        for i, (node, position) in enumerate(zip(nodes, positions)):
            node_obj = {
                "id": i,
                "label": node["label"],
                "type": node["type"],
                "strength": node["strength"],
                "position": position
            }
            export_data["neural_patterns"]["nodes"].append(node_obj)
        
        # Generate connections between nodes - more nuanced connections
        num_nodes = len(export_data["neural_patterns"]["nodes"])
        if num_nodes > 1:
            # Create a more realistic network - not all nodes are connected
            # Each node should connect to 2-4 other nodes
            for i, node in enumerate(export_data["neural_patterns"]["nodes"]):
                # Determine number of connections for this node
                num_connections = random.randint(1, min(4, num_nodes-1))
                
                # Find potential targets (exclude self)
                potential_targets = [j for j in range(num_nodes) if j != i]
                random.shuffle(potential_targets)
                targets = potential_targets[:num_connections]
                
                for target in targets:
                    # Skip if this connection already exists in reverse
                    if any(c["source"] == target and c["target"] == i 
                           for c in export_data["neural_patterns"]["connections"]):
                        continue
                    
                    # Create connection with meaningful strength based on node types
                    source_node = export_data["neural_patterns"]["nodes"][i]
                    target_node = export_data["neural_patterns"]["nodes"][target]
                    
                    # Calculate connection strength based on node types
                    base_strength = random.uniform(0.3, 0.9)
                    if source_node["type"] == target_node["type"]:
                        # Same type nodes have stronger connections
                        strength = base_strength * 1.2
                    elif (source_node["type"] == "belief" and target_node["type"] == "concept") or \
                         (source_node["type"] == "concept" and target_node["type"] == "belief"):
                        # Beliefs and concepts have strong connections
                        strength = base_strength * 1.1
                    else:
                        strength = base_strength
                    
                    # Ensure it's within bounds
                    strength = min(1.0, max(0.1, strength))
                    
                connection = {
                        "source": i,
                    "target": target,
                        "strength": strength,
                        "type": self._determine_connection_type(source_node["type"], target_node["type"])
                }
                export_data["neural_patterns"]["connections"].append(connection)
        
        return export_data

    def _generate_neural_metrics(self):
        """Generate neural metrics based on user data"""
        # Calculate how much user has engaged with the system
        journal_count = len(self.user_data.get("journal_entries", []))
        belief_count = len(self.user_data.get("beliefs", []))
        meditation_minutes = self.user_data.get("meditation_stats", {}).get("total_minutes", 0)
        
        # Generate metrics
        metrics = {
            "coherence": min(1.0, max(0.3, 0.5 + (journal_count * 0.02) + (belief_count * 0.03))),
            "complexity": min(1.0, max(0.2, 0.4 + (belief_count * 0.04))),
            "resonance": min(1.0, max(0.3, 0.4 + (meditation_minutes * 0.001))),
            "energy": random.uniform(0.5, 0.9),
            "integration": min(1.0, max(0.2, 0.3 + (journal_count * 0.01) + (belief_count * 0.02) + (meditation_minutes * 0.0005)))
        }
        
        return metrics

    def _calculate_session_duration(self):
        """Calculate approximate session duration in minutes"""
        # This is just an estimate since we don't track actual session start time
        return random.randint(5, 30)

    def _extract_keywords(self, text):
        """Extract potential keywords from text content"""
        if not text:
            return []
            
        # Very simple keyword extraction - split and filter words
        common_words = {"and", "the", "is", "in", "of", "to", "a", "an", "that", "this", 
                       "it", "with", "for", "as", "on", "at", "by", "from", "was", "were"}
        
        words = text.lower().split()
        # Filter words: remove common words and short words, keep only alphabetic words
        filtered = [word for word in words if word not in common_words and len(word) > 4 and word.isalpha()]
        
        # Count frequency
        word_count = {}
        for word in filtered:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # Sort by frequency
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        
        # Take only the words, capitalize them
        return [word.capitalize() for word, count in sorted_words[:5]]

    def _generate_network_positions(self, num_nodes):
        """Generate positions for nodes in a network visualization"""
        positions = []
        
        if num_nodes <= 1:
            positions.append({"x": 0, "y": 0})
            return positions
        
        # Create positions in a circle first
        radius = 70
        for i in range(num_nodes):
            angle = (i / num_nodes) * 2 * math.pi
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            positions.append({"x": x, "y": y})
        
        # Add a little randomness to make it look more natural
        for pos in positions:
            pos["x"] += random.uniform(-15, 15)
            pos["y"] += random.uniform(-15, 15)
        
        return positions

    def _determine_connection_type(self, source_type, target_type):
        """Determine the type of connection based on the types of connected nodes"""
        if source_type == target_type:
            return "reinforcing"
        elif (source_type == "belief" and target_type == "concept") or \
             (source_type == "concept" and target_type == "belief"):
            return "conceptual"
        elif (source_type == "insight" or target_type == "insight"):
            return "revelatory"
        else:
            connection_types = ["associative", "causal", "temporal", "symbolic"]
            return random.choice(connection_types)

    def export_data_to_file(self, data, file_path, description="data"):
        """Export data to a file with error handling
        
        Args:
            data: The data to export (should be JSON serializable)
            file_path: The full path to save the file to
            description: Description of the data for error messages
        
        Returns:
            (success, message): Tuple with success boolean and message
        """
        try:
            # Ensure directory exists
            directory = os.path.dirname(file_path)
            os.makedirs(directory, exist_ok=True)
            
            # Write the data
            with open(file_path, "w") as f:
                json.dump(data, f, indent=2)
                
            return True, f"{description} exported successfully to {file_path}"
        except Exception as e:
            error_msg = f"Error exporting {description}: {str(e)}"
            print(error_msg)
            return False, error_msg

    def export_to_custom_location(self):
        """Export Mind Mirror data to a custom location"""
        # Create a file dialog
        from tkinter import filedialog
        
        # Generate the data
        export_data = self.generate_export_data()
        
        # Ask user for save location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
            title="Export Mind Mirror Data"
        )
        
        if not file_path:
            return  # User cancelled
            
        # Export the data
        success, message = self.export_data_to_file(export_data, file_path, "Mind Mirror neural pattern data")
        
        if success:
            messagebox.showinfo("Export Successful", message)
        else:
            messagebox.showerror("Export Failed", message)
    
    def generate_neural_pattern(self):
        """Generate a neural pattern visualization based on selected type"""
        pattern_type = self.pattern_type.get()
        
        # Clear the canvas
        self.pattern_canvas.delete("all")
        
        if pattern_type == "web":
            self.generate_neural_web()
        elif pattern_type == "stream":
            self.generate_thought_stream()
        else:  # cloud
            self.generate_concept_cloud()
    
    def generate_neural_web(self):
        """Generate a web-like neural pattern visualization"""
        width = 800
        height = 400
        
        # Create nodes
        nodes = []
        for i in range(8):
            x = random.randint(100, width-100)
            y = random.randint(100, height-100)
            size = random.randint(15, 30)
            
            node = self.pattern_canvas.create_oval(
                x-size, y-size, x+size, y+size,
                fill=ENERGY_CYAN,
                outline=PEARL_WHITE,
                width=2
            )
            
            # Node labels
            topics = ["Awareness", "Perception", "Identity", "Thoughts", 
                    "Beliefs", "Emotions", "Intuition", "Consciousness"]
            
            label = self.pattern_canvas.create_text(
                x, y,
                text=topics[i % len(topics)],
                fill=PEARL_WHITE,
                font=self.normal_font
            )
            
            nodes.append((x, y, node, label))
        
        # Connect nodes
        for i, (x1, y1, _, _) in enumerate(nodes):
            for j, (x2, y2, _, _) in enumerate(nodes):
                if i < j and random.random() < 0.4:
                    line = self.pattern_canvas.create_line(
                        x1, y1, x2, y2,
                        fill=ETHEREAL_PINK,
                        width=2,
                        dash=(4, 4)
                    )
    
    def generate_thought_stream(self):
        """Generate a flowing stream of thoughts visualization"""
        width = 800
        height = 400
        
        # Draw main flow paths
        for i in range(3):
            y_base = 100 + i * 100
            points = []
            
            for x in range(0, width+50, 50):
                y = y_base + random.randint(-20, 20)
                points.extend([x, y])
            
            # Create the flow path
            self.pattern_canvas.create_line(
                points,
                fill=MIND_GREEN,
                width=3,
                smooth=True
            )
            
            # Add thought bubbles along the stream
            num_thoughts = random.randint(2, 4)
            for _ in range(num_thoughts):
                x = random.randint(100, width-100)
                y = y_base + random.randint(-30, 30)
                size = random.randint(20, 40)
                
                bubble = self.pattern_canvas.create_oval(
                    x-size, y-size, x+size, y+size,
                    fill=COSMIC_INDIGO,
                    outline=MIND_GREEN,
                    width=2
                )
                
                thoughts = ["I wonder...", "Perhaps...", "What if...", 
                           "Maybe...", "I think...", "I feel..."]
                
                text = self.pattern_canvas.create_text(
                    x, y,
                    text=random.choice(thoughts),
                    fill=PEARL_WHITE,
                    font=self.normal_font
                )
    
    def generate_concept_cloud(self):
        """Generate a cloud visualization of concepts"""
        width = 800
        height = 400
        center_x = width // 2
        center_y = height // 2
        
        # Draw central concept
        central_radius = 50
        central = self.pattern_canvas.create_oval(
            center_x-central_radius, center_y-central_radius,
            center_x+central_radius, center_y+central_radius,
            fill=ETHEREAL_PINK,
            outline=PEARL_WHITE,
            width=3
        )
        
        central_text = self.pattern_canvas.create_text(
            center_x, center_y,
            text="Consciousness",
            fill=COSMIC_BLUE,
            font=self.title_font
        )
        
        # Create surrounding concepts
        concepts = ["Awareness", "Perception", "Memory", "Imagination", 
                   "Intuition", "Logic", "Emotion", "Identity"]
        
        for i, concept in enumerate(concepts):
            angle = i * 2 * math.pi / len(concepts)
            distance = 150
            
            x = center_x + distance * math.cos(angle)
            y = center_y + distance * math.sin(angle)
            
            # Draw concept circle
            radius = 30
            circle = self.pattern_canvas.create_oval(
                x-radius, y-radius, x+radius, y+radius,
                fill=COSMIC_GOLD,
                outline=PEARL_WHITE,
                width=2
            )
            
            # Concept label
            text = self.pattern_canvas.create_text(
                x, y,
                text=concept,
                fill=COSMIC_BLUE,
                font=self.normal_font
            )
            
            # Connect to center
            line = self.pattern_canvas.create_line(
                center_x, center_y, x, y,
                fill=PEARL_WHITE,
                width=2,
                dash=(6, 3)
            )
    
    def toggle_ambient_sound(self):
        """Toggle ambient sound on/off"""
        # Check if pygame is available
        if not hasattr(self, 'pygame_available') or not self.pygame_available:
            messagebox.showinfo(
                "Sound Not Available",
                "Sound functionality is not available. Pygame mixer could not be initialized."
            )
            return
            
        sound_path = "resources/sounds/ambient.mp3"
        
        # Check if sound file exists, if not show message
        if not os.path.exists(sound_path):
            messagebox.showinfo(
                "Sound Not Found",
                "Ambient sound file not found. Please add a file named 'ambient.mp3' to the resources/sounds directory."
            )
            return
        
        if self.ambient_playing:
            pygame.mixer.music.stop()
            self.ambient_playing = False
            self.sound_button.config(text="Sound: Off")
        else:
            try:
                pygame.mixer.music.load(sound_path)
                pygame.mixer.music.play(-1)  # Loop forever
                self.ambient_playing = True
                self.sound_button.config(text="Sound: On")
            except Exception as e:
                messagebox.showerror("Sound Error", f"Error playing sound: {str(e)}")
    
    def load_user_data(self):
        """Load user data from JSON file"""
        try:
            # Ensure user_data directory exists
            os.makedirs("user_data", exist_ok=True)
            
            user_data_path = "user_data/user_profile.json"
            if os.path.exists(user_data_path):
                with open(user_data_path, "r") as f:
                    loaded_data = json.load(f)
                    # Update user_data with loaded values, keeping defaults for missing values
                    for key, value in loaded_data.items():
                        self.user_data[key] = value
                print(f"User data loaded successfully from {user_data_path}")
            else:
                print(f"No existing user data found at {user_data_path}, using default values")
        except json.JSONDecodeError as e:
            # Handle corrupted JSON file
            self._handle_corrupted_data("user_data/user_profile.json", e)
        except Exception as e:
            print(f"Error loading user data: {str(e)}")
            print("Using default values")
    
    def save_user_data(self):
        """Save user data to JSON file with backup"""
        try:
            # Ensure user_data directory exists using absolute path
            user_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data")
            os.makedirs(user_data_dir, exist_ok=True)
            
            # Create a backup of the current file if it exists
            user_data_path = os.path.join(user_data_dir, "user_profile.json")
            if os.path.exists(user_data_path):
                backup_path = os.path.join(user_data_dir, f"user_profile_backup_{int(time.time())}.json")
                try:
                    with open(user_data_path, "r") as src:
                        with open(backup_path, "w") as dst:
                            dst.write(src.read())
                except Exception as e:
                    print(f"Warning: Could not create backup file: {str(e)}")
            
            # Save the current data
            with open(user_data_path, "w") as f:
                json.dump(self.user_data, f, indent=2)
            
            # Maintain max 5 backup files
            self._cleanup_backup_files(user_data_dir)
            
        except Exception as e:
            print(f"Error saving user data: {str(e)}")
            messagebox.showerror(
                "Data Save Error",
                f"Could not save your data: {str(e)}\nYour changes in this session may be lost."
            )

    def _handle_corrupted_data(self, file_path, error):
        """Handle corrupted data files by creating a backup and using defaults"""
        print(f"Error loading data from {file_path}: {str(error)}")
        try:
            # Rename the corrupted file instead of deleting it
            backup_path = f"{file_path}.corrupted_{int(time.time())}"
            os.rename(file_path, backup_path)
            print(f"Corrupted file backed up to {backup_path}")
            messagebox.showwarning(
                "Data Load Error",
                f"Your data file appears to be corrupted and could not be loaded. "
                f"A backup has been created at {backup_path}. "
                f"Default values will be used instead."
            )
        except Exception as e:
            print(f"Error handling corrupted data file: {str(e)}")

    def _cleanup_backup_files(self, user_data_dir):
        """Keep only the 5 most recent backup files"""
        try:
            # List all backup files
            backup_files = []
            for filename in os.listdir(user_data_dir):
                if filename.startswith("user_profile_backup_") and filename.endswith(".json"):
                    backup_files.append(os.path.join(user_data_dir, filename))
            
            # Sort by modification time, oldest first
            backup_files.sort(key=lambda x: os.path.getmtime(x))
            
            # Remove oldest files if we have more than 5 backups
            while len(backup_files) > 5:
                oldest = backup_files.pop(0)
                os.remove(oldest)
                
        except Exception as e:
            print(f"Warning: Could not clean up backup files: {str(e)}")

    def on_tab_change(self, event):
        """Handle tab change events to ensure proper rendering"""
        # Get the currently selected tab
        tab_id = self.tab_control.select()
        tab_name = self.tab_control.tab(tab_id, "text")
        print(f"Switched to {tab_name} tab")
        
        # Ensure proper redraw of the tab contents
        selected_tab = self.tab_control.nametowidget(tab_id)
        selected_tab.update()
    
    def create_placeholder_tabs(self):
        """Create content for tabs that aren't fully implemented yet"""
        # Create content for the Consciousness Explorer tab
        self.create_consciousness_explorer_tab()
        
        # Create content for the Mind Tools tab
        self.create_mind_tools_tab()

    def create_consciousness_explorer_tab(self):
        """Create the Consciousness Explorer tab with meditation and self-reflection tools"""
        # Main container
        main_frame = tk.Frame(self.consciousness_tab, bg=COSMIC_BLUE)
        main_frame.pack(fill="both", expand=True, padx=20, pady=5)  # Minimal padding
        
        # Header
        header_label = tk.Label(
            main_frame,
            text="Consciousness Explorer",
            font=self.title_font,
            fg=MYSTICAL_PURPLE,
            bg=COSMIC_BLUE
        )
        header_label.pack(pady=(0, 10))  # Reduced padding
        
        # Create a notebook for sub-tabs
        sub_tabs = ttk.Notebook(main_frame)
        
        # Apply custom styling to sub-tabs
        style = ttk.Style()
        style.configure("TNotebook.Tab", 
                       padding=[10, 5],  # Slightly smaller padding for sub-tabs
                       font=('Helvetica', 10))  # Slightly smaller font for sub-tabs
        
        # Create frames for sub-tabs
        meditation_frame = tk.Frame(sub_tabs, bg=COSMIC_BLUE)
        reflection_frame = tk.Frame(sub_tabs, bg=COSMIC_BLUE)
        
        # Add sub-tabs to notebook
        sub_tabs.add(meditation_frame, text="Meditation")
        sub_tabs.add(reflection_frame, text="Self-Reflection")
        
        # Pack the sub-tabs
        sub_tabs.pack(fill="both", expand=True, pady=10)  # Added vertical padding
        
        # Create meditation content
        self.create_meditation_content(meditation_frame)
        
        # Create self-reflection content
        self.create_self_reflection_content(reflection_frame)

    def create_meditation_content(self, parent_frame):
        """Create content for the meditation section"""
        # Main frame for meditation content
        meditation_main_frame = ttk.Frame(parent_frame)
        meditation_main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Header
        header_label = ttk.Label(
            meditation_main_frame, 
            text="Meditation Practice", 
            font=("Helvetica", 16, "bold"),
            foreground=MYSTICAL_PURPLE
        )
        header_label.pack(pady=(0, 20), anchor=tk.W)
        
        # Description
        description = (
            "Select a meditation practice to begin your journey inward. "
            "Each meditation focuses on different aspects of consciousness exploration."
        )
        desc_label = ttk.Label(
            meditation_main_frame, 
            text=description,
            wraplength=600,
            font=("Helvetica", 11)
        )
        desc_label.pack(pady=(0, 20), anchor=tk.W)
        
        # Create two frames for content organization
        left_frame = ttk.Frame(meditation_main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        right_frame = ttk.Frame(meditation_main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Meditation list (left)
        list_frame = ttk.LabelFrame(left_frame, text="Available Meditations")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Get available meditations using get_available_meditations() instead of load_meditations()
        self.meditation_listbox = tk.Listbox(
            list_frame,
            height=10,
            selectbackground=MYSTICAL_PURPLE,
            activestyle='none',
            exportselection=False
        )
        self.meditation_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add scrollbar
        meditation_scrollbar = ttk.Scrollbar(self.meditation_listbox, orient="vertical")
        meditation_scrollbar.config(command=self.meditation_listbox.yview)
        meditation_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.meditation_listbox.config(yscrollcommand=meditation_scrollbar.set)
        
        # Populate the meditation list
        meditations = self.get_available_meditations()
        for meditation in meditations:
            self.meditation_listbox.insert(tk.END, meditation['title'])
        
        if self.meditation_listbox.size() > 0:
            self.meditation_listbox.selection_set(0)
        
        self.meditation_listbox.bind('<<ListboxSelect>>', self.on_meditation_select)
        
        # Meditation details (right)
        details_frame = ttk.LabelFrame(right_frame, text="Meditation Details")
        details_frame.pack(fill=tk.BOTH, expand=True)
        
        # Details content
        details_content = ttk.Frame(details_frame)
        details_content.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Title
        self.meditation_title_var = tk.StringVar()
        title_label = ttk.Label(
            details_content,
            textvariable=self.meditation_title_var,
            font=("Helvetica", 12, "bold"),
            foreground=MYSTICAL_PURPLE
        )
        title_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Duration
        duration_frame = ttk.Frame(details_content)
        duration_frame.pack(fill=tk.X, pady=(0, 10))
        
        duration_label = ttk.Label(
            duration_frame,
            text="Duration:",
            font=("Helvetica", 11),
            width=10
        )
        duration_label.pack(side=tk.LEFT)
        
        self.meditation_duration_var = tk.StringVar()
        duration_value = ttk.Label(
            duration_frame,
            textvariable=self.meditation_duration_var,
            font=("Helvetica", 11)
        )
        duration_value.pack(side=tk.LEFT)
        
        # Type
        type_frame = ttk.Frame(details_content)
        type_frame.pack(fill=tk.X, pady=(0, 10))
        
        type_label = ttk.Label(
            type_frame,
            text="Type:",
            font=("Helvetica", 11),
            width=10
        )
        type_label.pack(side=tk.LEFT)
        
        self.meditation_type_var = tk.StringVar()
        type_value = ttk.Label(
            type_frame,
            textvariable=self.meditation_type_var,
            font=("Helvetica", 11)
        )
        type_value.pack(side=tk.LEFT)
        
        # Description
        desc_frame = ttk.Frame(details_content)
        desc_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        desc_label = ttk.Label(
            desc_frame,
            text="Description:",
            font=("Helvetica", 11),
            width=10
        )
        desc_label.pack(anchor=tk.NW)
        
        self.meditation_desc_var = tk.StringVar()
        self.meditation_desc_text = tk.Text(
            desc_frame,
            wrap=tk.WORD,
            height=6,
            width=40,
            font=("Helvetica", 11),
            background="#F0F0F0",
            relief=tk.FLAT,
            state=tk.DISABLED
        )
        self.meditation_desc_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Start button
        start_button = ttk.Button(
            details_content,
            text="Begin Meditation",
            command=self.start_meditation,
            style="Accent.TButton"
        )
        start_button.pack(pady=(10, 0))
        
        # Select the first meditation by default
        if self.meditation_listbox.size() > 0:
            self.on_meditation_select(None)
    
    def create_self_reflection_content(self, parent_frame):
        """Create self-reflection content in the given frame"""
        # Header
        header = tk.Label(
            parent_frame,
            text="Self-Reflection Practice",
            font=self.subtitle_font,
            fg=ENERGY_CYAN,
            bg=COSMIC_BLUE
        )
        header.pack(pady=(20, 10))
        
        # Description
        description = tk.Label(
            parent_frame,
            text="Deepen your self-understanding through guided reflection prompts.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=600
        )
        description.pack(pady=(0, 20))
        
        # Main content frame
        content_frame = tk.Frame(parent_frame, bg=COSMIC_BLUE)
        content_frame.pack(fill="both", expand=True, padx=20)
        
        # Prompt frame
        prompt_frame = tk.Frame(content_frame, bg=MYSTICAL_PURPLE, bd=1, relief=tk.RAISED)
        prompt_frame.pack(fill="x", pady=10)
        
        prompt_label = tk.Label(
            prompt_frame,
            text="REFLECTION PROMPT",
            font=self.normal_font,
            fg=ENERGY_CYAN,
            bg=MYSTICAL_PURPLE
        )
        prompt_label.pack(pady=(10, 5))
        
        # Initialize reflection prompts
        self.reflection_prompts = [
            "What patterns of thought do you notice recurring in your daily life?",
            "How do your beliefs about reality shape what you perceive as possible?",
            "In what ways does your sense of self shift throughout the day?",
            "What aspects of your consciousness seem most fundamental to who you are?",
            "How would your experience change if you could perceive beyond your current sensory limits?",
            "What beliefs do you hold that might be limiting your perception?",
            "How do your emotions influence your perception of reality?",
            "What would it mean to truly understand consciousness?",
            "How do you know what is real versus what is illusion?",
            "In what ways are you more than your thoughts and feelings?"
        ]
        self.current_prompt = random.choice(self.reflection_prompts)
        
        # Display the prompt
        self.prompt_display = tk.Label(
            prompt_frame,
            text=f'"{self.current_prompt}"',
            font=("Georgia", 12, "italic"),
            fg=PEARL_WHITE,
            bg=MYSTICAL_PURPLE,
            wraplength=600,
            justify=tk.CENTER
        )
        self.prompt_display.pack(pady=(0, 10), padx=20)
        
        # New prompt button
        new_prompt_btn = tk.Button(
            prompt_frame,
            text="New Prompt",
            font=self.small_font,
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            command=self.new_reflection_prompt
        )
        new_prompt_btn.pack(pady=(0, 10))
        
        # Reflection input frame
        reflection_input_frame = tk.Frame(content_frame, bg=COSMIC_BLUE)
        reflection_input_frame.pack(fill="both", expand=True, pady=10)
        
        # Text area for reflection
        self.reflection_text = tk.Text(
            reflection_input_frame,
            font=("Helvetica", 12),
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            wrap=tk.WORD,
            height=10,
            width=80,
            padx=10,
            pady=10
        )
        self.reflection_text.pack(fill="both", expand=True, pady=10)
        
        # Save button
        save_frame = tk.Frame(content_frame, bg=COSMIC_BLUE)
        save_frame.pack(fill="x", pady=10)
        
        save_btn = tk.Button(
            save_frame,
            text="Save Reflection",
            font=self.normal_font,
            bg=NEURAL_GREEN,
            fg=PEARL_WHITE,
            command=self.save_reflection
        )
        save_btn.pack(side=tk.RIGHT, padx=10)

    def create_mind_tools_tab(self):
        """Create the Mind Tools tab with various consciousness tools"""
        # Clear any existing widgets
        for widget in self.mind_tools_tab.winfo_children():
            widget.destroy()
            
        # Apply a grid layout for more control
        self.mind_tools_tab.grid_columnconfigure(0, weight=1)
        self.mind_tools_tab.grid_rowconfigure(1, weight=1)
        
        # Header
        header_label = tk.Label(
            self.mind_tools_tab,
            text="Mind Tools",
            font=self.title_font,
            fg=MYSTICAL_PURPLE,
            bg=COSMIC_BLUE
        )
        header_label.grid(row=0, column=0, sticky="ew", pady=(0, 3))  # Minimal top padding
        
        # Create a notebook for sub-tabs with lower height
        sub_tabs = ttk.Notebook(self.mind_tools_tab)
        
        # Style for subtabs - more compact
        style = ttk.Style()
        style.configure("MindTools.TNotebook", padding=0)
        style.configure("MindTools.TNotebook.Tab", padding=(8, 2))
        
        # Create frames for sub-tabs
        journal_frame = tk.Frame(sub_tabs, bg=COSMIC_BLUE)
        beliefs_frame = tk.Frame(sub_tabs, bg=COSMIC_BLUE)
        integration_frame = tk.Frame(sub_tabs, bg=COSMIC_BLUE)
        
        # Add sub-tabs to notebook
        sub_tabs.add(journal_frame, text="Journal")
        sub_tabs.add(beliefs_frame, text="Belief Examination")
        sub_tabs.add(integration_frame, text="Integration")
        
        # Grid the notebook with weight to expand
        sub_tabs.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        # Create journal content
        self.create_journal_content(journal_frame)
        
        # Create beliefs content
        self.create_beliefs_content(beliefs_frame)
        
        # Create integration content
        self.create_integration_content(integration_frame)

    def create_journal_content(self, parent_frame):
        """Create content for the journal section"""
        # Create a frame for journal content
        journal_main_frame = ttk.Frame(parent_frame)
        journal_main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Header
        header_label = ttk.Label(
            journal_main_frame, 
            text="Consciousness Journal", 
            font=("Helvetica", 16, "bold"),
            foreground=MYSTICAL_PURPLE
        )
        header_label.pack(pady=(0, 20), anchor=tk.W)
        
        # Description
        description = (
            "Record your insights, experiences, and reflections on your consciousness exploration. "
            "Your journal entries are stored securely and can be reviewed at any time."
        )
        desc_label = ttk.Label(
            journal_main_frame, 
            text=description,
            wraplength=600,
            font=("Helvetica", 11)
        )
        desc_label.pack(pady=(0, 20), anchor=tk.W)
        
        # Create list and detail frames
        list_frame = ttk.LabelFrame(journal_main_frame, text="Journal Entries")
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Journal entries list
        self.journal_listbox = tk.Listbox(
            list_frame,
            height=15,
            selectbackground=MYSTICAL_PURPLE,
            activestyle='none',
            exportselection=False
        )
        self.journal_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add scrollbar to listbox
        journal_scrollbar = ttk.Scrollbar(self.journal_listbox, orient="vertical")
        journal_scrollbar.config(command=self.journal_listbox.yview)
        journal_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.journal_listbox.config(yscrollcommand=journal_scrollbar.set)
        
        # Load journal entries
        self.load_journal_entries()
        
        # Buttons for journal management
        button_frame = ttk.Frame(list_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        new_button = ttk.Button(
            button_frame,
            text="New Entry",
            command=self.new_journal_entry,
            style="Accent.TButton"
        )
        new_button.pack(side=tk.LEFT, padx=(0, 5))
        
        view_button = ttk.Button(
            button_frame,
            text="View",
            command=self.view_journal_entry
        )
        view_button.pack(side=tk.LEFT, padx=5)
        
        edit_button = ttk.Button(
            button_frame,
            text="Edit",
            command=self.edit_journal_entry
        )
        edit_button.pack(side=tk.LEFT, padx=5)
        
        delete_button = ttk.Button(
            button_frame,
            text="Delete",
            command=self.delete_journal_entry
        )
        delete_button.pack(side=tk.LEFT, padx=5)
        
        # Detail frame (preview of selected entry)
        detail_frame = ttk.LabelFrame(journal_main_frame, text="Entry Preview")
        detail_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Preview content
        self.preview_title = ttk.Label(
            detail_frame,
            text="Select an entry to preview",
            font=("Helvetica", 12, "bold"),
            foreground=MYSTICAL_PURPLE
        )
        self.preview_title.pack(anchor=tk.W, padx=15, pady=(15, 5))
        
        self.preview_date = ttk.Label(
            detail_frame,
            text="",
            font=("Helvetica", 10),
            foreground="gray"
        )
        self.preview_date.pack(anchor=tk.W, padx=15, pady=(0, 10))
        
        # Preview text
        self.preview_text = tk.Text(
            detail_frame,
            wrap=tk.WORD,
            height=12,
            width=40,
            font=("Helvetica", 11),
            background="#F0F0F0",
            relief=tk.FLAT,
            state=tk.DISABLED
        )
        self.preview_text.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        # Bind selection event
        self.journal_listbox.bind('<<ListboxSelect>>', self.on_journal_selection)
    
    def create_beliefs_content(self, parent_frame):
        """Create belief examination content in the given frame"""
        # Header
        header = tk.Label(
            parent_frame,
            text="Belief Examination",
            font=self.subtitle_font,
            fg=ENERGY_CYAN,
            bg=COSMIC_BLUE
        )
        header.pack(pady=(20, 10))
        
        # Description
        description = tk.Label(
            parent_frame,
            text="Examine and question your beliefs to understand how they shape your perception of reality.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=600
        )
        description.pack(pady=(0, 20))
        
        # Main content split into two sections
        content_frame = tk.Frame(parent_frame, bg=COSMIC_BLUE)
        content_frame.pack(fill="both", expand=True, padx=20)
        
        # Top section - New belief examination
        new_frame = tk.Frame(content_frame, bg=MYSTICAL_PURPLE)
        new_frame.pack(fill="x", pady=(0, 10))
        
        new_label = tk.Label(
            new_frame,
            text="EXAMINE A BELIEF",
            font=self.normal_font,
            fg=ENERGY_CYAN,
            bg=MYSTICAL_PURPLE
        )
        new_label.pack(pady=(15, 10), padx=20)
        
        # Entry for belief
        entry_frame = tk.Frame(new_frame, bg=MYSTICAL_PURPLE)
        entry_frame.pack(fill="x", padx=20, pady=(0, 10))
        
        belief_label = tk.Label(
            entry_frame,
            text="Enter a belief to examine:",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=MYSTICAL_PURPLE
        )
        belief_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.belief_entry = tk.Entry(
            entry_frame,
            font=self.normal_font,
            width=40
        )
        self.belief_entry.pack(side=tk.LEFT, fill="x", expand=True)
        
        # Examine button
        examine_btn = tk.Button(
            new_frame,
            text="Examine This Belief",
            font=self.normal_font,
            bg=NEURAL_GREEN,
            fg=PEARL_WHITE,
            command=lambda: self.examine_belief()
        )
        examine_btn.pack(pady=(0, 15))
        
        # Bottom section - Saved beliefs
        saved_frame = tk.Frame(content_frame, bg=MYSTICAL_PURPLE)
        saved_frame.pack(fill="both", expand=True)
        
        saved_label = tk.Label(
            saved_frame,
            text="YOUR EXAMINED BELIEFS",
            font=self.subtitle_font,
            fg=ENERGY_CYAN,
            bg=MYSTICAL_PURPLE
        )
        saved_label.pack(pady=(15, 10), padx=20)
        
        # Create a frame for the listbox and scrollbar
        list_frame = tk.Frame(saved_frame, bg=MYSTICAL_PURPLE)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for saved beliefs
        self.beliefs_listbox = tk.Listbox(
            list_frame,
            font=self.normal_font,
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            selectbackground=ETHEREAL_PINK,
            height=10,
            width=40,
            yscrollcommand=scrollbar.set
        )
        self.beliefs_listbox.pack(side=tk.LEFT, fill="both", expand=True)
        
        # Configure the scrollbar
        scrollbar.config(command=self.beliefs_listbox.yview)
        
        # Populate with existing beliefs
        self.load_beliefs()
        
        # Delete button
        delete_btn = tk.Button(
            saved_frame,
            text="Delete Selected",
            font=self.small_font,
            bg=ATTENTION_RED,
            fg=PEARL_WHITE,
            command=self.delete_belief
        )
        delete_btn.pack(anchor="e", padx=20, pady=10)

    def create_integration_content(self, parent_frame):
        """Create integration content in the given frame"""
        # Clear existing widgets
        for widget in parent_frame.winfo_children():
            widget.destroy()
            
        # Configure grid for better control
        parent_frame.grid_columnconfigure(0, weight=1)
        
        # Simplified description with smaller font
        description = tk.Label(
            parent_frame,
            text="Connect Mind Mirror with other consciousness exploration tools",
            font=("Helvetica", 10),
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            anchor="w"
        )
        description.grid(row=0, column=0, sticky="ew", padx=5, pady=3)
        
        # Create a canvas with scrollbar for potential overflow
        canvas = tk.Canvas(parent_frame, bg=COSMIC_BLUE, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
        content_frame = tk.Frame(canvas, bg=COSMIC_BLUE)
        
        # Configure scrolling
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        scrollbar.grid(row=1, column=1, sticky="ns")
        parent_frame.grid_rowconfigure(1, weight=1)
        
        # Create window in canvas for content
        canvas_window = canvas.create_window((0, 0), window=content_frame, anchor="nw")
        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width))
        
        # Reality Glitcher integration - more compact layout
        rg_frame = tk.Frame(content_frame, bg=MYSTICAL_PURPLE, bd=1, relief=tk.RAISED)
        rg_frame.pack(fill="x", pady=5, ipady=0)
        
        # Header and button in same row
        header_frame = tk.Frame(rg_frame, bg=MYSTICAL_PURPLE)
        header_frame.pack(fill="x", padx=5, pady=2)
        
        rg_label = tk.Label(
            header_frame,
            text="Reality Glitcher",
            font=("Helvetica", 12, "bold"),
            fg=ENERGY_CYAN,
            bg=MYSTICAL_PURPLE
        )
        rg_label.pack(side=tk.LEFT, anchor="w", padx=5)
        
        rg_btn = tk.Button(
            header_frame,
            text="Connect",
            font=("Helvetica", 9),
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            command=self.integrate_with_reality_glitcher,
            padx=5,
            pady=1
        )
        rg_btn.pack(side=tk.RIGHT, padx=5)
        
        # Description
        rg_desc = tk.Label(
            rg_frame,
            text="Export neural patterns for targeted perception glitches. Your consciousness patterns influence reality distortion.",
            font=("Helvetica", 9),
            fg=PEARL_WHITE,
            bg=MYSTICAL_PURPLE,
            wraplength=500,
            justify=tk.LEFT
        )
        rg_desc.pack(fill="x", padx=10, pady=(0, 8), anchor="w")
        
        # Future integrations - more compact
        future_frame = tk.Frame(content_frame, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        future_frame.pack(fill="x", pady=5)
        
        future_label = tk.Label(
            future_frame,
            text="Future Integrations",
            font=("Helvetica", 12, "bold"),
            fg=ENERGY_CYAN,
            bg=DEEP_THOUGHT
        )
        future_label.pack(anchor="w", padx=10, pady=(5, 0))
        
        future_desc = tk.Label(
            future_frame,
            text="Additional integration options will be available in future updates.",
            font=("Helvetica", 9),
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT,
            wraplength=500,
            justify=tk.LEFT
        )
        future_desc.pack(anchor="w", padx=10, pady=(0, 5))
    
    def create_self_reflection_tab(self):
        """Create the self-reflection tab with interactive prompts"""
        # Header frame
        header = tk.Frame(self.reflection_tab, bg=COSMIC_BLUE)
        header.pack(fill="x", pady=(20, 10))
        
        title_label = tk.Label(
            header,
            text="Self-Reflection",
            font=self.title_font,
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        title_label.pack()
        
        desc_label = tk.Label(
            header,
            text="Record and analyze your self-reflections to deepen self-awareness.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=700
        )
        desc_label.pack(pady=(5, 20))
        
        # Main content frame
        content_frame = tk.Frame(self.reflection_tab, bg=COSMIC_BLUE)
        content_frame.pack(fill="both", expand=True, padx=40, pady=10)
        
        # Reflection prompts section
        prompts_frame = tk.Frame(content_frame, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        prompts_frame.pack(fill="x", pady=10)
        
        prompts_label = tk.Label(
            prompts_frame,
            text="REFLECTION PROMPTS",
            font=self.subtitle_font,
            fg=AMBIENT_TEAL,
            bg=DEEP_THOUGHT
        )
        prompts_label.pack(anchor="w", padx=20, pady=10)
        
        # List of reflection prompts
        self.reflection_prompts = [
            "What patterns of thought have you noticed today?",
            "How has your perspective shifted recently?",
            "What beliefs are limiting your growth?",
            "What insights have emerged from your meditation practice?",
            "How do your emotions affect your perception of reality?",
            "What aspects of yourself have you been avoiding examining?",
            "How does your sense of identity influence your decisions?",
            "What recurring thoughts occupy your consciousness?"
        ]
        
        # Randomly select a prompt
        self.current_prompt = random.choice(self.reflection_prompts)
        
        # Display the current prompt
        self.prompt_display = tk.Label(
            prompts_frame,
            text=f'"{self.current_prompt}"',
            font=("Helvetica", 14, "italic"),
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT,
            wraplength=700,
            justify=tk.LEFT
        )
        self.prompt_display.pack(fill="x", padx=20, pady=(0, 10))
        
        # Button to get a new prompt
        new_prompt_btn = tk.Button(
            prompts_frame,
            text="New Prompt",
            font=self.normal_font,
            bg=MYSTICAL_PURPLE,
            fg=PEARL_WHITE,
            command=self.new_reflection_prompt
        )
        new_prompt_btn.pack(anchor="e", padx=20, pady=10)
        
        # Reflection area
        reflection_input_frame = tk.Frame(content_frame, bg=COSMIC_BLUE)
        reflection_input_frame.pack(fill="both", expand=True, pady=20)
        
        reflection_label = tk.Label(
            reflection_input_frame,
            text="YOUR REFLECTION",
            font=self.subtitle_font,
            fg=MIND_GOLD,
            bg=COSMIC_BLUE
        )
        reflection_label.pack(anchor="w")
        
        # Text area for reflection
        self.reflection_text = tk.Text(
            reflection_input_frame,
            font=("Helvetica", 12),
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            wrap=tk.WORD,
            height=10,
            width=80,
            padx=10,
            pady=10
        )
        self.reflection_text.pack(fill="both", expand=True, pady=10)
        
        # Save button
        save_frame = tk.Frame(content_frame, bg=COSMIC_BLUE)
        save_frame.pack(fill="x", pady=10)
        
        save_btn = tk.Button(
            save_frame,
            text="Save Reflection",
            font=self.normal_font,
            bg=NEURAL_GREEN,
            fg=PEARL_WHITE,
            command=self.save_reflection
        )
        save_btn.pack(side=tk.RIGHT, padx=10)
        
    def new_reflection_prompt(self):
        """Display a new reflection prompt"""
        new_prompt = random.choice(self.reflection_prompts)
        # Make sure we don't get the same prompt twice
        while new_prompt == self.current_prompt:
            new_prompt = random.choice(self.reflection_prompts)
        
        self.current_prompt = new_prompt
        self.prompt_display.config(text=f'"{self.current_prompt}"')
    
    def save_reflection(self):
        """Save the user's reflection to their journal"""
        reflection_text = self.reflection_text.get("1.0", tk.END).strip()
        
        if not reflection_text:
            messagebox.showinfo("Empty Reflection", "Please enter your reflection before saving.")
            return
        
        # Create timestamp for the reflection
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create reflection entry
        reflection_entry = {
            "timestamp": timestamp,
            "prompt": self.current_prompt,
            "content": reflection_text
        }
        
        # Add to user's journal entries
        if "journal_entries" not in self.user_data:
            self.user_data["journal_entries"] = []
        
        self.user_data["journal_entries"].append(reflection_entry)
        
        # Save user data
        self.save_user_data()
        
        # Give feedback
        messagebox.showinfo(
            "Reflection Saved",
            "Your reflection has been saved to your journal."
        )
        
        # Clear the text area
        self.reflection_text.delete("1.0", tk.END)
        
        # Show a new prompt
        self.new_reflection_prompt()

    def create_meditation_tab(self):
        """Create the meditation (consciousness expansion) tab"""
        # Header frame
        header = tk.Frame(self.meditation_tab, bg=COSMIC_BLUE)
        header.pack(fill="x", pady=(20, 10))
        
        title_label = tk.Label(
            header,
            text="Consciousness Expansion",
            font=self.title_font,
            fg=MIND_GOLD,
            bg=COSMIC_BLUE
        )
        title_label.pack()
        
        desc_label = tk.Label(
            header,
            text="Guided meditation practices to expand your consciousness and mindfulness.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=700
        )
        desc_label.pack(pady=(5, 20))
        
        # Main content area
        content_frame = tk.Frame(self.meditation_tab, bg=COSMIC_BLUE)
        content_frame.pack(fill="both", expand=True, padx=40, pady=10)
        
        # Left panel - Meditation selection
        left_panel = tk.Frame(content_frame, bg=COSMIC_BLUE)
        left_panel.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 20))
        
        # Meditation selection header
        select_label = tk.Label(
            left_panel,
            text="SELECT MEDITATION",
            font=self.subtitle_font,
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        select_label.pack(anchor="w", pady=(0, 10))
        
        # List of available meditations
        self.available_meditations = self.get_available_meditations()
        self.meditation_listbox = tk.Listbox(
            left_panel,
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            selectbackground=MYSTICAL_PURPLE,
            height=10,
            selectmode=tk.SINGLE
        )
        self.meditation_listbox.pack(fill="both", expand=True)
        
        # Populate the listbox
        for meditation in self.available_meditations:
            self.meditation_listbox.insert(tk.END, meditation["name"])
        
        # If we have meditations, select the first one
        if self.available_meditations:
            self.meditation_listbox.selection_set(0)
            self.meditation_listbox.bind("<<ListboxSelect>>", self.on_meditation_select)
        
        # Right panel - Meditation details and controls
        right_panel = tk.Frame(content_frame, bg=COSMIC_BLUE)
        right_panel.pack(side=tk.RIGHT, fill="both", expand=True, padx=(20, 0))
        
        # Meditation details frame
        details_frame = tk.Frame(right_panel, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        details_frame.pack(fill="both", expand=True, pady=10)
        
        # Meditation title
        self.meditation_title = tk.Label(
            details_frame,
            text="Select a meditation",
            font=self.subtitle_font,
            fg=MIND_GOLD,
            bg=DEEP_THOUGHT
        )
        self.meditation_title.pack(anchor="w", padx=20, pady=(20, 10))
        
        # Meditation description
        self.meditation_desc = tk.Label(
            details_frame,
            text="Choose a meditation from the list to begin your consciousness exploration.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT,
            wraplength=400,
            justify=tk.LEFT
        )
        self.meditation_desc.pack(anchor="w", padx=20, pady=(0, 20))
        
        # Duration frame
        duration_frame = tk.Frame(details_frame, bg=DEEP_THOUGHT)
        duration_frame.pack(fill="x", padx=20, pady=(0, 10))
        
        duration_label = tk.Label(
            duration_frame,
            text="DURATION (MINUTES):",
            font=self.normal_font,
            fg=AMBIENT_TEAL,
            bg=DEEP_THOUGHT
        )
        duration_label.pack(side=tk.LEFT)
        
        # Duration selector
        self.duration_var = tk.StringVar(value="5")
        durations = ["5", "10", "15", "20", "30"]
        
        self.duration_menu = tk.OptionMenu(
            duration_frame,
            self.duration_var,
            *durations
        )
        self.duration_menu.config(font=self.normal_font, bg=COSMIC_BLUE, fg=PEARL_WHITE)
        self.duration_menu.pack(side=tk.LEFT, padx=(10, 0))
        
        # Start button
        self.start_button = tk.Button(
            details_frame,
            text="Start Meditation",
            font=self.subtitle_font,
            bg=NEURAL_GREEN,
            fg=PEARL_WHITE,
            command=self.start_meditation
        )
        self.start_button.pack(side=tk.RIGHT, padx=20, pady=20)
    
        # Initialize with first meditation if available
        if self.available_meditations:
            self.on_meditation_select(None)
    
    def get_available_meditations(self):
        """Get list of available meditation files from the resources directory"""
        meditations = []
        meditation_dir = "resources/meditations"
        
        if not os.path.exists(meditation_dir):
            os.makedirs(meditation_dir, exist_ok=True)
            # Create default meditations
            ensure_default_meditations()
        
        try:
            files = os.listdir(meditation_dir)
            for file in files:
                if file.endswith(".txt"):
                    # Extract name from filename
                    name = file.replace(".txt", "").replace("_", " ").title()
                    
                    # Read first few lines for description
                    try:
                        with open(os.path.join(meditation_dir, file), "r") as f:
                            content = f.read(500)  # Read first 500 chars for description
                            description = content.strip()[:150] + "..."  # Truncate for display
                    except:
                        description = "A guided meditation experience."
                    
                    meditations.append({
                        "title": name,
                        "file": file,
                        "description": description,
                        "duration": "10",
                        "type": "Consciousness Expansion"
                    })
        except Exception as e:
            print(f"Error loading meditations: {e}")
        
        # If no meditations found, create a default one
        if not meditations:
            ensure_default_meditations()
            return self.get_available_meditations()
        
        return meditations
    
    def on_meditation_select(self, event):
        """Handle selection of a meditation from the list"""
        selection = self.meditation_listbox.curselection()
        if not selection:
            if self.meditation_listbox.size() > 0:
                # Default select the first item
                self.meditation_listbox.selection_set(0)
                selection = (0,)
            else:
                return
            
        index = selection[0]
        meditations = self.get_available_meditations()
        
        if index >= len(meditations):
            return
        
        selected_meditation = meditations[index]
        
        # Update the display with the selected meditation info
        self.meditation_title_var.set(selected_meditation["title"])
        self.meditation_duration_var.set(f"{selected_meditation.get('duration', '10')} minutes")
        self.meditation_type_var.set(selected_meditation.get('type', 'Guided'))
        
        # Update description text
        self.meditation_desc_text.config(state=tk.NORMAL)
        self.meditation_desc_text.delete(1.0, tk.END)
        self.meditation_desc_text.insert(tk.END, selected_meditation["description"])
        self.meditation_desc_text.config(state=tk.DISABLED)
    
    def start_meditation(self):
        """Start the selected meditation"""
        # Get selected meditation
        selection = self.meditation_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a meditation from the list.")
            return
            
        index = selection[0]
        meditations = self.get_available_meditations()
        
        if index >= len(meditations):
            return
        
        selected_meditation = meditations[index]
        
        # Get meditation file
        meditation_file = selected_meditation["file"]
        meditation_path = os.path.join("resources/meditations", meditation_file)
        
        if not os.path.exists(meditation_path):
            messagebox.showerror("Error", f"Meditation file not found: {meditation_file}")
            return
        
        # Create meditation window
        med_window = tk.Toplevel(self.master)
        med_window.title(f"Meditation: {selected_meditation['title']}")
        med_window.geometry("800x600")
        med_window.configure(bg=COSMIC_BLUE)
        self._center_window(med_window)
        
        # Create meditation content
        main_frame = tk.Frame(med_window, bg=COSMIC_BLUE)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text=selected_meditation["title"],
            font=("Helvetica", 18, "bold"),
            fg=MYSTICAL_PURPLE,
            bg=COSMIC_BLUE
        )
        title_label.pack(pady=(0, 20))
        
        # Get duration from menu selection
        try:
            duration_minutes = int(self.meditation_duration_var.get().split()[0])
        except:
            duration_minutes = 10
        
        # Timer display
        timer_frame = tk.Frame(main_frame, bg=COSMIC_BLUE)
        timer_frame.pack(pady=20)
        
        timer_label = tk.Label(
            timer_frame,
            text="Time Remaining:",
            font=("Helvetica", 12),
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        timer_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.timer_var = tk.StringVar(value=f"{duration_minutes}:00")
        timer_display = tk.Label(
            timer_frame,
            textvariable=self.timer_var,
            font=("Helvetica", 20, "bold"),
            fg=ENERGY_CYAN,
            bg=COSMIC_BLUE
        )
        timer_display.pack(side=tk.LEFT)
        
        # Load meditation content
        try:
            with open(meditation_path, "r") as f:
                meditation_text = f.read()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load meditation: {str(e)}")
            med_window.destroy()
            return
        
        # Create a frame for the text
        text_frame = tk.Frame(main_frame, bg=COSMIC_BLUE)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Add a scrollbar
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget for meditation content
        text_widget = tk.Text(
            text_frame,
            wrap=tk.WORD,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            font=("Helvetica", 12),
            padx=15,
            pady=15,
            relief=tk.FLAT,
            yscrollcommand=scrollbar.set
        )
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        # Insert the meditation text
        text_widget.insert(tk.END, meditation_text)
        text_widget.config(state=tk.DISABLED)  # Make read-only
        
        # Controls
        controls_frame = tk.Frame(main_frame, bg=COSMIC_BLUE)
        controls_frame.pack(pady=20)
        
        # End button
        end_button = tk.Button(
            controls_frame,
            text="End Meditation",
            bg=NEURAL_GREEN,
            fg=PEARL_WHITE,
            font=("Helvetica", 12),
            command=med_window.destroy
        )
        end_button.pack(side=tk.RIGHT, padx=10)
        
        # Start timer
        self.remaining_seconds = duration_minutes * 60
        self.update_meditation_timer()
        
        # Record this meditation session
        now = datetime.now()
        session = {
            "type": "meditation",
            "title": selected_meditation["title"],
            "duration": duration_minutes,
            "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add to user data
        if "practice_sessions" not in self.user_data:
            self.user_data["practice_sessions"] = []
        
        self.user_data["practice_sessions"].append(session)
        self.save_user_data()
        
        # Update practice streak
        self.update_practice_streak()
        
    def update_meditation_timer(self):
        """Update the meditation timer"""
        if not hasattr(self, 'remaining_seconds'):
            return
            
        if self.remaining_seconds <= 0:
            self.timer_var.set("00:00")
            messagebox.showinfo("Meditation Complete", "Your meditation session has completed.")
            return
            
        # Update timer display
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        self.timer_var.set(f"{minutes}:{seconds:02d}")
        
        # Decrement timer
        self.remaining_seconds -= 1
        
        # Schedule next update
        self.master.after(1000, self.update_meditation_timer)
    
    def end_meditation(self):
        """End the current meditation session"""
        # Clean up timer and window
        self.remaining_seconds = 0
        
        if hasattr(self, 'meditation_window') and self.meditation_window.winfo_exists():
            self.meditation_window.destroy()

        # Record completion in user data
        now = datetime.now()
        if "completed_practices" not in self.user_data:
            self.user_data["completed_practices"] = []
        
        self.user_data["completed_practices"].append({
            "type": "meditation",
            "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        self.save_user_data()
        self.update_practice_streak()
        
        # Show completion message
        messagebox.showinfo("Meditation Complete", "Your meditation session has been completed.")

    def create_ego_dissolution_tab(self):
        """Create the ego dissolution tab for examining beliefs"""
        # Header frame
        header = tk.Frame(self.beliefs_tab, bg=COSMIC_BLUE)
        header.pack(fill="x", pady=(20, 10))
        
        title_label = tk.Label(
            header,
            text="Ego Dissolution",
            font=self.title_font,
            fg=ETHEREAL_PINK,
            bg=COSMIC_BLUE
        )
        title_label.pack()
        
        desc_label = tk.Label(
            header,
            text="Identify and question limiting beliefs to reduce ego attachment.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=700
        )
        desc_label.pack(pady=(5, 20))
        
        # Main content
        content_frame = tk.Frame(self.beliefs_tab, bg=COSMIC_BLUE)
        content_frame.pack(fill="both", expand=True, padx=40, pady=10)
        
        # Left side - Belief entry
        left_frame = tk.Frame(content_frame, bg=COSMIC_BLUE)
        left_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 20))
        
        # Belief entry section
        entry_frame = tk.Frame(left_frame, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        entry_frame.pack(fill="both", expand=True)
        
        entry_label = tk.Label(
            entry_frame,
            text="EXAMINE A BELIEF",
            font=self.subtitle_font,
            fg=ETHEREAL_PINK,
            bg=DEEP_THOUGHT
        )
        entry_label.pack(pady=(15, 10), padx=20)
        
        instruction = tk.Label(
            entry_frame,
            text="Enter a belief that may be limiting your growth or perception:",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT,
            wraplength=400,
            justify=tk.LEFT
        )
        instruction.pack(pady=(0, 15), padx=20, anchor="w")
        
        # Belief entry
        self.belief_entry = tk.Entry(
            entry_frame,
            font=("Helvetica", 12),
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            width=40
        )
        self.belief_entry.pack(pady=5, padx=20)
        
        # Example beliefs for inspiration
        examples_frame = tk.Frame(entry_frame, bg=DEEP_THOUGHT)
        examples_frame.pack(fill="x", padx=20, pady=15)
        
        examples_label = tk.Label(
            examples_frame,
            text="Examples:",
            font=self.normal_font,
            fg=AMBIENT_TEAL,
            bg=DEEP_THOUGHT
        )
        examples_label.pack(anchor="w")
        
        example_beliefs = [
            "I'm not creative enough to solve this problem.",
            "I need others' approval to feel worthy.",
            "My perception of reality is the only correct one.",
            "My thoughts define who I am."
        ]
        
        for example in example_beliefs:
            ex = tk.Label(
                examples_frame,
                text=f"• {example}",
                font=self.small_font,
                fg=PEARL_WHITE,
                bg=DEEP_THOUGHT,
                wraplength=350,
                justify=tk.LEFT
            )
            ex.pack(anchor="w", pady=2)
        
        # Examine button
        examine_btn = tk.Button(
            entry_frame,
            text="Examine Belief",
            font=self.normal_font,
            bg=MYSTICAL_PURPLE,
            fg=PEARL_WHITE,
            command=self.examine_belief
        )
        examine_btn.pack(pady=20)
        
        # Right side - Saved beliefs and insights
        right_frame = tk.Frame(content_frame, bg=COSMIC_BLUE)
        right_frame.pack(side=tk.RIGHT, fill="both", expand=True, padx=(20, 0))
        
        # Saved beliefs section
        saved_frame = tk.Frame(right_frame, bg=MYSTICAL_PURPLE, bd=1, relief=tk.RAISED)
        saved_frame.pack(fill="both", expand=True)
        
        saved_label = tk.Label(
            saved_frame,
            text="YOUR EXAMINED BELIEFS",
            font=self.subtitle_font,
            fg=ENERGY_CYAN,
            bg=MYSTICAL_PURPLE
        )
        saved_label.pack(pady=(15, 10), padx=20)
        
        # Create a frame for the listbox and scrollbar
        list_frame = tk.Frame(saved_frame, bg=MYSTICAL_PURPLE)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for saved beliefs
        self.beliefs_listbox = tk.Listbox(
            list_frame,
            font=self.normal_font,
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            selectbackground=ETHEREAL_PINK,
            height=10,
            width=40,
            yscrollcommand=scrollbar.set
        )
        self.beliefs_listbox.pack(side=tk.LEFT, fill="both", expand=True)
        
        # Configure the scrollbar
        scrollbar.config(command=self.beliefs_listbox.yview)
        
        # Populate with existing beliefs
        self.load_beliefs()
        
        # Delete button
        delete_btn = tk.Button(
            saved_frame,
            text="Delete Selected",
            font=self.small_font,
            bg=ATTENTION_RED,
            fg=PEARL_WHITE,
            command=self.delete_belief
        )
        delete_btn.pack(anchor="e", padx=20, pady=10)
    
    def examine_belief(self):
        """Open a dialog to examine and question a belief"""
        belief_text = self.belief_entry.get().strip()
        
        if not belief_text:
            messagebox.showinfo("Empty Belief", "Please enter a belief to examine.")
            return
        
        # Create examination window
        exam_window = tk.Toplevel(self.master)
        exam_window.title("Belief Examination")
        exam_window.geometry("700x500")
        exam_window.configure(bg=COSMIC_BLUE)
        
        # Belief frame
        belief_frame = tk.Frame(exam_window, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        belief_frame.pack(fill="x", padx=20, pady=20)
        
        belief_label = tk.Label(
            belief_frame,
            text="EXAMINING BELIEF:",
            font=self.subtitle_font,
            fg=ETHEREAL_PINK,
            bg=DEEP_THOUGHT
        )
        belief_label.pack(anchor="w", padx=20, pady=(15, 5))
        
        belief_display = tk.Label(
            belief_frame,
            text=belief_text,
            font=("Helvetica", 14, "bold"),
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT,
            wraplength=600,
            justify=tk.LEFT
        )
        belief_display.pack(fill="x", padx=20, pady=(0, 15))
        
        # Questions frame
        questions_frame = tk.Frame(exam_window, bg=COSMIC_BLUE)
        questions_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        questions_label = tk.Label(
            questions_frame,
            text="REFLECTION QUESTIONS",
            font=self.subtitle_font,
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        questions_label.pack(anchor="w")
        
        # List of questions to consider
        questions = [
            "Is this belief absolutely true? How can you know for certain?",
            "What evidence contradicts this belief?",
            "How does holding this belief affect your life and perception?",
            "How would your experience change if you let go of this belief?",
            "What alternative perspectives could be equally or more valid?"
        ]
        
        # Create a scrolled text area for responses
        response_frame = tk.Frame(questions_frame, bg=COSMIC_BLUE)
        response_frame.pack(fill="both", expand=True, pady=10)
        
        # Add questions with text areas for responses
        canvas = tk.Canvas(response_frame, bg=COSMIC_BLUE, highlightthickness=0)
        scrollbar = tk.Scrollbar(response_frame, orient="vertical", command=canvas.yview)
        
        scrollable_frame = tk.Frame(canvas, bg=COSMIC_BLUE)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add each question with a text response area
        response_widgets = []
        for q in questions:
            q_frame = tk.Frame(scrollable_frame, bg=COSMIC_BLUE)
            q_frame.pack(fill="x", pady=5)
            
            q_label = tk.Label(
                q_frame,
                text=q,
                font=self.normal_font,
                fg=MIND_GOLD,
                bg=COSMIC_BLUE,
                wraplength=600,
                justify=tk.LEFT
            )
            q_label.pack(anchor="w")
            
            response = tk.Text(
                q_frame,
                font=("Helvetica", 11),
                bg=COSMIC_INDIGO,
                fg=PEARL_WHITE,
                height=3,
                width=60,
                wrap=tk.WORD
            )
            response.pack(fill="x", pady=5)
            response_widgets.append(response)
        
        # Buttons frame
        buttons_frame = tk.Frame(exam_window, bg=COSMIC_BLUE)
        buttons_frame.pack(fill="x", padx=20, pady=20)
        
        # Save button
        save_btn = tk.Button(
            buttons_frame,
            text="Save Insights",
            font=self.normal_font,
            bg=NEURAL_GREEN,
            fg=PEARL_WHITE,
            command=lambda: self.save_belief_examination(belief_text, questions, response_widgets, exam_window)
        )
        save_btn.pack(side=tk.RIGHT, padx=5)
        
        # Cancel button
        cancel_btn = tk.Button(
            buttons_frame,
            text="Cancel",
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            command=exam_window.destroy
        )
        cancel_btn.pack(side=tk.RIGHT, padx=5)
    
    def save_belief_examination(self, belief, questions, responses, window):
        """Save the belief examination results"""
        # Gather responses
        responses_text = []
        for resp in responses:
            responses_text.append(resp.get("1.0", tk.END).strip())
        
        # Check if at least one response is provided
        if not any(responses_text):
            messagebox.showinfo("No Responses", "Please provide at least one response before saving.")
            return
        
        # Create a record of the examination
        examination = {
            "belief": belief,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "questions": questions,
            "responses": responses_text
        }
        
        # Add to user's beliefs data
        if "beliefs" not in self.user_data:
            self.user_data["beliefs"] = []
        
        self.user_data["beliefs"].append(examination)
        
        # Save user data
        self.save_user_data()
        
        # Add to listbox display
        self.beliefs_listbox.insert(tk.END, f"{examination['timestamp']} - {belief[:40]}...")
        
        # Clear the entry field
        self.belief_entry.delete(0, tk.END)
        
        # Close the window
        window.destroy()
        
        # Confirm to user
        messagebox.showinfo(
            "Belief Examined",
            "Your belief examination has been saved. Continue exploring how your beliefs shape your perception."
        )
    
    def load_beliefs(self):
        """Load and display the user's saved beliefs"""
        if "beliefs" in self.user_data and self.user_data["beliefs"]:
            self.beliefs_listbox.delete(0, tk.END)
            for belief in self.user_data["beliefs"]:
                self.beliefs_listbox.insert(
                    tk.END, 
                    f"{belief['timestamp']} - {belief['belief'][:40]}..."
                )
    
    def delete_belief(self):
        """Delete the selected belief from the list"""
        selection = self.beliefs_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a belief to delete.")
            return
        
        index = selection[0]
        if "beliefs" in self.user_data and index < len(self.user_data["beliefs"]):
            # Ask for confirmation
            confirm = messagebox.askyesno(
                "Confirm Deletion",
                "Are you sure you want to delete this belief examination?"
            )
            
            if confirm:
                # Remove from the user data
                del self.user_data["beliefs"][index]
                
                # Save the updated user data
                self.save_user_data()
                
                # Refresh the display
                self.load_beliefs()
                
                messagebox.showinfo("Deleted", "The belief examination has been deleted.")
    
    def create_journal_tab(self):
        """Create the journal tab for recording insights"""
        # Header frame
        header = tk.Frame(self.journal_tab, bg=COSMIC_BLUE)
        header.pack(fill="x", pady=(20, 10))
        
        title_label = tk.Label(
            header,
            text="Journal",
            font=self.title_font,
            fg=NEURAL_GREEN,
            bg=COSMIC_BLUE
        )
        title_label.pack()
        
        desc_label = tk.Label(
            header,
            text="Record your thoughts, experiences, and insights from your consciousness exploration.",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=700
        )
        desc_label.pack(pady=(5, 20))
        
        # Main content
        content_frame = tk.Frame(self.journal_tab, bg=COSMIC_BLUE)
        content_frame.pack(fill="both", expand=True, padx=40, pady=10)
        
        # Left panel - Entries list
        left_panel = tk.Frame(content_frame, bg=COSMIC_BLUE, width=300)
        left_panel.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 20))
        left_panel.pack_propagate(False)  # Prevents the frame from shrinking to fit its contents
        
        entries_label = tk.Label(
            left_panel,
            text="JOURNAL ENTRIES",
            font=self.subtitle_font,
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        entries_label.pack(anchor="w", pady=(0, 10))

        # Sort options frame
        sort_frame = tk.Frame(left_panel, bg=COSMIC_BLUE)
        sort_frame.pack(fill="x", pady=(0, 10))
        
        sort_label = tk.Label(
            sort_frame,
            text="Sort by:",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        sort_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.sort_var = tk.StringVar(value="newest")
        
        sort_newest = tk.Radiobutton(
            sort_frame,
            text="Newest",
            variable=self.sort_var,
            value="newest",
            command=self.load_journal_entries,
            font=self.small_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            selectcolor=DEEP_THOUGHT,
        )
        sort_newest.pack(side=tk.LEFT, padx=5)
        
        sort_oldest = tk.Radiobutton(
            sort_frame,
            text="Oldest",
            variable=self.sort_var,
            value="oldest",
            command=self.load_journal_entries,
            font=self.small_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            selectcolor=DEEP_THOUGHT,
        )
        sort_oldest.pack(side=tk.LEFT, padx=5)
        
        # Create a frame for the listbox and scrollbar
        list_frame = tk.Frame(left_panel, bg=COSMIC_BLUE)
        list_frame.pack(fill="both", expand=True)
        
        # Scrollbar
        entries_scrollbar = tk.Scrollbar(list_frame)
        entries_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for entries
        self.journal_listbox = tk.Listbox(
            list_frame,
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            selectbackground=NEURAL_GREEN,
            height=15,
            width=40,
            yscrollcommand=entries_scrollbar.set
        )
        self.journal_listbox.pack(side=tk.LEFT, fill="both", expand=True)
        
        # Configure scrollbar
        entries_scrollbar.config(command=self.journal_listbox.yview)
        
        # Search frame
        search_frame = tk.Frame(left_panel, bg=COSMIC_BLUE)
        search_frame.pack(fill="x", pady=(10, 0))
        
        search_label = tk.Label(
            search_frame,
            text="Search:",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        search_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.load_journal_entries())
        
        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=self.normal_font,
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE
        )
        search_entry.pack(side=tk.LEFT, fill="x", expand=True)
        
        # Buttons for entries list
        entries_buttons = tk.Frame(left_panel, bg=COSMIC_BLUE)
        entries_buttons.pack(fill="x", pady=10)
        
        new_entry_btn = tk.Button(
            entries_buttons,
            text="New Entry",
            font=self.normal_font,
            bg=NEURAL_GREEN,
            fg=PEARL_WHITE,
            command=self.new_journal_entry
        )
        new_entry_btn.pack(side=tk.LEFT, padx=5)
        
        view_entry_btn = tk.Button(
            entries_buttons,
            text="View Entry",
            font=self.normal_font,
            bg=MYSTICAL_PURPLE,
            fg=PEARL_WHITE,
            command=self.view_journal_entry
        )
        view_entry_btn.pack(side=tk.LEFT, padx=5)

        edit_entry_btn = tk.Button(
            entries_buttons,
            text="Edit Entry",
            font=self.normal_font,
            bg=MIND_GOLD,
            fg=PEARL_WHITE,
            command=self.edit_journal_entry
        )
        edit_entry_btn.pack(side=tk.LEFT, padx=5)
        
        delete_entry_btn = tk.Button(
            entries_buttons,
            text="Delete Entry",
            font=self.normal_font,
            bg=ATTENTION_RED,
            fg=PEARL_WHITE,
            command=self.delete_journal_entry
        )
        delete_entry_btn.pack(side=tk.LEFT, padx=5)
        
        # Right panel - Entry view/edit
        right_panel = tk.Frame(content_frame, bg=COSMIC_BLUE)
        right_panel.pack(side=tk.RIGHT, fill="both", expand=True, padx=(20, 0))
        
        # Placeholder message when no entry is selected
        self.journal_placeholder = tk.Frame(right_panel, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        self.journal_placeholder.pack(fill="both", expand=True)
        
        placeholder_label = tk.Label(
            self.journal_placeholder,
            text="Select an entry to view or create a new entry",
            font=self.subtitle_font,
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT
        )
        placeholder_label.pack(pady=50)
        
        # Create directory for journal entries if it doesn't exist
        self.ensure_journal_directory()
        
        # Load entries
        self.load_journal_entries()
        
        # Bind selection event
        self.journal_listbox.bind("<<ListboxSelect>>", self.on_journal_selection)
        self.journal_listbox.bind("<Double-1>", lambda e: self.view_journal_entry())

    def ensure_journal_directory(self):
        """Ensure journal entries directory exists"""
        journal_dir = os.path.join("resources", "journal")
        if not os.path.exists(journal_dir):
            os.makedirs(journal_dir)
    
    def load_journal_entries(self):
        """Load journal entries from files and populate the listbox"""
        # Clear existing entries in the listbox
        self.journal_listbox.delete(0, tk.END)
        
        # Initialize search_var if it doesn't exist
        if not hasattr(self, 'search_var'):
            self.search_var = tk.StringVar(value="")
        
        # Initialize sort_var if it doesn't exist
        if not hasattr(self, 'sort_var'):
            self.sort_var = tk.StringVar(value="newest")
        
        # Ensure the journal directory exists
        journal_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data", "journal")
        os.makedirs(journal_dir, exist_ok=True)
        
        # Load journal entries
        entries = []
        
        if os.path.exists(journal_dir):
            for filename in os.listdir(journal_dir):
                if filename.endswith(".json"):
                    try:
                        file_path = os.path.join(journal_dir, filename)
                        with open(file_path, "r") as f:
                            entry = json.load(f)
                            entry["filename"] = filename  # Store filename for later reference
                            entries.append(entry)
                    except Exception as e:
                        print(f"Error loading journal entry {filename}: {e}")
        
        # Sort entries by timestamp (newest first)
        entries.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        
        # Store entries for reference
        self.current_journal_entries = entries
        
        # Add entries to the listbox
        for entry in entries:
            # Format the timestamp
            try:
                entry_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")
                display_time = entry_time.strftime("%b %d, %Y")
            except:
                display_time = "Unknown date"
            
            # Get the title or use "Untitled"
            title = entry.get("title", "Untitled Entry")
            
            # Add to listbox
            self.journal_listbox.insert(tk.END, f"{title} - {display_time}")
        
        # Select the first entry if available
        if entries and self.journal_listbox.size() > 0:
            self.journal_listbox.selection_set(0)
            self.on_journal_selection(None)
    
    def migrate_legacy_entries(self):
        """Migrate any entries from user_data to individual files"""
        if "journal_entries" not in self.user_data:
            return
            
        journal_dir = os.path.join("resources", "journal")
        
        for entry in self.user_data["journal_entries"]:
            if "timestamp" not in entry:
                entry["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
            # Generate a unique filename
            timestamp = entry["timestamp"].replace(" ", "_").replace(":", "-")
            filename = f"entry_{timestamp}.json"
            file_path = os.path.join(journal_dir, filename)
            
            # Save entry to file if it doesn't already exist
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    json.dump(entry, f, indent=2)
        
        # Clear entries from user_data to avoid duplication
        # self.user_data["journal_entries"] = []
        # self.save_user_data()
    
    def on_journal_selection(self, event):
        """Handle selection of a journal entry from the list"""
        # Get selected index
        selection = self.journal_listbox.curselection()
        if not selection:
            return
            
        index = selection[0]
        
        # Check if the index is valid for our entries list
        if not hasattr(self, 'current_journal_entries') or index >= len(self.current_journal_entries):
            return
        
        # Get the selected entry
        entry = self.current_journal_entries[index]
        
        # Update preview widgets
        if hasattr(self, 'preview_title'):
            self.preview_title.config(text=entry.get("title", "Untitled Entry"))
        
        if hasattr(self, 'preview_date'):
            try:
                date_obj = datetime.strptime(entry.get("timestamp", ""), "%Y-%m-%d %H:%M:%S")
                date_str = date_obj.strftime("%B %d, %Y at %I:%M %p")
                self.preview_date.config(text=date_str)
            except:
                self.preview_date.config(text=entry.get("timestamp", "Unknown date"))
        
        if hasattr(self, 'preview_text'):
            self.preview_text.config(state=tk.NORMAL)
            self.preview_text.delete(1.0, tk.END)
            self.preview_text.insert(tk.END, entry.get("content", "No content"))
            self.preview_text.config(state=tk.DISABLED)
    
    def new_journal_entry(self):
        """Create a new journal entry"""
        # Create a new window for the entry
        entry_window = tk.Toplevel(self.master)
        entry_window.title("New Journal Entry")
        entry_window.geometry("700x500")
        entry_window.configure(bg=COSMIC_BLUE)
        entry_window.grab_set()  # Make window modal
        
        # Entry frame
        entry_frame = tk.Frame(entry_window, bg=COSMIC_BLUE)
        entry_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title/date frame
        header_frame = tk.Frame(entry_frame, bg=COSMIC_BLUE)
        header_frame.pack(fill="x", pady=10)
        
        # Date display
        today = datetime.now().strftime("%B %d, %Y - %H:%M")
        date_label = tk.Label(
            header_frame,
            text=today,
            font=self.subtitle_font,
            fg=NEURAL_GREEN,
            bg=COSMIC_BLUE
        )
        date_label.pack(anchor="w")
        
        # Title entry
        title_frame = tk.Frame(entry_frame, bg=COSMIC_BLUE)
        title_frame.pack(fill="x", pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="TITLE:",
            font=self.normal_font,
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        title_label.pack(side=tk.LEFT, padx=(0, 10))
        
        title_entry = tk.Entry(
            title_frame,
            font=("Helvetica", 12),
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            width=50
        )
        title_entry.pack(side=tk.LEFT, fill="x", expand=True)
        
        # Content area
        content_label = tk.Label(
            entry_frame,
            text="ENTRY:",
            font=self.normal_font,
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        content_label.pack(anchor="w", pady=(10, 5))
        
        # Create a frame for the text widget and scrollbar
        content_frame = tk.Frame(entry_frame, bg=COSMIC_BLUE)
        content_frame.pack(fill="both", expand=True)
        
        # Add scrollbar
        content_scrollbar = tk.Scrollbar(content_frame)
        content_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        content_text = tk.Text(
            content_frame,
            font=("Helvetica", 12),
            bg=COSMIC_INDIGO,
            fg=PEARL_WHITE,
            wrap=tk.WORD,
            padx=10,
            pady=10,
            yscrollcommand=content_scrollbar.set
        )
        content_text.pack(side=tk.LEFT, fill="both", expand=True)
        
        # Configure scrollbar
        content_scrollbar.config(command=content_text.yview)
        
        # Buttons
        button_frame = tk.Frame(entry_window, bg=COSMIC_BLUE)
        button_frame.pack(fill="x", padx=20, pady=10)
        
        save_btn = tk.Button(
            button_frame,
            text="Save Entry",
            font=self.normal_font,
            bg=NEURAL_GREEN,
            fg=PEARL_WHITE,
            command=lambda: self.save_journal_entry(title_entry.get(), content_text.get("1.0", tk.END), entry_window)
        )
        save_btn.pack(side=tk.RIGHT, padx=5)
        
        cancel_btn = tk.Button(
            button_frame,
            text="Cancel",
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            command=entry_window.destroy
        )
        cancel_btn.pack(side=tk.RIGHT, padx=5)
        
        # Set focus to title entry
        title_entry.focus_set()
    
    def save_journal_entry(self, title, content, window):
        """Save the journal entry to a file"""
        content = content.strip()
        if not content:
            messagebox.showinfo("Empty Entry", "Please write something in your entry before saving.")
            return
        
        # Use a default title if none provided
        if not title:
            title = "Untitled Entry"
        
        # Create necessary directories if they don't exist
        journal_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data", "journal")
        os.makedirs(journal_dir, exist_ok=True)
        
        # Generate timestamp for new entries
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp_str = timestamp.replace(" ", "_").replace(":", "-")
        filename = f"entry_{timestamp_str}.json"
        file_path = os.path.join(journal_dir, filename)
        
        # Create entry object
        entry = {
            "timestamp": timestamp,
            "title": title,
            "content": content,
            "id": str(uuid.uuid4()),
            "created_at": timestamp
        }
        
        # Save entry
        try:
            with open(file_path, "w") as f:
                json.dump(entry, f, indent=2)
            
            # Close window
            window.destroy()
            
            # Refresh entries
            self.load_journal_entries()
            
            # Confirm to user
            messagebox.showinfo("Entry Saved", "Your journal entry has been saved successfully.")
            
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save journal entry: {str(e)}")
    
    def delete_journal_entry(self):
        """Delete the selected journal entry"""
        selection = self.journal_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select an entry to delete.")
            return
        
        index = selection[0]
        if index < len(self.current_journal_entries):
            entry = self.current_journal_entries[index]
            
            # Ask for confirmation
            confirm = messagebox.askyesno(
                "Confirm Deletion",
                "Are you sure you want to delete this journal entry? This action cannot be undone."
            )
            
            if confirm:
                # Find and delete the file
                timestamp_str = entry["timestamp"].replace(" ", "_").replace(":", "-")
                filename = f"entry_{timestamp_str}.json"
                file_path = os.path.join("resources", "journal", filename)
                
                if os.path.exists(file_path):
                    os.remove(file_path)
                
                # Also remove from user_data for consistency
                if "journal_entries" in self.user_data:
                    entry_id = entry.get("id", "")
                    self.user_data["journal_entries"] = [
                        e for e in self.user_data["journal_entries"] 
                        if e.get("id", "") != entry_id
                    ]
                self.save_user_data()
                
                # Refresh the list
                self.load_journal_entries()
                
                messagebox.showinfo("Deleted", "The journal entry has been deleted.")

    def update_practice_streak(self):
        """Update the user's meditation practice streak based on the last session date"""
        if "meditation_stats" not in self.user_data:
            return
            
        # Get today's date and the last meditation date
        today = datetime.now().date()
        last_meditation_str = self.user_data["meditation_stats"].get("last_meditation")
        
        if not last_meditation_str:
            # First time meditating, set streak to 1
            self.user_data["meditation_stats"]["practice_streak"] = 1
            return
            
        try:
            # Parse the last meditation date
            last_meditation = datetime.strptime(last_meditation_str, "%Y-%m-%d").date()
            
            # Calculate days difference
            days_diff = (today - last_meditation).days
            
            if days_diff == 1:
                # Consecutive day, increment streak
                self.user_data["meditation_stats"]["practice_streak"] += 1
            elif days_diff > 1:
                # Streak broken, reset to 1
                self.user_data["meditation_stats"]["practice_streak"] = 1
            # If days_diff is 0, they already meditated today so don't change the streak
        except Exception as e:
            print(f"Error updating practice streak: {e}")
            # Reset to 1 if there's an error
            self.user_data["meditation_stats"]["practice_streak"] = 1

    def show_export_history(self):
        """Display the history of exports"""
        history_window = tk.Toplevel(self.master)
        history_window.title("Export History")
        history_window.geometry("550x400")
        history_window.configure(bg=COSMIC_BLUE)
        
        # Center the window
        self._center_window(history_window)
        
        # Header
        header = tk.Label(
            history_window,
            text="Mind Mirror Export History",
            font=self.title_font,
            fg=ENERGY_CYAN,
            bg=COSMIC_BLUE
        )
        header.pack(pady=(20, 10))
        
        # Description
        description = tk.Label(
            history_window,
            text="Records of neural pattern data exported from Mind Mirror",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        description.pack(pady=(0, 20))
        
        # Check if there are exports
        if not self.user_data.get("exports", []):
            no_exports = tk.Label(
                history_window,
                text="No export history found. Use the export menu to share your neural patterns.",
                font=self.normal_font,
                fg=MIND_GOLD,
                bg=COSMIC_BLUE,
                wraplength=450
            )
            no_exports.pack(pady=40)
            
            close_btn = tk.Button(
                history_window,
                text="Close",
                font=self.normal_font,
                bg=DEEP_THOUGHT,
                fg=PEARL_WHITE,
                command=history_window.destroy
            )
            close_btn.pack(pady=20)
            return
        
        # Create a frame for the export list
        list_frame = tk.Frame(history_window, bg=COSMIC_BLUE)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Create scrollable area
        canvas = tk.Canvas(list_frame, bg=COSMIC_BLUE, highlightthickness=0)
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=COSMIC_BLUE)
        
        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add export records
        for i, export in enumerate(reversed(self.user_data.get("exports", []))):
            export_frame = tk.Frame(scroll_frame, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
            export_frame.pack(fill="x", pady=5, padx=5)
            
            # Format date for display
            try:
                export_date = datetime.fromisoformat(export.get("timestamp", "")).strftime("%Y-%m-%d %H:%M")
            except:
                export_date = "Unknown date"
            
            # Header with date and target
            header_frame = tk.Frame(export_frame, bg=DEEP_THOUGHT)
            header_frame.pack(fill="x", padx=10, pady=5)
            
            date_label = tk.Label(
                header_frame,
                text=export_date,
                font=self.small_font,
                fg=MIND_GOLD,
                bg=DEEP_THOUGHT
            )
            date_label.pack(side="left")
            
            target_label = tk.Label(
                header_frame,
                text=f"Exported to: {export.get('target', 'Unknown')}",
                font=self.small_font,
                fg=ENERGY_CYAN,
                bg=DEEP_THOUGHT
            )
            target_label.pack(side="right")
            
            # Details
            details_frame = tk.Frame(export_frame, bg=DEEP_THOUGHT)
            details_frame.pack(fill="x", padx=10, pady=(0, 5))
            
            details_text = f"Nodes: {export.get('nodes', '?')} | Connections: {export.get('connections', '?')}"
            if export.get('file'):
                details_text += f" | File: {export.get('file')}"
                
            details_label = tk.Label(
                details_frame,
                text=details_text,
                font=self.small_font,
                fg=PEARL_WHITE,
                bg=DEEP_THOUGHT,
                justify=tk.LEFT,
                anchor="w"
            )
            details_label.pack(fill="x")
        
        # Close button
        close_btn = tk.Button(
            history_window,
            text="Close",
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            command=history_window.destroy
        )
        close_btn.pack(pady=20)

    def show_about(self):
        """Show information about the Mind Mirror application"""
        about_window = tk.Toplevel(self.master)
        about_window.title("About Mind Mirror")
        about_window.geometry("500x400")
        about_window.configure(bg=COSMIC_BLUE)
        about_window.resizable(False, False)
        
        # Center the window
        self._center_window(about_window)
        
        # Logo or title
        title_label = tk.Label(
            about_window,
            text="Mind Mirror",
            font=("Helvetica", 28, "bold"),
            fg=MYSTICAL_PURPLE,
            bg=COSMIC_BLUE
        )
        title_label.pack(pady=(30, 5))
        
        # Version
        version_label = tk.Label(
            about_window,
            text=f"Version {VERSION} ({VERSION_NAME})",
            font=("Helvetica", 12, "italic"),
            fg=ENERGY_CYAN,
            bg=COSMIC_BLUE
        )
        version_label.pack(pady=(0, 20))
        
        # Description
        desc_text = "Mind Mirror is a tool for exploring consciousness and neural patterns."
        desc_label = tk.Label(
            about_window,
            text=desc_text,
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=400
        )
        desc_label.pack(pady=(0, 15))
        
        # More details
        details_text = (
            "Part of the PROJECT89 Perception-Hacking Suite\n\n"
            "This software allows you to map and visualize your consciousness, "
            "examine your beliefs, and integrate with other consciousness-altering tools."
        )
        details_label = tk.Label(
            about_window,
            text=details_text,
            font=self.small_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE,
            wraplength=400,
            justify=tk.CENTER
        )
        details_label.pack(pady=(0, 20))
        
        # Footer with creation date
        footer_label = tk.Label(
            about_window,
            text="© 2023 PROJECT89",
            font=("Helvetica", 8),
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        footer_label.pack(side=tk.BOTTOM, pady=15)
        
        # Close button
        close_btn = tk.Button(
            about_window,
            text="Close",
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            command=about_window.destroy
        )
        close_btn.pack(pady=20)

    def view_journal_entry(self):
        """View the selected journal entry"""
        # Get selected index
        selection = self.journal_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select an entry to view.")
            return
            
        index = selection[0]
        
        # Check if the index is valid for our entries list
        if not hasattr(self, 'current_journal_entries') or index >= len(self.current_journal_entries):
            return
        
        # Get the selected entry
        entry = self.current_journal_entries[index]
        
        # Create view window
        view_window = tk.Toplevel(self.master)
        view_window.title("Journal Entry")
        view_window.geometry("700x500")
        view_window.configure(bg=COSMIC_BLUE)
        
        # Main frame
        main_frame = tk.Frame(view_window, bg=COSMIC_BLUE)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title and date
        try:
            date_obj = datetime.strptime(entry.get("timestamp", ""), "%Y-%m-%d %H:%M:%S")
            date_str = date_obj.strftime("%B %d, %Y at %I:%M %p")
        except:
            date_str = entry.get("timestamp", "Unknown date")
        
        date_label = tk.Label(
            main_frame,
            text=date_str,
            font=("Helvetica", 10),
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        date_label.pack(anchor=tk.W, pady=(0, 5))
        
        title_label = tk.Label(
            main_frame,
            text=entry.get("title", "Untitled Entry"),
            font=("Helvetica", 16, "bold"),
            fg=MYSTICAL_PURPLE,
            bg=COSMIC_BLUE
        )
        title_label.pack(anchor=tk.W, pady=(0, 20))
        
        # Content
        content_frame = tk.Frame(main_frame, bg=COSMIC_BLUE)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(content_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget
        content_text = tk.Text(
            content_frame,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            padx=15,
            pady=15,
            yscrollcommand=scrollbar.set
        )
        content_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=content_text.yview)
        
        # Insert content
        content_text.insert(tk.END, entry.get("content", "No content"))
        content_text.config(state=tk.DISABLED)  # Read-only
        
        # Buttons
        button_frame = tk.Frame(view_window, bg=COSMIC_BLUE)
        button_frame.pack(fill=tk.X, pady=15)
        
        close_button = tk.Button(
            button_frame,
            text="Close",
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            command=view_window.destroy
        )
        close_button.pack(side=tk.RIGHT, padx=5)

    def edit_journal_entry(self):
        """Edit the selected journal entry"""
        # Get selected index
        selection = self.journal_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select an entry to edit.")
            return
            
        # For now, just show a message
        messagebox.showinfo("Edit Entry", "Edit functionality will be implemented in a future update.")
        
        # Call view_journal_entry as a fallback
        self.view_journal_entry()

if __name__ == "__main__":
    app = EnchantedMindMirror()
    app.master.mainloop() 