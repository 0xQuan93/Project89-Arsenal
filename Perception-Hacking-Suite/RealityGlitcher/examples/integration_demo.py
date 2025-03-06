#!/usr/bin/env python3
"""
Mind Mirror Integration Demo

This script demonstrates the integration between Mind Mirror and 
Reality Glitcher, showing how consciousness data from Mind Mirror
can be used to create reality glitches.
"""

import os
import sys
import time
import random
import logging

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import RealityGlitcher
from main import RealityGlitcher, GlitchType

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def display_banner():
    """Display a banner for the integration demo"""
    banner = """
    ╭────────────────────────────────────────────────────────╮
    │                                                        │
    │   🧠 Mind Mirror ⟷ Reality Glitcher Integration Demo   │
    │                                                        │
    │   Merging consciousness data with reality distortion   │
    │                                                        │
    ╰────────────────────────────────────────────────────────╯
    """
    print(banner)

def check_mind_mirror_data():
    """Check if Mind Mirror export data is available"""
    # Get the path to the RealityGlitcher root directory
    reality_glitcher_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    import_path = os.path.join(reality_glitcher_dir, "imports", "mind_mirror_data.json")
    
    if os.path.exists(import_path):
        logger.info(f"Mind Mirror data found at {import_path}")
        return True
    else:
        logger.warning(f"No Mind Mirror data found at {import_path}. Please run Mind Mirror and export data first.")
        return False

def demonstrate_direct_glitches(glitcher):
    """Create some direct glitches for comparison"""
    logger.info("Creating direct glitches for comparison...")
    
    # Create a visual glitch
    visual_glitch = glitcher.create_glitch(
        GlitchType.VISUAL,
        intensity=0.6,
        duration=10.0,
        complexity=0.5,
        persistence=0.3,
        target="local_perception"
    )
    
    # Create a cognitive glitch
    cognitive_glitch = glitcher.create_glitch(
        GlitchType.COGNITIVE,
        intensity=0.4,
        duration=15.0,
        complexity=0.7,
        persistence=0.2,
        target="consensus_reality"
    )
    
    logger.info(f"Created {len(glitcher.active_glitches)} direct glitches")
    return glitcher.active_glitches

def demonstrate_mind_mirror_integration(glitcher):
    """Demonstrate integration with Mind Mirror"""
    logger.info("Beginning Mind Mirror integration demonstration...")
    
    # Store the count of glitches before integration
    glitches_before = len(glitcher.active_glitches)
    
    # Integrate with Mind Mirror
    success = glitcher.integrate_with_mind_mirror()
    
    if success:
        logger.info("Mind Mirror integration successful!")
        
        # Get Mind Mirror-based glitches (all new glitches after integration)
        mind_mirror_glitches = glitcher.active_glitches[glitches_before:]
        logger.info(f"Created {len(mind_mirror_glitches)} glitches from Mind Mirror data")
        
        # Print details of each Mind Mirror glitch
        for i, glitch in enumerate(mind_mirror_glitches, 1):
            print(f"\nMind Mirror Glitch #{i}:")
            print(f"  Type: {glitch.type.name}")
            print(f"  Target: {glitch.target}")
            print(f"  Intensity: {glitch.parameters.intensity:.2f}")
            print(f"  Stability: {glitch.stability:.2f}")
            
        return mind_mirror_glitches
    else:
        logger.error("Mind Mirror integration failed!")
        return []

def compare_glitches(direct_glitches, mind_mirror_glitches):
    """Compare direct glitches with those from Mind Mirror"""
    if not mind_mirror_glitches:
        logger.warning("No Mind Mirror glitches available for comparison")
        return
        
    print("\n" + "="*50)
    print("Comparing Direct Glitches vs Mind Mirror Glitches")
    print("="*50)
    
    # Calculate average properties
    direct_intensity = sum(g.parameters.intensity for g in direct_glitches) / len(direct_glitches) if direct_glitches else 0
    mm_intensity = sum(g.parameters.intensity for g in mind_mirror_glitches) / len(mind_mirror_glitches)
    
    direct_stability = sum(g.stability for g in direct_glitches) / len(direct_glitches) if direct_glitches else 0
    mm_stability = sum(g.stability for g in mind_mirror_glitches) / len(mind_mirror_glitches)
    
    # Print comparison table
    print(f"{'Property':<20} | {'Direct Glitches':<20} | {'Mind Mirror Glitches':<20}")
    print("-" * 65)
    print(f"{'Count':<20} | {len(direct_glitches):<20} | {len(mind_mirror_glitches):<20}")
    print(f"{'Avg. Intensity':<20} | {direct_intensity:.2f}{'':<15} | {mm_intensity:.2f}{'':<15}")
    print(f"{'Avg. Stability':<20} | {direct_stability:.2f}{'':<15} | {mm_stability:.2f}{'':<15}")
    print(f"{'Consciousness Data':<20} | {'No':<20} | {'Yes':<20}")
    print(f"{'Neural Pattern Link':<20} | {'No':<20} | {'Yes':<20}")

def simulate_reality_shifts():
    """Simulate the effects of reality glitches"""
    print("\nSimulating reality shifts...")
    effects = [
        "Visual perception beginning to distort...",
        "Cognitive frameworks reorganizing...",
        "Temporal sequencing becoming flexible...",
        "Spatial boundaries dissolving...",
        "Causal relationships inverting...",
        "Synchronistic events multiplying..."
    ]
    
    for i in range(5):
        effect = random.choice(effects)
        print(f"[{i+1}] {effect}")
        time.sleep(1.5)

def main():
    """Main demonstration function"""
    display_banner()
    
    # Check for Mind Mirror data
    if not check_mind_mirror_data():
        print("\nPlease follow these steps to generate Mind Mirror data:")
        print("1. Run Mind Mirror application")
        print("2. Use the Integration menu to export data to Reality Glitcher")
        print("3. Run this demo again")
        return
    
    # Create RealityGlitcher instance
    glitcher = RealityGlitcher()
    
    # Demonstrate direct glitches
    direct_glitches = demonstrate_direct_glitches(glitcher)
    
    # Small delay for readability
    time.sleep(1)
    
    # Demonstrate Mind Mirror integration
    mind_mirror_glitches = demonstrate_mind_mirror_integration(glitcher)
    
    # Small delay for readability
    time.sleep(1)
    
    # Compare the glitches
    compare_glitches(direct_glitches, mind_mirror_glitches)
    
    # Simulate reality shifts
    simulate_reality_shifts()
    
    # Get final reality status
    status = glitcher.get_reality_status()
    print("\nFinal Reality Status:")
    print(f"- Active Glitches: {status['active_glitches']}")
    print(f"- Reality Stability: {status['stability']:.2f}")
    print(f"- Safety Protocols: {'Active' if status['safetyProtocols'] else 'Inactive'}")
    
    print("\nDemo complete! Mind Mirror and Reality Glitcher have been integrated.")
    print("Your consciousness patterns are now affecting reality distortion.")

if __name__ == "__main__":
    main() 