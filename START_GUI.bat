@echo off
echo.
echo ================================================
echo    KEYSTRO - GUI Dashboard
echo    Educational Keystroke Analysis Tool
echo ================================================
echo.
echo Starting GUI...
echo.
py keystro_gui.py
if errorlevel 1 (
    echo.
    echo ERROR: Failed to start GUI
    echo Make sure Python and required packages are installed
    echo Run: pip install -r requirements.txt
    echo.
    pause
)
