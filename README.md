# Grassengine
Grasscutter setup tool
## 필수 구성 요소

### OS
#### 윈도우 전용

### 프로그램
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) 
__3.6 버전 이상이면 다됨__ (3.11은 vc c++ 14.x 필요)
- [Java 17](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
- [MongoDB](https://www.mongodb.com/try/download/community)

## 선택적 구성 요소

### 프로그램
- [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic)
Grassengine 자체에 프록시 내장

## 실행
- 설치
```shell
python setup.py
```
- 도움말
```shell
python main.py --help
```

## 기능
- Grasscutter 빌드
- 리소스 다운
- 실행 (**Grasscutter, Proxy**)

## 주의사항
```shell
python main.py start
```
로 실행한 다음에 
```shell
python main.py stop
```
로 꼭 끄기 안그러면 인터넷 안됨.

## TODO
- [X] Test
- [ ] Test
- [ ] 리소스 자동 적용
- [ ] exe 빌드
