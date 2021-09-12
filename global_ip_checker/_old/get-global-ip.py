import subprocess
from subprocess import PIPE

cmd = "curl ipecho.net/plain; echo"
proc = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
globalIP = proc.stdout
print('global IP: {}'.format(globalIP))