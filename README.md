``` bash
# 安裝package
python -m pip install -r requirements.txt
python3 -m pip install -r requirements.txt
*** 如果pyinstaller無法安裝，請使用系統管理員身份開啟ComandLine，並執行pip install pyinstaller
# 打包程式
pyinstaller --onefile   main.py
pyinstaller main.py  --add-data='./templates/basic/*;./templates/basic/' 
```