import requests

while True:
    domain = input("Domain (without 'https://' and trailing '/'): ")
    url = f"http://{domain}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            status = "Up"
        else:
            status = "Down"
        uptime = response.elapsed.total_seconds()
    except requests.ConnectionError:
        status = "Down"
        uptime = 0

    print(f"Domain: {domain}")
    print(f"Up Or Not: {status}")
    print(f"Uptime: {uptime} seconds")

    choice = input("Another site or Exit? [A/E]: ")
    if choice.upper() == 'E':
        break
