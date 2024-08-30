#!/bin/bash

read -p "HEY!!! The action you're about to do requires free memory of around 600-800MB. Continue? (Y/N): " response

if [[ "$response" =~ ^[Yy]$ ]]; then
    curl -s "https://monketools.neocities.org/MonkeMisc/monkemisc-requirements.txt" | while read -r line; do
        eval "$line"
    done

    read -p "Input your name: " name

    clear

    echo -e "\033[35mHello $name!\033[0m \033[33mDo you wanna install MonkeMisc? (Y/N)\033[0m"
    read -p "" install_response

    if [[ "$install_response" =~ ^[Yy]$ ]]; then
        npm install child_process
        npm install readline
        pip install os
        pip install psutil
        pip install speedtest
        pip install subprocess
        pip install time
        pip install colorama
        pip install requests
        pip install random
        wget https://monketools.neocities.org/MonkeMisc/monkeload.js
        node monkeload.js
    else
        echo "Aborting installation."
        clear
    fi
else
    echo "Operation aborted."
    clear
fi