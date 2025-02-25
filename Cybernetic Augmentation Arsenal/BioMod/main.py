from typing import Dict, Tuple
from .modules.biohacking import BioHacker
from .modules.cybernetic_implants import ImplantManager
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_systems() -> Tuple[ImplantManager, BioHacker]:
    """Initialize all BioMod systems with safety protocols"""
    logger.info("Initializing BioMod systems...")
    
    implant_manager = ImplantManager()
    biohacker = BioHacker()
    
    # Register core safety implants
    safety_implants = [
        {
            "id": "safety_core_v1",
            "type": "safety",
            "compatibility_version": "1.0",
            "safety_rating": "A+"
        },
        {
            "id": "neural_firewall_v2",
            "type": "protection",
            "compatibility_version": "2.0",
            "safety_rating": "A"
        }
    ]
    
    for implant in safety_implants:
        if not implant_manager.register_implant(implant):
            raise RuntimeError(f"Failed to register critical safety implant: {implant['id']}")
        logger.info(f"Registered safety implant: {implant['id']}")
    
    return implant_manager, biohacker

def main():
    try:
        implant_manager, biohacker = initialize_systems()
        logger.info("BioMod systems initialized successfully")
    except Exception as e:
        logger.error(f"Critical error during initialization: {e}")
        raise
    
if __name__ == "__main__":
    main()