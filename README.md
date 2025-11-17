# KEYSTRO - Educational Keystroke Analysis Tool

![Version](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.12-green.svg)
![License](https://img.shields.io/badge/license-Educational-yellow.svg)

## ⚠️ EDUCATIONAL USE ONLY ⚠️

This software is designed **EXCLUSIVELY** for educational purposes, security research, and authorized monitoring of your own devices. Unauthorized use of keystroke logging software is **ILLEGAL** and violates privacy laws.

---

## 🎯 Features

### Two Interfaces:
1. **Terminal Interface** (`keylogger_terminal.py`)
   - Professional KEYSTRO command-line interface
   - Real-time keystroke capture and display
   - Threat detection with red alert boxes
   - Interactive 6-option menu system
   - Color-coded output for easy reading
   - Detection summary with statistics

2. **GUI Dashboard** (`keystro_gui.py`)
   - Modern graphical interface with 4 tools
   - Prominent EDUCATIONAL USE AGREEMENT (required)
   - Session Viewer - Browse recorded keystrokes
   - Threat Analyzer - View detected threats
   - Statistics - Monitor storage and activity
   - Consent Manager - Manage permissions

### Core Capabilities:
- ✅ **True Keystroke Capture** - Records actual keystrokes from ANY application
- ✅ **Threat Detection** - Identifies suspicious patterns (passwords, credit cards, SSNs)
- ✅ **Encrypted Storage** - SQLite database with encryption
- ✅ **1MB Storage Limit** - Auto-deletes oldest entries when limit reached
- ✅ **Consent Mechanism** - Ethical safeguards built-in
- ✅ **Educational Agreement** - Legal protection for developers

---

## 📦 Installation

### 1. Install Python 3.12+
Download from [python.org](https://www.python.org/)

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

Required packages:
- `pynput` - Keyboard event capture
- `cryptography` - Database encryption

### 3. Grant Consent (Required)
```powershell
py setup_consent.py
```

---

## 🚀 Quick Start

### GUI Interface (Recommended for Beginners):
```powershell
# Double-click or run:
START_GUI.bat

# Or directly:
py keystro_gui.py
```

**First-time use:**
1. GUI opens with EDUCATIONAL USE AGREEMENT
2. Read the entire agreement carefully
3. Check "I have read and understand this agreement"
4. Click "I ACCEPT - PROCEED"
5. Dashboard opens with 4 tools

**Available Tools:**
- 📊 **Session Viewer** - View recorded keystroke sessions
- 🔍 **Threat Analyzer** - Analyze detected threats
- 📈 **Statistics** - View storage and activity stats
- ✓ **Consent Manager** - Manage monitoring permissions

### Terminal Interface (Advanced):
```powershell
# Double-click or run:
START_KEYSTRO.bat

# Or directly:
py keylogger_terminal.py
```

**Menu Options:**
1. **Start Recording** - Begin keystroke capture
2. **View Sessions** - Browse recorded data
3. **Statistics** - View detection summary
4. **Settings** - Configure options
5. **Help** - Display help information
6. **Exit** - Quit KEYSTRO

**Keyboard Control:**
- Press `ESC` to stop recording
- Press `Ctrl+C` to force quit

---

## 🔍 Threat Detection

KEYSTRO automatically analyzes keystrokes for suspicious patterns:

### Detected Keywords:
- `password`, `passwd`, `pwd`
- `credit`, `card`
- `ssn`, `social security`
- `bank`, `account`
- `login`, `username`

### Alert Display:
```
╔══════════════════════ THREAT DETECTED ══════════════════════╗
║ Process: chrome.exe                                         ║
║ PID: 12345                                                  ║
║ Path: C:\Program Files\Google\Chrome\Application\chrome.exe║
║ Confidence: HIGH                                            ║
║ Threat Score: 95/100                                        ║
║ Evidence: Keyword 'password' detected                       ║
║ Recommendation: Review this activity for security concerns  ║
╚═════════════════════════════════════════════════════════════╝
```

---

## 📊 Data Storage

- **Location**: `data/keystroke_logs.db`
- **Format**: Encrypted SQLite database
- **Size Limit**: 1 MB (configurable in `src/config.py`)
- **Auto-Cleanup**: When limit reached, oldest 20% automatically deleted

### Storage Structure:
```json
{
  "timestamp": "2025-01-10 14:30:45",
  "data": {
    "key": "a",
    "threat_detected": false,
    "threat_type": null,
    "confidence": null
  }
}
```

---

## 🛡️ Safeguards & Ethics

### Built-in Protections:
1. **Consent Requirement** - Must be granted before monitoring
2. **Educational Agreement** - Displayed prominently in GUI
3. **Legal Warnings** - Shown at startup in terminal
4. **Storage Limits** - Prevents excessive data accumulation
5. **Clear Labeling** - All interfaces identify as educational tools

### Consent Management:
```powershell
# Grant consent (required for first use)
py setup_consent.py

# Check consent status
# In GUI: Open "Consent Manager" tool
# In Terminal: Menu option 4 (Settings)

# Revoke consent
# In GUI: Open "Consent Manager" → Click "Revoke Consent"
```

---

## ⚙️ Configuration

Edit `src/config.py` to customize:

```python
class Config:
    MAX_STORAGE_SIZE = 1024 * 1024  # 1MB in bytes
    CONSENT_VALIDITY_DAYS = 30       # Consent expiration
    ENCRYPTION_KEY = Fernet.generate_key()  # Database encryption
```

---

## 📁 Project Structure

```
d:\Cyber Security\Keylogger\
│
├── keylogger_terminal.py      # Terminal interface (main)
├── keystro_gui.py              # GUI dashboard (new)
├── START_KEYSTRO.bat           # Terminal launcher
├── START_GUI.bat               # GUI launcher
├── setup_consent.py            # Consent granting utility
├── check_setup.py              # Pre-flight verification
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── src/
│   ├── storage.py              # Encrypted database
│   ├── consent_manager.py      # Consent lifecycle
│   ├── config.py               # Configuration
│   └── __init__.py
│
├── tests/
│   ├── test_safeguards.py      # Automated tests
│   └── __init__.py
│
├── data/
│   ├── keystroke_logs.db       # Encrypted keystroke data
│   └── consent.db              # Consent records
│
└── .vscode/
    └── settings.json           # Editor configuration
```

---

## 🧪 Testing

### Pre-flight Check:
```powershell
py check_setup.py
```

Verifies:
- ✓ Python version
- ✓ Dependencies installed
- ✓ Consent granted
- ✓ Storage accessible
- ✓ Encryption working

### Automated Tests:
```powershell
py -m pytest tests/test_safeguards.py -v
```

---

## 🚨 Legal Disclaimer

### IMPORTANT LEGAL NOTICE:

This software is provided **EXCLUSIVELY** for:
- ✓ Educational purposes in controlled environments
- ✓ Security research with proper authorization
- ✓ Personal monitoring of YOUR OWN devices only
- ✓ Academic study of cybersecurity concepts

### PROHIBITED USES (ILLEGAL):
- ✗ Monitoring other people's devices without explicit consent
- ✗ Capturing passwords, credit cards, or sensitive data from others
- ✗ Installing on shared computers without authorization
- ✗ Any use that violates privacy laws or regulations
- ✗ Commercial surveillance or data harvesting
- ✗ Malicious activities of any kind

### Legal Consequences:
Unauthorized use of keystroke logging software may result in:
- Criminal charges under computer fraud and abuse laws
- Civil lawsuits for privacy violations
- Substantial fines and imprisonment
- Permanent criminal record

### Developer Liability:
The developers of KEYSTRO are **NOT LIABLE** for any misuse of this software. By using KEYSTRO, you accept **FULL RESPONSIBILITY** for ensuring your use complies with all applicable laws and ethical standards.

---

## 📝 Support

### Common Issues:

**Q: "Module not found" error**
```powershell
pip install -r requirements.txt
```

**Q: "No consent" error**
```powershell
py setup_consent.py
```

**Q: GUI doesn't open**
- Check Python version (3.12+ required)
- Verify tkinter installed: `py -m tkinter`
- Run from terminal to see error messages

**Q: Terminal interface not capturing keys**
- Must be run with admin privileges on some systems
- Verify pynput installed: `pip install pynput`
- Check antivirus isn't blocking

**Q: Storage full warning**
- Delete old sessions: In GUI → Session Viewer → Clear All
- Or increase limit in `src/config.py`

---

## 🔄 Updates

### Version 2.0 (Current)
- ✅ Added GUI dashboard with 4 tools
- ✅ Prominent EDUCATIONAL USE AGREEMENT
- ✅ Session Viewer tool
- ✅ Threat Analyzer tool
- ✅ Statistics tool
- ✅ Consent Manager tool
- ✅ Professional card-based interface
- ✅ Color-coded threat levels
- ✅ Real-time data refresh

### Version 1.0
- ✅ Terminal KEYSTRO interface
- ✅ Real-time keystroke capture
- ✅ Threat detection system
- ✅ Encrypted storage
- ✅ Consent mechanism

---

## 🎓 Educational Use Cases

### Approved Learning Activities:
1. **Cybersecurity Education**
   - Study keystroke logging techniques
   - Understand detection methods
   - Learn about digital privacy

2. **Security Research**
   - Test threat detection algorithms
   - Analyze typing patterns
   - Evaluate storage security

3. **Personal Monitoring**
   - Track your own typing habits
   - Analyze your productivity
   - Test security awareness

### Ethical Guidelines:
- Always obtain explicit consent before monitoring
- Only monitor devices you own or have written authorization for
- Inform all users that monitoring is active
- Delete captured data when no longer needed
- Never share captured keystrokes with unauthorized parties

---

## 📧 Contact

For educational inquiries and authorized research collaboration:
- Report issues: Use GitHub Issues (if applicable)
- Security concerns: Contact your institution's IT security team
- Legal questions: Consult with a qualified attorney

---

## 📜 License

This software is provided for **EDUCATIONAL USE ONLY**. No warranty or liability is provided. Users assume all legal responsibility for their actions.

**Copyright © 2025 KEYSTRO Project**

---

## 🙏 Acknowledgments

KEYSTRO was created to educate users about:
- Keystroke logging technology
- Digital privacy importance
- Threat detection methods
- Ethical computing practices

**Use responsibly. Use ethically. Use legally.**

---

**Remember: With great power comes great responsibility. Use KEYSTRO only for good.**
