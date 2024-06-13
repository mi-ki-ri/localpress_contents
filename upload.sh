#!/bin/bash

# windowsかmacかを判定
if [ "$(uname)" == "Darwin" ]; then
    # Macの場合
    echo "Mac"
    . ./venv/bin/activate
    elif [ "$(expr substr $(uname -s) 1 5)" == "MINGW" ]; then
    # Windowsの場合
    echo "Windows"
    . ./venv/Scripts/activate
fi

. ./export_api_url.sh
. ./export_api_key.sh
python upload.py
