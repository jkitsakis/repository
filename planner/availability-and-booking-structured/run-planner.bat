@echo off
:start
title planner
echo Running Planner script...
python main.py
echo Python script finished. Waiting for the next run...
timeout /t 60 /nobreak
goto start
