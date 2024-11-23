@echo off
:start
title planner availability check
echo Running Python script...
python planner-available.py
echo Python script finished. Waiting for the next run...
timeout /t 60 /nobreak
goto start
