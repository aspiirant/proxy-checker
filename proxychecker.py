import requests

# function to check if a proxy is working
def check_proxy(proxy):
    try:
        response = requests.get("https://www.example.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return True
    except Exception as e:
        print(f"Exception occurred: {e}")
    return False

# main function
def main():
    print("Thank you for using my tool!")

    while True:
        command = input("Type check to begin (exit to stop): ")

        if command == "":
            print("No command was entered! Please try again.")
            break

        if command == "exit":
            print("Quitting..")
            break

        elif command == "check":
            file_path = input("Enter the path to the proxy file: ")

            # read the proxies from the file
            with open(file_path, 'r') as file:
                proxies = file.read().splitlines()

            available_proxies = []

            # check if the proxies are working
            for proxy in proxies:
                if check_proxy(proxy):
                    print(f"Proxy {proxy} is working!")
                    available_proxies.append(proxy)
                else:
                    print(f"Proxy {proxy} is not working!")

            # select your output file_path
            output_file_path = input("Enter the path to the output file: ")

            # write available proxies to that file_path
            with open(output_file_path, 'w') as file:
                for proxy in available_proxies:
                    file.write(proxy + "\n")

            if available_proxies:
                print(f"Succesfully printed all the available proxies to {output_file_path}")
            else:
                print("No proxies were available!")

if __name__ == "__main__":
    main()
