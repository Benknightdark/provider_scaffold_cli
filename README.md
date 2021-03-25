``` bash
# 安裝package
*** 使用系統管理員身份開啟ComandLine, 再安裝package
python -m pip install -r requirements.txt
# 打包程式
pyinstaller --onefile   main.py
# 範例Command
 ./main.py  basic --file_name home --app_name upl 
./main.py  list --file_name home --app_name upl 

```