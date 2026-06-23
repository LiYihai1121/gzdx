"""
gzdx - Python project framework.
"""

__version__ = "0.1.0"
__all__ = ["__version__"]

from gzdx.config import Settings
from gzdx.logger import setup_logging

__all__ += ["Settings", "setup_logging"]
