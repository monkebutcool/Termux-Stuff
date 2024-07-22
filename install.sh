#!/bin/bash

echo -e "\033[Do you want to install MonkeMisc? (Y/n) {Need 64.1MB free disk space}\033[0m"
echo "Made in https://apksntermux.blogspot.com/"

read -p "" choice

case $choice in
    [Yy])
        pkg upgrade && pkg update && apt update && apt upgrade && pkg install wget && pkg install python && cd $HOME && mkdir MonkeMisc && wget https://monkebutcool.github.io/Termux-Stuff/MonkeMisc.sh && echo -e "\033[32m Successfully installed MonkeMisc!\033[0m
        ;;
    [Nn])
        cd $HOME
        ;;
esac
