import tkinter as tk
from tkinter import ttk, Canvas, PhotoImage
import time
import threading
import random
import math
import pygame
from PIL import Image, ImageTk, ImageFilter, ImageOps, ImageDraw, ImageFont
import os
import json

# Create directories if they don't exist
os.makedirs("resources/sounds", exist_ok=True)
os.makedirs("resources/images", exist_ok=True)
os.makedirs("resources/fonts", exist_ok=True)
os.makedirs("journal", exist_ok=True)

# Initialize pygame mixer for sounds
pygame.mixer.init()

class EnchantedMindMirror:
    """A mystical tool for self-reflection, consciousness expansion, and ego dissolution."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("✧･ﾟ: *✧･ﾟ Enchanted Mind Mirror ･ﾟ✧*:･ﾟ✧")
        self.root.geometry("900x700")
        self.root.configure(bg="#111122")
        
        # Set app icon
        # self.root.iconbitmap("resources/images/mirror_icon.ico")
        
        # User data
        self.user_data = {
            "name": "",
            "journal_entries": [],
            "beliefs": {},
            "meditation_stats": {
                "total_duration": 0,
                "sessions": 0
            }
        }
        
        # Load user data if exists
        self.load_user_data()
        
        # Create the main container
        self.main_frame = tk.Frame(self.root, bg="#111122")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create the starfield canvas
        self.canvas = Canvas(self.main_frame, bg="#111122", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create stars
        self.stars = []
        for _ in range(200):
            x = random.randint(0, 900)
            y = random.randint(0, 700)
            size = random.uniform(0.5, 2.5)
            brightness = random.uniform(0.3, 1.0)
            twinkle_speed = random.uniform(0.02, 0.1)
            star = self.canvas.create_oval(x, y, x+size, y+size, 
                                          fill=self.get_star_color(brightness), 
                                          outline="")
            self.stars.append({
                "id": star,
                "brightness": brightness,
                "max_brightness": brightness,
                "twinkle_speed": twinkle_speed,
                "twinkle_direction": 1 if random.random() > 0.5 else -1
            })
        
        # Start animation
        self.animate_stars()
        
        # Create the welcome frame
        self.create_welcome_frame()
        
        # Initialize other variables
        self.current_module = None
        self.meditation_active = False
        self.meditation_duration = 120  # seconds
        
    def get_star_color(self, brightness):
        """Generate a mystical star color based on brightness."""
        r = min(255, int(220 * brightness))
        g = min(255, int(220 * brightness))
        b = min(255, int(255 * brightness))
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def animate_stars(self):
        """Animate the stars to twinkle."""
        for star in self.stars:
            # Update star brightness
            star["brightness"] += star["twinkle_speed"] * star["twinkle_direction"]
            
            # Change direction if limits reached
            if star["brightness"] <= 0.1:
                star["twinkle_direction"] = 1
            elif star["brightness"] >= star["max_brightness"]:
                star["twinkle_direction"] = -1
                
            # Update star color
            self.canvas.itemconfig(star["id"], fill=self.get_star_color(star["brightness"]))
        
        # Continue animation
        self.root.after(50, self.animate_stars)
        
    def create_welcome_frame(self):
        """Create the welcome screen with name entry."""
        self.welcome_frame = tk.Frame(self.canvas, bg="#111122", bd=0)
        self.canvas.create_window(450, 350, window=self.welcome_frame, width=600, height=500)
        
        # Title with mystical symbols
        title_label = tk.Label(self.welcome_frame, 
                             text="✧･ﾟ: *✧･ﾟ Enchanted Mind Mirror ･ﾟ✧*:･ﾟ✧",
                             font=("Garamond", 24, "bold"), 
                             fg="#e0e0ff", 
                             bg="#111122")
        title_label.pack(pady=(40, 20))
        
        # Subtitle
        subtitle = tk.Label(self.welcome_frame, 
                          text="A Portal to Your Inner Cosmos",
                          font=("Garamond", 16, "italic"), 
                          fg="#a0a0dd", 
                          bg="#111122")
        subtitle.pack(pady=(0, 40))
        
        # Entry for name with styled label
        name_frame = tk.Frame(self.welcome_frame, bg="#111122")
        name_frame.pack(pady=20)
        
        name_label = tk.Label(name_frame, 
                            text="What name shall I call you, seeker?", 
                            font=("Garamond", 14), 
                            fg="#d0d0ff", 
                            bg="#111122")
        name_label.pack(pady=(0, 10))
        
        self.name_entry = tk.Entry(name_frame, 
                                 font=("Garamond", 14),
                                 width=30, 
                                 bg="#1a1a2e", 
                                 fg="#e0e0ff", 
                                 insertbackground="#e0e0ff", 
                                 relief=tk.FLAT, 
                                 bd=0)
        self.name_entry.pack(pady=5, ipady=8)
        
        # Add a decorative line under the entry
        line_frame = tk.Frame(name_frame, height=2, width=300, bg="#6060a0")
        line_frame.pack(pady=(0, 20))
        
        # If we have a saved name, use it
        if self.user_data["name"]:
            self.name_entry.insert(0, self.user_data["name"])
        
        # Button frame for layout
        button_frame = tk.Frame(self.welcome_frame, bg="#111122")
        button_frame.pack(pady=30)
        
        # Enter button with magical styling
        enter_button = tk.Button(button_frame, 
                               text="✧ Enter the Mirror ✧", 
                               command=self.show_main_menu,
                               font=("Garamond", 14, "bold"), 
                               bg="#2d2d4a", 
                               fg="#e0e0ff",
                               activebackground="#3d3d6a",
                               activeforeground="#ffffff",
                               relief=tk.FLAT,
                               bd=0,
                               padx=20,
                               pady=10)
        enter_button.pack(side=tk.LEFT, padx=10)
        
        # Exit button
        exit_button = tk.Button(button_frame, 
                              text="✧ Exit ✧", 
                              command=self.root.destroy,
                              font=("Garamond", 14, "bold"), 
                              bg="#3d2d4a", 
                              fg="#e0e0ff",
                              activebackground="#5d3d6a",
                              activeforeground="#ffffff",
                              relief=tk.FLAT,
                              bd=0,
                              padx=20,
                              pady=10)
        exit_button.pack(side=tk.LEFT, padx=10)
        
    def show_main_menu(self):
        """Display the main menu after name entry."""
        # Get the user's name from entry
        name = self.name_entry.get().strip()
        if name:
            self.user_data["name"] = name
            self.save_user_data()
        
        # Clear the welcome frame if it exists
        if hasattr(self, 'welcome_frame'):
            self.welcome_frame.destroy()
        
        # Create the main menu frame
        self.menu_frame = tk.Frame(self.canvas, bg="#111122", bd=0)
        self.canvas.create_window(450, 350, window=self.menu_frame, width=700, height=600)
        
        # Greeting with user's name
        greeting = tk.Label(self.menu_frame, 
                          text=f"Greetings, {self.user_data['name'] or 'Seeker'}", 
                          font=("Garamond", 24, "bold"), 
                          fg="#e0e0ff", 
                          bg="#111122")
        greeting.pack(pady=(40, 10))
        
        # Mystical subtitle
        subtitle = tk.Label(self.menu_frame, 
                          text="What aspect of your consciousness shall we explore?", 
                          font=("Garamond", 16, "italic"), 
                          fg="#a0a0dd", 
                          bg="#111122")
        subtitle.pack(pady=(0, 50))
        
        # Create buttons for each module with magical styling
        button_configs = [
            {
                "text": "✧ Self Reflection ✧", 
                "desc": "Gaze into the mirror of your soul",
                "command": self.show_self_reflection
            },
            {
                "text": "✧ Consciousness Expansion ✧", 
                "desc": "Journey beyond the boundaries of self",
                "command": self.show_consciousness_expansion
            },
            {
                "text": "✧ Ego Dissolution ✧", 
                "desc": "Dissolve the illusions that bind you",
                "command": self.show_ego_dissolution
            },
            {
                "text": "✧ Dream Journal ✧", 
                "desc": "Record the messages from your subconscious",
                "command": self.show_journal
            }
        ]
        
        for config in button_configs:
            btn_frame = tk.Frame(self.menu_frame, bg="#111122")
            btn_frame.pack(pady=10, fill=tk.X, padx=100)
            
            btn = tk.Button(btn_frame, 
                          text=config["text"], 
                          command=config["command"],
                          font=("Garamond", 14, "bold"), 
                          bg="#2d2d4a", 
                          fg="#e0e0ff",
                          activebackground="#3d3d6a",
                          activeforeground="#ffffff",
                          relief=tk.FLAT,
                          bd=0,
                          padx=20,
                          pady=10,
                          width=30)
            btn.pack()
            
            # Description label
            desc = tk.Label(btn_frame, 
                          text=config["desc"], 
                          font=("Garamond", 11, "italic"), 
                          fg="#a0a0dd", 
                          bg="#111122")
            desc.pack(pady=(5, 0))
    
    def show_self_reflection(self):
        """Display the self reflection module."""
        self.clear_current_module()
        self.current_module = "self_reflection"
        
        # Create the self reflection frame
        self.reflection_frame = tk.Frame(self.canvas, bg="#111122", bd=0)
        self.canvas.create_window(450, 350, window=self.reflection_frame, width=700, height=600)
        
        # Title
        title = tk.Label(self.reflection_frame, 
                       text="✧ The Mirror of Self ✧", 
                       font=("Garamond", 24, "bold"), 
                       fg="#e0e0ff", 
                       bg="#111122")
        title.pack(pady=(30, 20))
        
        # Create a "mirror" effect canvas
        mirror_frame = tk.Frame(self.reflection_frame, bg="#111122")
        mirror_frame.pack(pady=20)
        
        mirror_canvas = Canvas(mirror_frame, width=400, height=300, 
                             bg="#1a1a2e", highlightthickness=2, 
                             highlightbackground="#6060a0")
        mirror_canvas.pack()
        
        # Create reflection text with mystical prompts
        reflection_prompts = [
            f"Look deeply, {self.user_data['name'] or 'Seeker'}. What do you see?",
            "Beyond the veil of appearance...",
            "Behind the mask of persona...",
            "Beneath the stories you tell yourself...",
            "Who are you, truly?",
            "What wisdom do you seek?",
            "What transformation do you desire?",
            "The mirror reflects your true essence...",
            "Gaze without judgment, with only curiosity..."
        ]
        
        # Add text to mirror with fade-in effect
        self.mirror_texts = []
        y_pos = 50
        for prompt in reflection_prompts:
            text_id = mirror_canvas.create_text(200, y_pos, 
                                              text=prompt, 
                                              font=("Garamond", 14, "italic"), 
                                              fill="#404080",
                                              width=350)
            self.mirror_texts.append(text_id)
            y_pos += 30
        
        # Add fade-in animation for the mirror texts
        self.fade_in_texts(mirror_canvas, self.mirror_texts)
        
        # Add ripple effect to the mirror
        self.ripple_effect(mirror_canvas)
        
        # Journal entry for reflections
        journal_frame = tk.Frame(self.reflection_frame, bg="#111122")
        journal_frame.pack(pady=20, fill=tk.X, padx=50)
        
        journal_label = tk.Label(journal_frame, 
                               text="Record your reflections:", 
                               font=("Garamond", 14), 
                               fg="#d0d0ff", 
                               bg="#111122")
        journal_label.pack(anchor="w", pady=(0, 5))
        
        self.reflection_entry = tk.Text(journal_frame, 
                                      height=4, 
                                      font=("Garamond", 12),
                                      bg="#1a1a2e", 
                                      fg="#e0e0ff", 
                                      insertbackground="#e0e0ff", 
                                      relief=tk.FLAT, 
                                      bd=0)
        self.reflection_entry.pack(fill=tk.X, pady=5)
        
        # Add a decorative line under the entry
        line_frame = tk.Frame(journal_frame, height=2, width=600, bg="#6060a0")
        line_frame.pack(pady=(0, 10))
        
        # Save button
        save_button = tk.Button(journal_frame, 
                              text="✧ Save Reflection ✧", 
                              command=self.save_reflection,
                              font=("Garamond", 12, "bold"), 
                              bg="#2d2d4a", 
                              fg="#e0e0ff",
                              activebackground="#3d3d6a",
                              activeforeground="#ffffff",
                              relief=tk.FLAT,
                              bd=0,
                              padx=15,
                              pady=5)
        save_button.pack(pady=5)
        
        # Back button with enhanced styling
        back_button = tk.Button(self.reflection_frame, 
                              text="✧ Return to Menu ✧", 
                              command=self.show_main_menu,
                              font=("Garamond", 12, "bold"), 
                              bg="#2d2d4a", 
                              fg="#e0e0ff",
                              activebackground="#3d3d6a",
                              activeforeground="#ffffff",
                              relief=tk.FLAT,
                              bd=0,
                              padx=15,
                              pady=8)
        back_button.pack(side=tk.BOTTOM, pady=20)
    
    def fade_in_texts(self, canvas, text_ids, current_alpha=0):
        """Gradually fade in text elements."""
        if current_alpha <= 100:
            # Calculate hex color based on alpha
            alpha_hex = int(current_alpha * 255 / 100)
            color = f"#{alpha_hex:02x}{alpha_hex:02x}{min(alpha_hex + 70, 255):02x}"
            
            # Update all text elements
            for text_id in text_ids:
                canvas.itemconfig(text_id, fill=color)
            
            # Schedule next fade step
            self.root.after(50, self.fade_in_texts, canvas, text_ids, current_alpha + 2)
    
    def ripple_effect(self, canvas):
        """Create a ripple effect on the mirror canvas."""
        # Check if current module is still reflection
        if self.current_module != "self_reflection":
            return
            
        # Create ripple
        x = random.randint(50, 350)
        y = random.randint(50, 250)
        
        # Create concentric circles that expand and fade
        circles = []
        for size in range(5, 40, 5):
            circle = canvas.create_oval(x-size, y-size, x+size, y+size, 
                                      outline="#8080ff", fill="", 
                                      width=1.5)
            circles.append(circle)
        
        # Animate ripples
        self.animate_ripples(canvas, circles, 1)
        
        # Schedule next ripple
        delay = random.randint(3000, 8000)  # Random delay between ripples
        self.root.after(delay, self.ripple_effect, canvas)
    
    def animate_ripples(self, canvas, circles, step):
        """Animate the ripple circles to expand and fade."""
        # Check if current module is still reflection
        if self.current_module != "self_reflection":
            return
            
        if step <= 20:
            # Expand and fade circles
            for i, circle in enumerate(circles):
                size = 5 + i*5 + step
                alpha = int(max(0, 200 - step*10 - i*15))
                color = f"#{alpha:02x}{alpha:02x}{min(alpha + 70, 255):02x}"
                
                x1, y1, x2, y2 = canvas.coords(circle)
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                
                canvas.coords(circle, 
                            center_x - size, center_y - size,
                            center_x + size, center_y + size)
                canvas.itemconfig(circle, outline=color)
            
            # Schedule next animation frame
            self.root.after(50, self.animate_ripples, canvas, circles, step + 1)
        else:
            # Remove circles when animation is complete
            for circle in circles:
                canvas.delete(circle)
    
    def save_reflection(self):
        """Save the user's reflection to their journal."""
        reflection_text = self.reflection_entry.get("1.0", tk.END).strip()
        if reflection_text:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = {
                "timestamp": timestamp,
                "content": reflection_text,
                "type": "reflection"
            }
            self.user_data["journal_entries"].append(entry)
            self.save_user_data()
            
            # Clear the entry field
            self.reflection_entry.delete("1.0", tk.END)
            
            # Show confirmation message
            self.show_message("Reflection saved to your journal.", "#111122", "#a0a0dd")
    
    def show_consciousness_expansion(self):
        """Display the consciousness expansion (meditation) module."""
        self.clear_current_module()
        self.current_module = "consciousness_expansion"
        
        # Create the meditation frame
        self.meditation_frame = tk.Frame(self.canvas, bg="#111122", bd=0)
        self.canvas.create_window(450, 350, window=self.meditation_frame, width=700, height=600)
        
        # Title
        title = tk.Label(self.meditation_frame, 
                       text="✧ Consciousness Expansion ✧", 
                       font=("Garamond", 24, "bold"), 
                       fg="#e0e0ff", 
                       bg="#111122")
        title.pack(pady=(30, 20))
        
        # Meditation image/canvas
        meditation_canvas = Canvas(self.meditation_frame, width=400, height=200, 
                                 bg="#111122", highlightthickness=0)
        meditation_canvas.pack(pady=10)
        
        # Create a simple mandala on the canvas
        self.draw_mandala(meditation_canvas, 200, 100, 80)
        
        # Duration slider
        duration_frame = tk.Frame(self.meditation_frame, bg="#111122")
        duration_frame.pack(pady=20, fill=tk.X, padx=50)
        
        duration_label = tk.Label(duration_frame, 
                                text="Meditation Duration (minutes):", 
                                font=("Garamond", 14), 
                                fg="#d0d0ff", 
                                bg="#111122")
        duration_label.pack(anchor="w", pady=(0, 5))
        
        self.duration_slider = ttk.Scale(duration_frame, 
                                       from_=1, 
                                       to=20, 
                                       orient='horizontal',
                                       value=2)
        self.duration_slider.pack(fill=tk.X, pady=5)
        
        # Duration value label
        self.duration_value = tk.Label(duration_frame, 
                                     text="2 minutes", 
                                     font=("Garamond", 12), 
                                     fg="#a0a0dd", 
                                     bg="#111122")
        self.duration_value.pack(pady=(0, 10))
        
        # Update duration value label when slider changes
        def update_duration_label(event):
            value = round(self.duration_slider.get())
            self.duration_value.config(text=f"{value} minutes")
            self.meditation_duration = value * 60  # Convert to seconds
        
        self.duration_slider.bind("<Motion>", update_duration_label)
        
        # Start button
        self.start_button = tk.Button(self.meditation_frame, 
                                    text="✧ Begin Meditation Journey ✧", 
                                    command=self.start_meditation,
                                    font=("Garamond", 14, "bold"), 
                                    bg="#2d2d4a", 
                                    fg="#e0e0ff",
                                    activebackground="#3d3d6a",
                                    activeforeground="#ffffff",
                                    relief=tk.FLAT,
                                    bd=0,
                                    padx=20,
                                    pady=10)
        self.start_button.pack(pady=20)
        
        # Progress elements (initially hidden)
        self.progress_frame = tk.Frame(self.meditation_frame, bg="#111122")
        self.progress_frame.pack(pady=20, fill=tk.X, padx=50)
        self.progress_frame.pack_forget()  # Hide initially
        
        self.progress_label = tk.Label(self.progress_frame, 
                                     text="", 
                                     font=("Garamond", 14, "italic"), 
                                     fg="#e0e0ff", 
                                     bg="#111122",
                                     wraplength=500)
        self.progress_label.pack(pady=10)
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", 
                                          length=500, mode="determinate")
        self.progress_bar.pack(pady=10)
        
        # Back button with enhanced styling
        self.back_button = tk.Button(self.meditation_frame, 
                                   text="✧ Return to Menu ✧", 
                                   command=self.show_main_menu,
                                   font=("Garamond", 12, "bold"), 
                                   bg="#2d2d4a", 
                                   fg="#e0e0ff",
                                   activebackground="#3d3d6a",
                                   activeforeground="#ffffff",
                                   relief=tk.FLAT,
                                   bd=0,
                                   padx=15,
                                   pady=8)
        self.back_button.pack(side=tk.BOTTOM, pady=20)
    
    def draw_mandala(self, canvas, x, y, radius):
        """Draw a simple mandala on the given canvas."""
        # Draw concentric circles
        for r in range(10, radius, 10):
            canvas.create_oval(x-r, y-r, x+r, y+r, 
                              outline="#6060a0", 
                              width=1.5)
        
        # Draw radial lines
        for angle in range(0, 360, 15):
            angle_rad = math.radians(angle)
            x1 = x + radius * math.cos(angle_rad)
            y1 = y + radius * math.sin(angle_rad)
            canvas.create_line(x, y, x1, y1, 
                              fill="#6060a0", 
                              width=1.5)
        
        # Central circle
        canvas.create_oval(x-15, y-15, x+15, y+15, 
                          fill="#3d3d6a", 
                          outline="#8080d0", 
                          width=2)
    
    def start_meditation(self):
        """Begin the guided meditation session."""
        # Disable start button
        self.start_button.config(state=tk.DISABLED)
        self.back_button.config(state=tk.DISABLED)
        
        # Show progress elements
        self.progress_frame.pack(pady=20, fill=tk.X, padx=50)
        
        # Set meditation active flag
        self.meditation_active = True
        
        # Start meditation in a separate thread
        meditation_thread = threading.Thread(target=self.run_meditation)
        meditation_thread.daemon = True
        meditation_thread.start()
    
    def run_meditation(self):
        """Run the guided meditation with progressive prompts."""
        # Meditation guidance text
        guidance = [
            "Close your eyes. Take a deep breath.",
            "Feel the gentle rhythm of your breath... in... and out...",
            "With each breath, feel your awareness expanding...",
            "First, become aware of your physical form, the vessel of consciousness...",
            "Now, gently expand your awareness to include the space around you...",
            "Feel the energetic field that extends beyond your physical form...",
            "Expand further... sense the entire room... the building... the landscape...",
            "Continue expanding... feel the connection to all living beings around you...",
            "Now, expand to encompass the entire planet... feel its rhythms and currents...",
            "Expand beyond the planet... into the cosmos... the stars... the galaxies...",
            "You are vast... boundless... connected to all that is...",
            "In this expanded state, you are both everything and nothing...",
            "Wisdom flows freely through your infinite awareness...",
            "Rest in this boundless consciousness... simply being... observing...",
            "When you are ready, slowly begin to return to your centered awareness...",
            "Gradually, gently, bring your focus back to your physical form...",
            "Take a deep breath... and when you are ready, open your eyes..."
        ]
        
        # Total steps for progress bar
        total_steps = len(guidance) + self.meditation_duration
        
        # Update progress for each guidance step
        step = 0
        for i, prompt in enumerate(guidance):
            if not self.meditation_active:
                break
                
            # Update progress label and bar on the main thread
            self.root.after(0, lambda p=prompt: self.progress_label.config(text=p))
            self.root.after(0, lambda s=step, t=total_steps: self.progress_bar.config(value=(s/t)*100))
            
            # Pause between prompts
            time.sleep(5)
            step += 1
        
        # Silence for the main meditation duration
        self.root.after(0, lambda: self.progress_label.config(text="Rest in silent awareness..."))
        
        # Update progress bar every second
        for _ in range(self.meditation_duration):
            if not self.meditation_active:
                break
                
            step += 1
            self.root.after(0, lambda s=step, t=total_steps: self.progress_bar.config(value=(s/t)*100))
            time.sleep(1)
        
        # Only show completion message if meditation wasn't cancelled
        if self.meditation_active:
            # Update user stats
            self.user_data["meditation_stats"]["total_duration"] += self.meditation_duration
            self.user_data["meditation_stats"]["sessions"] += 1
            self.save_user_data()
            
            # Show completion message
            self.root.after(0, lambda: self.progress_label.config(
                text="Meditation complete. Your consciousness has expanded."
            ))
            self.root.after(0, lambda: self.progress_bar.config(value=100))
        
        # Re-enable buttons on the main thread
        self.root.after(0, lambda: self.start_button.config(state=tk.NORMAL))
        self.root.after(0, lambda: self.back_button.config(state=tk.NORMAL))
        
        # Reset meditation flag
        self.meditation_active = False
    
    def show_ego_dissolution(self):
        """Display the ego dissolution module."""
        self.clear_current_module()
        self.current_module = "ego_dissolution"
        
        # Create the ego dissolution frame
        self.ego_frame = tk.Frame(self.canvas, bg="#111122", bd=0)
        self.canvas.create_window(450, 350, window=self.ego_frame, width=700, height=600)
        
        # Title
        title = tk.Label(self.ego_frame, 
                       text="✧ Ego Dissolution ✧", 
                       font=("Garamond", 24, "bold"), 
                       fg="#e0e0ff", 
                       bg="#111122")
        title.pack(pady=(30, 10))
        
        # Subtitle
        subtitle = tk.Label(self.ego_frame, 
                          text="Examine and release limiting beliefs", 
                          font=("Garamond", 16, "italic"), 
                          fg="#a0a0dd", 
                          bg="#111122")
        subtitle.pack(pady=(0, 30))
        
        # Default beliefs if user has none
        if not self.user_data.get("beliefs"):
            self.user_data["beliefs"] = {
                "belief1": "I am separate from others.",
                "belief2": "I am limited by my past.",
                "belief3": "I am not good enough."
            }
            self.save_user_data()
        
        # Create belief entries
        self.belief_entries = {}
        self.belief_frames = {}
        
        beliefs_container = tk.Frame(self.ego_frame, bg="#111122")
        beliefs_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Add beliefs from user data
        for i, (key, belief) in enumerate(self.user_data["beliefs"].items()):
            self.add_belief_frame(beliefs_container, key, belief)
        
        # Add button
        add_button = tk.Button(self.ego_frame, 
                             text="✧ Add New Belief ✧", 
                             command=lambda: self.add_belief_frame(beliefs_container),
                             font=("Garamond", 12, "bold"), 
                             bg="#2d2d4a", 
                             fg="#e0e0ff",
                             activebackground="#3d3d6a",
                             activeforeground="#ffffff",
                             relief=tk.FLAT,
                             bd=0,
                             padx=15,
                             pady=5)
        add_button.pack(pady=10)
        
        # Save button
        save_button = tk.Button(self.ego_frame, 
                              text="✧ Save Beliefs ✧", 
                              command=self.save_beliefs,
                              font=("Garamond", 12, "bold"), 
                              bg="#2d2d4a", 
                              fg="#e0e0ff",
                              activebackground="#3d3d6a",
                              activeforeground="#ffffff",
                              relief=tk.FLAT,
                              bd=0,
                              padx=15,
                              pady=5)
        save_button.pack(pady=5)
        
        # Back button with enhanced styling
        back_button = tk.Button(self.ego_frame, 
                              text="✧ Return to Menu ✧", 
                              command=self.show_main_menu,
                              font=("Garamond", 12, "bold"), 
                              bg="#2d2d4a", 
                              fg="#e0e0ff",
                              activebackground="#3d3d6a",
                              activeforeground="#ffffff",
                              relief=tk.FLAT,
                              bd=0,
                              padx=15,
                              pady=8)
        back_button.pack(side=tk.BOTTOM, pady=20)
    
    def add_belief_frame(self, container, key=None, belief=None):
        """Add a new belief frame with entry and reflection questions."""
        if key is None:
            # Generate a new key for the belief
            existing_keys = list(self.belief_entries.keys())
            if not existing_keys:
                key = "belief1"
            else:
                # Extract the number from the last key and increment
                last_num = int(existing_keys[-1].replace("belief", ""))
                key = f"belief{last_num + 1}"
        
        # Create frame for the belief
        belief_frame = tk.Frame(container, bg="#1a1a2e", bd=0)
        belief_frame.pack(fill=tk.X, pady=10, padx=5)
        
        # Belief entry with label
        entry_frame = tk.Frame(belief_frame, bg="#1a1a2e")
        entry_frame.pack(fill=tk.X, padx=10, pady=10)
        
        belief_label = tk.Label(entry_frame, 
                              text="Limiting Belief:", 
                              font=("Garamond", 12, "bold"), 
                              fg="#d0d0ff", 
                              bg="#1a1a2e")
        belief_label.pack(side=tk.LEFT, padx=(0, 10))
        
        belief_entry = tk.Entry(entry_frame, 
                              font=("Garamond", 12),
                              width=50, 
                              bg="#2d2d4a", 
                              fg="#e0e0ff", 
                              insertbackground="#e0e0ff", 
                              relief=tk.FLAT, 
                              bd=0)
        belief_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5, padx=(0, 10))
        
        # Add initial value if provided
        if belief:
            belief_entry.insert(0, belief)
        
        # Store reference to the entry widget
        self.belief_entries[key] = belief_entry
        self.belief_frames[key] = belief_frame
        
        # Delete button
        delete_button = tk.Button(entry_frame, 
                                text="✕", 
                                command=lambda k=key: self.delete_belief(k),
                                font=("Garamond", 12), 
                                bg="#3d3d6a", 
                                fg="#e0e0ff",
                                activebackground="#5d5d8a",
                                activeforeground="#ffffff",
                                relief=tk.FLAT,
                                bd=0,
                                width=2,
                                height=1)
        delete_button.pack(side=tk.RIGHT)
        
        # Challenge questions
        questions_frame = tk.Frame(belief_frame, bg="#1a1a2e")
        questions_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        
        questions = [
            "Is this belief really true, or just a story?",
            "How does this belief limit you?",
            "Who would you be without this belief?",
            "What new belief could you choose instead?"
        ]
        
        for question in questions:
            q_label = tk.Label(questions_frame, 
                             text=f"• {question}", 
                             font=("Garamond", 11, "italic"), 
                             fg="#a0a0dd", 
                             bg="#1a1a2e",
                             anchor="w",
                             justify=tk.LEFT)
            q_label.pack(fill=tk.X, pady=2, anchor="w")
    
    def delete_belief(self, key):
        """Delete a belief entry."""
        # Remove the frame from the UI
        if key in self.belief_frames:
            self.belief_frames[key].destroy()
            del self.belief_frames[key]
        
        # Remove from entries dict
        if key in self.belief_entries:
            del self.belief_entries[key]
    
    def save_beliefs(self):
        """Save the current beliefs to user data."""
        # Clear existing beliefs
        self.user_data["beliefs"] = {}
        
        # Add current beliefs from entries
        for key, entry in self.belief_entries.items():
            belief_text = entry.get().strip()
            if belief_text:
                self.user_data["beliefs"][key] = belief_text
        
        # Save user data
        self.save_user_data()
        
        # Show confirmation message
        self.show_message("Your beliefs have been saved.", "#111122", "#a0a0dd")
    
    def show_journal(self):
        """Display the user's dream and reflection journal."""
        self.clear_current_module()
        self.current_module = "journal"
        
        # Create the journal frame
        self.journal_frame = tk.Frame(self.canvas, bg="#111122", bd=0)
        self.canvas.create_window(450, 350, window=self.journal_frame, width=700, height=600)
        
        # Title
        title = tk.Label(self.journal_frame, 
                       text="✧ Your Mystical Journal ✧", 
                       font=("Garamond", 24, "bold"), 
                       fg="#e0e0ff", 
                       bg="#111122")
        title.pack(pady=(30, 10))
        
        # Subtitle with stats
        meditation_time = self.user_data["meditation_stats"]["total_duration"] // 60
        meditation_sessions = self.user_data["meditation_stats"]["sessions"]
        journal_entries = len(self.user_data["journal_entries"])
        
        stats_text = f"Meditation: {meditation_time} minutes across {meditation_sessions} sessions • Journal Entries: {journal_entries}"
        stats = tk.Label(self.journal_frame, 
                       text=stats_text, 
                       font=("Garamond", 12, "italic"), 
                       fg="#a0a0dd", 
                       bg="#111122")
        stats.pack(pady=(0, 20))
        
        # Journal entries container with scrollbar
        container_frame = tk.Frame(self.journal_frame, bg="#111122")
        container_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Canvas and scrollbar for scrolling
        canvas = Canvas(container_frame, bg="#111122", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#111122")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add entries from user data (most recent first)
        if self.user_data["journal_entries"]:
            for entry in reversed(self.user_data["journal_entries"]):
                self.add_journal_entry(scrollable_frame, entry)
        else:
            # Empty state
            empty_label = tk.Label(scrollable_frame, 
                                 text="Your journal is empty. Record reflections to see them here.", 
                                 font=("Garamond", 14, "italic"), 
                                 fg="#a0a0dd", 
                                 bg="#111122")
            empty_label.pack(pady=50)
        
        # New entry button
        new_entry_button = tk.Button(self.journal_frame, 
                                   text="✧ New Journal Entry ✧", 
                                   command=self.show_new_entry,
                                   font=("Garamond", 12, "bold"), 
                                   bg="#2d2d4a", 
                                   fg="#e0e0ff",
                                   activebackground="#3d3d6a",
                                   activeforeground="#ffffff",
                                   relief=tk.FLAT,
                                   bd=0,
                                   padx=15,
                                   pady=5)
        new_entry_button.pack(pady=10)
        
        # Back button with enhanced styling
        back_button = tk.Button(self.journal_frame, 
                              text="✧ Return to Menu ✧", 
                              command=self.show_main_menu,
                              font=("Garamond", 12, "bold"), 
                              bg="#2d2d4a", 
                              fg="#e0e0ff",
                              activebackground="#3d3d6a",
                              activeforeground="#ffffff",
                              relief=tk.FLAT,
                              bd=0,
                              padx=15,
                              pady=8)
        back_button.pack(side=tk.BOTTOM, pady=20)
    
    def add_journal_entry(self, container, entry):
        """Add a journal entry to the container."""
        # Create frame for the entry
        entry_frame = tk.Frame(container, bg="#1a1a2e", bd=0)
        entry_frame.pack(fill=tk.X, pady=10, padx=5)
        
        # Header with date
        header_frame = tk.Frame(entry_frame, bg="#2d2d4a")
        header_frame.pack(fill=tk.X)
        
        date_label = tk.Label(header_frame, 
                            text=entry["timestamp"], 
                            font=("Garamond", 12), 
                            fg="#d0d0ff", 
                            bg="#2d2d4a")
        date_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        type_label = tk.Label(header_frame, 
                            text=entry.get("type", "Journal").capitalize(), 
                            font=("Garamond", 12, "italic"), 
                            fg="#a0a0dd", 
                            bg="#2d2d4a")
        type_label.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # Content
        content_frame = tk.Frame(entry_frame, bg="#1a1a2e")
        content_frame.pack(fill=tk.X, padx=10, pady=10)
        
        content_text = tk.Text(content_frame, 
                             font=("Garamond", 12),
                             width=80, 
                             height=4, 
                             bg="#1a1a2e", 
                             fg="#e0e0ff", 
                             relief=tk.FLAT, 
                             bd=0,
                             wrap=tk.WORD)
        content_text.pack(fill=tk.X)
        content_text.insert("1.0", entry["content"])
        content_text.config(state=tk.DISABLED)
    
    def show_new_entry(self):
        """Show form for creating a new journal entry."""
        # Create a new window for the entry
        entry_window = tk.Toplevel(self.root)
        entry_window.title("New Journal Entry")
        entry_window.geometry("600x400")
        entry_window.configure(bg="#111122")
        
        # Title
        title = tk.Label(entry_window, 
                       text="✧ New Journal Entry ✧", 
                       font=("Garamond", 20, "bold"), 
                       fg="#e0e0ff", 
                       bg="#111122")
        title.pack(pady=(20, 10))
        
        # Type selection
        type_frame = tk.Frame(entry_window, bg="#111122")
        type_frame.pack(fill=tk.X, padx=20, pady=10)
        
        type_label = tk.Label(type_frame, 
                            text="Entry Type:", 
                            font=("Garamond", 12), 
                            fg="#d0d0ff", 
                            bg="#111122")
        type_label.pack(side=tk.LEFT, padx=(0, 10))
        
        entry_type = tk.StringVar(value="journal")
        
        journal_radio = tk.Radiobutton(type_frame, 
                                     text="Journal", 
                                     variable=entry_type, 
                                     value="journal",
                                     font=("Garamond", 12),
                                     fg="#d0d0ff",
                                     bg="#111122",
                                     selectcolor="#2d2d4a",
                                     activebackground="#111122",
                                     activeforeground="#e0e0ff")
        journal_radio.pack(side=tk.LEFT, padx=10)
        
        dream_radio = tk.Radiobutton(type_frame, 
                                   text="Dream", 
                                   variable=entry_type, 
                                   value="dream",
                                   font=("Garamond", 12),
                                   fg="#d0d0ff",
                                   bg="#111122",
                                   selectcolor="#2d2d4a",
                                   activebackground="#111122",
                                   activeforeground="#e0e0ff")
        dream_radio.pack(side=tk.LEFT, padx=10)
        
        reflection_radio = tk.Radiobutton(type_frame, 
                                        text="Reflection", 
                                        variable=entry_type, 
                                        value="reflection",
                                        font=("Garamond", 12),
                                        fg="#d0d0ff",
                                        bg="#111122",
                                        selectcolor="#2d2d4a",
                                        activebackground="#111122",
                                        activeforeground="#e0e0ff")
        reflection_radio.pack(side=tk.LEFT, padx=10)
        
        # Content entry
        content_frame = tk.Frame(entry_window, bg="#111122")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        content_label = tk.Label(content_frame, 
                               text="Entry Content:", 
                               font=("Garamond", 12), 
                               fg="#d0d0ff", 
                               bg="#111122")
        content_label.pack(anchor="w", pady=(0, 5))
        
        content_text = tk.Text(content_frame, 
                             font=("Garamond", 12),
                             bg="#1a1a2e", 
                             fg="#e0e0ff", 
                             insertbackground="#e0e0ff", 
                             relief=tk.FLAT, 
                             bd=0,
                             wrap=tk.WORD)
        content_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Save button
        save_button = tk.Button(entry_window, 
                              text="✧ Save Entry ✧", 
                              command=lambda: self.save_journal_entry(entry_type.get(), content_text.get("1.0", tk.END), entry_window),
                              font=("Garamond", 12, "bold"), 
                              bg="#2d2d4a", 
                              fg="#e0e0ff",
                              activebackground="#3d3d6a",
                              activeforeground="#ffffff",
                              relief=tk.FLAT,
                              bd=0,
                              padx=15,
                              pady=5)
        save_button.pack(pady=10)
    
    def save_journal_entry(self, entry_type, content, window):
        """Save a new journal entry."""
        content = content.strip()
        if content:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            entry = {
                "timestamp": timestamp,
                "content": content,
                "type": entry_type
            }
            self.user_data["journal_entries"].append(entry)
            self.save_user_data()
            
            # Close the entry window
            window.destroy()
            
            # Refresh journal if current module is journal
            if self.current_module == "journal":
                self.show_journal()
            
            # Show confirmation message
            self.show_message("Journal entry saved successfully.", "#111122", "#a0a0dd")
    
    def show_message(self, message, bg_color, fg_color, duration=2000):
        """Show a temporary message overlay."""
        message_frame = tk.Frame(self.canvas, bg=bg_color, bd=2, relief=tk.RAISED)
        message_window = self.canvas.create_window(450, 650, window=message_frame)
        
        message_label = tk.Label(message_frame, 
                               text=message, 
                               font=("Garamond", 12), 
                               fg=fg_color, 
                               bg=bg_color,
                               padx=20, 
                               pady=10)
        message_label.pack()
        
        # Schedule message removal
        self.root.after(duration, lambda: self.canvas.delete(message_window))
    
    def clear_current_module(self):
        """Clear any current module frames."""
        if self.current_module == "self_reflection" and hasattr(self, "reflection_frame"):
            self.reflection_frame.destroy()
        elif self.current_module == "consciousness_expansion" and hasattr(self, "meditation_frame"):
            # Cancel any active meditation
            self.meditation_active = False
            self.meditation_frame.destroy()
        elif self.current_module == "ego_dissolution" and hasattr(self, "ego_frame"):
            self.ego_frame.destroy()
        elif self.current_module == "journal" and hasattr(self, "journal_frame"):
            self.journal_frame.destroy()
    
    def load_user_data(self):
        """Load user data from file if it exists."""
        try:
            with open("journal/user_data.json", "r") as f:
                self.user_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Use default user data
            pass
    
    def save_user_data(self):
        """Save user data to file."""
        try:
            with open("journal/user_data.json", "w") as f:
                json.dump(self.user_data, f, indent=2)
        except:
            print("Error saving user data")
    
    def run(self):
        """Run the Mind Mirror application."""
        self.root.mainloop()

if __name__ == "__main__":
    app = EnchantedMindMirror()
    app.run()