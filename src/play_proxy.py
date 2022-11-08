import os

def main(port: int = int(5555)):
    try:
        os.chdir(os.getcwd() + "\src") # type: ignore

        print("Proxy를 시작합니다...")

        os.system(r"reg import .\proxy.reg >nul 2>nul")
        print("Proxy On Success")
        os.system("title Exit Ctrl+C")
        os.system(f"netsh winhttp set proxy 127.0.0.1:{port} >nul 2>nul")
        os.system(f"mitmdump -s proxy.py -k -p {port}")
    except KeyboardInterrupt:
        os.system("TASKKILL /F /IM mitmdump.exe >nul 2>nul")
        print("Proxy Kill Success")
        os.system(r"reg import .\D_proxy.reg >nul 2>nul")
        print("Proxy Off Success")
