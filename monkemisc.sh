#!/bin/bash

echo -e "\033[1mMonkeMisc\033[0m"
echo "Which one you want to install?"
echo "[1] Force Deleter FDel"
echo "[2] YouTube Channel Finder FindYT"
echo "[3] Website Up Or Not SiteUpNot"
echo "[A] Author"

read -p "Enter your choice: " choice

case $choice in
    1)
        echo "Force Deleter FDel selected"
        ;;
    2)
        echo "YouTube Channel Finder FindYT selected"
        ;;
    3)
        echo "Website Up Or Not SiteUpNot selected"
        ;;
    [Aa])
        echo "Author selected. Visit: https://apksntermux.blogspot.com/"
        ;;
    *)
        echo "Invalid choice. Exiting."
        ;;
esac
