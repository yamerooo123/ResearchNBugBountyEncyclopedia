#a tool with many features that perform simple automating tasks by B0untyHunt3rM0n4
#version 0.2 beta
#DISCLAIMER 
#Use it at your own risk and under law regulations. Happy hacking!
#Feel free to modify the code.
import socket
import requests

#if you get "socket.gaierror: [Errno 11001] getaddrinfo failed" mean you enter the incorrect host address.
def search_by_domain(domain_as_input):
    try:
        domain_name = socket.gethostbyname(domain_as_input)
        print(f"the man found {domain_name}")
        if domain_name.startswith("104."):
            print('the man can smell dirty CloudFlare. No need to try reverse DNSlookup.')
        else:
            return
    except socket.gaierror as error:
        print(f"the man couldn't found what thou seek. Reason: {error}")


#sometimes the function may return an error due to target security is STONKS!
#the function is simply sending GET request to HTTP instead of HTTPS and turning off SSL cert.
#You may try HEAD request method or use Burp Suite to try to different request methods.

def search_by_ip(ip_input):
    #can switch to http or https
    url = requests.get(f'http://{ip_input}', verify=False)
    try:
        ip_addr = socket.gethostbyaddr(ip_input)
        print(f"the man found {ip_addr}")
        if url.status_code == 200:
            print("the man is certain. there is no domain protection")
            print(url.text) 
        else:
            print(f"failed with status code: {url.status_code}")
    except socket.herror as error:
        print(f"the man couldn't found what thou seek: reason {error}")

def find_subdomain(domain_as_input):
    wordlist = open('WTFCloud\subdns.txt', 'r')
    storing = wordlist.read()
    stored = storing.splitlines()
    print("Find a place to save the result!")
    for n in stored:
        #can change to http or https 
        add_subdns_portion = f"https://{n}.{domain_as_input}" 
        try:
            search_subdns = requests.get(add_subdns_portion, timeout=5)
            if search_subdns.status_code == 200:
                print(f'[+] {add_subdns_portion}')
            else:
                pass
        except requests.Timeout:
            pass
        except requests.RequestException:
            continue


#usage: just python3 or python WTFCloud.py. 
host_or_ip_as_input = input("Find Hostname/domain(1) \n"
                            "Find IP address(2) \n"
                            "Find Subdomain(3) \n"
                            "any button to exit:")

if host_or_ip_as_input == "1":
    try:
        domain_as_input = input("thee shall give me a name:")
        search_by_domain(domain_as_input)
    except socket.herror as error:
        print("the man couldn't find it. Give me the man URL such as google.com, yahoo.com etc")
    
    
elif host_or_ip_as_input == "2":
    try:
        ip_input = input("thee shall give me an IP address:")
        search_by_ip(ip_input)
    except socket.gaierror:
        print("the man couldn't found what thou seek")

elif host_or_ip_as_input == "3":
    try:
        domain_as_input = input("thee shall give me a name:")
        find_subdomain(domain_as_input)
    except socket.herror as error:
        print("the man couldn't find it. Give me the man URL such as google.com, yahoo.com etc")

else:
    print("The man will disappear now...")
    