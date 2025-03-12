@echo off
echo PROJECT89 PERCEPTION-HACKING SUITE
echo ==============================
echo.

echo Checking for Python...
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher and ensure it's in your PATH.
    pause
    exit /b 1
)

rem Get the current directory
set CURRENT_DIR=%~dp0
set CURRENT_DIR=%CURRENT_DIR:~0,-1%

echo Current directory: %CURRENT_DIR%

rem Ensure PYTHONPATH includes the current directory for proper imports
set PYTHONPATH=%CURRENT_DIR%;%PYTHONPATH%

echo Installing dependencies. This may take a moment...
python -m pip install -r "%CURRENT_DIR%\combined_requirements.txt"

rem Install specific UI dependencies for Reality Glitcher if needed
echo Installing additional UI dependencies...
python -m pip install pillow tkinter

rem Create a small Python script to check paths and launch the app
echo import os > "%CURRENT_DIR%\check_and_launch.py"
echo import sys >> "%CURRENT_DIR%\check_and_launch.py"
echo import importlib.util >> "%CURRENT_DIR%\check_and_launch.py"
echo. >> "%CURRENT_DIR%\check_and_launch.py"
echo # Set up the current directory in the Python path >> "%CURRENT_DIR%\check_and_launch.py"
echo current_dir = r'%CURRENT_DIR:\=\\%' >> "%CURRENT_DIR%\check_and_launch.py"
echo if current_dir not in sys.path: >> "%CURRENT_DIR%\check_and_launch.py"
echo     sys.path.insert(0, current_dir) >> "%CURRENT_DIR%\check_and_launch.py"
echo. >> "%CURRENT_DIR%\check_and_launch.py"
echo # Print debugging information >> "%CURRENT_DIR%\check_and_launch.py"
echo print(f"Current directory: {current_dir}") >> "%CURRENT_DIR%\check_and_launch.py"
echo print(f"Python path: {sys.path}") >> "%CURRENT_DIR%\check_and_launch.py"
echo. >> "%CURRENT_DIR%\check_and_launch.py"
echo # Check if RealityGlitcher directory exists >> "%CURRENT_DIR%\check_and_launch.py"
echo reality_glitcher_path = os.path.join(current_dir, 'RealityGlitcher') >> "%CURRENT_DIR%\check_and_launch.py"
echo print(f"Reality Glitcher path: {reality_glitcher_path}") >> "%CURRENT_DIR%\check_and_launch.py"
echo if os.path.exists(reality_glitcher_path): >> "%CURRENT_DIR%\check_and_launch.py"
echo     print("Reality Glitcher directory found") >> "%CURRENT_DIR%\check_and_launch.py"
echo else: >> "%CURRENT_DIR%\check_and_launch.py"
echo     print("ERROR: Reality Glitcher directory not found!") >> "%CURRENT_DIR%\check_and_launch.py"
echo. >> "%CURRENT_DIR%\check_and_launch.py"
echo # Check if MindMirror directory exists >> "%CURRENT_DIR%\check_and_launch.py"
echo mind_mirror_path = os.path.join(current_dir, 'MindMirror') >> "%CURRENT_DIR%\check_and_launch.py"
echo print(f"Mind Mirror path: {mind_mirror_path}") >> "%CURRENT_DIR%\check_and_launch.py"
echo if os.path.exists(mind_mirror_path): >> "%CURRENT_DIR%\check_and_launch.py"
echo     print("Mind Mirror directory found") >> "%CURRENT_DIR%\check_and_launch.py"
echo else: >> "%CURRENT_DIR%\check_and_launch.py"
echo     print("ERROR: Mind Mirror directory not found!") >> "%CURRENT_DIR%\check_and_launch.py"
echo. >> "%CURRENT_DIR%\check_and_launch.py"
echo # Create necessary directories if they don't exist >> "%CURRENT_DIR%\check_and_launch.py"
echo os.makedirs(os.path.join(mind_mirror_path, 'user_data'), exist_ok=True) >> "%CURRENT_DIR%\check_and_launch.py"
echo os.makedirs(os.path.join(reality_glitcher_path, 'imports'), exist_ok=True) >> "%CURRENT_DIR%\check_and_launch.py"
echo. >> "%CURRENT_DIR%\check_and_launch.py"
echo # Now import and run the combined app >> "%CURRENT_DIR%\check_and_launch.py"
echo print("Launching the application...") >> "%CURRENT_DIR%\check_and_launch.py"
echo combined_app_path = os.path.join(current_dir, 'combined_app.py') >> "%CURRENT_DIR%\check_and_launch.py"
echo spec = importlib.util.spec_from_file_location("combined_app", combined_app_path) >> "%CURRENT_DIR%\check_and_launch.py"
echo app_module = importlib.util.module_from_spec(spec) >> "%CURRENT_DIR%\check_and_launch.py"
echo sys.modules["combined_app"] = app_module >> "%CURRENT_DIR%\check_and_launch.py"
echo spec.loader.exec_module(app_module) >> "%CURRENT_DIR%\check_and_launch.py"
echo print("Application module loaded") >> "%CURRENT_DIR%\check_and_launch.py"
echo. >> "%CURRENT_DIR%\check_and_launch.py"
echo # Call the main function to start the app >> "%CURRENT_DIR%\check_and_launch.py"
echo if hasattr(app_module, 'main'): >> "%CURRENT_DIR%\check_and_launch.py"
echo     print("Calling main() function") >> "%CURRENT_DIR%\check_and_launch.py"
echo     app_module.main() >> "%CURRENT_DIR%\check_and_launch.py"
echo else: >> "%CURRENT_DIR%\check_and_launch.py"
echo     print("ERROR: No main() function found in combined_app.py") >> "%CURRENT_DIR%\check_and_launch.py"

echo.
echo Launching Perception-Hacking Suite...
python "%CURRENT_DIR%\check_and_launch.py"

echo.
echo Application closed.
pause 