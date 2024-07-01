import requests

def find_subdomain(domain_as_input):
    wordlist = open('WTFCloud\\subdns.txt', 'r')
    storing = wordlist.read()
    stored = storing.splitlines()
    print("Find a place to save the result!")
    for n in stored:
        # can change to http or https
        add_subdns_portion = f"https://{n}.{domain_as_input}" 
        print(f"Checking: {add_subdns_portion}")  # Verbose output for each subdomain
        try:
            search_subdns = requests.head(add_subdns_portion, timeout=5)  # Use HEAD request to avoid downloading content
            if search_subdns.status_code == 200:
                print(f'[+] {add_subdns_portion} exists!')
            else:
                print(f'[-] {add_subdns_portion} does not exist.')
        except requests.Timeout:
            print(f'[!] Timeout while trying to connect to {add_subdns_portion}')
            continue  # Ensure it continues to the next subdomain
        except requests.RequestException as e:
            print(f'[!] Error accessing {add_subdns_portion}: {e}')
            continue  # Ensure it continues to the next subdomain

    wordlist.close()
    print("Subdomain enumeration completed.")

# Usage
domain_as_input = "google.com"
find_subdomain(domain_as_input)
