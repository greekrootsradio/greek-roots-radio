#!/bin/bash

cd ~/cyprus

echo "$(date) Starting ZETA" >> cyprus.log

python3 main.py >> cyprus.log 2>> cyprus_error.log
