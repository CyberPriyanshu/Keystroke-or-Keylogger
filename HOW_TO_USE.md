# 🎯 KEYSTRO - Complete Usage Guide

## 📋 Table of Contents
1. [Quick Start](#quick-start)
2. [Terminal Interface](#terminal-interface)
3. [GUI Dashboard](#gui-dashboard)
4. [New Features Added](#new-features-added)
5. [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start

### First Time Setup:

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Grant consent (REQUIRED)
py setup_consent.py

# 3. Choose your interface:
# For GUI:
START_GUI.bat

# For Terminal:
START_KEYSTRO.bat
```

---

## 💻 Terminal Interface (KEYSTRO CLI)

### Launch:
```powershell
START_KEYSTRO.bat
# OR
py keylogger_terminal.py
```

### What You'll See:

```
┌─────────────────────────────────────────┐
│          K E Y S T R O                  │
│    Educational Keystroke Recording      │
└─────────────────────────────────────────┘

⚠️ LEGAL WARNING (in red background)

MENU:
[1] Start Recording
[2] View Sessions
[3] Statistics
[4] Settings
[5] Help
[6] Exit
```

### How to Use:

**Option 1: Start Recording**
1. Type `1` and press Enter
2. Start typing anywhere on your computer
3. Keystrokes appear in real-time:
   ```
   [14:30:45] Key: h
   [14:30:45] Key: e
   [14:30:46] Key: l
   [14:30:46] Key: l
   [14:30:47] Key: o
   ```
4. **If you type sensitive keywords** (password, credit card):
   ```
   ╔══════════════════ THREAT DETECTED ══════════════════╗
   ║ Process: chrome.exe                                 ║
   ║ Confidence: HIGH                                    ║
   ║ Evidence: Keyword 'password' detected               ║
   ║ Recommendation: Review this activity                ║
   ╚═════════════════════════════════════════════════════╝
   ```
5. Press **ESC** to stop recording

**Option 2: View Sessions**
- Shows all recorded keystroke sessions
- Displays timestamps and typed content

**Option 3: Statistics**
- Shows detection summary
- Confidence levels (High/Medium/Low)
- Total threats detected

**Option 4: Settings**
- Configure monitoring options

**Option 5: Help**
- Display help information

**Option 6: Exit**
- Quit KEYSTRO

---

## 🖥️ GUI Dashboard (New & Enhanced!)

### Launch:
```powershell
START_GUI.bat
# OR
py keystro_gui.py
```

### First Launch Experience:

#### Step 1: Educational Use Agreement
![Agreement Dialog]
- Large modal dialog appears
- **Yellow-highlighted warnings**
- Read carefully!
- Check ✅ "I have read and understand this agreement"
- Click "✓ I ACCEPT - PROCEED" (button is disabled until checkbox checked)
- **NOTE**: If you click "✗ DECLINE", the application will close

#### Step 2: Dashboard Opens
You'll see **5 TOOL CARDS**:

```
┌──────────────────────────────────────────────────────┐
│              K E Y S T R O                           │
│    Educational Keystroke Analysis Dashboard          │
└──────────────────────────────────────────────────────┘

⚠️ EDUCATIONAL USE ONLY - Authorized Monitoring Required ⚠️

Select a tool to begin:

┌──────────────┐  ┌──────────────┐
│  📊          │  │  🔍          │
│ Session      │  │ Threat       │
│ Viewer       │  │ Analyzer     │
└──────────────┘  └──────────────┘

┌──────────────┐  ┌──────────────┐
│  📈          │  │  💾          │
│ Statistics   │  │ Data         │
│              │  │ Exporter     │
└──────────────┘  └──────────────┘

┌──────────────┐
│  ✓           │
│ Consent      │
│ Manager      │
└──────────────┘
```

---

## 🛠️ Tool-by-Tool Guide

### 📊 Tool 1: Session Viewer (ENHANCED!)

**What it does:**
- View all recorded keystroke sessions
- **NEW**: Shows typing speed (WPM/CPM)
- **NEW**: Shows error analysis (backspaces, deletes, accuracy)
- Real-time refresh
- Clear all data

**How to use:**
1. Click the "Session Viewer" card
2. New window opens showing:
   ```
   ═══════════════════════════════════════════
     KEYSTROKE SESSIONS - 15 entries
   ═══════════════════════════════════════════
   
   📊 TYPING STATISTICS:
      Total Characters: 450
      Total Duration: 180s (3.0 min)
      ⚡ Speed: 30 WPM (150 CPM)
      Average Session: 12.0s
   
   ⚠️ ERROR ANALYSIS:
      Backspaces: 12
      Deletes: 3
      Error Rate: 3.33%
      Accuracy: 96.67%
   
   📝 SESSION DETAILS:
   
   [1] 2025-11-17 14:30:45
       App: Keylogger
       Window: Typed: Hello world
       Duration: 5s | Speed: 24 WPM (120 CPM)
   ```

**Buttons:**
- 🔄 **Refresh** - Reload latest data
- 🗑️ **Clear All** - Delete all sessions (asks for confirmation)

**Window behavior:**
- ✅ Stays open after clicking
- ✅ Can open multiple tools simultaneously
- ✅ Close with X button when done

---

### 🔍 Tool 2: Threat Analyzer

**What it does:**
- Shows detected threats
- Groups by application
- Recent activity log

**How to use:**
1. Click "Threat Analyzer" card
2. See summary:
   ```
   ╔═══════════════════════════════════════╗
   ║     SESSION ACTIVITY SUMMARY          ║
   ╚═══════════════════════════════════════╝
   
   Sessions by Application:
     • Keylogger: 15
     • chrome.exe: 5
   
   Note: Threat detection is shown in real-time 
   in the terminal interface. Red alert boxes 
   appear when suspicious keywords are detected.
   
   Recent Activity:
   [1] 2025-11-17 14:30:45
     App: Keylogger
     Window: Typed: Hello world
   ```

**Button:**
- 🔄 **Refresh Analysis** - Update data

---

### 📈 Tool 3: Statistics

**What it does:**
- Shows total sessions recorded
- Storage usage (current size / 1MB limit)
- Warns when approaching limit
- Consent status
- Recent session breakdown

**How to use:**
1. Click "Statistics" card
2. Monitor your usage:
   ```
   ╔═══════════════════════════════════════╗
   ║       KEYSTRO STATISTICS              ║
   ╚═══════════════════════════════════════╝
   
   Total Sessions Recorded: 15
   
   STORAGE INFORMATION:
   Database Size: 0.05 MB / 1 MB
   Usage: 5.0%
   Database Location: D:\...\data\keystroke_logs.db
   
   CONSENT STATUS:
   ✓ Valid consent recorded
     Database: D:\...\data\consent.db
   
   SESSION BREAKDOWN:
   1. 2025-11-17 14:30:45 - Keylogger
   2. 2025-11-17 14:31:12 - Keylogger
   ...
   ```

**Button:**
- 🔄 **Refresh Statistics** - Update data

---

### 💾 Tool 4: Data Exporter (NEW!)

**What it does:**
- **Export sessions to JSON format**
- **Export sessions to TXT format**
- Preview data before export
- Auto-generates timestamped filenames

**How to use:**

#### Export to JSON:
1. Click "Data Exporter" card
2. Click "📄 Export to JSON" button
3. Save dialog opens with filename: `keystro_export_20251117_143045.json`
4. Choose location and click Save
5. Success message appears!

**JSON format:**
```json
[
  {
    "timestamp": "2025-11-17T14:30:45.123456",
    "app_name": "Keylogger",
    "window_title": "Typed: Hello world",
    "duration": 5
  }
]
```

#### Export to TXT:
1. Click "📝 Export to TXT" button
2. Save dialog opens with filename: `keystro_export_20251117_143045.txt`
3. Choose location and click Save
4. Success message appears!

**TXT format:**
```
======================================================================
KEYSTRO - Activity Log Export
Generated: 2025-11-17 14:30:45
Total Entries: 15
======================================================================

[1] 2025-11-17T14:30:45.123456
    App: Keylogger
    Window: Typed: Hello world
    Duration: 5s

[2] 2025-11-17T14:31:12.654321
    App: Keylogger
    Window: Typed: Testing export
    Duration: 8s
```

**Preview Panel:**
- Shows first 10 sessions
- Live preview of what will be exported

---

### ✓ Tool 5: Consent Manager

**What it does:**
- View consent status (GRANTED/NOT GRANTED)
- Grant new consent
- Revoke existing consent
- View consent database location

**How to use:**

#### Check Status:
1. Click "Consent Manager" card
2. See current status:
   ```
   ╔═══════════════════════════════════════╗
   ║      CONSENT INFORMATION              ║
   ╚═══════════════════════════════════════╝
   
   Status: ACTIVE
   
   Monitoring is AUTHORIZED for this device.
   
   Permissions:
     • Keystroke recording: ENABLED
     • Threat detection: ENABLED
     • Data storage: ENABLED
   ```

#### Grant Consent:
1. Click "✓ Grant Consent" button
2. Confirmation dialog appears:
   ```
   Do you consent to keystroke monitoring on this device?
   
   By clicking Yes, you confirm:
   • This is YOUR device
   • You have legal authority to monitor it
   • You understand the EDUCATIONAL USE AGREEMENT
   ```
3. Click "Yes"
4. Success message!

#### Revoke Consent:
1. Click "✗ Revoke Consent" button
2. Confirmation dialog:
   ```
   Are you sure you want to revoke consent?
   
   This will prevent all monitoring activities.
   ```
3. Click "Yes"
4. Consent revoked!

**Buttons:**
- ✓ **Grant Consent** - Authorize monitoring
- ✗ **Revoke Consent** - Remove authorization
- 🔄 **Refresh** - Update status display

---

## 🆕 New Features Added

### ✅ 1. WPM/CPM Calculation
**Where:** Session Viewer tool

**What it shows:**
- **WPM** (Words Per Minute) - Average: 40 WPM is normal
- **CPM** (Characters Per Minute) - WPM × 5
- Per-session speed
- Overall average speed

**How it's calculated:**
```
CPM = (Total Characters / Duration in seconds) × 60
WPM = CPM / 5
```

### ✅ 2. Error & Behavior Analysis
**Where:** Session Viewer tool

**What it tracks:**
- Backspace count
- Delete key count
- Error rate percentage
- Typing accuracy percentage

**Example output:**
```
⚠️ ERROR ANALYSIS:
   Backspaces: 12
   Deletes: 3
   Error Rate: 3.33%
   Accuracy: 96.67%
```

### ✅ 3. JSON/TXT Export
**Where:** Data Exporter tool (new!)

**Features:**
- Export all sessions to JSON or TXT
- Timestamped filenames
- File save dialog
- Data preview before export
- Success confirmation

---

## 🔧 Troubleshooting

### Problem: Tools close immediately after clicking

**Solution:** ✅ FIXED! Tools now stay open properly.

**If still happening:**
1. Close GUI completely
2. Reopen: `py keystro_gui.py`
3. Accept agreement
4. Try clicking tools again

---

### Problem: Agreement dialog doesn't show

**Check:**
1. Make sure you didn't decline it before
2. Delete `data/consent.db` to reset
3. Restart GUI

---

### Problem: No data in Session Viewer

**Reason:** You need to record keystrokes first!

**Solution:**
1. Open terminal: `py keylogger_terminal.py`
2. Select option 1 (Start Recording)
3. Type something
4. Press ESC
5. Now open GUI and check Session Viewer

---

### Problem: Export buttons don't work

**Check:**
1. Make sure you have recorded sessions
2. Try Refresh button first
3. Check if preview shows data

---

### Problem: WPM/CPM shows 0

**Reason:** Duration might be 0 seconds

**Solution:**
- Type for at least 1-2 seconds per session
- WPM calculation needs time duration

---

## 📊 Usage Tips

### For Best Results:

1. **Terminal for Recording:**
   - Use terminal interface to capture keystrokes
   - Watch real-time threat detection
   - See colored output

2. **GUI for Analysis:**
   - Use GUI to review sessions
   - Export data for reports
   - Monitor statistics
   - Manage consent

3. **Regular Monitoring:**
   - Check Statistics tool to monitor storage (1MB limit)
   - Export important sessions before clearing
   - Review threat analyzer regularly

4. **Professional Workflow:**
   ```
   1. Grant consent (Consent Manager)
   2. Record in terminal (KEYSTRO CLI)
   3. Analyze in GUI (Session Viewer)
   4. Export data (Data Exporter)
   5. Review threats (Threat Analyzer)
   6. Monitor storage (Statistics)
   ```

---

## 🎯 Summary

**Terminal Interface:**
- ✅ Real-time keystroke capture
- ✅ Threat detection with red boxes
- ✅ Interactive menu system
- ✅ Professional ASCII branding

**GUI Dashboard:**
- ✅ 5 professional tools
- ✅ WPM/CPM calculation (NEW!)
- ✅ Error analysis (NEW!)
- ✅ JSON/TXT export (NEW!)
- ✅ Fixed: Tools stay open properly
- ✅ Consent management
- ✅ Statistics monitoring

**Project is now FULLY FUNCTIONAL with all requested features!** 🎉

---

**Need help?** Check the README.md or PROJECT_STATUS.md for more details.
