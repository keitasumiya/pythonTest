import requests

response = requests.get('https://ifconfig.io/ip')
_globalIP = ''.join(response.text.splitlines())
# print(response.text)
print(_globalIP)
print(_globalIP)
print(_globalIP=="182.168.226.134")
print(_globalIP=="182.168.226.132")

# import requests

# url = 'https://ifconfig.io/'
# response = requests.get(url, verify=False)



# import urllib.request
# import json
# import ssl

# url = 'https://ifconfig.io/'

# context = ssl.create_default_context()
# context.check_hostname = False
# context.verify_mode = ssl.CERT_NONE

# try:
#     with urllib.request.urlopen(url, context=context) as response:
#         body = json.loads(response.read())
#         headers = response.getheaders()
#         status = response.getcode()

#         print(headers)
#         print(status)
#         print(body)

# except urllib.error.URLError as e:
#      print(e.reason)