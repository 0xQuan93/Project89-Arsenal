@echo off
echo PROJECT89 REALITY GLITCHER LAUNCHER
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

rem Make sure the Reality Glitcher imports directory exists
if not exist "%CURRENT_DIR%\RealityGlitcher\imports" mkdir "%CURRENT_DIR%\RealityGlitcher\imports"

rem Create a direct launcher for Reality Glitcher
echo import os > "%CURRENT_DIR%\launch_glitcher.py"
echo import sys >> "%CURRENT_DIR%\launch_glitcher.py"
echo import subprocess >> "%CURRENT_DIR%\launch_glitcher.py"
echo. >> "%CURRENT_DIR%\launch_glitcher.py"
echo # Set up the current directory in the Python path >> "%CURRENT_DIR%\launch_glitcher.py"
echo current_dir = r'%CURRENT_DIR:\=\\%' >> "%CURRENT_DIR%\launch_glitcher.py"
echo reality_glitcher_dir = os.path.join(current_dir, 'RealityGlitcher') >> "%CURRENT_DIR%\launch_glitcher.py"
echo. >> "%CURRENT_DIR%\launch_glitcher.py"
echo if current_dir not in sys.path: >> "%CURRENT_DIR%\launch_glitcher.py"
echo     sys.path.insert(0, current_dir) >> "%CURRENT_DIR%\launch_glitcher.py"
echo if reality_glitcher_dir not in sys.path: >> "%CURRENT_DIR%\launch_glitcher.py"
echo     sys.path.insert(0, reality_glitcher_dir) >> "%CURRENT_DIR%\launch_glitcher.py"
echo. >> "%CURRENT_DIR%\launch_glitcher.py"
echo # Print debug info >> "%CURRENT_DIR%\launch_glitcher.py"
echo print(f"Current directory: {current_dir}") >> "%CURRENT_DIR%\launch_glitcher.py"
echo print(f"Reality Glitcher directory: {reality_glitcher_dir}") >> "%CURRENT_DIR%\launch_glitcher.py"
echo print(f"Python path: {sys.path}") >> "%CURRENT_DIR%\launch_glitcher.py"
echo. >> "%CURRENT_DIR%\launch_glitcher.py"
echo # Make sure the imports directory exists >> "%CURRENT_DIR%\launch_glitcher.py"
echo os.makedirs(os.path.join(reality_glitcher_dir, 'imports'), exist_ok=True) >> "%CURRENT_DIR%\launch_glitcher.py"
echo. >> "%CURRENT_DIR%\launch_glitcher.py"
echo # Run Reality Glitcher directly >> "%CURRENT_DIR%\launch_glitcher.py"
echo print("Launching Reality Glitcher...") >> "%CURRENT_DIR%\launch_glitcher.py"
echo os.chdir(reality_glitcher_dir) >> "%CURRENT_DIR%\launch_glitcher.py"
echo reality_glitcher_script = os.path.join(reality_glitcher_dir, 'main.py') >> "%CURRENT_DIR%\launch_glitcher.py"
echo. >> "%CURRENT_DIR%\launch_glitcher.py"
echo # Check if the script exists >> "%CURRENT_DIR%\launch_glitcher.py"
echo if os.path.exists(reality_glitcher_script): >> "%CURRENT_DIR%\launch_glitcher.py"
echo     print(f"Found Reality Glitcher main script at: {reality_glitcher_script}") >> "%CURRENT_DIR%\launch_glitcher.py"
echo     # First try dynamic import >> "%CURRENT_DIR%\launch_glitcher.py"
echo     try: >> "%CURRENT_DIR%\launch_glitcher.py"
echo         print("Trying to import the Reality Glitcher module...") >> "%CURRENT_DIR%\launch_glitcher.py"
echo         import importlib.util >> "%CURRENT_DIR%\launch_glitcher.py"
echo         spec = importlib.util.spec_from_file_location("reality_glitcher_main", reality_glitcher_script) >> "%CURRENT_DIR%\launch_glitcher.py"
echo         glitcher_module = importlib.util.module_from_spec(spec) >> "%CURRENT_DIR%\launch_glitcher.py"
echo         sys.modules["reality_glitcher_main"] = glitcher_module >> "%CURRENT_DIR%\launch_glitcher.py"
echo         spec.loader.exec_module(glitcher_module) >> "%CURRENT_DIR%\launch_glitcher.py"
echo         print("Successfully imported Reality Glitcher module") >> "%CURRENT_DIR%\launch_glitcher.py"
echo         # If there's a main function, call it >> "%CURRENT_DIR%\launch_glitcher.py"
echo         if hasattr(glitcher_module, 'main'): >> "%CURRENT_DIR%\launch_glitcher.py"
echo             print("Calling main() function") >> "%CURRENT_DIR%\launch_glitcher.py"
echo             glitcher_module.main() >> "%CURRENT_DIR%\launch_glitcher.py"
echo         else: >> "%CURRENT_DIR%\launch_glitcher.py"
echo             print("No main() function found, trying direct execution as fallback") >> "%CURRENT_DIR%\launch_glitcher.py"
echo             exec(open(reality_glitcher_script).read()) >> "%CURRENT_DIR%\launch_glitcher.py"
echo     except Exception as e: >> "%CURRENT_DIR%\launch_glitcher.py"
echo         print(f"Error importing Reality Glitcher: {e}") >> "%CURRENT_DIR%\launch_glitcher.py"
echo         print("Falling back to subprocess approach") >> "%CURRENT_DIR%\launch_glitcher.py"
echo         # Fallback to running via subprocess >> "%CURRENT_DIR%\launch_glitcher.py"
echo         subprocess.run([sys.executable, reality_glitcher_script]) >> "%CURRENT_DIR%\launch_glitcher.py"
echo else: >> "%CURRENT_DIR%\launch_glitcher.py"
echo     print(f"ERROR: Reality Glitcher main script not found at: {reality_glitcher_script}") >> "%CURRENT_DIR%\launch_glitcher.py"
echo     # Try to find main.py somewhere in the RealityGlitcher directory >> "%CURRENT_DIR%\launch_glitcher.py"
echo     for root, dirs, files in os.walk(reality_glitcher_dir): >> "%CURRENT_DIR%\launch_glitcher.py"
echo         if 'main.py' in files: >> "%CURRENT_DIR%\launch_glitcher.py"
echo             found_script = os.path.join(root, 'main.py') >> "%CURRENT_DIR%\launch_glitcher.py"
echo             print(f"Found alternative main.py at: {found_script}") >> "%CURRENT_DIR%\launch_glitcher.py"
echo             os.chdir(root) >> "%CURRENT_DIR%\launch_glitcher.py"
echo             subprocess.run([sys.executable, found_script]) >> "%CURRENT_DIR%\launch_glitcher.py"
echo             break >> "%CURRENT_DIR%\launch_glitcher.py"
echo     else: >> "%CURRENT_DIR%\launch_glitcher.py"
echo         print("Could not find any main.py file in the RealityGlitcher directory!") >> "%CURRENT_DIR%\launch_glitcher.py"

echo.
echo Launching Reality Glitcher...
python "%CURRENT_DIR%\launch_glitcher.py"

echo.
echo Reality Glitcher closed.
pause 