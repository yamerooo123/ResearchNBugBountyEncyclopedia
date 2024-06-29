import socket
import requests

def search_by_ip(ip_input):
    try:
        # Perform reverse DNS lookup
        ip_addr = socket.gethostbyaddr(ip_input)
        print(f"The man found {ip_addr}")
        
        # Construct the URL
        url = f'https://{ip_input}'
        
        # Make the HTTP request
        response = requests.get(url)
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful. Printing content:")
            print(response.text)  # Print the HTML content of the webpage
        else:
            print(f"Request failed with status code: {response.status_code}")
    
    except socket.gaierror:
        print("The man couldn't find what thou seek: DNS resolution error")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")

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
    
