from portscan import *

def port_scan(HoI_as_input):
    # Uncomment and use if you have a port list file
    # port_wordlist = open('UniversalKit/port1000top.txt', 'r')
    # storing = port_wordlist.read()

    storing = '1-10000'
    try:
        scanning = PortScan(HoI_as_input, storing, thread_num=500, show_refused=False, wait_time=3, stop_after_count=True)
        discovered_ports = scanning.run()
        
    except ValueError:
        print(r'Eh! something does not feel right')

    answer_me = input("All done! \n"
                      "Would you like to scan for a specific port? Y/N: ")

    if answer_me == "Y":
        target_port = input("Enter the specific port number: ")
        try:
            scanning = PortScan(HoI_as_input, target_port, thread_num=500, show_refused=False, wait_time=3, stop_after_count=True)
            discovered_ports = scanning.run()
            
        except ValueError:
            print(r'Eh! something does not feel right')
    else:
        print('Bye!')

# Example usage
if __name__ == "__main__":
    HoI_as_input = input("Enter IP: ")
    port_scan(HoI_as_input)
