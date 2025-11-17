# KEYSTRO - QUICK REFERENCE CARD

## 🚀 LAUNCH COMMANDS

### GUI Dashboard:
```powershell
START_GUI.bat
# or
py keystro_gui.py
```

### Terminal Interface:
```powershell
START_KEYSTRO.bat
# or
py keylogger_terminal.py
```

---

## 🎯 FIRST TIME SETUP

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Grant consent (required!)
py setup_consent.py

# 3. Launch your preferred interface
START_GUI.bat
```

---

## 📊 GUI TOOLS

| Tool | Icon | Purpose |
|------|------|---------|
| Session Viewer | 📊 | View recorded keystrokes |
| Threat Analyzer | 🔍 | Analyze activity patterns |
| Statistics | 📈 | Storage & consent info |
| Consent Manager | ✓ | Grant/revoke permissions |

---

## ⌨️ TERMINAL MENU

1. **Start Recording** - Capture keystrokes (ESC to stop)
2. **View Sessions** - Browse recorded data
3. **Statistics** - View detection summary
4. **Settings** - Configure options
5. **Help** - Display help
6. **Exit** - Quit KEYSTRO

---

## 🔍 THREAT DETECTION

### Monitored Keywords:
- `password`, `passwd`, `pwd`
- `credit`, `card`
- `ssn`, `social security`
- `bank`, `account`
- `login`, `username`

### Alert Display:
Red boxes appear in terminal with:
- Process name & PID
- Confidence level (HIGH/MEDIUM/LOW)
- Threat score (0-100)
- Evidence & recommendation

---

## 💾 DATA STORAGE

**Location**: `data/keystroke_logs.db`
**Format**: Encrypted SQLite
**Limit**: 1 MB (auto-cleanup at 20%)

**View Data**:
- Terminal: Menu option 2 (View Sessions)
- GUI: Open "Session Viewer" tool

**Clear Data**:
- Terminal: Menu option 3 → Clear option
- GUI: Session Viewer → "Clear All" button

---

## 🛡️ CONSENT MANAGEMENT

### Check Status:
```powershell
# GUI: Open "Consent Manager" tool
# Terminal: Menu option 4 (Settings)
```

### Grant Consent:
```powershell
py setup_consent.py
# or GUI: Consent Manager → "Grant Consent"
```

### Revoke Consent:
```powershell
# GUI: Consent Manager → "Revoke Consent"
# or delete data/consent.db
```

---

## ⚠️ LEGAL REMINDERS

✅ **ALLOWED**:
- Educational purposes
- Your own devices
- Authorized research
- Personal monitoring

❌ **PROHIBITED** (ILLEGAL):
- Other people's devices
- Shared computers without consent
- Capturing sensitive data from others
- Commercial surveillance
- Malicious activities

---

## 🔧 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| "Module not found" | `pip install -r requirements.txt` |
| "No consent" | `py setup_consent.py` |
| GUI won't open | Check Python 3.12+, test `py -m tkinter` |
| Keys not captured | Run with admin, check antivirus |
| Storage full | Clear sessions in GUI/Terminal |

---

## 📁 PROJECT FILES

```
keylogger_terminal.py  ← Terminal interface (main)
keystro_gui.py         ← GUI dashboard (new!)
START_KEYSTRO.bat      ← Terminal launcher
START_GUI.bat          ← GUI launcher
setup_consent.py       ← Consent setup
check_setup.py         ← Pre-flight check
README.md              ← Full documentation
PROJECT_STATUS.md      ← This file!
```

---

## 🎓 EDUCATIONAL USE CASES

1. **Learn Cybersecurity**
   - Study keystroke logging techniques
   - Understand threat detection
   - Learn about digital privacy

2. **Security Research**
   - Test threat algorithms
   - Analyze typing patterns
   - Evaluate storage security

3. **Personal Monitoring**
   - Track typing habits
   - Analyze productivity
   - Test security awareness

---

## 💡 PRO TIPS

1. **Start with GUI** - Easier for beginners, shows agreement
2. **Use Terminal for Recording** - Real-time capture with threat detection
3. **Check Storage Regularly** - View statistics to avoid hitting 1MB limit
4. **Test Threat Detection** - Type "password" to see red alerts
5. **Revoke When Done** - Good practice to revoke consent after testing

---

## 📞 NEED HELP?

1. **Check README.md** - Full documentation with examples
2. **Run Pre-flight Check** - `py check_setup.py`
3. **Test Interface** - Launch with terminal to see errors
4. **Verify Dependencies** - `pip list | Select-String "pynput|cryptography"`

---

**Remember**: Use KEYSTRO responsibly, ethically, and legally! 🛡️

**Version**: 2.0 (GUI + Terminal)
**Updated**: 2025-01-10
