#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Author:zhangteng

import os
import sys
import threading

wifi_password = 'security'

def getSerialNumber():
    adb_cmd = os.popen('adb devices').read().split('\n')
    serialNumberList = []
    for line in adb_cmd:
        tokens = line.split('\t')
        if len(tokens) == 2:
            serialNumberList.append(tokens[0])
    return serialNumberList

def setup(deviceID, filePath):
    print(deviceID)
    #os.system("adb -s %s install -r %s/arm/CtsDeviceAdmin.apk" % (deviceID, filePath))
    os.system("adb -s %s push %s/CTS_setup.jar /mnt/sdcard/Music" % (deviceID, filePath))
    os.system("adb -s %s shell uiautomator runtest /mnt/sdcard/Music/CTS_setup.jar -c com.dzsoft.smart.testcase.Case_52236 -e find %s" % (deviceID, wifi_password))
    os.system("adb -s %s shell rm /mnt/sdcard/Music/CTS_setup.jar" % deviceID)
    os.system("adb -s %s push %s/android-cts-media-1.2 /sdcard/test" % (deviceID, filePath))
    
    
def main():
    filePath = sys.path[0]
    serialList = getSerialNumber()
    num = len(serialList)
    while True:
        flag = raw_input("已经连接%s台设备，请确认！继续请按Y，退出请按N：" % num)
        if flag[0].lower() == 'y':
            threads = []
            for i in range(num):
                t = threading.Thread(target=setup, args=(serialList[i], filePath))
                threads.append(t)
            for i in range(num):
                threads[i].start()
            for i in range(num):
                threads[i].join()
            break
        elif flag[0].lower() == 'n':
            break
            
if __name__ == "__main__":
    main()

