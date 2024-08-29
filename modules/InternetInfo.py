import speedtest
import platform
import socket
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
    if device_type == "Windows":
        version = platform.version()
        if "10" in version or "11" in version:
            return "Windows 10/11"
        else:
            return "FreeDOS"
    elif device_type == "Linux":
        try:
            distro = subprocess.getoutput('lsb_release -d').split(':')[1].strip()
        except Exception:
            distro = "Unknown"
        if "Debian" in distro or "Ubuntu" in distro or "Mint" in distro:
            return "Debian/Ubuntu"
        elif "Fedora" in distro:
            return "Fedora"
        elif "Red Hat" in distro or "CentOS" in distro:
            return "RedHat"
        elif "Arch" in distro or "Manjaro" in distro:
            return "Arch"
        elif "openSUSE" in distro:
            return "OpenSUSE"
        elif "SteamOS" in distro:
            return "SteamOS"
        else:
            return f"Linux ({distro})"
    elif device_type == "Darwin":
        return f"MacOS {platform.mac_ver()[0]}"
    elif device_type == "Android":
        version = platform.release()
        nickname = subprocess.getoutput("getprop ro.build.version.codename")
        return f"Android {nickname} {version}" if nickname else f"Android {version}"
    elif device_type == "iOS":
        version = platform.release()
        return f"iOS {version}"
    elif device_type == "Chrome OS":
        return "ChromeOS"
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
    connection_type = "Unknown"
    vpn_company = "No VPN"

    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:  # IPv4
                ip_address = addr.address
            if addr.family == psutil.AF_LINK:  # MAC
                mac_address = addr.address
            if "Ethernet" in interface:
                is_ethernet = True
                connection_type = "Ethernet"
            elif "Wi-Fi" in interface or "wlan" in interface:
                wifi_name = interface
                connection_type = "Wi-Fi"
            elif "ppp" in interface or "rmnet" in interface:
                connection_type = "Cellular Data"

    # Check if VPN is running by listing network interfaces and looking for VPN indicators
    try:
        vpn_status = subprocess.getoutput('nmcli connection show')
        if 'vpn' in vpn_status.lower():
            vpn_company = "Possible VPN detected"
    except Exception:
        vpn_company = "No VPN"

    return wifi_name, mac_address, ip_address, is_ethernet, connection_type, vpn_company

def get_proxy_settings():
    proxy = os.environ.get('http_proxy') or os.environ.get('https_proxy')
    return proxy if proxy else "No Proxy"

def main():
    download_speed, upload_speed = get_internet_speed()
    device_type = get_device_type()
    default_browser = get_default_browser()
    wifi_name, mac_address, ip_address, is_ethernet, connection_type, vpn_company = get_network_info()
    proxy = get_proxy_settings()

    print(f"Device Type: {device_type}")
    print(f"Default Browser: {default_browser}")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Connection Type: {connection_type}")
    print(f"Wi-Fi Name: {wifi_name or 'Not Connected'}")
    print(f"Ethernet Connected: {'Yes' if is_ethernet else 'No'}")
    print(f"MAC Address: {mac_address}")
    print(f"IP Address: {ip_address}")
    print(f"Proxy: {proxy}")
    print(f"VPN Company: {vpn_company}")

if __name__ == "__main__":
    main()