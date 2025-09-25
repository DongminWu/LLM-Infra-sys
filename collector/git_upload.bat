@echo off
echo Starting article fetching and Git push process...

REM Switch to collector directory
cd /d "%~dp0"

echo Executing Python script...
python main.py urls.txt

if %errorlevel% neq 0 (
    echo Python script execution failed, exiting...
    pause
    exit /b 1
)

echo Python script execution completed

REM Switch to parent directory
cd ..

echo Adding README.md to Git...
git add README.md

if %errorlevel% neq 0 (
    echo Failed to add README.md to Git, exiting...
    pause
    exit /b 1
)

echo Committing changes...
git commit -m "Update article list"

REM Check if there are changes to commit
if %errorlevel% equ 1 (
    echo No changes to commit, skipping push...
) else (
    echo Pushing changes to remote repository...
    git push
    if %errorlevel% neq 0 (
        echo Push failed, exiting...
        pause
        exit /b 1
    )
    echo Push successful!
)

echo Process completed!
pause