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
        self.config = {
            "glitch_intensity": 0.7,      # Default intensity for glitches
            "max_active_glitches": 5,     # Maximum number of active glitches allowed
            "auto_stabilize": True,       # Automatically stabilize reality if too unstable
            "mind_mirror_integration": True  # Enable Mind Mirror integration
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
        # Get the imports directory
        imports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imports")
        logger.info(f"Searching for Mind Mirror data in {imports_dir}")
        
        # Ensure imports directory exists
        os.makedirs(imports_dir, exist_ok=True)
        
        # Check for notification file first
        notification_path = os.path.join(imports_dir, ".new_import")
        latest_data_file = None
        
        if os.path.exists(notification_path):
            try:
                # Read the timestamp from notification file
                with open(notification_path, "r") as f:
                    timestamp = f.read().strip()
                    
                # Look for the corresponding data file
                data_file = f"mind_mirror_data_{timestamp}.json"
                data_path = os.path.join(imports_dir, data_file)
                
                if os.path.exists(data_path):
                    latest_data_file = data_path
                    logger.info(f"Found new import notification for {data_file}")
                    
                    # Remove the notification file after processing
                    os.remove(notification_path)
            except Exception as e:
                logger.error(f"Error processing notification file: {str(e)}")
        
        # If no notification file or it didn't point to valid data,
        # search for the most recent data file
        if not latest_data_file:
            try:
                # Find all mind mirror data files
                data_files = [f for f in os.listdir(imports_dir) 
                             if f.startswith("mind_mirror_data_") and f.endswith(".json")]
                
                if data_files:
                    # Sort by modification time, newest first
                    data_files.sort(key=lambda x: os.path.getmtime(os.path.join(imports_dir, x)), reverse=True)
                    latest_data_file = os.path.join(imports_dir, data_files[0])
                    logger.info(f"Using most recent Mind Mirror data file: {data_files[0]}")
                else:
                    # Fall back to the generic filename
                    fallback_path = os.path.join(imports_dir, "mind_mirror_data.json")
                    if os.path.exists(fallback_path):
                        latest_data_file = fallback_path
                        logger.info("Using generic Mind Mirror data file")
            except Exception as e:
                logger.error(f"Error finding Mind Mirror data files: {str(e)}")
        
        # No data file found
        if not latest_data_file:
            logger.warning(f"No Mind Mirror data found in {imports_dir}. Integration inactive.")
            return None
        
        # Load and validate the data file
        try:
            with open(latest_data_file, "r") as f:
                data = json.load(f)
                
            # Check for metadata file
            meta_file = os.path.basename(latest_data_file).replace("mind_mirror_data_", "meta_")
            meta_path = os.path.join(imports_dir, meta_file)
            metadata = {}
            
            if os.path.exists(meta_path):
                try:
                    with open(meta_path, "r") as f:
                        metadata = json.load(f)
                    logger.info(f"Loaded metadata: export from {metadata.get('source', 'unknown')}, user: {metadata.get('user', 'unknown')}")
                except:
                    logger.warning(f"Could not load metadata file {meta_file}")
            
            # Validate the data structure
            if not all(key in data for key in ["source", "neural_patterns", "metadata"]):
                logger.error("Invalid Mind Mirror data format")
                return None
        
            # Log information about the loaded data
            logger.info(f"Successfully loaded Mind Mirror data from user: {data.get('user', 'Unknown')}")
            logger.info(f"Version: {data.get('version', 'unknown')} {data.get('version_name', '')}")
            logger.info(f"Pattern type: {data.get('metadata', {}).get('pattern_type', 'unknown')}")
            logger.info(f"Nodes: {len(data.get('neural_patterns', {}).get('nodes', []))}")
            logger.info(f"Connections: {len(data.get('neural_patterns', {}).get('connections', []))}")
            
            # If metrics are included, log them
            metrics = data.get('neural_patterns', {}).get('metrics', {})
            if metrics:
                logger.info(f"Neural metrics: coherence={metrics.get('coherence', 0):.2f}, complexity={metrics.get('complexity', 0):.2f}")
            
            return data
        except FileNotFoundError:
            logger.warning(f"Mind Mirror data file not found at {latest_data_file}. Integration inactive.")
            return None
        except json.JSONDecodeError:
            logger.error(f"Mind Mirror data file {latest_data_file} is corrupted or invalid JSON")
            return None
        except Exception as e:
            logger.error(f"Error loading Mind Mirror data: {str(e)}")
            return None
            
    def generate_glitches_from_mind_mirror(self, mind_mirror_data: Dict) -> List[Dict]:
        """
        Generate glitches based on neural patterns imported from Mind Mirror
        
        Args:
            mind_mirror_data: Dictionary containing neural pattern data from Mind Mirror
            
        Returns:
            List of generated glitch configurations
        """
        if not mind_mirror_data:
            logger.warning("Cannot generate glitches: No Mind Mirror data provided")
            return []
        
        neural_patterns = mind_mirror_data.get("neural_patterns", {})
        nodes = neural_patterns.get("nodes", [])
        connections = neural_patterns.get("connections", [])
        metrics = neural_patterns.get("metrics", {})
        
        if not nodes or not connections:
            logger.warning("Cannot generate glitches: Mind Mirror data missing nodes or connections")
            return []
        
        logger.info(f"Generating glitches from {len(nodes)} nodes and {len(connections)} connections")
        
        # Get metadata for contextualization
        metadata = mind_mirror_data.get("metadata", {})
        pattern_type = metadata.get("pattern_type", "unknown")
        source_activity = metadata.get("source_activity", "reflection")
        intensity = metadata.get("intensity", 0.5)
        
        # Get neural metrics if available, or calculate basic versions
        coherence = metrics.get("coherence", 0.5)
        complexity = metrics.get("complexity", 0.5)
        stability = metrics.get("stability", 0.5)
        
        # Generate base glitches
        glitches = []
        
        # Group nodes by type for pattern analysis
        node_types = {}
        for node in nodes:
            node_type = node.get("type", "unknown")
            if node_type not in node_types:
                node_types[node_type] = []
            node_types[node_type].append(node)
        
        # Use dominant node types to influence glitch characteristics
        dominant_types = sorted(node_types.keys(), key=lambda k: len(node_types[k]), reverse=True)
        
        # Create pattern-based glitches
        if pattern_type == "meditation":
            # Meditation patterns create subtle, harmonious glitches
            glitches.append({
                "type": "visual_echo",
                "intensity": 0.3 + (coherence * 0.4),
                "persistence": 0.2 + (stability * 0.6),
                "source": "mind_mirror_meditation",
                "color_shift": {"h": 240, "s": 0.2, "v": 0.9}  # Blue/purple hues
            })
            
            glitches.append({
                "type": "field_distortion",
                "intensity": 0.2 + (coherence * 0.3),
                "wave_pattern": "sine",
                "frequency": 0.05 + (1 - complexity) * 0.15,  # Lower complexity = smoother waves
                "source": "mind_mirror_meditation",
            })
            
        elif pattern_type == "creative":
            # Creative patterns create colorful, dynamic glitches
            glitches.append({
                "type": "reality_fragment",
                "intensity": 0.4 + (complexity * 0.5),
                "fragmentation": 0.3 + (complexity * 0.6),
                "rotation": 0.2 + (stability * 0.3),
                "source": "mind_mirror_creative",
                "color_shift": {"h": 120, "s": 0.7, "v": 0.9}  # Green/yellow hues
            })
            
            glitches.append({
                "type": "time_slip",
                "intensity": 0.3 + (complexity * 0.6),
                "duration": 0.4 + (stability * 0.4),
                "echo_count": int(2 + complexity * 5),
                "source": "mind_mirror_creative",
            })
            
        elif pattern_type == "analytical":
            # Analytical patterns create structured, geometric glitches
            glitches.append({
                "type": "digital_corruption",
                "intensity": 0.5 + (complexity * 0.4),
                "pattern": "grid",
                "density": 0.3 + (coherence * 0.6),
                "source": "mind_mirror_analytical",
                "color_shift": {"h": 200, "s": 0.5, "v": 0.8}  # Blue/cyan hues
            })
            
            glitches.append({
                "type": "perspective_warp",
                "intensity": 0.4 + (coherence * 0.4),
                "warp_type": "fractal",
                "iterations": int(3 + complexity * 4),
                "source": "mind_mirror_analytical",
            })
            
        elif pattern_type == "emotional":
            # Emotional patterns create fluid, intense glitches
            color_hue = 0  # Red for intense emotions
            if "calm" in dominant_types or "peace" in dominant_types:
                color_hue = 240  # Blue for calm emotions
            elif "joy" in dominant_types or "happiness" in dominant_types:
                color_hue = 60  # Yellow for happy emotions
            
            glitches.append({
                "type": "reality_wave",
                "intensity": 0.5 + (intensity * 0.5),
                "wave_height": 0.3 + (coherence * 0.6),
                "turbulence": 0.4 + (complexity * 0.5),
                "source": "mind_mirror_emotional",
                "color_shift": {"h": color_hue, "s": 0.8, "v": 0.9}
            })
            
            glitches.append({
                "type": "dissolve_effect",
                "intensity": 0.4 + (intensity * 0.5),
                "persistence": 0.3 + (stability * 0.6),
                "particle_size": 0.1 + (complexity * 0.3),
                "source": "mind_mirror_emotional",
            })
        
        # Default case - generate generic glitches
        else:
            # Extract node strengths to influence glitch intensity
            node_strengths = [node.get("strength", 0.5) for node in nodes]
            avg_strength = sum(node_strengths) / len(node_strengths) if node_strengths else 0.5
            
            # Extract connection weights to influence glitch complexity
            connection_weights = [conn.get("weight", 0.5) for conn in connections]
            avg_weight = sum(connection_weights) / len(connection_weights) if connection_weights else 0.5
            
            # Generate generic glitches
            glitches.append({
                "type": "visual_static",
                "intensity": 0.3 + (avg_strength * 0.6),
                "grain_size": 0.1 + (complexity * 0.2),
                "persistence": 0.3 + (stability * 0.6),
                "source": "mind_mirror_generic",
            })
            
            glitches.append({
                "type": "reality_bend",
                "intensity": 0.2 + (avg_weight * 0.7),
                "bend_amount": 0.2 + (coherence * 0.5),
                "elasticity": 0.3 + (complexity * 0.5),
                "source": "mind_mirror_generic",
            })
        
        # Add universal entanglement effect based on overall neural pattern
        entanglement_effect = {
            "type": "quantum_entanglement",
            "intensity": 0.3 + (coherence * 0.6),
            "connection_strength": 0.4 + (stability * 0.5),
            "connection_count": int(3 + complexity * 10),
            "source": "mind_mirror_integration",
        }
        glitches.append(entanglement_effect)
        
        # Normalize intensities to user preference if available
        global_intensity = self.config.get("glitch_intensity", 0.7)
        for glitch in glitches:
            glitch["intensity"] *= global_intensity
        
        # Log the generated glitches
        logger.info(f"Generated {len(glitches)} glitches from Mind Mirror data")
        for i, glitch in enumerate(glitches):
            logger.debug(f"Glitch {i+1}: {glitch['type']} (intensity: {glitch['intensity']:.2f})")
        
        return glitches
    
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
    
    def integrate_with_mind_mirror(self):
        """
        Integrate with Mind Mirror by loading neural pattern data and creating glitches
        """
        logger.info("Beginning Mind Mirror integration...")
        
        # Load Mind Mirror data
        mind_mirror_data = self.load_mind_mirror_data()
        
        # Get generated glitches from Mind Mirror data
        if mind_mirror_data:
            generated_glitches = self.generate_glitches_from_mind_mirror(mind_mirror_data)
            
            if not generated_glitches:
                logger.warning("No glitches generated from Mind Mirror data")
                return
            
            logger.info(f"Successfully generated {len(generated_glitches)} glitches from Mind Mirror neural patterns")
            
            # Clear any previous Mind Mirror glitches
            self.active_glitches = [g for g in self.active_glitches if not g.target.startswith("neural_pattern_")]
            
            # Add the glitches to active glitches
            for glitch_config in generated_glitches:
                # Map the glitch type string to enum
                glitch_type_map = {
                    "visual_echo": GlitchType.VISUAL,
                    "field_distortion": GlitchType.SPATIAL,
                    "reality_fragment": GlitchType.VISUAL,
                    "time_slip": GlitchType.TEMPORAL,
                    "digital_corruption": GlitchType.COGNITIVE,
                    "perspective_warp": GlitchType.SPATIAL,
                    "reality_wave": GlitchType.SYNCHRONISTIC,
                    "dissolve_effect": GlitchType.VISUAL,
                    "visual_static": GlitchType.VISUAL,
                    "reality_bend": GlitchType.SPATIAL,
                    "quantum_entanglement": GlitchType.SYNCHRONISTIC
                }
                
                glitch_type = glitch_type_map.get(
                    glitch_config["type"], 
                    random.choice(list(GlitchType))
                )
                
                # Create parameters from the glitch config
                params = GlitchParameters(
                    intensity=glitch_config.get("intensity", 0.5),
                    duration=glitch_config.get("duration", random.uniform(10.0, 30.0)),
                    complexity=glitch_config.get("complexity", 0.6),
                    persistence=glitch_config.get("persistence", 0.5)
                )
                
                # Create the glitch object
                glitch = Glitch(
                    glitch_type=glitch_type,
                    parameters=params,
                    target=f"neural_pattern_{glitch_config['type']}"
                )
                
                self.active_glitches.append(glitch)
                glitch.activate()
                logger.info(f"Activated Mind Mirror glitch: {glitch_config['type']}")
            
            logger.info(f"Mind Mirror integration complete. {len(generated_glitches)} glitches created.")
        else:
            logger.warning("Mind Mirror integration failed. No data available.")
        
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