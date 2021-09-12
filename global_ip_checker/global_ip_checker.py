import sys
import datetime
import requests
import platform

def importOSRelatedLibraries():
    platformSystem = platform.system()
    if IsPrint: print(platformSystem)
    if platformSystem == "Darwin":
        import os
    elif platformSystem == "Windows":
        from plyer import notification

def getGlobalIP():
    response = requests.get('https://ifconfig.io/ip')
    _globalIP = ''.join(response.text.splitlines())
    return _globalIP

def readPreviousGlobalIP(_fileName):
    try:
        f = open(_fileName, 'r', encoding='UTF-8')
        _previousGlobalIP = f.read()
        f.close()
    except:
        _previousGlobalIP = "123.123.123.123"
    return _previousGlobalIP

def showNotificationOnMac(_message, _title="", _subtitle="", _sound=""):
    # _sound: Blow,Bottle,Frog,Funk,Glass,Hero,Morse,Ping,Pop,Purr,Sosumi,Tink
    os.system("osascript -e 'display notification \"" + _message + "\" with title \"" + _title + "\" subtitle \"" + _subtitle + "\" sound name \"" + _sound + "\"'")

def showNotificationOnWindows(_message, _title="", _app_name="", _app_icon="", _timeout=5):
    notification.notify(
        title=_title,
        message=_message,
        app_name=_app_name,
        app_icon=_app_icon,
        timeout=5
    )

def checkGlobalIPChangingAndNotification(_globalIP, _previousGlobalIP):
    if _globalIP != _previousGlobalIP:
        _platformSystem = platform.system()
        # print(_platformSystem)
        _title = "Global IP was changed"
        _message = "New Global IP: " + _globalIP
        if _platformSystem == "Darwin":
            showNotificationOnMac(_message, _title=_title)
        elif _platformSystem == "Windows":
            showNotificationOnWindows(_message, _title=_title)

        _changedFlag = ", changed"
    else:
        _changedFlag = ""
    return _changedFlag

def writeGlobalIPIntoLog(_logFileName, _globalIP, _changedFlagStr):
    dtNow = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    f = open(_logFileName, 'a', encoding='UTF-8')
    f.write(dtNow + ', ' + _globalIP + _changedFlagStr + '\n')
    f.close()

def writeGlobalIPIntoTxt(_checkFileName, _globalIP):
    f = open(_checkFileName, 'w', encoding='UTF-8')
    f.write(_globalIP)
    f.close()

def mainProcess():
    checkFileName = 'global-ip.txt'
    logFileName = 'global-ip-log.txt'
    importOSRelatedLibraries()
    globalIP = getGlobalIP()
    if IsPrint: print(globalIP)
    previousGlobalIP = readPreviousGlobalIP(checkFileName)
    changedFlagStr = checkGlobalIPChangingAndNotification(globalIP, previousGlobalIP)
    writeGlobalIPIntoLog(logFileName, globalIP, changedFlagStr)
    writeGlobalIPIntoTxt(checkFileName, globalIP)


# ==============================================================================================================
if __name__ == "__main__":
    IsPrint = True
    if len(sys.argv) == 2: 
        if sys.argv[1] == "noPrint": 
            IsPrint = False
    mainProcess()

