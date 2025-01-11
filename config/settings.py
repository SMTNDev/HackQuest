# HackQuest Game Settings

# Game Metadata
GAME_NAME = "HackQuest"
VERSION = "1.6.0"
AUTHOR = "SMTNDev"
DESCRIPTION = "A terminal-based hacking simulator game."
COPYRIGHT = "© 2025 HackQuest Team"

# Game Colors (ANSI Escape Codes)
COLORS = {
    "info": "\033[94m",       # Blue
    "success": "\033[92m",    # Green
    "warning": "\033[93m",    # Yellow
    "error": "\033[91m",      # Red
    "hint": "\033[96m",       # Cyan
    "log": "\033[90m",        # Gray
    "reset": "\033[0m",       # Reset
}

# Animation Settings
ANIMATION_SPEED = 0.05  # Delay between characters for typewriter effect
WELCOME_ANIMATION_DELAY = 0.1  # Delay for welcome screen animation

# Game Levels
LEVELS = {
    "level1": {
        "name": "Password Retrieval Challenge",
        "description": "Identify the correct password from the hints provided.",
    },
    "level2": {
        "name": "File Decryption Challenge",
        "description": "Decrypt the file contents using the provided key.",
    },
    "level3": {
        "name": "Log Analysis Challenge",
        "description": "Identify the anomaly in the server logs.",
    },
}

# Debug Mode
DEBUG_MODE = False  # Set to True for verbose debugging information

# Logging Configuration
LOG_FILE = "logs/game_logs.txt"
LOG_LEVEL = "INFO"

# ASCII Art for the Welcome Screen
ASCII_ART = """

██   ██  █████   ██████ ██   ██  ██████  ██    ██ ███████ ███████ ████████ 
██   ██ ██   ██ ██      ██  ██  ██    ██ ██    ██ ██      ██         ██    
███████ ███████ ██      █████   ██    ██ ██    ██ █████   ███████    ██    
██   ██ ██   ██ ██      ██  ██  ██ ▄▄ ██ ██    ██ ██           ██    ██    
██   ██ ██   ██  ██████ ██   ██  ██████   ██████  ███████ ███████    ██    
                                    ▀▀                                     
                                                                           

"""

# Separator Style
SEPARATOR = "-" * 50

# Credits
CREDITS = """
Developed by the HackQuest Team
Special thanks to all contributors and testers!
"""
