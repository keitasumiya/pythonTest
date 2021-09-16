# Global IP Checker with Gmail

## Article

[Global IPの変更をGmail APIを使って通知する](https://keitasumiya.net/blog/2021/global_ip_checker_gmail/)



## Requirement

- OS: Mac, Windows
- python3
  - datetime
  - requests
  - platform
  - json
  - import pickle
  - import os.path
  - from googleapiclient.discovery import build
  - from google_auth_oauthlib.flow import InstalledAppFlow
  - from google.auth.transport.requests import Request
  - import base64
  - from email.mime.text import MIMEText
  - from apiclient import errors



## Tested Environment

- Mac
  - macOS Big Sur 11.5.2 on M1 MacBook Air 2020
- Windows
  - Windows 10 pro on Desktop PC 



## Install Gmail Libraries

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```



## Usage

```shell
python3 main.py
or
python main.py
```



