"""
Simple tests to verify ethical safeguards
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from consent_manager import ConsentManager
from storage import SecureStorage
import config

class TestEthicalSafeguards(unittest.TestCase):
    """Test that ethical safeguards are in place"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.consent_manager = ConsentManager()
    
    def test_no_logging_without_consent(self):
        """Verify that consent is required"""
        # Delete any existing consent
        if config.CONSENT_FILE.exists():
            config.CONSENT_FILE.unlink()
        
        # Should have no valid consent
        self.assertFalse(self.consent_manager.has_valid_consent())
    
    def test_consent_can_be_revoked(self):
        """Verify consent can be revoked"""
        # Give consent
        scopes = {'app_names': True, 'window_titles': False}
        self.consent_manager.record_consent(scopes, "Test User")
        
        # Verify consent exists
        self.assertTrue(self.consent_manager.has_valid_consent())
        
        # Revoke consent
        self.consent_manager.revoke_consent()
        
        # Verify consent is revoked
        self.assertFalse(self.consent_manager.has_valid_consent())
    
    def test_storage_is_encrypted(self):
        """Verify data is encrypted in storage"""
        storage = SecureStorage()
        
        # Store some test data
        storage.store_activity("TestApp", "Test Window", 60)
        
        # Read raw database file
        with open(config.DATABASE_FILE, 'rb') as f:
            raw_data = f.read()
        
        # Verify we can't find plaintext in the file
        self.assertNotIn(b"TestApp", raw_data)
        self.assertNotIn(b"Test Window", raw_data)
    
    def test_keystrokes_config_is_false(self):
        """Verify keystrokes are NOT enabled"""
        cfg = config.load_config()
        self.assertFalse(cfg.get('log_keystrokes'))
        self.assertEqual(config.DEFAULT_CONFIG['log_keystrokes'], False)
    
    def test_upload_disabled_by_default(self):
        """Verify uploads are disabled by default"""
        cfg = config.load_config()
        self.assertFalse(cfg.get('enable_upload'))

if __name__ == '__main__':
    print("=" * 70)
    print("Running Ethical Safeguard Tests")
    print("=" * 70)
    unittest.main(verbosity=2)
