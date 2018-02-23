@echo off

SET source_root_folder=\\invci-package-stg-sha.ecs.ads.autodesk.com\InvCI_PRD
SET dest_root_folder_Main=\\shanetapp04\backup\InvCI\Main_Triage_Builds_x64
SET dest_root_folder_QA=\\shanetapp04\backup\InvCI\R23QA_Triage_Builds_x64
SET dest_root_folder_22QA=\\shanetapp04\backup\InvCI\R22QA_Triage_Builds_x64
SET SCRIPTBASEDIR=%~dp0

NET USE \\invci-package-stg-sha.ecs.ads.autodesk.com\InvCI_PRD "QA@autodesk1" /user:ads.autodesk.com\itools

REM mirror the production packages to staging backup folder
ECHO Main_Triage_Builds copy...
START "" /D "%SCRIPTBASEDIR%src" "MianCI.bat"

ECHO R23QA_Triage_builds copy..
START "" /D "%SCRIPTBASEDIR%src" "R23QACI.bat"

ECHO R22QA_Triage_builds copy..
START "" /D "%SCRIPTBASEDIR%src" "R22QACI.bat"

REM Clean CI from root folder
ECHO Clean CI from root folder...
pushd %~dp0
cd src
START python CIClean.py All

:end