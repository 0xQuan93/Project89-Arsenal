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
import json
import os

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
    """Represents a single reality glitch that can be applied to perception"""
    
    def __init__(self, 
                 glitch_type: GlitchType, 
                 parameters: GlitchParameters,
                 target: str = "consensus_reality"):
        """Initialize a new reality glitch
        
        Args:
            glitch_type: The type of glitch
            parameters: Parameters controlling the glitch's behavior
            target: What the glitch targets ("local_perception" or "consensus_reality")
        """
        self.id = str(uuid.uuid4())[:8]
        self.type = glitch_type
        self.parameters = parameters
        self.target = target
        self.active = False
        self.created_at = time.time()
        self.source = "direct_creation"  # Default source
        
        # Calculate stability based on parameters
        self.stability = self._calculate_stability()
        
        logger.debug(f"Created {glitch_type.name} glitch (ID: {self.id}) with " 
                    f"stability {self.stability:.2f}")
        
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
        logger.info(f"Stability rating: {self.stability:.2f}")
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
        """Display the ASCII art banner for Reality Glitcher"""
        banner = r"""
        ______          _ _ _         _____ _ _ _      _               
        | ___ \        | (_) |       |  __ \ (_) |    | |              
        | |_/ /___  ___| |_| |_ _   _| |  \/ |_| |_ __| |__   ___ _ __ 
        |    // _ \/ _ \ | | __| | | | | __| | | __/ _` '_ \ / _ \ '__|
        | |\ \  __/  __/ | | |_| |_| | |_\ \ | | || (_| | | |  __/ |   
        \_| \_\___|\___|_|_|\__|\__, |\____/_|_|\__\__,_| |_|\___|_|   
                                 __/ |                                  
                                |___/                                   
        """
        logger.info(f"\n{banner}")
        
    def load_mind_mirror_data(self) -> Optional[Dict]:
        """
        Load neural pattern data exported from Mind Mirror
        This allows RealityGlitcher to synchronize with the user's neural patterns
        
        Returns:
            Dictionary containing Mind Mirror data or None if file not found or invalid
        """
        # Construct the path to the Mind Mirror data file
        import_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imports", "mind_mirror_data.json")
        logger.info(f"Attempting to load Mind Mirror data from {import_path}")
        
        try:
            with open(import_path, "r") as f:
                data = json.load(f)
                
            # Validate the data structure
            if not all(key in data for key in ["source", "neural_patterns", "metadata"]):
                logger.error("Invalid Mind Mirror data format")
                return None
                
            logger.info(f"Successfully loaded Mind Mirror data from user: {data.get('user', 'Unknown')}")
            logger.info(f"Pattern type: {data.get('metadata', {}).get('pattern_type', 'unknown')}")
            logger.info(f"Nodes: {len(data.get('neural_patterns', {}).get('nodes', []))}")
            logger.info(f"Connections: {len(data.get('neural_patterns', {}).get('connections', []))}")
            
            return data
        except FileNotFoundError:
            logger.warning(f"No Mind Mirror data found at {import_path}. Integration inactive.")
            return None
        except json.JSONDecodeError:
            logger.error("Mind Mirror data file is corrupted or invalid JSON")
            return None
        except Exception as e:
            logger.error(f"Error loading Mind Mirror data: {str(e)}")
            return None
            
    def generate_glitches_from_mind_mirror(self) -> List[Glitch]:
        """
        Generate glitches based on neural patterns from Mind Mirror
        
        Returns:
            List of generated glitches
        """
        mind_data = self.load_mind_mirror_data()
        if not mind_data:
            return []
            
        generated_glitches = []
        
        try:
            # Extract neural patterns
            nodes = mind_data.get("neural_patterns", {}).get("nodes", [])
            connections = mind_data.get("neural_patterns", {}).get("connections", [])
            
            # Generate glitches based on strongest nodes
            strong_nodes = sorted(nodes, key=lambda x: x.get("strength", 0), reverse=True)[:3]
            
            for node in strong_nodes:
                # Map node concepts to glitch types
                concept_map = {
                    "Perception": GlitchType.VISUAL,
                    "Consciousness": GlitchType.COGNITIVE,
                    "Reality": GlitchType.SYNCHRONISTIC, 
                    "Mind": GlitchType.COGNITIVE,
                    "Time": GlitchType.TEMPORAL,
                    "Space": GlitchType.SPATIAL,
                    "Self": GlitchType.COGNITIVE,
                    "Awareness": GlitchType.VISUAL,
                    "Memory": GlitchType.TEMPORAL,
                    "Identity": GlitchType.COGNITIVE,
                    "Dream": GlitchType.VISUAL
                }
                
                node_label = node.get("label", "")
                glitch_type = concept_map.get(node_label, random.choice(list(GlitchType)))
                
                # Create parameters based on the node strength
                params = GlitchParameters(
                    intensity=node.get("strength", 0.5),
                    duration=random.uniform(5.0, 15.0),
                    complexity=mind_data.get("metadata", {}).get("consciousness_level", 0.5),
                    persistence=0.7
                )
                
                # Create and add the glitch
                glitch = Glitch(
                    glitch_type=glitch_type,
                    parameters=params,
                    target=f"neural_pattern_{node_label.lower()}"
                )
                
                generated_glitches.append(glitch)
                logger.info(f"Generated {glitch_type.name} glitch from neural pattern '{node_label}'")
            
            # Generate one glitch from the strongest connection if available
            if connections:
                strongest_connection = max(connections, key=lambda x: x.get("strength", 0))
                source_id = strongest_connection.get("source", 0)
                target_id = strongest_connection.get("target", 0)
                
                # Find the connected nodes
                source_node = next((n for n in nodes if n.get("id") == source_id), {})
                target_node = next((n for n in nodes if n.get("id") == target_id), {})
                
                connection_type = strongest_connection.get("type", "association")
                
                # Map connection types to glitch types
                connection_map = {
                    "association": GlitchType.COGNITIVE,
                    "causation": GlitchType.TEMPORAL,
                    "similarity": GlitchType.VISUAL
                }
                
                glitch_type = connection_map.get(connection_type, GlitchType.SYNCHRONISTIC)
                
                # Create parameters based on the connection strength
                params = GlitchParameters(
                    intensity=strongest_connection.get("strength", 0.5),
                    duration=random.uniform(10.0, 30.0),
                    complexity=0.8,
                    persistence=0.5
                )
                
                # Create and add the glitch
                connection_label = f"{source_node.get('label', 'Node')}_{target_node.get('label', 'Node')}"
                glitch = Glitch(
                    glitch_type=glitch_type,
                    parameters=params,
                    target=f"connection_{connection_label.lower()}"
                )
                
                generated_glitches.append(glitch)
                logger.info(f"Generated {glitch_type.name} glitch from connection between '{source_node.get('label', 'Node')}' and '{target_node.get('label', 'Node')}'")
        
        except Exception as e:
            logger.error(f"Error generating glitches from Mind Mirror data: {str(e)}")
        
        return generated_glitches
    
    def create_glitch(self, 
                     glitch_type: GlitchType, 
                     intensity: float, 
                     duration: float, 
                     target: str = "local_perception",
                     complexity: float = 0.5,
                     persistence: float = 0.3,
                     from_mind_mirror: bool = False) -> Optional[Glitch]:
        """Creates a new reality glitch with the specified parameters
        
        Args:
            glitch_type: The type of glitch to create
            intensity: How strong the glitch is (0.0-1.0)
            duration: How long the glitch lasts in seconds
            target: What the glitch affects ("local_perception" or "consensus_reality")
            complexity: How complex the glitch's effects are (0.0-1.0)
            persistence: How long the glitch's effects linger (0.0-1.0)
            from_mind_mirror: Whether this glitch is derived from Mind Mirror data
            
        Returns:
            The created Glitch or None if creation failed
        """
        # Check if reality can handle another glitch
        active_count = len([g for g in self.active_glitches if g.active])
        if active_count >= 5 and not self._check_safety_protocols():
            logger.warning("Too many active glitches. Reality becoming unstable.")
            return None
            
        # Create glitch parameters
        params = GlitchParameters(
            intensity=intensity,
            duration=duration,
            complexity=complexity,
            persistence=persistence
        )
        
        # Create and activate glitch
        glitch = Glitch(glitch_type, params, target)
        
        # Add source information if from Mind Mirror
        if from_mind_mirror:
            glitch.source = "Mind Mirror"
            logger.info(f"Creating {glitch_type.name} glitch with neural pattern influence")
        
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
        return {
            "active_glitches": len(self.active_glitches),
            "stability": self._calculate_current_stability(),
            "safetyProtocols": self.safety_protocols,
            "perceptionFilters": self.perception_filters,
            "timestamp": time.time()
        }
    
    def integrate_with_mind_mirror(self) -> bool:
        """
        Integrates with Mind Mirror by loading exported neural pattern data
        and generating corresponding glitches.
        
        Returns:
            True if integration was successful, False otherwise
        """
        logger.info("Beginning integration with Mind Mirror...")
        
        # Get generated glitches from Mind Mirror data
        generated_glitches = self.generate_glitches_from_mind_mirror()
        
        if not generated_glitches:
            logger.warning("No glitches could be generated from Mind Mirror data")
            return False
            
        # Add the glitches to active glitches
        for glitch in generated_glitches:
            self.active_glitches.append(glitch)
            glitch.activate()
            logger.info(f"Activated Mind Mirror glitch: {glitch.type.name}")
            
        logger.info(f"Mind Mirror integration complete. {len(generated_glitches)} glitches created.")
        return True
        
    def _calculate_current_stability(self) -> float:
        """Calculates the current stability of reality based on active glitches"""
        if not self.active_glitches:
            return 1.0
        return sum(g.stability for g in self.active_glitches) / len(self.active_glitches)
    
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
                print(f"Stability: {status['stability']:.2f}")
                
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