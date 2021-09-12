#!/bin/zsh

set -CEuo pipefail
SCRIPT_DIR=$(cd $(dirname $0) && pwd)
cd ${SCRIPT_DIR}

/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 global_ip_checker.py noPrint