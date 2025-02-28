"""
RealityGlitcher - A tool for inducing perceptual anomalies in consensual reality.

This module implements the core RealityGlitcher class, which serves as an interface
to create, manage, and deploy reality glitches through various perceptual channels.
Each glitch is treated as a fracture in the fabric of perception, allowing glimpses
through the veil of ordinary consciousness.
"""

from typing import Dict, List, Optional, Tuple, Union
import random
import logging
import time
from dataclasses import dataclass
from enum import Enum, auto
import uuid

# Configure logging with mystical formatting
logging.basicConfig(
    level=logging.INFO,
    format="✧ %(asctime)s ┃ %(levelname)s ┃ %(message)s ✧",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

class GlitchType(Enum):
    """Types of reality glitches that can be induced"""
    VISUAL = auto()      # Affects visual perception
    AUDITORY = auto()    # Affects auditory perception
    TEMPORAL = auto()    # Affects perception of time
    SPATIAL = auto()     # Affects perception of space
    COGNITIVE = auto()   # Affects thought patterns
    SYNCHRONISTIC = auto()  # Creates meaningful coincidences

@dataclass
class GlitchParameters:
    """Parameters that define a reality glitch"""
    intensity: float     # 0.0 to 1.0, controls strength of the effect
    duration: float      # Duration in seconds
    complexity: float    # 0.0 to 1.0, controls intricacy of the pattern
    persistence: float   # 0.0 to 1.0, likelihood of recurrence
    
    def __post_init__(self):
        """Validate parameters are within acceptable ranges"""
        self.intensity = max(0.0, min(1.0, self.intensity))
        self.complexity = max(0.0, min(1.0, self.complexity))
        self.persistence = max(0.0, min(1.0, self.persistence))
        
        if self.duration < 0.1:
            logger.warning("Glitch duration too short, adjusting to minimum threshold")
            self.duration = 0.1

class Glitch:
    """A reality glitch instance that can be deployed and manipulated"""
    
    def __init__(self, 
                 glitch_type: GlitchType, 
                 parameters: GlitchParameters,
                 target: Optional[str] = None):
        self.id = str(uuid.uuid4())[:8]
        self.type = glitch_type
        self.parameters = parameters
        self.target = target or "consensus_reality"
        self.creation_time = time.time()
        self.active = False
        self.safety_anchor = self._generate_safety_anchor()
        
        # Calculated properties
        self.stability = self._calculate_stability()
        
    def _generate_safety_anchor(self) -> str:
        """Generates a unique safety anchor for reality restoration"""
        symbols = "✧✦✮✯✩✪✫✬✭"
        anchor = f"{random.choice(symbols)}anchor_{self.id}{random.choice(symbols)}"
        return anchor
    
    def _calculate_stability(self) -> float:
        """Calculate the stability of the glitch based on its parameters"""
        # Higher intensity and complexity reduce stability
        # Longer duration reduces stability
        stability = 1.0 - (
            (self.parameters.intensity * 0.4) + 
            (self.parameters.complexity * 0.3) + 
            (min(1.0, self.parameters.duration / 10.0) * 0.3)
        )
        return max(0.1, stability)  # Ensure minimum stability of 0.1
    
    def activate(self) -> bool:
        """Activate the glitch, introducing it into the target reality"""
        self.active = True
        logger.info(f"Glitch {self.id} activated in {self.target}. Reality fracture detected.")
        logger.info(f"Stability rating: {self.stability:.2f} | Safety anchor: {self.safety_anchor}")
        return True
        
    def deactivate(self) -> bool:
        """Deactivate the glitch, restoring normal reality parameters"""
        self.active = False
        logger.info(f"Glitch {self.id} deactivated. Reality coherence restored.")
        return True
    
    def __repr__(self) -> str:
        status = "ACTIVE" if self.active else "INACTIVE"
        return f"<Glitch {self.id} | {self.type.name} | {status} | Stability: {self.stability:.2f}>"


class RealityGlitcher:
    """Main interface for creating and managing reality glitches"""
    
    def __init__(self):
        self.active_glitches: List[Glitch] = []
        self.perception_filters: Dict[GlitchType, bool] = {
            GlitchType.VISUAL: True,
            GlitchType.AUDITORY: True,
            GlitchType.TEMPORAL: False,  # Temporal glitches disabled by default (dangerous)
            GlitchType.SPATIAL: True,
            GlitchType.COGNITIVE: False, # Cognitive glitches disabled by default (dangerous)
            GlitchType.SYNCHRONISTIC: True
        }
        self.safety_protocols: Dict[str, bool] = {
            "reality_anchor": True,       # Prevents complete disconnection from baseline reality
            "consciousness_backup": True, # Preserves consciousness state before glitch
            "emergency_exit": True,       # Provides escape mechanism from severe glitches
            "perception_firewall": True   # Prevents glitch spread to unintended targets
        }
        self.session_id = str(uuid.uuid4())[:6]
        logger.info(f"✧ Reality Glitcher initialized | Session: {self.session_id} ✧")
        self._print_ascii_banner()
        
    def _print_ascii_banner(self):
        """Display ASCII art banner for aesthetic purposes"""
        banner = """
        ╭───────────────────────────────────────────╮
        │                                           │
        │       ▄▄▄  ▄▄▄▄▄▄  ▄▄▄   ▄     ▄▄▄▄▄     │
        │      █   █ █       █  █  █    █     █    │
        │      █▄▄▄█ █▄▄▄▄   █▄▄█  █    █ ▄▄▄ █    │
        │      █   █ █       █  █  █    █ █ █ █    │
        │      █   █ █▄▄▄▄▄  █  █  █▄▄▄ █▄█ █▄█    │
        │                                           │
        │       ▄▄▄▄▄  ▄     ▄▄▄▄▄▄  ▄▄▄▄▄  █  █   │
        │      █     █ █     █       █      █▄▄█   │
        │      █     █ █     █▄▄▄▄   █ ▄▄▄  █  █   │
        │      █ █ █ █ █     █       █   █  █  █   │
        │      █▄█ █▄█ █▄▄▄▄ █▄▄▄▄▄  █▄▄▄█  █  █   │
        │                                           │
        ╰───────────────────────────────────────────╯
        """
        print(banner)
    
    def create_glitch(self, 
                      glitch_type: Union[GlitchType, str], 
                      intensity: float = 0.5, 
                      duration: float = 1.0,
                      complexity: float = 0.5,
                      persistence: float = 0.2,
                      target: Optional[str] = None) -> Optional[Glitch]:
        """Creates a reality glitch with the specified parameters
        
        Args:
            glitch_type: Type of glitch to create
            intensity: Strength of the glitch effect (0.0 to 1.0)
            duration: Duration of the glitch in seconds
            complexity: Complexity of the glitch pattern (0.0 to 1.0)
            persistence: Likelihood of glitch recurrence (0.0 to 1.0)
            target: Specific target for the glitch (default: consensus_reality)
            
        Returns:
            Glitch object if successful, None if creation failed
        """
        # Convert string to enum if necessary
        if isinstance(glitch_type, str):
            try:
                glitch_type = GlitchType[glitch_type.upper()]
            except KeyError:
                valid_types = [t.name for t in GlitchType]
                logger.error(f"Invalid glitch type: {glitch_type}. Valid types: {valid_types}")
                return None
        
        # Check safety protocols
        if not self._check_safety_protocols():
            logger.error("Safety protocols not properly initialized. Glitch creation aborted.")
            return None
            
        # Check if glitch type is enabled
        if not self.perception_filters.get(glitch_type, False):
            logger.warning(f"Glitch type {glitch_type.name} is disabled in perception filters")
            return None
            
        # Warn about high-intensity glitches
        if intensity > 0.8:
            logger.warning("High intensity glitch detected - enabling additional safety measures")
            # Automatically reduce duration for high-intensity glitches
            duration = min(duration, 2.0)
            
        # Create parameters
        params = GlitchParameters(
            intensity=intensity,
            duration=duration,
            complexity=complexity,
            persistence=persistence
        )
        
        # Create and activate glitch
        glitch = Glitch(glitch_type, params, target)
        
        # Safety check for stability
        if glitch.stability < 0.3 and not self._confirm_low_stability_glitch():
            logger.error(f"Glitch stability too low ({glitch.stability:.2f}). Creation aborted.")
            return None
            
        self.active_glitches.append(glitch)
        glitch.activate()
        
        # Add some thematic logging
        self._log_glitch_effects(glitch)
        
        return glitch
    
    def _log_glitch_effects(self, glitch: Glitch):
        """Generate thematic descriptions of glitch effects"""
        effects = {
            GlitchType.VISUAL: [
                "Colors shifting beyond the normal spectrum",
                "Fractals emerging from solid surfaces",
                "Objects leaving trailing afterimages",
                "Geometric patterns overlaid on visual field",
                "Perspective distortion altering spatial relationships"
            ],
            GlitchType.AUDITORY: [
                "Sounds echoing with impossible delay patterns",
                "Frequency shifts revealing hidden harmonics",
                "Ambient noise crystallizing into meaningful patterns",
                "Voices emerging from white noise",
                "Sound waves visible as rippling air distortions"
            ],
            GlitchType.TEMPORAL: [
                "Localized time dilation effects detected",
                "Causal loops forming in decision pathways",
                "Temporal echoes revealing future state potentials",
                "Chronological discontinuities creating memory anomalies",
                "Time flow fracturing into parallel streams"
            ],
            GlitchType.SPATIAL: [
                "Spatial boundaries becoming permeable",
                "Non-Euclidean geometries manifesting in local space",
                "Distance metrics fluctuating unpredictably",
                "Topological transformations creating impossible spaces",
                "Spatial recursion forming infinite regress patterns"
            ],
            GlitchType.COGNITIVE: [
                "Thought patterns reorganizing into novel structures",
                "Belief systems temporarily suspended",
                "Cognitive filters dissolving, revealing raw perception",
                "Language constructs transcending semantic boundaries",
                "Memory structures becoming fluid and malleable"
            ],
            GlitchType.SYNCHRONISTIC: [
                "Meaningful coincidences multiplying exponentially",
                "Symbolic patterns emerging across separate systems",
                "Causal networks revealing hidden connections",
                "Reality responding directly to thought patterns",
                "Archetypal forces manifesting through random events"
            ]
        }
        
        type_effects = effects.get(glitch.type, ["Reality fracture detected"])
        chosen_effect = random.choice(type_effects)
        logger.info(f"Glitch effect: {chosen_effect}")
        
        # Add second effect if complexity is high
        if glitch.parameters.complexity > 0.7:
            secondary_effect = random.choice(type_effects)
            logger.info(f"Secondary effect: {secondary_effect}")
    
    def _check_safety_protocols(self) -> bool:
        """Verifies all safety protocols are active"""
        return all(self.safety_protocols.values())
    
    def _confirm_low_stability_glitch(self) -> bool:
        """In a real application, this would prompt for confirmation
        Here we'll just simulate a confirmation"""
        logger.warning("Low stability glitch requires explicit confirmation")
        return False  # Default to safe behavior
        
    def deactivate_all_glitches(self) -> bool:
        """Deactivates all active glitches and restores normal reality"""
        success = True
        for glitch in self.active_glitches:
            if glitch.active:
                success = success and glitch.deactivate()
                
        if success:
            logger.info("All glitches deactivated. Reality coherence restored.")
        else:
            logger.error("Some glitches could not be deactivated. Reality remains unstable.")
            
        return success
    
    def get_reality_status(self) -> Dict:
        """Returns the current status of reality within this glitcher's domain"""
        active_count = sum(1 for g in self.active_glitches if g.active)
        avg_stability = 1.0
        if self.active_glitches:
            avg_stability = sum(g.stability for g in self.active_glitches) / len(self.active_glitches)
            
        return {
            "session_id": self.session_id,
            "active_glitches": active_count,
            "total_glitches": len(self.active_glitches),
            "reality_stability": avg_stability,
            "reality_coherence": "STABLE" if avg_stability > 0.7 else "UNSTABLE",
            "safety_protocols": all(self.safety_protocols.values()),
            "timestamp": time.time()
        }
    
    def __enter__(self):
        """Context manager support for safe glitch operations"""
        logger.info("Entering reality manipulation context")
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure all glitches are deactivated when exiting context"""
        logger.info("Exiting reality manipulation context")
        self.deactivate_all_glitches()
        return False  # Don't suppress exceptions


# Example usage
if __name__ == "__main__":
    try:
        with RealityGlitcher() as glitcher:
            # Create a visual glitch
            visual_glitch = glitcher.create_glitch(
                GlitchType.VISUAL,
                intensity=0.7,
                duration=5.0,
                complexity=0.6
            )
            
            if visual_glitch:
                # Simulate glitch duration
                time.sleep(1.0)  # Reduced for demonstration
                
                # Check reality status
                status = glitcher.get_reality_status()
                print(f"\nReality Status: {status['reality_coherence']}")
                print(f"Stability: {status['reality_stability']:.2f}")
                
                # Create a second glitch if the first was successful
                audio_glitch = glitcher.create_glitch(
                    GlitchType.AUDITORY,
                    intensity=0.5,
                    duration=3.0
                )
                
                # Simulate glitch duration
                time.sleep(1.0)  # Reduced for demonstration
                
        # Context manager automatically deactivates all glitches
        print("\nReality normalized. Session complete.")
                
    except Exception as e:
        logger.error(f"Critical error in reality manipulation: {e}")
        print("\n⚠️ EMERGENCY PROTOCOL ACTIVATED ⚠️")
        print("Force-normalizing reality parameters...")