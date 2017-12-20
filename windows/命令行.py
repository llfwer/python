import os

import time


def auto_restart():
    for i in range(30):
        os.system('adb shell am start -S com.upchina/.LaunchActivity')
        time.sleep(8)


def look():
    for i in range(8888):
        print('====================================================')
        os.system('adb shell ls /sdcard/android/data/com.upchina/cache/voice')
        time.sleep(1)


def capture():
    os.system('adb shell /system/bin/screencap -p /sdcard/screen.png')
    time.sleep(3)
    os.system('adb pull /sdcard/screen.png screen.png')


capture()
