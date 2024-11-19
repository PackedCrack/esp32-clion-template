@echo off
if not defined IDF_PATH (
    echo Environment variable IDF_PATH is not set. Cannot continue.
    exit /b 1
)

call espidf_source.bat

python "%IDF_PATH%\tools\idf.py" %*
