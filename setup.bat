@echo off

net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Demande de privileges admin...
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList '%*'"
    exit /b
)

set "file=startupExplorer.exe"
set "source=%~dp0%file%"
set "target=C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"

echo Nom du fichier : %file%
echo Chemin d'origine : %source%
echo Chemin de destination : %target%

if exist "%target%%file%" (
    echo Un autre fichier startupExplorer.exe existe dans le chemin de destination.
    echo Terminaison du processus en cours...
    taskkill /IM "%file%" /F >nul
    echo Suppression de l'ancienne version du fichier...
    del "%target%%file%"
)

echo Copie du fichier %file% dans le dossier de démarrage...
copy "%source%" "%target%"

if errorlevel 1 (
    echo Une erreur s'est produite lors de la copie du fichier.
    timeout /t 5 > nul
    exit /b
) else (
    echo Le fichier a été copié avec succès.
)

echo Demarrage du fichier %file%...
start "" "%target%%file%"

if errorlevel 1 (
    echo Une erreur s'est produite lors du demarrage du fichier.
    timeout /t 3 > nul
) else (
    echo Le fichier a été demarre avec succes.
)

set "programFilesFolder=C:\Program Files"
set "startupDataFolder=%programFilesFolder%\Startup Data"

if exist "%startupDataFolder%" (
    echo Suprresion de Startup Data...
    del "startupDataFolder"
    echo Suppresion avec succès!
)

echo Creation du dossier "Startup Data" dans Program Files...
mkdir "%startupDataFolder%"
attrib +h +s "%startupDataFolder%"
echo Dossier "Startup Data" cree avec succes.

set "assetsFolder=%~dp0assets"

echo Copie du contenu du dossier "assets" dans "Startup Data"...
xcopy "%assetsFolder%\*" "%startupDataFolder%\" /E /I /Y

if errorlevel 1 (
    echo Une erreur s'est produite lors de la copie du contenu du dossier "assets".
    timeout /t 5 > nul
    exit /b
) else (
    echo Contenu du dossier "assets" copie avec succes dans "Startup Data".
)

echo Termine.
timeout /t 3 > nul
