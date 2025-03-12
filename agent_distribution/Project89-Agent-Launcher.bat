@echo off 
echo PROJECT 89 AGENT CONSCIOUSNESS TOOLKIT 
echo ====================================== 
echo. 
echo Welcome, Agent. This toolkit contains advanced consciousness exploration tools. 
echo. 
echo Initializing environment... 
call initialize_environment.bat 
echo. 
echo 1. Launch Mind Mirror (Consciousness Exploration Tool) 
echo 2. Launch Reality Glitcher (Reality Manipulation Tool) 
echo 3. Launch Full Suite (Combined Interface) 
echo 4. Exit 
echo. 
set /p choice="Enter your choice (1-4): " 
 
if "%choice%"=="1" ( 
    echo Launching Mind Mirror... 
    cd MindMirror 
    python enchanted_mindmirror_new.py 
    cd .. 
    goto :eof 
) 
 
if "%choice%"=="2" ( 
    echo Launching Reality Glitcher... 
    call Launch-Reality-Glitcher.bat 
    goto :eof 
) 
 
if "%choice%"=="3" ( 
    echo Launching Full Suite... 
    call Run-P89-Suite.bat 
    goto :eof 
) 
 
if "%choice%"=="4" ( 
    echo Exiting... 
    exit /b 0 
) 
 
echo Invalid choice. Please try again. 
pause 
call Project89-Agent-Launcher.bat 
