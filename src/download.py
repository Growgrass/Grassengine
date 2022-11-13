import requests

def download(URL: str, FILE_NAME: str = None):  # type: ignore
    if FILE_NAME == None:
        FILE_NAME = URL.split("/")[-1]
    
    with open(f"{FILE_NAME}", "wb") as file:
        get = requests.get(URL)
        file.write(get.content)