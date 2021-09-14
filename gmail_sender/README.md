# Gmail-API with Python

## My Article

[Gmail APIを使ってPythonでメール送信する](https://keitasumiya.net/blog/gmail-api_python/)



## Requirement

- OS: Mac, Windows
- python3
  - import pickle
  - import os.path
  - from googleapiclient.discovery import build
  - from google_auth_oauthlib.flow import InstalledAppFlow
  - from google.auth.transport.requests import Request
  - import base64
  - from email.mime.text import MIMEText
  - from apiclient import errors
  - import json



## Tested Environment

- Mac
  - macOS Big Sur 11.5.2 on M1 MacBook Air 2020



## Usage

```shell
python3 main.py
or
python main.py
```



## References

- [Gmail APIを使ってPythonでメール送信する](https://keitasumiya.net/blog/gmail-api_python/)
- [Gmail APIとPythonを使ってメール送信を自動化する方法 – Valmore](https://valmore.work/automate-gmail-sending/)
