### LOCALDATA 동물병원 데이터 전처리기

---

LOCALDATA (https://www.localdata.go.kr/) 에서 제공하는 동물병원 데이터를 전처리하는 모듈입니다.

현재는 티티케어 앱에 맞춰 전처리를 자동으로 진행하게끔 코드가 Fix되어 있습니다.

---

#### 개발 환경

Python3.9 (venv/bin/python)

```
Package         Version
--------------- ---------
certifi         2021.10.8
numpy           1.22.2
pandas          1.4.1
pip             21.1.2
pyproj          3.3.0
python-dateutil 2.8.2
pytz            2021.3
setuptools      57.0.0
six             1.16.0
wheel           0.36.2
```

MacOS Monterey (Macbook '14 M1 Pro)

---

#### 실행 방법 (MacOS or Linux)

```
sh run.sh
```

---

### 실행 시 주의사항

처음 data.csv 파일을 만들 때, 동물병원 Excel 데이터를 다운받고 이를 .csv 파일로 변환해줘야합니다.

그 이후, Excel 파일에 있는 관리번호를 data.csv에 붙여넣기를 해야합니다.

Excel 셀에 15자 이상의 숫자를 입력하면 모든 숫자가 0으로 변경되는 문제
https://docs.microsoft.com/ko-kr/office/troubleshoot/excel/last-digits-changed-to-zeros
