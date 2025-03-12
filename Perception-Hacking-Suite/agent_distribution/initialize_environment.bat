@echo off
setlocal enabledelayedexpansion

echo ============================================
echo PROJECT 89 ENVIRONMENT INITIALIZATION SCRIPT
echo ============================================
echo.
echo This script will set up the necessary environment 
echo for the Project 89 Agent Arsenal applications.
echo.

:: Get the current directory
set "CURRENT_DIR=%~dp0"

:: Create directories for MindMirror if they don't exist
if not exist "%CURRENT_DIR%MindMirror\user_data" (
    echo Creating MindMirror user data directories...
    mkdir "%CURRENT_DIR%MindMirror\user_data"
    mkdir "%CURRENT_DIR%MindMirror\user_data\journal"
)

if not exist "%CURRENT_DIR%MindMirror\exports" (
    echo Creating MindMirror export directories...
    mkdir "%CURRENT_DIR%MindMirror\exports"
    mkdir "%CURRENT_DIR%MindMirror\exports\reality_glitcher"
)

if not exist "%CURRENT_DIR%MindMirror\resources" (
    echo Creating MindMirror resource directories...
    mkdir "%CURRENT_DIR%MindMirror\resources"
    mkdir "%CURRENT_DIR%MindMirror\resources\sounds"
    mkdir "%CURRENT_DIR%MindMirror\resources\images"
)

:: Create directories for RealityGlitcher if they don't exist
if not exist "%CURRENT_DIR%RealityGlitcher\imports" (
    echo Creating RealityGlitcher import directories...
    mkdir "%CURRENT_DIR%RealityGlitcher\imports"
)

if not exist "%CURRENT_DIR%RealityGlitcher\exports" (
    echo Creating RealityGlitcher export directories...
    mkdir "%CURRENT_DIR%RealityGlitcher\exports"
)

if not exist "%CURRENT_DIR%RealityGlitcher\resources" (
    echo Creating RealityGlitcher resource directories...
    mkdir "%CURRENT_DIR%RealityGlitcher\resources"
    mkdir "%CURRENT_DIR%RealityGlitcher\resources\sounds"
    mkdir "%CURRENT_DIR%RealityGlitcher\resources\images"
)

if not exist "%CURRENT_DIR%RealityGlitcher\user_data" (
    echo Creating RealityGlitcher user data directories...
    mkdir "%CURRENT_DIR%RealityGlitcher\user_data"
)

:: Copy any existing MindMirror exports to RealityGlitcher imports
echo Checking for MindMirror exports to import into RealityGlitcher...
set "MM_EXPORTS=%CURRENT_DIR%MindMirror\exports\reality_glitcher"
set "RG_IMPORTS=%CURRENT_DIR%RealityGlitcher\imports"

if exist "%MM_EXPORTS%" (
    for %%f in ("%MM_EXPORTS%\*.json") do (
        if exist "%%f" (
            echo Found export: %%~nxf
            copy "%%f" "%RG_IMPORTS%\%%~nxf"
            echo Copied to RealityGlitcher imports directory.
        )
    )
)

:: Create a notification file for RealityGlitcher if new imports are available
set "FOUND_EXPORTS=0"
for %%f in ("%MM_EXPORTS%\*.json") do (
    if exist "%%f" (
        set "FOUND_EXPORTS=1"
    )
)

if "%FOUND_EXPORTS%"=="1" (
    echo Creating notification for RealityGlitcher...
    echo %DATE% %TIME% > "%RG_IMPORTS%\.new_import"
)

echo Environment initialization complete!
echo.
echo The following directories have been set up:
echo.
echo MindMirror:
echo - User data directory for storing user profiles and settings
echo - Journal directory for storing meditation journals
echo - Exports directory for exporting consciousness maps
echo.
echo RealityGlitcher:
echo - Imports directory for importing consciousness maps
echo - Exports directory for exporting reality glitches
echo - User data directory for storing user profiles and settings
echo.
echo Ready to launch applications.
echo.
pause 
pause 