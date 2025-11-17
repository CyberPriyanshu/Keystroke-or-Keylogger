import sqlite3
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from cryptography.fernet import Fernet
import config

class SecureStorage:
    """Handles encrypted storage of activity logs"""
    
    def __init__(self):
        self.db_path = config.DATABASE_FILE
        self.key_file = config.DATA_DIR / ".key"
        self.cipher = self._get_or_create_cipher()
        self._init_database()
    
    def _get_or_create_cipher(self) -> Fernet:
        """Get or create encryption key"""
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            # Hide the key file on Windows
            try:
                import ctypes
                ctypes.windll.kernel32.SetFileAttributesW(str(self.key_file), 2)  # FILE_ATTRIBUTE_HIDDEN
            except:
                pass
        return Fernet(key)
    
    def _init_database(self):
        """Initialize SQLite database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activity_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                app_name TEXT,
                window_title TEXT,
                duration_seconds INTEGER,
                encrypted_data TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_timestamp ON activity_logs(timestamp)
        ''')
        
        conn.commit()
        conn.close()
    
    def _encrypt(self, data: str) -> str:
        """Encrypt data"""
        return self.cipher.encrypt(data.encode()).decode()
    
    def _decrypt(self, encrypted_data: str) -> str:
        """Decrypt data"""
        return self.cipher.decrypt(encrypted_data.encode()).decode()
    
    def store_activity(self, app_name: str, window_title: Optional[str], duration_seconds: int):
        """Store an activity log entry with 1MB size limit"""
        # Check database size before storing
        if self.db_path.exists():
            db_size_mb = self.db_path.stat().st_size / (1024 * 1024)
            if db_size_mb >= 1.0:
                print(f"⚠️  WARNING: Database size limit reached ({db_size_mb:.2f} MB). Oldest entries will be deleted.")
                self._cleanup_old_entries()
        
        timestamp = datetime.now().isoformat()
        
        # Create data object
        data = {
            'timestamp': timestamp,
            'app_name': app_name,
            'window_title': window_title,
            'duration': duration_seconds
        }
        
        # Encrypt the data
        encrypted = self._encrypt(json.dumps(data))
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO activity_logs (timestamp, app_name, window_title, duration_seconds, encrypted_data)
            VALUES (?, ?, ?, ?, ?)
        ''', (timestamp, app_name, window_title or '', duration_seconds, encrypted))
        
        conn.commit()
        conn.close()
    
    def _cleanup_old_entries(self):
        """Delete oldest 20% of entries to stay under 1MB limit"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get total count
        cursor.execute('SELECT COUNT(*) FROM activity_logs')
        total = cursor.fetchone()[0]
        
        if total > 0:
            delete_count = max(1, int(total * 0.2))  # Delete oldest 20%
            cursor.execute('''
                DELETE FROM activity_logs 
                WHERE id IN (
                    SELECT id FROM activity_logs 
                    ORDER BY timestamp ASC 
                    LIMIT ?
                )
            ''', (delete_count,))
            
            conn.commit()
            print(f"✓ Deleted {delete_count} oldest entries to maintain 1MB limit")
        
        conn.close()
    
    def get_logs(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> List[Dict]:
        """Retrieve and decrypt activity logs"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query = 'SELECT encrypted_data FROM activity_logs'
        params = []
        
        if start_date or end_date:
            query += ' WHERE '
            conditions = []
            if start_date:
                conditions.append('timestamp >= ?')
                params.append(start_date.isoformat())
            if end_date:
                conditions.append('timestamp <= ?')
                params.append(end_date.isoformat())
            query += ' AND '.join(conditions)
        
        query += ' ORDER BY timestamp DESC'
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        
        # Decrypt and parse logs
        logs = []
        for row in rows:
            try:
                decrypted = self._decrypt(row[0])
                logs.append(json.loads(decrypted))
            except Exception as e:
                print(f"Error decrypting log: {e}")
        
        return logs
    
    def get_summary_stats(self, days: int = 7) -> Dict:
        """Get summary statistics for the last N days"""
        start_date = datetime.now() - timedelta(days=days)
        logs = self.get_logs(start_date=start_date)
        
        # Aggregate by app
        app_times = {}
        total_time = 0
        
        for log in logs:
            app = log.get('app_name', 'Unknown')
            duration = log.get('duration', 0)
            app_times[app] = app_times.get(app, 0) + duration
            total_time += duration
        
        return {
            'total_entries': len(logs),
            'total_time_seconds': total_time,
            'app_breakdown': app_times,
            'period_days': days
        }
    
    def delete_all_logs(self) -> bool:
        """Securely delete all stored logs"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM activity_logs')
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error deleting logs: {e}")
            return False
    
    def cleanup_old_logs(self, retention_days: int):
        """Delete logs older than retention period"""
        cutoff_date = datetime.now() - timedelta(days=retention_days)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM activity_logs WHERE timestamp < ?', (cutoff_date.isoformat(),))
        deleted = cursor.rowcount
        conn.commit()
        conn.close()
        
        return deleted
