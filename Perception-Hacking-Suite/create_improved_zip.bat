@echo off
echo PROJECT89 IMPROVED ZIP PACKAGE CREATOR
echo ==============================================
echo This script creates an improved ZIP package with better launchers
echo for the Reality Glitcher UI.
echo.

rem Check if PowerShell is available for creating ZIP
powershell -Command "Write-Host 'PowerShell is available.'" >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ERROR: PowerShell is not available. Cannot create ZIP file.
    pause
    exit /b 1
)

rem Create exclude patterns file first
echo Creating exclude patterns...
echo user_data > exclude_patterns.txt
echo __pycache__ >> exclude_patterns.txt
echo *.pyc >> exclude_patterns.txt
echo .git >> exclude_patterns.txt
echo .gitignore >> exclude_patterns.txt
echo *.log >> exclude_patterns.txt
echo *.tmp >> exclude_patterns.txt
echo *.bak >> exclude_patterns.txt
echo node_modules >> exclude_patterns.txt
echo .env >> exclude_patterns.txt
echo .env.local >> exclude_patterns.txt
echo .DS_Store >> exclude_patterns.txt

rem Clean up any existing package directory
if exist "improved_zip" (
    echo Cleaning up existing package directory...
    rmdir /s /q "improved_zip"
)

rem Create fresh output directory structure
echo Creating fresh directory structure...
mkdir "improved_zip"
mkdir "improved_zip\MindMirror"
mkdir "improved_zip\MindMirror\user_data"
mkdir "improved_zip\MindMirror\user_data\journal"
mkdir "improved_zip\MindMirror\resources"
mkdir "improved_zip\MindMirror\resources\journal"
mkdir "improved_zip\RealityGlitcher"
mkdir "improved_zip\RealityGlitcher\imports"
mkdir "improved_zip\RealityGlitcher\reality-glitcher-ui"
mkdir "improved_zip\RealityGlitcher\reality-glitcher-ui\build"

rem Copy core files to the package directory
echo Copying core files to package directory...
copy combined_app.py improved_zip\
copy combined_requirements.txt improved_zip\

rem Copy the improved launcher scripts
copy fixed_zip_launcher.bat improved_zip\Run-P89-Suite.bat
copy launch_reality_glitcher.bat improved_zip\Launch-Reality-Glitcher.bat

echo Copying MindMirror files...
rem Copy MindMirror files excluding user data and cache
xcopy /E /I /Y MindMirror\*.py improved_zip\MindMirror\
xcopy /E /I /Y MindMirror\resources\*.* improved_zip\MindMirror\resources\ /EXCLUDE:exclude_patterns.txt

echo Copying RealityGlitcher files...
rem Copy RealityGlitcher files excluding cache and temporary files
xcopy /E /I /Y RealityGlitcher\*.py improved_zip\RealityGlitcher\
xcopy /E /I /Y RealityGlitcher\resources\*.* improved_zip\RealityGlitcher\resources\ /EXCLUDE:exclude_patterns.txt

echo Copying Reality Glitcher UI files...
rem Copy the built UI files
if exist "RealityGlitcher\reality-glitcher-ui\build" (
    xcopy /E /I /Y RealityGlitcher\reality-glitcher-ui\build\*.* improved_zip\RealityGlitcher\reality-glitcher-ui\build\ /EXCLUDE:exclude_patterns.txt
) else (
    echo WARNING: Reality Glitcher UI build files not found. UI will not be included.
)

rem Create README file
echo Creating README file...
echo # PROJECT89 PERCEPTION-HACKING SUITE > improved_zip\README.txt
echo. >> improved_zip\README.txt
echo ## Requirements >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo - Python 3.8 or higher must be installed >> improved_zip\README.txt
echo - Python must be in your system PATH >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo ## Running the Applications >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo There are two launcher scripts available: >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo 1. Run-P89-Suite.bat - Launches the combined suite with both Mind Mirror and Reality Glitcher >> improved_zip\README.txt
echo 2. Launch-Reality-Glitcher.bat - Directly launches just the Reality Glitcher component >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo If you're having issues with the Reality Glitcher UI not appearing when using the combined suite, >> improved_zip\README.txt
echo try using the dedicated Reality Glitcher launcher instead. >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo The first time you run either script, it will install all required dependencies. >> improved_zip\README.txt
echo This may take a few moments. >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo ## Troubleshooting >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo If you encounter any issues: >> improved_zip\README.txt
echo. >> improved_zip\README.txt
echo 1. Ensure Python 3.8+ is installed >> improved_zip\README.txt
echo 2. Make sure Python is in your system PATH >> improved_zip\README.txt
echo 3. Try running the dedicated Reality Glitcher launcher if the UI doesn't appear in the combined suite >> improved_zip\README.txt
echo 4. Check the output of the launcher for any error messages >> improved_zip\README.txt
echo 5. If all else fails, try running these commands manually in a terminal: >> improved_zip\README.txt
echo    python -m pip install -r combined_requirements.txt >> improved_zip\README.txt
echo    python combined_app.py  # For the combined suite >> improved_zip\README.txt
echo    cd RealityGlitcher && python main.py  # For just the Reality Glitcher >> improved_zip\README.txt

rem Create the ZIP file
echo Creating ZIP file...
cd improved_zip
powershell -NoProfile -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('.', '..\PROJECT89-Perception-Hacking-Suite-Improved.zip')"
cd ..

if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to create ZIP file.
    pause
    exit /b 1
)

rem Clean up temporary files
del exclude_patterns.txt

echo.
echo Improved ZIP package created successfully!
echo.
echo You can find the ZIP file at: PROJECT89-Perception-Hacking-Suite-Improved.zip
echo.
echo To distribute this package:
echo 1. Send the ZIP file to users
echo 2. Have them extract all files to a directory
echo 3. Run the "Run-P89-Suite.bat" file for the full suite
echo 4. Or run "Launch-Reality-Glitcher.bat" just for the Reality Glitcher component
echo.
echo NOTE: This approach requires Python to be installed on the user's system.
echo.
pause 