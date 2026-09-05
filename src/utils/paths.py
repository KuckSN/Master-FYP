from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
CONFIGS_DIR = PROJECT_ROOT / "configs"

__all__ = ["PROJECT_ROOT", "DATA_DIR", "MODELS_DIR", "CONFIGS_DIR"]

