#!/bin/bash

set -CEuo pipefail
SCRIPT_DIR=$(cd $(dirname $0) && pwd)
cd ${SCRIPT_DIR}

python3 check-global-ip.py