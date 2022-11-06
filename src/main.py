import os, re, typer

app = typer.Typer(name="Grassengine")

@app.command(name="main")
def main():
    print("!Grassengine!")
    print("""

    Grasscutter 설치기

    만든이: Growgrass
    버전: 1.0.0
    """)

@app.command(name="setup", help="기본 설치")
def setup(option: str = typer.Argument(default=None, help="option: Grasscutter, Resources")):  # type: ignore

    if option == "Grasscutter":
        os.system("git clone https://github.com/Grasscutters/Grasscutter")

        os.chdir(os.getcwd() + "\Grasscutter") # type: ignore
        os.system("del /Q start.cmd start_config.cmd")
        os.system(".\gradlew.bat") # type: ignore
        os.system(".\gradlew jar") # type: ignore
    elif option == "Resources":
        os.system("rmdir /Q resources")
        os.chdir("../")
        os.system("git clone https://github.com/tamilpp25/Grasscutter_Resources")
        print("""
        Grasscutter_Resources 폴더 안에있는 Resources 폴더를 Grasscutter 폴더로 복사한다음 이름을 resources로 바꾸어 주세요.
        """)
    else:
        print("python main.py setup --help")

@app.command(name="start", help="Grasscutter 시작")
def start():
    os.chdir(os.getcwd() + "\Grasscutter") # type: ignore

    jar = os.listdir()
    jar = str(jar)
    jar = str(re.findall(r'grasscutter.*?.jar', jar)).replace(r"['", "").replace(r"']", "")

    print("Grasscutter를 시작합니다...")

    if jar == "[]":
        print("python main.py setup --Grasscutter 을 먼저 실행해 주세요.")
    else:
        os.system(f"java -jar {jar}")

if __name__ == "__main__":
    app()
