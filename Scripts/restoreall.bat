@echo off
set version=version-53d1b11b188e46c2
echo Veuillez patienter... Cela peut prendre plus ou moins de temps.
xcopy /E /I /Y "%cd%\Textures" "C:\Users\%username%\AppData\Local\Roblox\Versions\%version%\content\textures"
del /S /F /Q "C:\Users\%username%\AppData\Local\Temp\FPSUnlocker.exe"