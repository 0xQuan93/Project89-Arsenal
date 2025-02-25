"""
BioMod initialization module
Handles core cybernetic and biohacking implementations
"""

from .modules.cybernetic_implants import ImplantManager
from .modules.biohacking import BioHacker

class BioMod:
    def __init__(self):
        self.implant_manager = ImplantManager()
        self.biohacker = BioHacker() 