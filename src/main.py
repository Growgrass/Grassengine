import os
from pathlib import Path

os.system("git clone https://github.com/Grasscutters/Grasscutter")
os.chdir(os.getcwd() + "\Grasscutter")
os.system("del /Q start.cmd start_config.cmd")

jar = os.listdir()
print(jar)

os.system(".\gradlew.bat")
os.system(".\gradlew jar")

with open("start.cmd", "w") as file:
    file.write(f"java -jar {jar}")

os.system(".\start.cmd")
