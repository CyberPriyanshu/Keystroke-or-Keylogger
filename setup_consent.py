"""
Quick setup script to grant consent for terminal keylogger testing
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from consent_manager import ConsentManager

def setup_consent():
    """Grant consent for keylogger"""
    print("Setting up consent for keylogger...")
    
    consent_manager = ConsentManager()
    
    # Grant all scopes
    scopes = {
        'app_names': True,
        'window_titles': True,
        'usage_time': True,
        'analytics': True
    }
    
    consent_manager.record_consent(scopes, "Test User")
    
    print("✅ Consent granted!")
    print("✅ You can now run: py keylogger_terminal.py")

if __name__ == "__main__":
    setup_consent()
