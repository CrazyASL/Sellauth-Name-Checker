import random
import string
import requests

def display_banner():
    banner = """
███████╗███████╗██╗     ██╗      █████╗ ██╗   ██╗████████╗██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔════╝██║     ██║     ██╔══██╗██║   ██║╚══██╔══╝██║  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████╗█████╗  ██║     ██║     ███████║██║   ██║   ██║   ███████║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
╚════██║██╔══╝  ██║     ██║     ██╔══██║██║   ██║   ██║   ██╔══██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║███████╗███████╗███████╗██║  ██║╚██████╔╝   ██║   ██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """
    print(banner)

def generate_random_subdomain(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def check_subdomain(subdomain):
    url = f'https://{subdomain}.sellauth.com/'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0',
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"\033[91mTaken | {subdomain}.sellauth.com\033[0m")
        else:
            print(f"\033[92mAvailable | {subdomain}.sellauth.com\033[0m")
    except requests.RequestException:
        print(f"\033[92mAvailable | {subdomain}.sellauth.com\033[0m")

def main():
    display_banner()
    num_subdomains = int(input("How many subdomains to check? "))
    length_of_subdomain = int(input("Length of subdomains: "))

    for _ in range(num_subdomains):
        random_subdomain = generate_random_subdomain(length_of_subdomain)
        check_subdomain(random_subdomain)

    print("\nDeveloped by notcrazyfrr | discord.gg/slotting")

if __name__ == "__main__":
    main()
