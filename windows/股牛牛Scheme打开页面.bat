@echo off 

: ����url
set /p url=������url :
: ����python
python E:\python\windows\UrlEncode.py "%url%" > Output
: ���շ���ֵ
set /p encodeurl=<Output
echo %encodeurl%

:��ҳ��
adb -d shell am start -d upchinagnn://?url=%encodeurl% -a android.intent.action.VIEW

pause

del Output