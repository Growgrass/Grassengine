import os, re, typer, zipfile
from src import play_proxy
from src import download

app = typer.Typer(name="Grassengine", help="Grassengine 도움말")

@app.command(name="main", help="main")
def main():
    print("!Grassengine!")
    print("""

    Grasscutter 설치기

    만든이: Growgrass
    버전: 3b.1a.tn
    """)

@app.command(name="setup", help="기본 설치")
def setup(option: str = typer.Argument(default=None, help="option: Grasscutter, Resources, Proxy")):  # type: ignore

    if option == "Java":
        download.download(URL="https://download.oracle.com/java/17/archive/jdk-17.0.5_windows-x64_bin.zip", FILE_NAME="java_17.zip")

        try:
            with zipfile.ZipFile("java_17.zip") as z:
                z.extractall("Java")
                print("Extracted all")
            os.system("del /Q java_17.zip")
            os.chdir(os.getcwd() + r"\Java\jdk-17.0.5\bin") # type: ignore
            os.system("rename java.exe GE_JAVA.exe")
        except:
            print("Invalid file")
    if option == "Grasscutter":
        os.system("git clone https://github.com/Grasscutters/Grasscutter")

        os.chdir(os.getcwd() + "\Grasscutter") # type: ignore
        os.system("del /Q start.cmd start_config.cmd")
        os.system(".\gradlew.bat") # type: ignore
        os.system(".\gradlew jar") # type: ignore
        print("Done!")
    elif option == "Resources":
        os.chdir(os.getcwd() + "\Grasscutter") # type: ignore
        os.system("rmdir /Q resources")
        os.chdir("../")
        os.system("git clone https://github.com/tamilpp25/Grasscutter_Resources")
        os.system(r"move Grasscutter_Resources\Resources Grasscutter")
        os.chdir(os.getcwd() + "\Grasscutter") # type: ignore
        os.system("rename Resources resources")
        print("Done!")
    elif option == "Proxy":
        os.system("pip install mitmdump")
        os.system(r"certutil -addstore root %USERPROFILE%\.mitmproxy\mitmproxy-ca-cert.cer")
        print("Done!")
    else:
        print("python main.py setup --help")

@app.command(name="grasscutter", help="Grasscutter 시작")
def grasscutter():
    os.chdir(os.getcwd() + "\Grasscutter") # type: ignore

    jar = os.listdir()
    jar = str(jar)
    jar = str(re.findall(r'grasscutter.*?.jar', jar)).replace(r"['", "").replace(r"']", "")

    os.chdir("../")
    java = os.getcwd() + r"\Java\jdk-17.0.5\bin" # type: ignore

    print("Grasscutter를 시작합니다...")

    if jar == "[]":
        print("python main.py setup --Grasscutter 을 먼저 실행해 주세요.")
    else:
        os.chdir(os.getcwd() + "\Grasscutter") # type: ignore
        os.system(f"start {java}\GE_JAVA.exe -jar {jar}") # type: ignore

@app.command(name="proxy", help="프록시 실행")
def proxy(port: int = typer.Argument(default=int(5555), help="포트 설정")):
    play_proxy.main(port=port)

@app.command(name="start", help="예초기 와 프록시 실행")  # type: ignore
def start(port: int = typer.Argument(default=int(5555), help="포트 설정")):
    grasscutter()
    os.chdir("../")
    proxy(port=port)

@app.command(name="stop", help="종료")
def stop():
    os.chdir(os.getcwd() + "\src") # type: ignore

    print("Grasscutter와 Proxy를 종료 합니다...")

    os.system("TASKKILL /F /IM GE_JAVA.exe >nul 2>nul")
    print("Grasscutter Kill Success")
    os.system("TASKKILL /F /IM mitmdump.exe >nul 2>nul")
    print("Proxy Kill Success")
    os.system(r"reg import .\D_proxy.reg >nul 2>nul")
    print("Proxy Off Success")

if __name__ == "__main__":
    main()
    app()
