@ECHO OFF

for %%i in ("%source_root_folder%\R23QA_Triage_Builds_x64") do (
	xcopy %%i %dest_root_folder_QA% /E /D
)