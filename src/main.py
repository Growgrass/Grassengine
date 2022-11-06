import os, re, shutil
from pathlib import Path

os.system("git clone https://github.com/Grasscutters/Grasscutter")
os.system("git clone https://github.com/tamilpp25/Grasscutter_Resources")

os.chdir(os.getcwd() + "\Grasscutter")
os.system("del /Q start.cmd start_config.cmd")
os.system("rmdir /Q resources")

os.system(".\gradlew.bat")
os.system(".\gradlew jar")

jar = os.listdir()
jar = str(jar)
jar = str(re.findall(r'grasscutter.*?.jar', jar)).replace(r"['", "").replace(r"']", "")

with open("start.cmd", "w") as file:
    file.write(f"java -jar {jar}")

os.chdir("../")
os.chdir(os.getcwd() + "\Grasscutter_Resources")
shutil.copytree("Resources", "../Grasscutter/resources")

os.system(".\start.cmd")
