#CloudFlare detection by detecting ip address by B0untyHunt3rM0n4
#version 0.1 beta
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
    except socket.gaierror as error:
        print(f"the man couldn't found what thou seek. Reason: {error}")


#sometimes the function may return an error due to target security is STONKS!
#the function is simply sending GET request to HTTP instead of HTTPS and turning off SSL cert.
#You may try HEAD request method or use Burp Suite to try to different request methods.

def search_by_ip(ip_input):
    #can switch to http or https
    url = requests.get(f'https://{ip_input}', verify=False)
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


#usage: just python3 or python WTFCloud.py. 
ip_as_input = input(r"hostname(1) or IP address(2) or any button to exit:")

if ip_as_input == "1":
    try:
        domain_as_input = input("thee shall give me a name:")
        search_by_domain(domain_as_input)
    except socket.herror as error:
        print("the man couldn't find it. Give me the man URL such as google.com, yahoo.com etc")
    
    
elif ip_as_input == "2":
    try:
        ip_input = input("thee shall give me an IP address:")
        search_by_ip(ip_input)
    except socket.gaierror:
        print("the man couldn't found what thou seek")
else:
    print("The man will disappear now...")
    