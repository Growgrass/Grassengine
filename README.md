# Grassengine
Grasscutter setup tool
## 필수 구성 요소

### OS
#### 윈도우 전용

### 프로그램
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) 
__3.6 버전 이상이면 다됨__ (3.11은 vc c++ 14.x 필요)
- [MongoDB](https://www.mongodb.com/try/download/community)

## 선택적 구성 요소

### 프로그램
- [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic)
Grassengine 자체에 프록시 내장

## 실행
### 관리자 권한 필수
- 설치
```shell
python install.py
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
프록시는 콘솔내에서 Ctrl+C로 끄기 안그럼 인터넷 안됌
- 인터넷이 안될때
```shell
python main.py stop
```

## TODO
- [X] Test
- [ ] Test
- [X] 리소스 자동 적용
- [ ] exe 빌드
- [X] 자바 자동 적용
