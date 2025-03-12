@echo off 
echo PROJECT 89 DEPENDENCIES INSTALLER 
echo ============================== 
echo. 
echo This script will install all required dependencies for the Project 89 tools. 
echo. 
echo Checking for Python... 
where python >nul 2>nul 
if %ERRORLEVEL% neq 0 ( 
    echo ERROR: Python is not installed or not in PATH. 
    echo Please install Python 3.8 or higher and ensure it's in your PATH. 
    pause 
    exit /b 1 
) 
echo Installing dependencies... This may take a moment... 
python -m pip install --upgrade pip 
python -m pip install -r combined_requirements.txt 
echo. 
echo Dependencies installed successfully! 
echo You can now run the Project89-Agent-Launcher.bat file to start using the tools. 
pause 
