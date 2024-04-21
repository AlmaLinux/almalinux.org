:: Install hugo && npm dependencies
::
:: Written by Noam Alum
::
:: Visit alum.sh for more scripts like this :)

@echo off
setlocal enabledelayedexpansion

:: Highlights
set Info=[[36mINFO[0m]
set Error=[[31mERROR[0m]

:: check if hugo/npm is installed
echo %Info% This might take a few minutes, be patient.
set "dictionary[hugo]=Hugo.Hugo.Extended"
set "dictionary[npm]=Node.js"

for %%d in (hugo npm) do (
    where >nul 2>&1 %%d
    if errorlevel 1 (
        echo %Info% Dependency "%%d" missing, installing now...

        :: install dependency
        winget install --accept-package-agreements --accept-source-agreements !dictionary[%%d]! >nul 2>&1
        if errorlevel 1 (
            echo %Error% Installation of "%%d" was not successful.
        )
    )
)

:: install npm dependencies
echo %Info% Installing npm dependencies...
CMD /C npm install >nul 2>&1
if errorlevel 1 (
    echo %Error% Installation of "npm dependencies" was not successful, try running "npm install".
    exit /b 1
)

:: How to start
echo %Info% Run "hugo server" to view the website.

endlocal