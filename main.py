import os, re, typer

app = typer.Typer(name="Grassengine", help="Grassengine 도움말")

@app.command(name="main", help="main")
def main():
    print("!Grassengine!")
    print("""

    Grasscutter 설치기

    만든이: Growgrass
    버전: 1.0.0
    """)

@app.command(name="setup", help="기본 설치")
def setup(option: str = typer.Argument(default=None, help="option: Grasscutter, Resources, Proxy")):  # type: ignore

    if option == "Grasscutter":
        os.system("git clone https://github.com/Grasscutters/Grasscutter")

        os.chdir(os.getcwd() + "\Grasscutter") # type: ignore
        os.system("del /Q start.cmd start_config.cmd")
        os.system(".\gradlew.bat") # type: ignore
        os.system(".\gradlew jar") # type: ignore
    elif option == "Resources":
        os.chdir(os.getcwd() + "\Grasscutter") # type: ignore
        os.system("rmdir /Q resources")
        os.chdir("../")
        os.system("git clone https://github.com/tamilpp25/Grasscutter_Resources")
        print("""
        Grasscutter_Resources 폴더 안에있는 Resources 폴더를 Grasscutter 폴더로 복사한다음 이름을 resources로 바꾸어 주세요.
        """)
    elif option == "Proxy":
        os.system("pip install mitmdump")
        os.system(r"certutil -addstore root %USERPROFILE%\.mitmproxy\mitmproxy-ca-cert.cer")
    else:
        print("python main.py setup --help")

@app.command(name="grasscutter", help="Grasscutter 시작")
def grasscutter():
    os.chdir(os.getcwd() + "\Grasscutter") # type: ignore

    jar = os.listdir()
    jar = str(jar)
    jar = str(re.findall(r'grasscutter.*?.jar', jar)).replace(r"['", "").replace(r"']", "")

    print("Grasscutter를 시작합니다...")

    if jar == "[]":
        print("python main.py setup --Grasscutter 을 먼저 실행해 주세요.")
    else:
        os.system(f"start java -jar {jar}")

@app.command(name="proxy", help="프록시 실행")
def proxy(port: int = typer.Argument(default=int(5555), help="포트 설정")):
    os.chdir(os.getcwd() + "\src") # type: ignore

    print("Proxy를 시작합니다...")
    
    os.system(r"reg import .\proxy.reg >nul 2>nul")
    print("Proxy On Success")
    os.system(f"netsh winhttp set proxy 127.0.0.1:{port} >nul 2>nul")
    os.system(f"start mitmdump -s proxy.py -k -p {port}")

@app.command(name="start", help="예초기 와 프록시 실행")  # type: ignore
def start(port: int = typer.Argument(default=int(5555), help="포트 설정")):
    grasscutter()
    os.chdir("../")
    proxy(port=port)

@app.command(name="stop", help="종료")
def stop():
    os.chdir(os.getcwd() + "\src") # type: ignore

    print("Grasscutter와 Proxy를 종료 합니다...")

    os.system("TASKKILL /F /IM java.exe")
    print("Grasscutter Kill Success")
    os.system("TASKKILL /F /IM mitmdump.exe")
    print("Proxy Kill Success")
    os.system(r"reg import .\D_proxy.reg >nul 2>nul")
    print("Proxy Off Success")

if __name__ == "__main__":
    main()
    app()
