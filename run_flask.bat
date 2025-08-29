@echo off
REM Change to project folder
cd /d "C:\Users\shaik.mohammedarif\Desktop\Python"

REM Start Flask server in a new terminal
start cmd /k "python flask_app.py"

REM Wait a few seconds for Flask to start
timeout /t 5 >nul

REM Automatically upload CSV
curl -X POST -F "file=@data.csv" http://127.0.0.1:5000/upload_csv

REM Open browser to view CSV rows
start http://127.0.0.1:5000/
