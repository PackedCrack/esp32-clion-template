# Clion template project for ESP32.


## Windows

If you don't have ESP-IDF installed see [Install ESP-IDF](#install-esp-idf)


### Toolchain

1. Settings -> Build, Execution, Deployment -> Toolchains
2. Add (Alt + Insert) -> MinGW
3. Name: Xtensa ESP32
4. Add environment -> From file
5. Environment file: \esp32-cpp-template\espidf_source.bat
6. Open \esp32-cpp-template\espidf_source.bat and insert the absoulte path to activate.bat and export.bat
7. Settings -> Build, Execution, Deployment -> CMake
8. Delete (Alt + Delete) all profiles.
9. Add (Alt + Insert)
10. Toolchain: XTensa ESP32
11. (Optional) Repeat 8. and 9. for all the profiles you need.
12. Apply -> OK

### Accessing idf.py menuconfig
1. View -> Tool Windows -> Terminal (Alt + F12)
2. `.\<esp-idf directory>\export.ps1`
3. `python .\<esp-idf directory>\tools\idf.py menuconfig`

If menuconfig is glitchy in powershell it can be run in the command prompt:
1. New Predefined Session (It's an arrow pointing down next to Local in the Terminal window. It is **only** visible if you're mouse is hovering on the Terminal window.)
2. Command Prompt
3. `.\<esp-idf directory>\export.bat`
4. `python .\<esp-idf directory>\tools\idf.py menuconfig`

Don't forget to set the target:
`idf.py set-target esp32`
`idf.py set-target esp32-s2`
`idf.py set-target esp32-s3`

### Flash Compiled Binary

1. Under Run / Debug Configurations in the top right corner, select Flash.
2. Build the configuration

### Flash and Monitor
1. Configuration -> Edit
2. Copy the 'flash' configuration by selecting it and clicking Copy Configuration (Ctrl + D)
3. Name: flash_and_monitor
4. Executable: \esp32-cpp-template\flash_and_monitor.bat
5. Open \esp32-cpp-template\flash_and_monitor.bat and insert the absoulte path to idf.py
6. Program arguments: monitor -p <COM PORT>
7. Working directory: \esp32-cpp-template\
8. Environment variables: IDF_PATH=C:\path\to\esp-idf
9. Check 'Emulate terminal in the output console'.
10. Press the Play button to flash and monitor.

## Install ESP-IDF

1. `cd <esp-idf directory>`
2. `mkdir esp`
3. `cd esp`
4. `git clone --recursive https://github.com/espressif/esp-idf.git`

5. `cd esp-idf`

6. `powershell -ExecutionPolicy Bypass -File install.ps1`

7. `python <installation directory>\esp\esp-idf\tools\idf_tools.py install-python-env`