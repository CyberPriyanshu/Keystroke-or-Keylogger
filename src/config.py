import os
import json
from pathlib import Path

# Application metadata
APP_NAME = "Consent-Based Activity Logger (CAL)"
APP_VERSION = "1.0.0-edu"
APP_PURPOSE = "Educational Activity Monitoring Tool"

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
CONSENT_FILE = DATA_DIR / "consent.json"
DATABASE_FILE = DATA_DIR / "activity_logs.db"
CONFIG_FILE = DATA_DIR / "config.json"

# Create data directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Default configuration
DEFAULT_CONFIG = {
    "log_interval_seconds": 5,  # How often to check active window
    "retention_days": 30,  # How long to keep logs
    "enable_upload": False,  # Disabled by default
    "anonymize_data": True,
    "log_window_titles": True,
    "log_app_names": True,
    "log_keystrokes": False,  # ALWAYS FALSE - not implemented
}

# Consent scopes
CONSENT_SCOPES = {
    "app_names": {
        "label": "Application Names",
        "description": "Log which applications you use (e.g., Chrome, VSCode)",
        "required": True
    },
    "window_titles": {
        "label": "Window Titles",
        "description": "Log the titles of active windows (may contain page titles, document names)",
        "required": False
    },
    "usage_time": {
        "label": "Usage Duration",
        "description": "Track how long you spend in each application",
        "required": True
    },
    "analytics": {
        "label": "Anonymous Analytics",
        "description": "Allow anonymized usage patterns for research (no personal data)",
        "required": False
    }
}

# UI Colors
COLOR_PRIMARY = "#2C3E50"
COLOR_SUCCESS = "#27AE60"
COLOR_DANGER = "#E74C3C"
COLOR_WARNING = "#F39C12"
COLOR_BG = "#ECF0F1"

def load_config():
    """Load configuration from file or create default"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    return DEFAULT_CONFIG.copy()

def save_config(config):
    """Save configuration to file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)
