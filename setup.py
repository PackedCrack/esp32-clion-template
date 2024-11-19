import os
import winreg
import subprocess


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

IDF_PATH = input("Enter the absolute path to esp-idf installation directory (e.g. C:\\Users\\qwerty\\Documents\\esp-idf): ")
EXPORT_BAT_PATH = IDF_PATH + "\\export.bat"
IDF_PY_PATH = IDF_PATH + "\\tools\\idf.py"
ACTIVATE_BAT_PATH = input("Enter the absolute path to activate.bat (e.g. C:\\Users\\qwerty\\.espressif\\python_env\\idf5.5_py3.9_env\\Scripts\\activate.bat): ")

# write espidf_sources.bat
espidf_source = PROJECT_PATH + "\\espidf_source.bat"
with open(espidf_source, 'w') as file:
    file.write("@call " + ACTIVATE_BAT_PATH + "\n")
    file.write("@call " + EXPORT_BAT_PATH + "\n")

# write flash_and_monitor.bat
flash_and_monitor = PROJECT_PATH + "\\flash_and_monitor.bat"
with open(flash_and_monitor, 'w') as file:
    file.write("python " + IDF_PY_PATH + " %*\n")

# set environment variable
def set_user_env_var(name, value):
    key = winreg.HKEY_CURRENT_USER
    subkey = r"Environment"
    try:
        with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as regKey:
            winreg.SetValueEx(regKey, name, 0, winreg.REG_SZ, value)
            os.environ[name] = value
        print("Environment variable {} set to {}.".format(name, value))
    except Exception as err:
        print("Failed to set environment variable: {}".format(err))

set_user_env_var("IDF_PATH", IDF_PATH)
#set_user_env_var("IDF_PY_PATH", IDF_PATH + "\\tools\\idf.py")

# set cmake project name
cmakelists = PROJECT_PATH + "\\CMakeLists.txt"
with open(cmakelists, 'r') as file:
    lines = file.readlines()

with open(cmakelists, 'w') as file:
    projectName = input("Enter the esp32 project's name: ")
    lineToFind = "project(${PROJECT} esp-template-project LANGUAGES C CXX)"
    for line in lines:
        if line.strip() == lineToFind:
            # Replace the project name in the matched line
            line = line.replace('esp-template-project', projectName)
        file.write(line)

# set target
filepath = os.path.join(os.getcwd(), "idf.bat")
target = input("Enter the ESP32 target (e.g. esp32, esp32-s2, esp32-s3): ")
subprocess.run(["cmd", "/c", filepath, "set-target", target], shell=True, check=True)