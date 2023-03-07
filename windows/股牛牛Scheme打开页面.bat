@echo off 

: 输入url
set /p url=请输入url :
: 调用python
python C:\Users\ROWE\PycharmProjects\python\windows\UrlEncode.py "%url%" > Output
: 接收返回值
set /p encodeurl=<Output
echo %encodeurl%

:打开页面
adb -d shell am start -d upchinagnn://?url=%encodeurl% -a android.intent.action.VIEW

pause

del Output