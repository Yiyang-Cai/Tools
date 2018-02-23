@ECHO OFF

for %%i in ("%source_root_folder%\Main_Triage_Builds_x64") do (
	xcopy %%i %dest_root_folder_Main% /E /D
)
