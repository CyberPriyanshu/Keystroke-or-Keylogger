"""
Quick verification script to check if everything is set up correctly
Run this BEFORE running the main application
"""

import sys
import os

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version OK:", f"{version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print("❌ Python version too old. Need 3.8+, you have:", f"{version.major}.{version.minor}.{version.micro}")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required = {
        'cryptography': 'Encryption library',
        'win32gui': 'Windows API (pywin32)',
        'psutil': 'Process information',
        'tkinter': 'GUI library',
    }
    
    missing = []
    for module, description in required.items():
        try:
            if module == 'win32gui':
                import win32gui
            elif module == 'tkinter':
                import tkinter
            else:
                __import__(module)
            print(f"✅ {description} ({module}) installed")
        except ImportError:
            print(f"❌ {description} ({module}) NOT installed")
            missing.append(module)
    
    return len(missing) == 0, missing

def check_platform():
    """Check if running on Windows"""
    import platform
    if platform.system() == 'Windows':
        print("✅ Platform: Windows")
        return True
    else:
        print("⚠️  Platform:", platform.system(), "- This tool is designed for Windows")
        return False

def check_directories():
    """Check project structure"""
    base_dir = os.path.dirname(__file__)
    required_dirs = ['src', 'tests']
    required_files = [
        'main.py',
        'requirements.txt',
        'README.md',
        'ETHICAL_AGREEMENT.md',
        'INSTALLATION.md',
        'src/config.py',
        'src/consent_manager.py',
        'src/activity_logger.py',
        'src/storage.py',
        'src/dashboard.py',
    ]
    
    all_ok = True
    for dirname in required_dirs:
        path = os.path.join(base_dir, dirname)
        if os.path.isdir(path):
            print(f"✅ Directory exists: {dirname}/")
        else:
            print(f"❌ Directory missing: {dirname}/")
            all_ok = False
    
    for filename in required_files:
        path = os.path.join(base_dir, filename)
        if os.path.isfile(path):
            print(f"✅ File exists: {filename}")
        else:
            print(f"❌ File missing: {filename}")
            all_ok = False
    
    return all_ok

def main():
    print("=" * 70)
    print("🔍 Pre-Flight Check - Consent-Based Activity Logger (CAL)")
    print("=" * 70)
    print()
    
    checks_passed = 0
    total_checks = 4
    
    # Check 1: Python version
    print("📋 Check 1: Python Version")
    if check_python_version():
        checks_passed += 1
    print()
    
    # Check 2: Dependencies
    print("📋 Check 2: Dependencies")
    deps_ok, missing = check_dependencies()
    if deps_ok:
        checks_passed += 1
    else:
        print()
        print("⚠️  Missing dependencies detected!")
        print("   Install them with: pip install -r requirements.txt")
    print()
    
    # Check 3: Platform
    print("📋 Check 3: Operating System")
    if check_platform():
        checks_passed += 1
    print()
    
    # Check 4: Project structure
    print("📋 Check 4: Project Files")
    if check_directories():
        checks_passed += 1
    print()
    
    # Summary
    print("=" * 70)
    print(f"📊 Results: {checks_passed}/{total_checks} checks passed")
    print("=" * 70)
    
    if checks_passed == total_checks:
        print("✅ All checks passed! You're ready to run: python main.py")
        return 0
    else:
        print("❌ Some checks failed. Please fix the issues above before running.")
        print()
        print("Common fixes:")
        print("  • Install dependencies: pip install -r requirements.txt")
        print("  • Make sure you're in the project directory")
        print("  • Run on Windows OS (required for Windows API functions)")
        return 1

if __name__ == "__main__":
    sys.exit(main())
