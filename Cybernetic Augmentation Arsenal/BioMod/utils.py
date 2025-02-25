"""
Utility functions for BioMod operations
"""
from typing import Any, Dict, List
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_implant_compatibility(implant_data: Dict[str, Any]) -> bool:
    """Validates if an implant is compatible with current system"""
    required_fields = ['type', 'compatibility_version', 'safety_rating']
    return all(field in implant_data for field in required_fields)

def calculate_bio_metrics(data: List[float]) -> Dict[str, float]:
    """Calculates various biometric measurements"""
    if not data:
        return {}
    return {
        "average": sum(data) / len(data),
        "peak": max(data),
        "stability": sum(1 for x in data if 0.4 <= x <= 0.6) / len(data)
    } 