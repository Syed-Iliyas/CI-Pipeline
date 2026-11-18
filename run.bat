@echo off
REM Double-click this file to run the calculator. No virtual environment needed.
cd /d "%~dp0"
python -m calculator.calculator %*
echo.
pause
