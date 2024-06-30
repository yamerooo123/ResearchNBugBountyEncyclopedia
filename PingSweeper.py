#For network pentesting! Actually you can use Nmap -sn <ip> but i prefer my own script lol
#PingSweeper finds all alive hosts that response to ICMP requests by B0untyHunt3rM0n4
#version 0.1 beta
#DISCLAIMER 
#Use it at your own risk and under law regulations. Happy hacking!
#Feel free to modify the code.
from pythonping import *

def TrySinglePing(network_portion):
    PingThis = ping(f'{network_portion}', verbose=False)
    print(PingThis)
    
def TryMultiplePing(network_portion):
    RemoveLastIPportion = network_portion.rsplit('.', 1)[0]
    for n in range(1,255):
        AutoIncrement = f'{RemoveLastIPportion}.{n}'
        Ping = ping(f'{AutoIncrement}', verbose=False)
        if Ping.success:
            print(f"Reachable: {Ping}")
        else:
            print(f"Unreachable: {Ping}")



#usage 
enter_input = input("Do you want to ping a single IP address or the whole network?(Type 1 or 2): ")
if enter_input == "1":
    network_portion = input("Enter IP address: ")
    TrySinglePing(network_portion)
elif enter_input == "2":
    network_portion = input("Enter IP network portion: ")
    TryMultiplePing(network_portion)
else:
    print("I will just disappear until you call me again.")