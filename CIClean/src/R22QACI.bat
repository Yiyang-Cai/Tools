@ECHO OFF

for %%i in ("%source_root_folder%\R22QA_Triage_Builds_x64") do (
	xcopy %%i %dest_root_folder_22QA% /E /D
)