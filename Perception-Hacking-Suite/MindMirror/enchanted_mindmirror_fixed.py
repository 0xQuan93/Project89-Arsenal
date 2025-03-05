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
    """Create default meditation files if they don't exist"""
    meditation_dir = "resources/meditations"
    os.makedirs(meditation_dir, exist_ok=True)
    
    default_meditations = {
        "cosmic_awareness.txt": """
Settle into a comfortable position and close your eyes.
Take three deep breaths, feeling your body relax with each exhale.
Imagine your consciousness expanding beyond the boundaries of your body.
Feel yourself becoming one with the cosmos, a conscious node in the universal network.
Observe thoughts as cosmic events, arising and passing like stars being born and dying.
Experience the vastness of your awareness, limitless and eternal.
Rest in this expanded state of being, neither attaching to nor rejecting any experience.
When you're ready, slowly return to your body, carrying this cosmic perspective with you.
        """,
        
        "inner_light.txt": """
Close your eyes and bring your attention to the center of your chest.
Imagine a small point of light glowing there, pulsing with your heartbeat.
With each breath, this light grows brighter and expands outward.
Let it fill your entire body, illuminating you from within.
Feel the warmth and clarity this light brings to every cell.
Now imagine this light extending beyond your body, connecting with all beings.
Rest in this radiance, knowing this light is your true nature.
Whenever you're ready, slowly open your eyes, maintaining awareness of this inner illumination.
        """,
        
        "quantum_self.txt": """
Take a comfortable seat and allow your body to settle.
Bring awareness to the sensation of your body existing in multiple states simultaneously.
Just as a quantum particle exists as a probability wave until observed,
Experience yourself as pure potential, not fixed in any single identity.
Notice how your sense of self shifts and changes moment to moment.
Allow any fixed idea of who you are to dissolve into a field of possibilities.
Rest in this quantum state of being - fluid, undefined, and full of potential.
When you're ready to return, bring with you this understanding of your quantum nature.
        """
    }
    
    for filename, content in default_meditations.items():
        file_path = os.path.join(meditation_dir, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content.strip())

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
        
        # Create the main container
        self.main_container = tk.Frame(self.master, bg=COSMIC_BLUE)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create cosmic background with stars
        self.background_canvas = tk.Canvas(self.main_container, bg=COSMIC_BLUE, highlightthickness=0)
        self.background_canvas.pack(fill=tk.BOTH, expand=True)
        
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
        # Configure style for ttk widgets
        style = ttk.Style()
        style.configure("TNotebook", background=COSMIC_BLUE, borderwidth=0)
        style.configure("TNotebook.Tab", background=COSMIC_BLUE, foreground=PEARL_WHITE, padding=[20, 10])
        style.map("TNotebook.Tab", 
                 background=[("selected", MYSTICAL_PURPLE)],
                 foreground=[("selected", PEARL_WHITE)])
        
        # Create main content frame over the background
        self.main_frame = tk.Frame(self.background_canvas, bg=COSMIC_BLUE)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)
        
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tab frames with contrasting background colors
        self.dashboard_tab = tk.Frame(self.notebook, bg=COSMIC_BLUE)
        self.reflection_tab = tk.Frame(self.notebook, bg=COSMIC_BLUE)
        self.meditation_tab = tk.Frame(self.notebook, bg=COSMIC_BLUE)
        self.beliefs_tab = tk.Frame(self.notebook, bg=COSMIC_BLUE)
        self.journal_tab = tk.Frame(self.notebook, bg=COSMIC_BLUE)
        self.neural_tab = tk.Frame(self.notebook, bg=COSMIC_BLUE)
        
        # Add tabs to notebook
        self.notebook.add(self.dashboard_tab, text="Dashboard")
        self.notebook.add(self.reflection_tab, text="Self-Reflection")
        self.notebook.add(self.meditation_tab, text="Consciousness Expansion")
        self.notebook.add(self.beliefs_tab, text="Ego Dissolution")
        self.notebook.add(self.journal_tab, text="Journal")
        self.notebook.add(self.neural_tab, text="Neural Patterns")
        
        # Set up event binding for tab selection to ensure proper drawing
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)
        
        # Create content for dashboard tab
        self.create_dashboard_tab()
        
        # Create content for neural patterns tab
        self.create_neural_patterns_tab()
        
        # Add placeholder content for other tabs
        self.create_placeholder_tabs()
        
        # Create status bar
        self.create_status_bar()
    
    def create_dashboard_tab(self):
        """Create the dashboard tab content"""
        # Welcome header
        header_frame = tk.Frame(self.dashboard_tab, bg=COSMIC_BLUE)
        header_frame.pack(fill="x", pady=(20, 30))
        
        welcome_text = f"Welcome back, {self.user_data['name']}"
        welcome_label = tk.Label(
            header_frame,
            text=welcome_text,
            font=self.title_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        welcome_label.pack()
        
        subtitle = "Your consciousness exploration dashboard"
        subtitle_label = tk.Label(
            header_frame,
            text=subtitle,
            font=("Helvetica", 14),
            fg=AMBIENT_TEAL,
            bg=COSMIC_BLUE
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Main dashboard content
        content_frame = tk.Frame(self.dashboard_tab, bg=COSMIC_BLUE)
        content_frame.pack(fill="both", expand=True, padx=40)
        
        # Left side - Stats and streak
        left_frame = tk.Frame(content_frame, bg=COSMIC_BLUE)
        left_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=(0, 20))
        
        # Practice streak
        streak_frame = tk.Frame(left_frame, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        streak_frame.pack(fill="x", pady=10, ipady=10)
        
        streak_label = tk.Label(
            streak_frame,
            text="PRACTICE STREAK",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT
        )
        streak_label.pack(pady=(10, 5))
        
        streak_count = tk.Label(
            streak_frame,
            text=str(self.user_data["meditation_stats"]["practice_streak"]),
            font=("Helvetica", 40, "bold"),
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
        streak_text.pack(pady=(0, 10))
        
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
        recommendations_label.pack(anchor="w", pady=(0, 15))
        
        # Define recommendations with associated actions
        recommendations = [
            {
                "title": "Begin Your Meditation Practice",
                "description": "Regular meditation enhances self-awareness. Start with short sessions to build your practice.",
                "button_text": "Start Meditation",
                "command": lambda: self.notebook.select(self.meditation_tab)
            },
            {
                "title": "Record Your Insights",
                "description": "Journaling enhances reflection and consolidates insights. Document your inner journey.",
                "button_text": "Open Journal",
                "command": lambda: self.notebook.select(self.journal_tab)
            },
            {
                "title": "Explore Neural Patterns",
                "description": "Visualize how your thoughts connect to reveal deeper cognitive patterns.",
                "button_text": "View Patterns",
                "command": lambda: self.notebook.select(self.neural_tab)
            }
        ]
        
        for rec in recommendations:
            rec_frame = tk.Frame(right_frame, bg=MYSTICAL_PURPLE, bd=1, relief=tk.RAISED)
            rec_frame.pack(fill="x", pady=5, ipady=5)
            
            title = tk.Label(
                rec_frame,
                text=rec["title"],
                font=("Helvetica", 14, "bold"),
                fg=MIND_GOLD,
                bg=MYSTICAL_PURPLE,
                anchor="w"
            )
            title.pack(fill="x", padx=10, pady=(5, 3))
            
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
            desc.pack(fill="x", padx=10, pady=(0, 5))
            
            button = tk.Button(
                rec_frame,
                text=rec["button_text"],
                font=self.small_font,
                bg=COSMIC_BLUE,
                fg=PEARL_WHITE,
                bd=0,
                command=rec["command"]
            )
            button.pack(anchor="e", padx=10, pady=5)
    
    def create_neural_patterns_tab(self):
        """Create the neural patterns visualization tab"""
        # Header frame
        header = tk.Frame(self.neural_tab, bg=COSMIC_BLUE)
        header.pack(fill="x", pady=(20, 10))
        
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
        description.pack(pady=(5, 20))
        
        # Main content frame
        pattern_frame = tk.Frame(self.neural_tab, bg=COSMIC_INDIGO)
        pattern_frame.pack(fill="both", expand=True, padx=30, pady=10)
        
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
        controls = tk.Frame(self.neural_tab, bg=COSMIC_BLUE)
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
        status_bar = tk.Frame(self.master, bg=DEEP_THOUGHT, height=30)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Version info
        version_label = tk.Label(
            status_bar,
            text=f"Mind Mirror v{VERSION} | {VERSION_NAME}",
            font=("Helvetica", 8),
            fg=PEARL_WHITE,
            bg=DEEP_THOUGHT
        )
        version_label.pack(side=tk.LEFT, padx=10)
        
        # Sound toggle button
        self.sound_button = tk.Button(
            status_bar,
            text="Sound: Off",
            font=("Helvetica", 8),
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            bd=0,
            command=self.toggle_ambient_sound
        )
        self.sound_button.pack(side=tk.RIGHT, padx=10)
        
        # Integration button
        integration_button = tk.Button(
            status_bar,
            text="Reality Glitcher Integration",
            font=("Helvetica", 8),
            bg=DEEP_THOUGHT,
            fg=ENERGY_CYAN,
            bd=0,
            command=self.show_integration_options
        )
        integration_button.pack(side=tk.RIGHT, padx=10)
    
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
        progress_window.geometry("400x250")
        progress_window.configure(bg=COSMIC_BLUE)
        
        # Progress content
        header = tk.Label(
            progress_window,
            text="Exporting Neural Patterns",
            font=self.title_font,
            fg=ENERGY_CYAN,
            bg=COSMIC_BLUE
        )
        header.pack(pady=(20, 10))
        
        # Generate neural pattern data for export
        neural_data = self.generate_export_data()
        
        # Show progress information
        status_label = tk.Label(
            progress_window,
            text="Preparing neural pattern data...",
            font=self.normal_font,
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
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
        
        # Start progress simulation
        progress["value"] = 0
        progress_window.update()
        
        # Simulate progress steps
        steps = ["Generating pattern data", "Formatting for transfer", "Connecting to Reality Glitcher", "Transferring data"]
        for i, step in enumerate(steps):
            progress["value"] = (i + 1) * 25
            status_label.config(text=step)
            progress_window.update()
            time.sleep(0.7)  # Simulate processing time
        
        # Try to actually write the data to Reality Glitcher directory
        export_path = os.path.join(reality_glitcher_path, "imports")
        os.makedirs(export_path, exist_ok=True)
        
        try:
            with open(os.path.join(export_path, "mind_mirror_data.json"), "w") as f:
                json.dump(neural_data, f, indent=2)
            export_success = True
        except Exception as e:
            export_success = False
            error_message = str(e)
        
        # Show completion message
        if export_success:
            status_label.config(text="Neural patterns successfully exported to Reality Glitcher!")
            messagebox.showinfo(
                "Export Complete",
                "Neural patterns have been successfully exported to Reality Glitcher!\n\n"
                "You can now use these patterns in your Reality Glitcher experiments."
            )
        else:
            status_label.config(text=f"Error exporting data: {error_message}")
            messagebox.showerror(
                "Export Error",
                f"Could not export neural patterns: {error_message}\n\n"
                "Make sure Reality Glitcher is properly installed and accessible."
            )
            
        # Add close button
        close_button = tk.Button(
            progress_window,
            text="Close",
            font=self.normal_font,
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            command=progress_window.destroy
        )
        close_button.pack(pady=20)
        
    def generate_export_data(self):
        """Generate neural pattern data for export to Reality Glitcher"""
        # Create sample data structure that Reality Glitcher would understand
        export_data = {
            "source": "Mind Mirror",
            "version": VERSION,
            "timestamp": datetime.now().isoformat(),
            "user": self.user_data["name"],
            "neural_patterns": {
                "nodes": [],
                "connections": []
            },
            "metadata": {
                "pattern_type": "thought_web",
                "consciousness_level": 0.8,
                "color_scheme": "cosmic",
                "energy_signature": "alpha_theta_blend"
            }
        }
        
        # Generate some sample nodes based on any available user data
        thought_seeds = ["Perception", "Consciousness", "Reality", "Mind", "Time", "Space", 
                        "Self", "Awareness", "Memory", "Identity", "Dream", "Existence"]
        
        # Add any insights from user data
        for insight in self.user_data.get("insights", []):
            thought_seeds.append(insight)
        
        # Generate nodes
        for i, thought in enumerate(thought_seeds[:10]):  # Limit to 10 nodes
            node = {
                "id": i,
                "label": thought,
                "type": "concept",
                "strength": random.uniform(0.5, 1.0),
                "position": {
                    "x": random.uniform(-100, 100),
                    "y": random.uniform(-100, 100)
                }
            }
            export_data["neural_patterns"]["nodes"].append(node)
        
        # Generate some connections between nodes
        num_connections = min(15, len(export_data["neural_patterns"]["nodes"]) * 2)
        for _ in range(num_connections):
            source = random.randint(0, len(export_data["neural_patterns"]["nodes"]) - 1)
            target = random.randint(0, len(export_data["neural_patterns"]["nodes"]) - 1)
            if source != target:
                connection = {
                    "source": source,
                    "target": target,
                    "strength": random.uniform(0.1, 0.9),
                    "type": random.choice(["association", "causation", "similarity"])
                }
                export_data["neural_patterns"]["connections"].append(connection)
        
        return export_data
    
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
            with open("user_data/user_profile.json", "r") as f:
                self.user_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # User data doesn't exist or is invalid, use defaults
            pass
    
    def save_user_data(self):
        """Save user data to JSON file"""
        with open("user_data/user_profile.json", "w") as f:
            json.dump(self.user_data, f, indent=2)

    def on_tab_change(self, event):
        """Handle tab change events to ensure proper rendering"""
        # Get the currently selected tab
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")
        print(f"Switched to {tab_name} tab")
        
        # Ensure proper redraw of the tab contents
        selected_tab = self.notebook.nametowidget(tab_id)
        selected_tab.update()
    
    def create_placeholder_tabs(self):
        """Create content for all tabs"""
        # Self-Reflection tab
        self.create_self_reflection_tab()
            
        # Meditation tab
        self.create_meditation_tab()
            
        # Beliefs tab
        self.create_ego_dissolution_tab()
            
        # Journal tab
        self.create_journal_tab()
    
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
                        "name": name,
                        "file": file,
                        "description": description
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
        if not self.available_meditations:
            return
            
        selection = self.meditation_listbox.curselection()
        if not selection:
            return
            
        index = selection[0]
        selected_meditation = self.available_meditations[index]
        
        # Update the display
        self.meditation_title.config(text=selected_meditation["name"])
        self.meditation_desc.config(text=selected_meditation["description"])
    
    def start_meditation(self):
        """Start the selected meditation"""
        # Get selected meditation
        selection = self.meditation_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a meditation from the list.")
            return
            
        index = selection[0]
        selected_meditation = self.available_meditations[index]
        duration = int(self.duration_var.get())
        
        # Update meditation stats
        if "meditation_stats" not in self.user_data:
            self.user_data["meditation_stats"] = {
                "sessions": 0,
                "total_minutes": 0,
                "last_meditation": None,
                "practice_streak": 0
            }
        
        self.user_data["meditation_stats"]["sessions"] += 1
        self.user_data["meditation_stats"]["total_minutes"] += duration
        
        # Update last meditation date
        today = datetime.now().strftime("%Y-%m-%d")
        self.user_data["meditation_stats"]["last_meditation"] = today
        
        # Update practice streak
        self.update_practice_streak()
        
        # Save user data
        self.save_user_data()
        
        # Create meditation window
        self.meditation_window = tk.Toplevel(self.master)
        self.meditation_window.title(f"Meditation: {selected_meditation['name']}")
        self.meditation_window.geometry("800x600")
        self.meditation_window.configure(bg=COSMIC_BLUE)
        
        # Create cosmic background for meditation window
        self.meditation_bg = tk.Canvas(self.meditation_window, bg=COSMIC_BLUE, highlightthickness=0)
        self.meditation_bg.pack(fill="both", expand=True)
        
        # Add stars to meditation background
        meditation_stars = []
        for _ in range(100):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            size = random.uniform(0.5, 3)
            opacity = random.uniform(0.4, 1.0)
            star = self.meditation_bg.create_oval(
                x, y, x + size, y + size,
                fill=PEARL_WHITE, outline="",
                stipple="gray50" if opacity < 0.7 else ""
            )
            meditation_stars.append(star)
        
        # Meditation content
        meditation_frame = tk.Frame(self.meditation_bg, bg=COSMIC_BLUE)
        meditation_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)
        
        # Meditation title
        title = tk.Label(
            meditation_frame,
            text=selected_meditation["name"],
            font=self.title_font,
            fg=MIND_GOLD,
            bg=COSMIC_BLUE
        )
        title.pack(pady=(0, 20))
        
        # Timer display
        self.time_remaining = duration * 60  # convert to seconds
        
        self.timer_display = tk.Label(
            meditation_frame,
            text=f"{duration}:00",
            font=("Helvetica", 40, "bold"),
            fg=PEARL_WHITE,
            bg=COSMIC_BLUE
        )
        self.timer_display.pack(pady=10)
        
        # Meditation guidance text
        guidance_frame = tk.Frame(meditation_frame, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
        guidance_frame.pack(fill="both", expand=True, pady=20)
        
        # Get meditation content
        try:
            with open(os.path.join("resources/meditations", selected_meditation["file"]), "r") as f:
                meditation_text = f.read()
        except:
            meditation_text = "Close your eyes and breathe deeply. Focus on your breath and let go of thoughts."
        
        guidance_text = tk.Text(
            guidance_frame,
            font=("Helvetica", 14),
            bg=DEEP_THOUGHT,
            fg=PEARL_WHITE,
            wrap=tk.WORD,
            padx=20,
            pady=20,
            height=10,
            width=50
        )
        guidance_text.pack(fill="both", expand=True)
        guidance_text.insert("1.0", meditation_text)
        guidance_text.config(state="disabled")  # Make read-only
        
        # Control buttons
        controls_frame = tk.Frame(meditation_frame, bg=COSMIC_BLUE)
        controls_frame.pack(fill="x", pady=20)
        
        # End button
        end_btn = tk.Button(
            controls_frame,
            text="End Session",
            font=self.normal_font,
            bg=ATTENTION_RED,
            fg=PEARL_WHITE,
            command=self.end_meditation
        )
        end_btn.pack(side=tk.RIGHT)
        
        # Start timer
        self.update_meditation_timer()
        
    def update_meditation_timer(self):
        """Update the meditation timer display"""
        if not hasattr(self, 'meditation_window') or not self.meditation_window.winfo_exists():
            return
            
        if self.time_remaining <= 0:
            self.timer_display.config(text="00:00")
            messagebox.showinfo("Meditation Complete", "Your meditation session has completed.")
            self.meditation_window.destroy()
            return
            
        # Update timer display
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        self.timer_display.config(text=f"{minutes}:{seconds:02d}")
        
        # Decrement timer
        self.time_remaining -= 1
        
        # Schedule next update - use meditation_window instead of master for the after call
        self.meditation_window.after(1000, self.update_meditation_timer)
    
    def end_meditation(self):
        """End the current meditation session"""
        if hasattr(self, 'meditation_window') and self.meditation_window.winfo_exists():
            self.meditation_window.destroy()
            messagebox.showinfo("Session Ended", "Your meditation session has been ended.")

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
        """Load and display journal entries from files"""
        self.journal_listbox.delete(0, tk.END)
        
        # First, make sure entries are in user_data for backward compatibility
        if "journal_entries" not in self.user_data:
            self.user_data["journal_entries"] = []
            
        # Ensure any old entries in user_data are saved to files
        self.migrate_legacy_entries()
        
        # Get all journal entry files
        journal_dir = os.path.join("resources", "journal")
        entries = []
        
        if os.path.exists(journal_dir):
            for filename in os.listdir(journal_dir):
                if filename.endswith(".json"):
                    try:
                        file_path = os.path.join(journal_dir, filename)
                        with open(file_path, "r") as f:
                            entry = json.load(f)
                            entries.append(entry)
                    except Exception as e:
                        print(f"Error loading journal entry {filename}: {e}")
        
        # Filter entries based on search
        search_term = self.search_var.get().lower()
        if search_term:
            entries = [e for e in entries if 
                      search_term in e.get("title", "").lower() or 
                      search_term in e.get("content", "").lower()]
        
        # Sort entries based on user preference
        sort_order = self.sort_var.get()
        if sort_order == "newest":
            entries.sort(key=lambda x: datetime.strptime(x.get("timestamp", "1970-01-01 00:00:00"), 
                                                         "%Y-%m-%d %H:%M:%S"), reverse=True)
        else:
            entries.sort(key=lambda x: datetime.strptime(x.get("timestamp", "1970-01-01 00:00:00"), 
                                                         "%Y-%m-%d %H:%M:%S"))
        
        # Store entries for reference
        self.current_journal_entries = entries
        
        # Add entries to the listbox
        for entry in entries:
            # Format the timestamp
            try:
                entry_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")
                display_time = entry_time.strftime("%b %d, %Y - %H:%M")
            except:
                display_time = entry.get("timestamp", "Unknown date")
            
            # Get the title or use "Untitled"
            title = entry.get("title", "Untitled Entry")
            
            # Add to listbox
            self.journal_listbox.insert(tk.END, f"{display_time} - {title}")
    
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
        """Handle selection of a journal entry"""
        # Do nothing on selection - wait for view button press or double-click
        pass
    
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
        """Save a journal entry to an individual file"""
        content = content.strip()
        if not content:
            messagebox.showinfo("Empty Entry", "Please write something in your entry before saving.")
            return
        
        # Use a default title if none provided
        if not title:
            title = "Untitled Entry"
        
        # Create entry object
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "title": title,
            "content": content,
            "id": f"entry_{int(time.time())}"  # Unique ID for the entry
        }
        
        # Save to a file
        self.save_journal_entry_to_file(entry)
        
        # Close the window
        window.destroy()
        
        # Refresh the entries list
        self.load_journal_entries()
        
        # Confirm to user
        messagebox.showinfo("Entry Saved", "Your journal entry has been saved.")
    
    def save_journal_entry_to_file(self, entry):
        """Save journal entry to an individual file"""
        # Ensure directory exists
        self.ensure_journal_directory()
        
        # Create filename from timestamp
        timestamp = entry["timestamp"].replace(" ", "_").replace(":", "-")
        filename = f"entry_{timestamp}.json"
        file_path = os.path.join("resources", "journal", filename)
        
        # Save to file
        with open(file_path, "w") as f:
            json.dump(entry, f, indent=2)
            
        # Also keep a reference in user_data for backward compatibility
        if "journal_entries" not in self.user_data:
            self.user_data["journal_entries"] = []
            
        # Update user data
        self.user_data["journal_entries"] = [e for e in self.user_data["journal_entries"] 
                                            if e.get("id", "") != entry.get("id", "")]
        self.user_data["journal_entries"].append(entry)
        self.save_user_data()
    
    def view_journal_entry(self):
        """View a selected journal entry"""
        selection = self.journal_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select an entry to view.")
            return
        
        index = selection[0]
        if index < len(self.current_journal_entries):
            entry = self.current_journal_entries[index]
            
            # Create view window
            view_window = tk.Toplevel(self.master)
            view_window.title("Journal Entry")
            view_window.geometry("700x500")
            view_window.configure(bg=COSMIC_BLUE)
            view_window.grab_set()  # Make window modal
            
            # Content frame
            content_frame = tk.Frame(view_window, bg=COSMIC_BLUE)
            content_frame.pack(fill="both", expand=True, padx=20, pady=20)
            
            # Header with timestamp and title
            try:
                entry_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")
                display_time = entry_time.strftime("%B %d, %Y - %H:%M")
            except:
                display_time = entry.get("timestamp", "Unknown date")
                
            time_label = tk.Label(
                content_frame,
                text=display_time,
                font=self.subtitle_font,
                fg=NEURAL_GREEN,
                bg=COSMIC_BLUE
            )
            time_label.pack(anchor="w")
            
            title = entry.get("title", "Untitled Entry")
            title_label = tk.Label(
                content_frame,
                text=title,
                font=("Helvetica", 16, "bold"),
                fg=MIND_GOLD,
                bg=COSMIC_BLUE
            )
            title_label.pack(anchor="w", pady=(5, 15))
            
            # Entry content in a scrolled text widget
            text_frame = tk.Frame(content_frame, bg=DEEP_THOUGHT, bd=1, relief=tk.RAISED)
            text_frame.pack(fill="both", expand=True)
            
            # Scrollbar
            scrollbar = tk.Scrollbar(text_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Text widget with entry content
            content_text = tk.Text(
                text_frame,
                font=("Helvetica", 12),
                bg=DEEP_THOUGHT,
                fg=PEARL_WHITE,
                wrap=tk.WORD,
                padx=20,
                pady=20,
                yscrollcommand=scrollbar.set
            )
            content_text.pack(fill="both", expand=True)
            content_text.insert("1.0", entry.get("content", ""))
            content_text.config(state="disabled")  # Read-only
            
            # Configure scrollbar
            scrollbar.config(command=content_text.yview)
            
            # Buttons
            button_frame = tk.Frame(view_window, bg=COSMIC_BLUE)
            button_frame.pack(fill="x", padx=20, pady=10)
            
            edit_btn = tk.Button(
                button_frame,
                text="Edit",
                font=self.normal_font,
                bg=MIND_GOLD,
                fg=PEARL_WHITE,
                command=lambda: self.edit_journal_entry(index=index)
            )
            edit_btn.pack(side=tk.LEFT, padx=5)
            
            close_btn = tk.Button(
                button_frame,
                text="Close",
                font=self.normal_font,
                bg=DEEP_THOUGHT,
                fg=PEARL_WHITE,
                command=view_window.destroy
            )
            close_btn.pack(side=tk.RIGHT, padx=5)
    
    def edit_journal_entry(self, index=None):
        """Edit an existing journal entry"""
        # If no index provided, get from selection
        if index is None:
            selection = self.journal_listbox.curselection()
            if not selection:
                messagebox.showinfo("No Selection", "Please select an entry to edit.")
                return
            index = selection[0]
        
        if index < len(self.current_journal_entries):
            entry = self.current_journal_entries[index]
            
            # Create edit window
            edit_window = tk.Toplevel(self.master)
            edit_window.title("Edit Journal Entry")
            edit_window.geometry("700x500")
            edit_window.configure(bg=COSMIC_BLUE)
            edit_window.grab_set()  # Make window modal
            
            # Entry frame
            entry_frame = tk.Frame(edit_window, bg=COSMIC_BLUE)
            entry_frame.pack(fill="both", expand=True, padx=20, pady=20)
            
            # Title/date frame
            header_frame = tk.Frame(entry_frame, bg=COSMIC_BLUE)
            header_frame.pack(fill="x", pady=10)
            
            # Display original timestamp
            try:
                entry_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")
                display_time = entry_time.strftime("%B %d, %Y - %H:%M")
            except:
                display_time = entry.get("timestamp", "Unknown date")
                
            date_label = tk.Label(
                header_frame,
                text=f"Created: {display_time}",
                font=self.subtitle_font,
                fg=NEURAL_GREEN,
                bg=COSMIC_BLUE
            )
            date_label.pack(anchor="w")
            
            # Add edit timestamp
            edit_label = tk.Label(
                header_frame,
                text=f"Editing: {datetime.now().strftime('%B %d, %Y - %H:%M')}",
                font=self.small_font,
                fg=AMBIENT_TEAL,
                bg=COSMIC_BLUE
            )
            edit_label.pack(anchor="w")
            
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
            title_entry.insert(0, entry.get("title", ""))
            
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
            content_text.insert("1.0", entry.get("content", ""))
            
            # Configure scrollbar
            content_scrollbar.config(command=content_text.yview)
            
            # Buttons
            button_frame = tk.Frame(edit_window, bg=COSMIC_BLUE)
            button_frame.pack(fill="x", padx=20, pady=10)
            
            # Include original ID and timestamp to update the correct file
            entry_id = entry.get("id", f"entry_{int(time.time())}")
            original_timestamp = entry.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            
            update_btn = tk.Button(
                button_frame,
                text="Update Entry",
                font=self.normal_font,
                bg=NEURAL_GREEN,
                fg=PEARL_WHITE,
                command=lambda: self.update_journal_entry(
                    entry_id, 
                    original_timestamp,
                    title_entry.get(),
                    content_text.get("1.0", tk.END),
                    edit_window
                )
            )
            update_btn.pack(side=tk.RIGHT, padx=5)
            
            cancel_btn = tk.Button(
                button_frame,
                text="Cancel",
                font=self.normal_font,
                bg=DEEP_THOUGHT,
                fg=PEARL_WHITE,
                command=edit_window.destroy
            )
            cancel_btn.pack(side=tk.RIGHT, padx=5)
    
    def update_journal_entry(self, entry_id, original_timestamp, title, content, window):
        """Update an existing journal entry"""
        content = content.strip()
        if not content:
            messagebox.showinfo("Empty Entry", "Please write something in your entry before saving.")
            return
        
        # Use a default title if none provided
        if not title:
            title = "Untitled Entry"
        
        # Find the existing file
        journal_dir = os.path.join("resources", "journal")
        timestamp_str = original_timestamp.replace(" ", "_").replace(":", "-")
        old_filename = f"entry_{timestamp_str}.json"
        old_file_path = os.path.join(journal_dir, old_filename)
        
        # Create updated entry object
        # Keep the original timestamp for file identification
        updated_entry = {
            "timestamp": original_timestamp,
            "title": title,
            "content": content,
            "id": entry_id,
            "last_edited": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Delete old file if it exists
        if os.path.exists(old_file_path):
            os.remove(old_file_path)
        
        # Save updated entry
        self.save_journal_entry_to_file(updated_entry)
        
        # Close window
        window.destroy()
        
        # Refresh entries
        self.load_journal_entries()
        
        # Confirm to user
        messagebox.showinfo("Entry Updated", "Your journal entry has been updated.")
    
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

if __name__ == "__main__":
    app = EnchantedMindMirror()
    app.master.mainloop() 