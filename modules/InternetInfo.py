import speedtest
import platform
import socket
import uuid
import webbrowser
import psutil
import subprocess
import os

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    return download_speed, upload_speed

def get_device_type():
    device_type = platform.system()
    if device_type == "Windows" or device_type == "Linux":
        return "PC"
    elif device_type == "Darwin":
        return "Mac"
    elif device_type == "Android" or device_type == "iOS":
        return "Mobile"
    return "Unknown"

def get_default_browser():
    try:
        return webbrowser.get().name
    except webbrowser.Error:
        return "Unknown"

def get_network_info():
    interfaces = psutil.net_if_addrs()
    wifi_name = None
    mac_address = None
    ip_address = None
    is_ethernet = False

    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4
                ip_address = addr.address
            if addr.family == psutil.AF_LINK:  # MAC
                mac_address = addr.address
            if "Ethernet" in interface:
                is_ethernet = True
            elif "Wi-Fi" in interface or "wlan" in interface:
                wifi_name = interface

    return wifi_name, mac_address, ip_address, is_ethernet

def get_proxy_settings():
    proxy = os.environ.get('http_proxy') or os.environ.get('https_proxy')
    return proxy if proxy else "No Proxy"

def main():
    download_speed, upload_speed = get_internet_speed()
    device_type = get_device_type()
    default_browser = get_default_browser()
    wifi_name, mac_address, ip_address, is_ethernet = get_network_info()
    proxy = get_proxy_settings()

    print(f"Device Type: {device_type}")
    print(f"Default Browser: {default_browser}")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Wi-Fi Name: {wifi_name or 'Not Connected'}")
    print(f"Ethernet Connected: {'Yes' if is_ethernet else 'No'}")
    print(f"MAC Address: {mac_address}")
    print(f"IP Address: {ip_address}")
    print(f"Proxy: {proxy}")

if __name__ == "__main__":
    main()
