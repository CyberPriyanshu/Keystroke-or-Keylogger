"""
KEYSTRO - Tools-Based GUI Dashboard
Educational Keystroke Analysis Tool with Security Features
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import os
import sys
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from storage import SecureStorage
from consent_manager import ConsentManager
import config as Config

class EducationalAgreementDialog:
    """Prominent Educational Use Agreement Dialog"""
    
    def __init__(self, parent):
        self.accepted = False
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("⚠️ EDUCATIONAL USE AGREEMENT - REQUIRED ⚠️")
        self.dialog.geometry("800x700")
        self.dialog.configure(bg='#1a1a1a')
        self.dialog.resizable(False, False)
        
        # Make dialog modal
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center on screen
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (700 // 2)
        self.dialog.geometry(f"800x700+{x}+{y}")
        
        self.create_agreement_ui()
        
    def create_agreement_ui(self):
        """Create the agreement interface"""
        
        # Warning header with red background
        header_frame = tk.Frame(self.dialog, bg='#cc0000', height=80)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        warning_icon = tk.Label(
            header_frame, 
            text="⚠️", 
            font=("Arial", 36, "bold"),
            bg='#cc0000',
            fg='white'
        )
        warning_icon.pack(pady=10)
        
        title_label = tk.Label(
            header_frame,
            text="EDUCATIONAL USE AGREEMENT",
            font=("Arial", 18, "bold"),
            bg='#cc0000',
            fg='white'
        )
        title_label.pack()
        
        # Main content area
        content_frame = tk.Frame(self.dialog, bg='#2a2a2a')
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Scrolled text for agreement
        agreement_text = scrolledtext.ScrolledText(
            content_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg='#1a1a1a',
            fg='#ffffff',
            insertbackground='white',
            relief='solid',
            borderwidth=2,
            padx=15,
            pady=15
        )
        agreement_text.pack(fill='both', expand=True, pady=(0, 15))
        
        # Agreement content with highlighted sections
        agreement_content = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                    KEYSTRO EDUCATIONAL USE AGREEMENT                      ║
║                         READ CAREFULLY BEFORE USE                         ║
╚═══════════════════════════════════════════════════════════════════════════╝

IMPORTANT LEGAL NOTICE:

This software (KEYSTRO) is designed EXCLUSIVELY for:

    ✓ Educational purposes in controlled environments
    ✓ Security research with proper authorization
    ✓ Personal monitoring of YOUR OWN devices only
    ✓ Academic study of cybersecurity concepts

═══════════════════════════════════════════════════════════════════════════

⚠️ PROHIBITED USES (ILLEGAL - DO NOT PROCEED IF INTENDED):

    ✗ Monitoring other people's devices without explicit consent
    ✗ Capturing passwords, credit cards, or sensitive data from others
    ✗ Installing on shared computers without authorization
    ✗ Any use that violates privacy laws or regulations
    ✗ Commercial surveillance or data harvesting
    ✗ Malicious activities of any kind

═══════════════════════════════════════════════════════════════════════════

LEGAL CONSEQUENCES OF MISUSE:

Unauthorized use of keystroke logging software may result in:
    • Criminal charges under computer fraud and abuse laws
    • Civil lawsuits for privacy violations
    • Substantial fines and imprisonment
    • Permanent criminal record

═══════════════════════════════════════════════════════════════════════════

YOUR RESPONSIBILITIES:

By clicking "I ACCEPT", you acknowledge and agree that:

1. You will use this software ONLY for legitimate educational purposes
2. You have legal authorization for any monitoring you perform
3. You will NOT use this tool to violate anyone's privacy
4. You understand the legal consequences of misuse
5. You accept FULL RESPONSIBILITY for your actions
6. The developers are NOT LIABLE for any misuse of this software

═══════════════════════════════════════════════════════════════════════════

CONSENT REQUIREMENT:

This tool includes a consent mechanism that MUST be used when monitoring
devices. Bypassing or disabling consent features is a violation of this
agreement and may be illegal.

═══════════════════════════════════════════════════════════════════════════

YOUR SIGNATURE:

By proceeding, you are digitally signing this agreement and confirming that
you have read, understood, and will comply with all terms above.

Timestamp: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """

═══════════════════════════════════════════════════════════════════════════
"""
        
        agreement_text.insert('1.0', agreement_content)
        
        # Highlight critical sections in yellow
        agreement_text.tag_config('highlight', background='#ffeb3b', foreground='#000000')
        
        # Highlight specific phrases
        highlights = [
            "EDUCATIONAL USE AGREEMENT",
            "READ CAREFULLY BEFORE USE",
            "PROHIBITED USES",
            "LEGAL CONSEQUENCES OF MISUSE",
            "YOUR RESPONSIBILITIES",
            "CONSENT REQUIREMENT",
            "EXCLUSIVELY for",
            "ILLEGAL",
            "Criminal charges",
            "FULL RESPONSIBILITY",
            "NOT LIABLE",
            "may be illegal"
        ]
        
        for phrase in highlights:
            start = '1.0'
            while True:
                start = agreement_text.search(phrase, start, stopindex='end')
                if not start:
                    break
                end = f"{start}+{len(phrase)}c"
                agreement_text.tag_add('highlight', start, end)
                start = end
        
        agreement_text.config(state='disabled')
        
        # Checkbox for confirmation
        self.confirm_var = tk.BooleanVar(value=False)
        confirm_check = tk.Checkbutton(
            content_frame,
            text="I have read and understand this agreement",
            variable=self.confirm_var,
            font=("Arial", 11, "bold"),
            bg='#2a2a2a',
            fg='white',
            selectcolor='#1a1a1a',
            activebackground='#2a2a2a',
            activeforeground='white',
            command=self.on_checkbox_change
        )
        confirm_check.pack(pady=(0, 10))
        
        # Buttons frame
        button_frame = tk.Frame(content_frame, bg='#2a2a2a')
        button_frame.pack(fill='x')
        
        # Decline button (always enabled)
        decline_btn = tk.Button(
            button_frame,
            text="✗ DECLINE",
            font=("Arial", 12, "bold"),
            bg='#cc0000',
            fg='white',
            activebackground='#aa0000',
            activeforeground='white',
            width=20,
            height=2,
            command=self.on_decline,
            relief='raised',
            borderwidth=3
        )
        decline_btn.pack(side='left', padx=(0, 10))
        
        # Accept button (disabled initially)
        self.accept_btn = tk.Button(
            button_frame,
            text="✓ I ACCEPT - PROCEED",
            font=("Arial", 12, "bold"),
            bg='#555555',
            fg='#888888',
            width=25,
            height=2,
            command=self.on_accept,
            state='disabled',
            relief='raised',
            borderwidth=3
        )
        self.accept_btn.pack(side='right')
        
        # Protocol for window close
        self.dialog.protocol("WM_DELETE_WINDOW", self.on_decline)
        
    def on_checkbox_change(self):
        """Enable/disable accept button based on checkbox"""
        if self.confirm_var.get():
            self.accept_btn.config(
                bg='#00cc00',
                fg='white',
                state='normal',
                activebackground='#00aa00',
                activeforeground='white'
            )
        else:
            self.accept_btn.config(
                bg='#555555',
                fg='#888888',
                state='disabled'
            )
    
    def on_accept(self):
        """Handle acceptance"""
        self.accepted = True
        self.dialog.destroy()
    
    def on_decline(self):
        """Handle decline"""
        self.accepted = False
        self.dialog.destroy()


class KeystroTool:
    """Base class for KEYSTRO tools"""
    
    def __init__(self, name, description, icon):
        self.name = name
        self.description = description
        self.icon = icon
        self.window = None
        
    def launch(self, parent):
        """Launch the tool window"""
        if self.window and tk.Toplevel.winfo_exists(self.window):
            self.window.lift()
            return
        
        self.window = tk.Toplevel(parent)
        self.window.title(f"{self.icon} {self.name}")
        self.window.geometry("900x650")
        self.window.configure(bg='#1a1a1a')
        
        self.setup_ui()
    
    def setup_ui(self):
        """Override in subclass"""
        pass


class SessionViewerTool(KeystroTool):
    """View recorded keystroke sessions"""
    
    def __init__(self):
        super().__init__(
            "Session Viewer",
            "View and analyze recorded keystroke sessions",
            "📊"
        )
        self.storage = SecureStorage()
        
    def setup_ui(self):
        # Header
        header = tk.Label(
            self.window,
            text=f"{self.icon} {self.name}",
            font=("Arial", 18, "bold"),
            bg='#1a1a1a',
            fg='#00ffff'
        )
        header.pack(pady=15)
        
        # Control frame
        control_frame = tk.Frame(self.window, bg='#1a1a1a')
        control_frame.pack(fill='x', padx=20, pady=10)
        
        refresh_btn = tk.Button(
            control_frame,
            text="🔄 Refresh",
            font=("Arial", 11, "bold"),
            bg='#0066cc',
            fg='white',
            command=self.load_sessions,
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=5
        )
        refresh_btn.pack(side='left', padx=5)
        
        clear_btn = tk.Button(
            control_frame,
            text="🗑️ Clear All",
            font=("Arial", 11, "bold"),
            bg='#cc0000',
            fg='white',
            command=self.clear_all,
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=5
        )
        clear_btn.pack(side='left', padx=5)
        
        # Session display
        display_frame = tk.Frame(self.window, bg='#1a1a1a')
        display_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.session_text = scrolledtext.ScrolledText(
            display_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg='#0a0a0a',
            fg='#00ff00',
            insertbackground='white',
            relief='solid',
            borderwidth=2,
            padx=10,
            pady=10
        )
        self.session_text.pack(fill='both', expand=True)
        
        # Load initial data
        self.load_sessions()
        
    def load_sessions(self):
        """Load and display sessions"""
        self.session_text.delete('1.0', tk.END)
        
        logs = self.storage.get_logs()
        
        if not logs:
            self.session_text.insert('1.0', "No sessions recorded yet.\n\nStart recording in the terminal to see data here.")
            return
        
        output = "═══════════════════════════════════════════════════════════\n"
        output += f"  KEYSTROKE SESSIONS - {len(logs)} entries\n"
        output += "═══════════════════════════════════════════════════════════\n\n"
        
        for i, log in enumerate(logs, 1):
            output += f"[{i}] {log.get('timestamp', 'N/A')}\n"
            output += f"    App: {log.get('app_name', 'N/A')}\n"
            output += f"    Window: {log.get('window_title', 'N/A')}\n"
            output += f"    Duration: {log.get('duration', 0)}s\n"
            output += "\n"
        
        self.session_text.insert('1.0', output)
        
    def clear_all(self):
        """Clear all sessions"""
        if messagebox.askyesno("Confirm", "Delete all recorded sessions?"):
            self.storage.delete_all_logs()
            self.load_sessions()
            messagebox.showinfo("Success", "All sessions cleared.")


class ThreatAnalyzerTool(KeystroTool):
    """Analyze threats in recorded data"""
    
    def __init__(self):
        super().__init__(
            "Threat Analyzer",
            "Analyze and view detected threats",
            "🔍"
        )
        self.storage = SecureStorage()
        
    def setup_ui(self):
        # Header
        header = tk.Label(
            self.window,
            text=f"{self.icon} {self.name}",
            font=("Arial", 18, "bold"),
            bg='#1a1a1a',
            fg='#ff3333'
        )
        header.pack(pady=15)
        
        # Stats frame
        stats_frame = tk.Frame(self.window, bg='#2a2a2a', relief='solid', borderwidth=2)
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        self.total_label = tk.Label(
            stats_frame,
            text="Total Threats: 0",
            font=("Arial", 12, "bold"),
            bg='#2a2a2a',
            fg='#ff3333'
        )
        self.total_label.pack(pady=10)
        
        # Threat display
        display_frame = tk.Frame(self.window, bg='#1a1a1a')
        display_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.threat_text = scrolledtext.ScrolledText(
            display_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg='#0a0a0a',
            fg='#ff6666',
            insertbackground='white',
            relief='solid',
            borderwidth=2,
            padx=10,
            pady=10
        )
        self.threat_text.pack(fill='both', expand=True)
        
        # Refresh button
        refresh_btn = tk.Button(
            self.window,
            text="🔄 Refresh Analysis",
            font=("Arial", 11, "bold"),
            bg='#cc0000',
            fg='white',
            command=self.analyze_threats,
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8
        )
        refresh_btn.pack(pady=15)
        
        # Load initial analysis
        self.analyze_threats()
        
    def analyze_threats(self):
        """Analyze and display threats"""
        self.threat_text.delete('1.0', tk.END)
        
        logs = self.storage.get_logs()
        # For now, show all logs since threat detection is in terminal only
        # In future, can add threat_detected field to storage
        
        self.total_label.config(text=f"Total Sessions: {len(logs)}")
        
        if not logs:
            self.threat_text.insert('1.0', "✓ No sessions recorded yet.\n\nStart recording in the terminal to see data here.")
            return
        
        output = "╔═══════════════════════════════════════════════════════════╗\n"
        output += "║              SESSION ACTIVITY SUMMARY                     ║\n"
        output += "╚═══════════════════════════════════════════════════════════╝\n\n"
        
        # Count by app
        app_counts = {}
        for log in logs:
            app = log.get('app_name', 'Unknown')
            app_counts[app] = app_counts.get(app, 0) + 1
        
        output += "Sessions by Application:\n"
        for app, count in app_counts.items():
            output += f"  • {app}: {count}\n"
        
        output += "\n" + "─" * 60 + "\n\n"
        output += "Note: Threat detection is shown in real-time in the terminal interface.\n"
        output += "Red alert boxes appear when suspicious keywords are detected.\n\n"
        output += "Recent Activity:\n\n"
        
        for i, log in enumerate(logs[:20], 1):  # Show last 20
            output += f"[{i}] {log.get('timestamp', 'N/A')}\n"
            output += f"  App: {log.get('app_name', 'N/A')}\n"
            output += f"  Window: {log.get('window_title', 'N/A')[:60]}...\n"
            output += "\n"
        
        self.threat_text.insert('1.0', output)


class StatisticsTool(KeystroTool):
    """View keystroke statistics"""
    
    def __init__(self):
        super().__init__(
            "Statistics",
            "View keystroke and storage statistics",
            "📈"
        )
        self.storage = SecureStorage()
        
    def setup_ui(self):
        # Header
        header = tk.Label(
            self.window,
            text=f"{self.icon} {self.name}",
            font=("Arial", 18, "bold"),
            bg='#1a1a1a',
            fg='#ffaa00'
        )
        header.pack(pady=15)
        
        # Stats display
        display_frame = tk.Frame(self.window, bg='#1a1a1a')
        display_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.stats_text = scrolledtext.ScrolledText(
            display_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg='#0a0a0a',
            fg='#ffcc00',
            insertbackground='white',
            relief='solid',
            borderwidth=2,
            padx=15,
            pady=15
        )
        self.stats_text.pack(fill='both', expand=True)
        
        # Refresh button
        refresh_btn = tk.Button(
            self.window,
            text="🔄 Refresh Statistics",
            font=("Arial", 11, "bold"),
            bg='#ff8800',
            fg='white',
            command=self.load_statistics,
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8
        )
        refresh_btn.pack(pady=15)
        
        # Load initial stats
        self.load_statistics()
        
    def load_statistics(self):
        """Load and display statistics"""
        self.stats_text.delete('1.0', tk.END)
        
        logs = self.storage.get_logs()
        
        # Calculate storage size
        db_path = self.storage.db_path
        db_size = os.path.getsize(db_path) if os.path.exists(db_path) else 0
        db_size_mb = db_size / (1024 * 1024)
        max_size_mb = 1.0  # 1MB limit (hardcoded in storage.py)
        
        output = "╔═══════════════════════════════════════════════════════════╗\n"
        output += "║                  KEYSTRO STATISTICS                       ║\n"
        output += "╚═══════════════════════════════════════════════════════════╝\n\n"
        
        output += f"Total Sessions Recorded: {len(logs)}\n\n"
        
        output += "─" * 60 + "\n\n"
        
        output += "STORAGE INFORMATION:\n\n"
        output += f"Database Size: {db_size_mb:.2f} MB / {max_size_mb:.0f} MB\n"
        output += f"Usage: {(db_size_mb / max_size_mb) * 100:.1f}%\n"
        output += f"Database Location: {db_path}\n\n"
        
        if db_size_mb > (max_size_mb * 0.8):
            output += "⚠️ WARNING: Approaching storage limit!\n"
            output += "   Oldest entries will be auto-deleted when limit is reached.\n\n"
        
        output += "─" * 60 + "\n\n"
        
        output += "CONSENT STATUS:\n\n"
        consent_mgr = ConsentManager()
        if consent_mgr.has_valid_consent():
            output += "✓ Valid consent recorded\n"
            output += f"  Database: {consent_mgr.db_path}\n"
        else:
            output += "✗ No valid consent found\n"
        
        output += "\n" + "─" * 60 + "\n\n"
        
        output += "SESSION BREAKDOWN:\n\n"
        if logs:
            # Show recent sessions
            recent = logs[:10]
            for i, log in enumerate(recent, 1):
                output += f"{i}. {log.get('timestamp', 'N/A')} - {log.get('app_name', 'N/A')}\n"
        else:
            output += "No sessions recorded yet.\n"
        
        self.stats_text.insert('1.0', output)


class ConsentManagerTool(KeystroTool):
    """Manage consent settings"""
    
    def __init__(self):
        super().__init__(
            "Consent Manager",
            "Manage monitoring consent and permissions",
            "✓"
        )
        self.consent_mgr = ConsentManager()
        
    def setup_ui(self):
        # Header
        header = tk.Label(
            self.window,
            text=f"{self.icon} {self.name}",
            font=("Arial", 18, "bold"),
            bg='#1a1a1a',
            fg='#00cc00'
        )
        header.pack(pady=15)
        
        # Status frame
        status_frame = tk.Frame(self.window, bg='#2a2a2a', relief='solid', borderwidth=2)
        status_frame.pack(fill='x', padx=20, pady=10)
        
        self.status_label = tk.Label(
            status_frame,
            text="",
            font=("Arial", 12, "bold"),
            bg='#2a2a2a',
            fg='white'
        )
        self.status_label.pack(pady=15)
        
        # Info display
        display_frame = tk.Frame(self.window, bg='#1a1a1a')
        display_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.consent_text = scrolledtext.ScrolledText(
            display_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg='#0a0a0a',
            fg='#00ff00',
            insertbackground='white',
            relief='solid',
            borderwidth=2,
            padx=10,
            pady=10
        )
        self.consent_text.pack(fill='both', expand=True)
        
        # Button frame
        button_frame = tk.Frame(self.window, bg='#1a1a1a')
        button_frame.pack(fill='x', padx=20, pady=15)
        
        grant_btn = tk.Button(
            button_frame,
            text="✓ Grant Consent",
            font=("Arial", 11, "bold"),
            bg='#00cc00',
            fg='white',
            command=self.grant_consent,
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=8
        )
        grant_btn.pack(side='left', padx=5)
        
        revoke_btn = tk.Button(
            button_frame,
            text="✗ Revoke Consent",
            font=("Arial", 11, "bold"),
            bg='#cc0000',
            fg='white',
            command=self.revoke_consent,
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=8
        )
        revoke_btn.pack(side='left', padx=5)
        
        refresh_btn = tk.Button(
            button_frame,
            text="🔄 Refresh",
            font=("Arial", 11, "bold"),
            bg='#0066cc',
            fg='white',
            command=self.load_consent_status,
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=8
        )
        refresh_btn.pack(side='left', padx=5)
        
        # Load initial status
        self.load_consent_status()
        
    def load_consent_status(self):
        """Load and display consent status"""
        self.consent_text.delete('1.0', tk.END)
        
        has_consent = self.consent_mgr.has_valid_consent()
        
        if has_consent:
            self.status_label.config(text="✓ CONSENT GRANTED", fg='#00ff00')
            status_text = "ACTIVE"
        else:
            self.status_label.config(text="✗ NO CONSENT", fg='#ff3333')
            status_text = "INACTIVE"
        
        output = "╔═══════════════════════════════════════════════════════════╗\n"
        output += "║                  CONSENT INFORMATION                      ║\n"
        output += "╚═══════════════════════════════════════════════════════════╝\n\n"
        
        output += f"Status: {status_text}\n\n"
        
        if has_consent:
            output += "Monitoring is AUTHORIZED for this device.\n\n"
            output += "Permissions:\n"
            output += "  • Keystroke recording: ENABLED\n"
            output += "  • Threat detection: ENABLED\n"
            output += "  • Data storage: ENABLED\n\n"
        else:
            output += "Monitoring is NOT authorized.\n\n"
            output += "To begin monitoring:\n"
            output += "  1. Click 'Grant Consent' button\n"
            output += "  2. Or run setup_consent.py\n"
            output += "  3. Or accept consent in terminal interface\n\n"
        
        output += "─" * 60 + "\n\n"
        output += "IMPORTANT:\n"
        output += "Consent must be obtained before monitoring any device.\n"
        output += "Monitoring without consent is illegal and unethical.\n"
        
        self.consent_text.insert('1.0', output)
        
    def grant_consent(self):
        """Grant consent"""
        result = messagebox.askyesno(
            "Grant Consent",
            "Do you consent to keystroke monitoring on this device?\n\n"
            "By clicking Yes, you confirm:\n"
            "• This is YOUR device\n"
            "• You have legal authority to monitor it\n"
            "• You understand the EDUCATIONAL USE AGREEMENT"
        )
        
        if result:
            self.consent_mgr.record_consent(
                scopes=['keystrokes'],
                signature=f"GUI User {datetime.now().strftime('%Y%m%d_%H%M%S')}"
            )
            messagebox.showinfo("Success", "Consent granted successfully!")
            self.load_consent_status()
        
    def revoke_consent(self):
        """Revoke consent"""
        result = messagebox.askyesno(
            "Revoke Consent",
            "Are you sure you want to revoke consent?\n\n"
            "This will prevent all monitoring activities."
        )
        
        if result:
            self.consent_mgr.revoke_consent()
            messagebox.showinfo("Success", "Consent revoked successfully!")
            self.load_consent_status()


class KeystroGUI:
    """Main KEYSTRO GUI Application"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("KEYSTRO - Educational Keystroke Analysis Tool")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a1a')
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1000 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"1000x700+{x}+{y}")
        
        # Initialize tools
        self.tools = [
            SessionViewerTool(),
            ThreatAnalyzerTool(),
            StatisticsTool(),
            ConsentManagerTool()
        ]
        
        # Show agreement first
        if not self.show_agreement():
            self.root.destroy()
            sys.exit(0)
        
        self.setup_ui()
        
    def show_agreement(self):
        """Show educational use agreement"""
        dialog = EducationalAgreementDialog(self.root)
        self.root.wait_window(dialog.dialog)
        
        if not dialog.accepted:
            messagebox.showwarning(
                "Agreement Required",
                "You must accept the Educational Use Agreement to use KEYSTRO."
            )
            return False
        
        # Record acceptance
        consent_mgr = ConsentManager()
        consent_mgr.record_consent(
            scopes=['gui_access'],
            signature=f"GUI Agreement {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        
        return True
        
    def setup_ui(self):
        """Setup main UI"""
        
        # Header with logo
        header_frame = tk.Frame(self.root, bg='#0a0a0a', height=120)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        logo_label = tk.Label(
            header_frame,
            text="KEYSTRO",
            font=("Courier New", 36, "bold"),
            bg='#0a0a0a',
            fg='#ffcc00'
        )
        logo_label.pack(pady=15)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Educational Keystroke Analysis Dashboard",
            font=("Arial", 12),
            bg='#0a0a0a',
            fg='#00ffff'
        )
        subtitle_label.pack()
        
        # Warning banner
        warning_frame = tk.Frame(self.root, bg='#cc0000', height=40)
        warning_frame.pack(fill='x')
        warning_frame.pack_propagate(False)
        
        warning_label = tk.Label(
            warning_frame,
            text="⚠️ EDUCATIONAL USE ONLY - Authorized Monitoring Required ⚠️",
            font=("Arial", 11, "bold"),
            bg='#cc0000',
            fg='white'
        )
        warning_label.pack(pady=8)
        
        # Main content
        content_frame = tk.Frame(self.root, bg='#1a1a1a')
        content_frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        info_label = tk.Label(
            content_frame,
            text="Select a tool to begin:",
            font=("Arial", 14, "bold"),
            bg='#1a1a1a',
            fg='white'
        )
        info_label.pack(pady=(0, 20))
        
        # Tools grid
        tools_frame = tk.Frame(content_frame, bg='#1a1a1a')
        tools_frame.pack(expand=True)
        
        for i, tool in enumerate(self.tools):
            row = i // 2
            col = i % 2
            
            tool_card = self.create_tool_card(tools_frame, tool)
            tool_card.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        
        # Configure grid weights
        for i in range(2):
            tools_frame.grid_rowconfigure(i, weight=1)
            tools_frame.grid_columnconfigure(i, weight=1)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg='#0a0a0a', height=50)
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="Terminal Interface: Run keylogger_terminal.py or START_KEYSTRO.bat",
            font=("Arial", 9),
            bg='#0a0a0a',
            fg='#888888'
        )
        footer_label.pack(pady=15)
        
    def create_tool_card(self, parent, tool):
        """Create a tool card button"""
        card = tk.Frame(
            parent,
            bg='#2a2a2a',
            relief='raised',
            borderwidth=3,
            width=350,
            height=150
        )
        card.pack_propagate(False)
        
        # Icon
        icon_label = tk.Label(
            card,
            text=tool.icon,
            font=("Arial", 48),
            bg='#2a2a2a',
            fg='white'
        )
        icon_label.pack(pady=(15, 5))
        
        # Name
        name_label = tk.Label(
            card,
            text=tool.name,
            font=("Arial", 14, "bold"),
            bg='#2a2a2a',
            fg='white'
        )
        name_label.pack()
        
        # Description
        desc_label = tk.Label(
            card,
            text=tool.description,
            font=("Arial", 9),
            bg='#2a2a2a',
            fg='#aaaaaa',
            wraplength=300
        )
        desc_label.pack(pady=5)
        
        # Make entire card clickable
        def on_enter(e):
            card.config(bg='#3a3a3a', borderwidth=4)
            icon_label.config(bg='#3a3a3a')
            name_label.config(bg='#3a3a3a')
            desc_label.config(bg='#3a3a3a')
        
        def on_leave(e):
            card.config(bg='#2a2a2a', borderwidth=3)
            icon_label.config(bg='#2a2a2a')
            name_label.config(bg='#2a2a2a')
            desc_label.config(bg='#2a2a2a')
        
        def on_click(e):
            tool.launch(self.root)
        
        for widget in [card, icon_label, name_label, desc_label]:
            widget.bind('<Enter>', on_enter)
            widget.bind('<Leave>', on_leave)
            widget.bind('<Button-1>', on_click)
        
        return card
        
    def run(self):
        """Run the application"""
        self.root.mainloop()


if __name__ == '__main__':
    app = KeystroGUI()
    app.run()
