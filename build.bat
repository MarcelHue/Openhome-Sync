@echo off
echo === Openhome Sync Build ===
echo.

echo [1/3] Cleaning old build...
rmdir /s /q dist 2>nul
rmdir /s /q build 2>nul
rmdir /s /q output 2>nul

echo [2/3] Running PyInstaller...
python -m PyInstaller --noconfirm --noconsole --name OpenhomeSync ^
    --icon icon.ico ^
    --add-data "find_pixel\win_readmouse.dll;find_pixel" ^
    --add-data "icon.ico;." ^
    main.py

if errorlevel 1 (
    echo.
    echo ERROR: PyInstaller failed!
    pause
    exit /b 1
)

echo [3/3] Building Installer...
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss

if errorlevel 1 (
    echo.
    echo ERROR: Inno Setup failed!
    pause
    exit /b 1
)

echo.
echo === Build complete! ===
echo Installer: output\Openhome-Sync-Setup.exe
pause
