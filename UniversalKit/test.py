from portscan import *
import requests
def port_scan(HoI_as_input):
    try:
        with open(r'UniversalKit\port1000top.txt', 'r') as port_wordlist:
            storing = port_wordlist.read().strip().split(',')
        
        # Assuming PortScan class initialization and usage
        scanning = PortScan(HoI_as_input, storing, thread_num=500, show_refused=False, wait_time=3, stop_after_count=True)
        open_port_discovered = scanning.run()
        
        if open_port_discovered:
            print(f"Open ports: {open_port_discovered}")
        else:
            print("No open ports discovered.")
        
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError as ve:
        print(f"ValueError: {ve}. Please check the input parameters.")
    except requests.RequestException as re:
        print(f"RequestException: {re}. Please check your network and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    HoI_as_input = input("Enter IP: ")
    port_scan(HoI_as_input)
