import requests

def check_proxy(proxy):
    try:
        response = requests.get("https://www.example.com", proxies={"http": proxy, "https": proxy}, timeout=10)
        if response.status_code == 200:
            return True
    except Exception as e:
        pass
    return False

def main():
    # Fill the list with your own proxy sites
    proxy_list = [
        "http://proxy1.example.com:8080",
        "http://proxy2.example.com:8080",
        "http://proxy3.example.com:8080",
        # Add more proxy servers as needed
    ]

    available_proxies = []

    for proxy in proxy_list:
        if check_proxy(proxy):
            available_proxies.append(proxy)

    # Write the available proxies to a text file
    with open("available_proxies.txt", "w") as file:
        file.write("\n".join(available_proxies))

if __name__ == "__main__":
    main()
