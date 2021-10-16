import sys
import datetime
import requests
import platform
import json
import gmailSender

def getGlobalIP():
    response = requests.get('http://inet-ip.info/ip')
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

def updateMailSettings(_jsonPath, _message):
    _json = json.loads(open(_jsonPath, 'r').read())
    _json["message"] = _message
    with open(_jsonPath, 'w') as f:
        json.dump(_json, f, indent=2, ensure_ascii=False)

def checkGlobalIPChangingAndNotification(_globalIP, _previousGlobalIP):
    if _globalIP != _previousGlobalIP:
        _platformSystem = platform.system()
        _message = "New Global IP: " + _globalIP
        updateMailSettings("mail-settings.json", _message)
        gmailSender.mainProcess()

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

