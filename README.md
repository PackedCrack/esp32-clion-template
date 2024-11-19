# Clion template project for ESP32.


## Windows

If you don't have ESP-IDF installed see [Install ESP-IDF](#install-esp-idf)

### Initial Setup

1. cd <project_directory>
2. python setup.py

### Toolchain

1. Settings -> Build, Execution, Deployment -> Toolchains
2. Add (Alt + Insert) -> MinGW
3. Name: Xtensa ESP32
4. Add environment -> From file
5. Environment file: \esp32-cpp-template\espidf_source.bat
6. Settings -> Build, Execution, Deployment -> CMake
7. Delete (Alt + Delete) all profiles.
8. Add (Alt + Insert)
9. Toolchain: XTensa ESP32
10. (Optional) Repeat 8. and 9. for all the profiles you need.
11. Apply -> OK

### Accessing idf.py menuconfig
1. View -> Tool Windows -> Terminal (Alt + F12)
2. `.\idf.bat menuconfig`

#### If menuconfig is glitchy in powershell it can be run in the command prompt:
1. New Predefined Session (It's an arrow pointing down next to Local in the Terminal window. It is **only** visible if you're mouse is hovering on the Terminal window.)
2. Command Prompt
3. `.\idf.bat menuconfig`

### Flash Compiled Binary

1. Under Run / Debug Configurations in the top right corner, select Flash.
2. Build the configuration

### Flash and Monitor
1. Configuration -> Edit
2. Copy the 'flash' configuration by selecting it and clicking Copy Configuration (Ctrl + D)
3. Name: flash_and_monitor
4. Executable: \esp32-cpp-template\flash_and_monitor.bat
5. Program arguments: monitor -p <COM PORT>
6. Working directory: \esp32-cpp-template\
7. Environment variables: IDF_PATH=C:\path\to\esp-idf
8. Check 'Emulate terminal in the output console'.
9. Press the Play button to flash and monitor.

## Install ESP-IDF

1. `cd <esp-idf directory>`
2. `mkdir esp`
3. `cd esp`
4. `git clone --recursive https://github.com/espressif/esp-idf.git`
5. `cd esp-idf`
6. `powershell -ExecutionPolicy Bypass -File install.ps1`
7. `python <installation directory>\esp\esp-idf\tools\idf_tools.py install-python-env`