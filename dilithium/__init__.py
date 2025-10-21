"""
Dilithium Post-Quantum Digital Signature Suite
"""

from .core import DilithiumParams, PolynomialRing
from .keygen import KeyGenerator
from .sign import Signer
from .verify import Verifier
from .config import SecurityConfig, SystemConfig

__version__ = "1.0.0"
__author__ = "Dilithium Development Team"

__all__ = [
    "DilithiumParams",
    "PolynomialRing", 
    "KeyGenerator",
    "Signer",
    "Verifier",
    "SecurityConfig",
    "SystemConfig"
] 