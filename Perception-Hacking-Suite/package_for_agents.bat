@echo off
setlocal enabledelayedexpansion

echo ===================================
echo PROJECT 89 AGENT ARSENAL PACKAGER
echo ===================================
echo.
echo This script will package the MindMirror and RealityGlitcher
echo applications into a distribution package for Project 89 agents.
echo.

:: Set the base paths
set "CURRENT_DIR=%~dp0"
set "DIST_DIR=%CURRENT_DIR%agent_distribution"
set "MM_DIR=%CURRENT_DIR%MindMirror"
set "RG_DIR=%CURRENT_DIR%RealityGlitcher"

:: Create timestamp for the zip file
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "TIMESTAMP=%dt:~0,8%_%dt:~8,6%"
set "ZIP_NAME=Project89_Agent_Arsenal_%TIMESTAMP%.zip"

:: Create the distribution directory if it doesn't exist
if not exist "%DIST_DIR%" (
    echo Creating distribution directory...
    mkdir "%DIST_DIR%"
)

:: Create the MindMirror directory in the distribution
if not exist "%DIST_DIR%\MindMirror" (
    echo Creating MindMirror directory...
    mkdir "%DIST_DIR%\MindMirror"
    mkdir "%DIST_DIR%\MindMirror\exports"
    mkdir "%DIST_DIR%\MindMirror\exports\reality_glitcher"
    mkdir "%DIST_DIR%\MindMirror\user_data"
    mkdir "%DIST_DIR%\MindMirror\user_data\journal"
    mkdir "%DIST_DIR%\MindMirror\resources"
    mkdir "%DIST_DIR%\MindMirror\resources\sounds"
    mkdir "%DIST_DIR%\MindMirror\resources\images"
)

:: Create the RealityGlitcher directory in the distribution
if not exist "%DIST_DIR%\RealityGlitcher" (
    echo Creating RealityGlitcher directory...
    mkdir "%DIST_DIR%\RealityGlitcher"
    mkdir "%DIST_DIR%\RealityGlitcher\imports"
    mkdir "%DIST_DIR%\RealityGlitcher\exports"
    mkdir "%DIST_DIR%\RealityGlitcher\resources"
    mkdir "%DIST_DIR%\RealityGlitcher\resources\sounds"
    mkdir "%DIST_DIR%\RealityGlitcher\resources\images"
    mkdir "%DIST_DIR%\RealityGlitcher\user_data"
)

echo Copying MindMirror files...
:: Copy MindMirror Python files
copy "%MM_DIR%\enchanted_mindmirror_new.py" "%DIST_DIR%\MindMirror\"
copy "%MM_DIR%\meditation_tracker.py" "%DIST_DIR%\MindMirror\"
copy "%MM_DIR%\consciousness_mapper.py" "%DIST_DIR%\MindMirror\"
copy "%MM_DIR%\quantum_visualizer.py" "%DIST_DIR%\MindMirror\"
copy "%MM_DIR%\user_profile.py" "%DIST_DIR%\MindMirror\"
copy "%MM_DIR%\main.py" "%DIST_DIR%\MindMirror\"

:: Copy MindMirror resources
if exist "%MM_DIR%\resources\sounds" (
    copy "%MM_DIR%\resources\sounds\*.wav" "%DIST_DIR%\MindMirror\resources\sounds\"
    copy "%MM_DIR%\resources\sounds\*.mp3" "%DIST_DIR%\MindMirror\resources\sounds\"
)
if exist "%MM_DIR%\resources\images" (
    copy "%MM_DIR%\resources\images\*.png" "%DIST_DIR%\MindMirror\resources\images\"
    copy "%MM_DIR%\resources\images\*.jpg" "%DIST_DIR%\MindMirror\resources\images\"
)

echo Copying RealityGlitcher files...
:: Copy RealityGlitcher Python files
copy "%RG_DIR%\quantum_reality_glitcher.py" "%DIST_DIR%\RealityGlitcher\"
copy "%RG_DIR%\glitch_designer.py" "%DIST_DIR%\RealityGlitcher\"
copy "%RG_DIR%\probability_scanner.py" "%DIST_DIR%\RealityGlitcher\"
copy "%RG_DIR%\synchronicity_engine.py" "%DIST_DIR%\RealityGlitcher\"
copy "%RG_DIR%\user_profile.py" "%DIST_DIR%\RealityGlitcher\"
copy "%RG_DIR%\main.py" "%DIST_DIR%\RealityGlitcher\"

:: Copy RealityGlitcher resources
if exist "%RG_DIR%\resources\sounds" (
    copy "%RG_DIR%\resources\sounds\*.wav" "%DIST_DIR%\RealityGlitcher\resources\sounds\"
    copy "%RG_DIR%\resources\sounds\*.mp3" "%DIST_DIR%\RealityGlitcher\resources\sounds\"
)
if exist "%RG_DIR%\resources\images" (
    copy "%RG_DIR%\resources\images\*.png" "%DIST_DIR%\RealityGlitcher\resources\images\"
    copy "%RG_DIR%\resources\images\*.jpg" "%DIST_DIR%\RealityGlitcher\resources\images\"
)

echo Creating initialization script...
copy "%CURRENT_DIR%initialize_environment.bat" "%DIST_DIR%\"

echo Checking for requirements.txt...
if not exist "%DIST_DIR%\requirements.txt" (
    echo Creating requirements.txt...
    (
        echo # Project 89 Agent Arsenal Requirements
        echo # Core requirements for MindMirror and RealityGlitcher
        echo numpy>=1.20.0
        echo scipy>=1.7.0
        echo matplotlib>=3.4.0
        echo pygame>=2.0.0
        echo tkinter>=8.6
        echo networkx>=2.6.0
        echo scikit-learn>=0.24.0
        echo pillow>=8.2.0
        echo sounddevice>=0.4.0
        echo qutip>=4.6.0
    ) > "%DIST_DIR%\requirements.txt"
)

echo Creating zip file for distribution...
powershell -NoProfile -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('%DIST_DIR%', '%CURRENT_DIR%%ZIP_NAME%')"
if errorlevel 1 (
    echo Warning: Could not create zip file. You may need to create it manually.
    echo - Right-click on the agent_distribution folder
    echo - Select "Send to" -> "Compressed (zipped) folder"
) else (
    echo Successfully created zip file: %ZIP_NAME%
)

echo Package preparation complete!
echo.
echo The following files have been created in %DIST_DIR%:
echo.
echo - MindMirror/ (directory with all MindMirror files)
echo - RealityGlitcher/ (directory with all RealityGlitcher files)
echo - initialize_environment.bat (script to set up the environment)
echo - requirements.txt (dependencies for both applications)
echo - README.md (documentation for agents)
echo - launch.py (main launcher script)
echo - combined_launcher.py (GUI launcher for both applications)
echo.
echo A distribution package has been created at:
echo %CURRENT_DIR%%ZIP_NAME%
echo.
echo You can now distribute this package to Project 89 agents.
echo.

pause 