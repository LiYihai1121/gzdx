"""Application configuration via environment variables / .env."""

from __future__ import annotations

import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Settings:
    """Immutable settings loaded from environment."""

    debug: bool = field(default_factory=lambda: os.getenv("GZDX_DEBUG", "false").lower() == "true")
    log_level: str = field(default_factory=lambda: os.getenv("GZDX_LOG_LEVEL", "INFO"))
    data_dir: str = field(default_factory=lambda: os.getenv("GZDX_DATA_DIR", "./data"))

    @classmethod
    def load(cls) -> Settings:
        """Build settings from environment (idempotent)."""
        return cls()


# Module-level singleton for easy import.
settings = Settings.load()
