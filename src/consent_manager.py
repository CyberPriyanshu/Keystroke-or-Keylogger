import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional
import config

class ConsentManager:
    """Manages user consent for activity logging"""
    
    def __init__(self):
        self.consent_file = config.CONSENT_FILE
        self._consent_data = None
    
    def has_valid_consent(self) -> bool:
        """Check if user has given valid consent"""
        if not self.consent_file.exists():
            return False
        
        try:
            with open(self.consent_file, 'r') as f:
                consent = json.load(f)
                return consent.get('agreed', False) and not consent.get('revoked', False)
        except:
            return False
    
    def get_consent_data(self) -> Optional[Dict]:
        """Get stored consent data"""
        if not self.consent_file.exists():
            return None
        
        try:
            with open(self.consent_file, 'r') as f:
                return json.load(f)
        except:
            return None
    
    def record_consent(self, scopes: Dict[str, bool], user_signature: str) -> bool:
        """Record user consent with selected scopes"""
        consent_data = {
            'agreed': True,
            'revoked': False,
            'timestamp': datetime.now().isoformat(),
            'scopes': scopes,
            'signature_hash': hashlib.sha256(user_signature.encode()).hexdigest(),
            'version': config.APP_VERSION,
            'ethical_agreement_acknowledged': True
        }
        
        try:
            with open(self.consent_file, 'w') as f:
                json.dump(consent_data, f, indent=2)
            self._consent_data = consent_data
            return True
        except Exception as e:
            print(f"Error recording consent: {e}")
            return False
    
    def revoke_consent(self) -> bool:
        """Revoke user consent"""
        if not self.consent_file.exists():
            return True
        
        try:
            with open(self.consent_file, 'r') as f:
                consent = json.load(f)
            
            consent['revoked'] = True
            consent['revoked_at'] = datetime.now().isoformat()
            
            with open(self.consent_file, 'w') as f:
                json.dump(consent, f, indent=2)
            
            self._consent_data = None
            return True
        except Exception as e:
            print(f"Error revoking consent: {e}")
            return False
    
    def get_active_scopes(self) -> Dict[str, bool]:
        """Get currently active consent scopes"""
        consent = self.get_consent_data()
        if not consent or consent.get('revoked', False):
            return {}
        return consent.get('scopes', {})
    
    def is_scope_allowed(self, scope: str) -> bool:
        """Check if a specific scope is allowed"""
        scopes = self.get_active_scopes()
        return scopes.get(scope, False)
