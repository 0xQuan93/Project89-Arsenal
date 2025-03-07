#!/usr/bin/env python3
"""
Integration Demo for Mind Mirror and Reality Glitcher

This script demonstrates how data exported from Mind Mirror can be imported into
Reality Glitcher to create personalized glitch effects based on neural patterns.
"""

import os
import sys
import json
import time
import random
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("IntegrationDemo")

# Add parent directory to path so we can import the Reality Glitcher
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Try to import Reality Glitcher
try:
    from main import RealityGlitcher
    logger.info("Successfully imported Reality Glitcher")
except ImportError as e:
    logger.error(f"Failed to import Reality Glitcher: {e}")
    sys.exit(1)

def check_for_mind_mirror_data() -> bool:
    """
    Check if Mind Mirror data is available in the imports directory.
    
    Returns:
        True if data is available, False otherwise
    """
    imports_dir = os.path.join(parent_dir, "imports")
    
    # Ensure imports directory exists
    os.makedirs(imports_dir, exist_ok=True)
    
    # Check for notification file first
    notification_path = os.path.join(imports_dir, ".new_import")
    if os.path.exists(notification_path):
        logger.info("Found new import notification file")
        return True
    
    # Check for any Mind Mirror data files
    data_files = [f for f in os.listdir(imports_dir) 
                 if (f.startswith("mind_mirror_data_") or f == "mind_mirror_data.json") 
                 and f.endswith(".json")]
    
    if data_files:
        logger.info(f"Found {len(data_files)} Mind Mirror data files")
        return True
    
    return False

def create_sample_mind_mirror_data() -> bool:
    """
    Create a sample Mind Mirror data file for testing the integration.
    This is only used if no real Mind Mirror data is available.
    
    Returns:
        True if successful, False otherwise
    """
    imports_dir = os.path.join(parent_dir, "imports")
    os.makedirs(imports_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    data_path = os.path.join(imports_dir, f"mind_mirror_data_{timestamp}.json")
    meta_path = os.path.join(imports_dir, f"meta_{timestamp}.json")
    notification_path = os.path.join(imports_dir, ".new_import")
    
    try:
        # Generate sample neural patterns
        nodes = []
        connections = []
        
        # Create sample nodes
        node_types = ["perception", "awareness", "concept", "memory", "emotion"]
        node_labels = ["Reality", "Perception", "Consciousness", "Time", "Space", 
                      "Self", "Mind", "Awareness", "Memory", "Identity"]
                      
        for i in range(10):
            nodes.append({
                "id": i,
                "label": random.choice(node_labels),
                "type": random.choice(node_types),
                "strength": random.uniform(0.3, 0.9),
                "position": {
                    "x": random.uniform(-1.0, 1.0),
                    "y": random.uniform(-1.0, 1.0),
                    "z": random.uniform(-1.0, 1.0)
                }
            })
        
        # Create sample connections
        connection_types = ["association", "causation", "similarity"]
        for i in range(15):
            source = random.randint(0, 9)
            target = random.randint(0, 9)
            if source != target:
                connections.append({
                    "source": source,
                    "target": target,
                    "type": random.choice(connection_types),
                    "weight": random.uniform(0.2, 0.8)
                })
        
        # Calculate sample metrics
        metrics = {
            "coherence": random.uniform(0.3, 0.8),
            "complexity": random.uniform(0.4, 0.9),
            "stability": random.uniform(0.2, 0.7)
        }
        
        # Create the data structure
        mind_mirror_data = {
            "source": "Mind Mirror",
            "user": "Demo User",
            "version": "1.0.0",
            "version_name": "Enchanted Mirror",
            "timestamp": datetime.now().isoformat(),
            "neural_patterns": {
                "nodes": nodes,
                "connections": connections,
                "metrics": metrics
            },
            "metadata": {
                "pattern_type": random.choice(["meditation", "creative", "analytical", "emotional"]),
                "source_activity": "demo integration",
                "intensity": random.uniform(0.4, 0.8),
                "consciousness_level": random.uniform(0.3, 0.9)
            }
        }
        
        # Create metadata file
        metadata = {
            "source": "Mind Mirror Demo",
            "user": "Demo User",
            "export_time": datetime.now().isoformat(),
            "pattern_description": "Sample neural pattern generated for integration testing"
        }
        
        # Write the data files
        with open(data_path, "w") as f:
            json.dump(mind_mirror_data, f, indent=2)
            
        with open(meta_path, "w") as f:
            json.dump(metadata, f, indent=2)
            
        # Create notification file
        with open(notification_path, "w") as f:
            f.write(timestamp)
            
        logger.info(f"Created sample Mind Mirror data files at {imports_dir}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to create sample Mind Mirror data: {e}")
        return False

def run_glitch_demo(glitcher: RealityGlitcher) -> None:
    """
    Run a demo of glitch effects based on Mind Mirror data
    
    Args:
        glitcher: Initialized RealityGlitcher instance
    """
    logger.info("Starting Reality Glitcher integration demo")
    
    # Integrate with Mind Mirror
    glitcher.integrate_with_mind_mirror()
    
    # Check if integration was successful
    if not glitcher.active_glitches:
        logger.warning("No glitches were created from Mind Mirror data")
        return
    
    logger.info(f"Created {len(glitcher.active_glitches)} glitches from Mind Mirror data")
    
    # Display information about the glitches
    for i, glitch in enumerate(glitcher.active_glitches):
        logger.info(f"Glitch {i+1}: {glitch.type.name}")
        logger.info(f"  Intensity: {glitch.parameters.intensity:.2f}")
        logger.info(f"  Duration: {glitch.parameters.duration:.2f}s")
        logger.info(f"  Target: {glitch.target}")
    
    # Simulate glitch effects over time
    logger.info("\nSimulating reality glitches based on Mind Mirror neural patterns...")
    
    total_duration = 10  # seconds for the demo
    check_interval = 0.5  # seconds between status updates
    
    start_time = time.time()
    while (time.time() - start_time) < total_duration:
        # Update glitch states
        active_count = sum(1 for g in glitcher.active_glitches if g.active)
        
        # Calculate current reality stability
        stability = glitcher._calculate_current_stability()
        
        # Display current status
        logger.info(f"Reality stability: {stability:.2f} - Active glitches: {active_count}")
        
        # Sleep for the check interval
        time.sleep(check_interval)
    
    logger.info("\nDemo complete - Final reality status:")
    logger.info(f"Reality stability: {glitcher._calculate_current_stability():.2f}")
    logger.info(f"Active glitches: {sum(1 for g in glitcher.active_glitches if g.active)}")

def main():
    """Main function to run the integration demo"""
    logger.info("=== Mind Mirror + Reality Glitcher Integration Demo ===")
    
    # Check if Mind Mirror data is available
    if not check_for_mind_mirror_data():
        logger.warning("No Mind Mirror data found. Creating sample data for demo purposes.")
        if not create_sample_mind_mirror_data():
            logger.error("Failed to create sample data. Exiting.")
            return
    
    # Initialize Reality Glitcher
    try:
        glitcher = RealityGlitcher()
        logger.info("Reality Glitcher initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize Reality Glitcher: {e}")
        return
    
    # Run the demo
    run_glitch_demo(glitcher)
    
    logger.info("=== Integration Demo Complete ===")
    logger.info("In a real application, these glitches would affect the user's")
    logger.info("perception through visual and cognitive effects based on their")
    logger.info("own neural patterns exported from Mind Mirror.")

if __name__ == "__main__":
    main() 