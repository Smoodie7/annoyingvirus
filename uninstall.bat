@echo off

set "file=startupExplorer.exe"
set "source=%~dp0%file%"
set "target=C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"

echo Nom du fichier : %file%
echo Chemin d'origine : %source%
echo Chemin de destination : %target%

if exist "%target%%file%" (
    echo Un fichier startupExplorer.exe existe dans le chemin de destination.
    echo Terminaison du processus en cours...
    taskkill /IM "%file%" /F >nul
    echo Suppression du fichier...
    del "%target%%file%"
)

set "programFilesFolder=C:\Program Files"
set "startupDataFolder=%programFilesFolder%\Startup Data"

if exist "%startupDataFolder%" (
    echo Suppresion de Startup Data...
    del "startupDataFolder"
    echo Suppresion avec succes!
)

echo Termine.
timeout /t 5 > nul
