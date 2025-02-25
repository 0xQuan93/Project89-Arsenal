from typing import Dict, List
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RealityGlitcher:
    def __init__(self):
        self.active_glitches: List[Dict] = []
        self.perception_filters = {
            "visual": True,
            "auditory": True,
            "temporal": False  # Temporal glitches are dangerous, disabled by default
        }
        self.safety_protocols = {
            "reality_anchor": True,
            "consciousness_backup": True,
            "emergency_exit": True
        }
    
    def create_glitch(self, glitch_type: str, intensity: float) -> Dict:
        """Creates a reality glitch of specified type and intensity"""
        if not self._check_safety_protocols():
            raise RuntimeError("Safety protocols not properly initialized")
            
        if not self.perception_filters.get(glitch_type, False):
            raise ValueError(f"Glitch type {glitch_type} is not enabled")
            
        if intensity > 0.8:
            logger.warning("High intensity glitch detected - enabling additional safety measures")
            
        glitch = {
            "type": glitch_type,
            "intensity": min(1.0, max(0.0, intensity)),
            "duration": random.uniform(0.1, 1.0),
            "safety_anchor": self._generate_safety_anchor()
        }
        self.active_glitches.append(glitch)
        return glitch
    
    def _check_safety_protocols(self) -> bool:
        """Verifies all safety protocols are active"""
        return all(self.safety_protocols.values())
    
    def _generate_safety_anchor(self) -> str:
        """Generates a unique safety anchor for reality restoration"""
        return f"anchor_{random.getrandbits(32):08x}"

def main():
    glitcher = RealityGlitcher()
    try:
        glitch = glitcher.create_glitch("visual", 0.5)
        logger.info(f"Created glitch: {glitch}")
    except (ValueError, RuntimeError) as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()