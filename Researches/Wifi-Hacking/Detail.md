Wifi Hacking Home Lab
---
**What you need:**

1. Realtek 8811CU Wireless LAN 802.11a
2. Kali Linux

Preparation
---

1. Make sure VM is using WiFi adapter or else Kali won't be able to detect it.

![image](https://github.com/user-attachments/assets/49f2b086-5d4f-4b9f-b57a-93e52e6ba5c5)

2. To verify it, you need to ensure that  wlan0 network interface is show up.
![image](https://github.com/user-attachments/assets/c9130857-0182-4e83-b128-801d614aa824)

3. Turn on **Monitor mode** using
```
sudo airmon-ng start wlan0
```
![image](https://github.com/user-attachments/assets/61134cd1-31ba-4be3-b0f8-8be3f9db30b8)
![image](https://github.com/user-attachments/assets/6b446609-5206-45bd-ac6a-1fd12736d483)

At this point, when we check NIC again, you will see that wlan0 status is now UP.

4. Now, run **airdump-ng wlan0** to find nearby wifi.
![image](https://github.com/user-attachments/assets/93697011-8291-4494-b101-8d41c30ac6db)

Airdump shows us nearby access points and the name of WiFi. This indicates that our rogue access point is now ready to rock, we are now ready to perform WiFi attacking!

**Experimentation**
---
Deauthentation (AKA. DeAuth attack) 
---
is DoS attack that disconnect users in the network. It happens when rouge access point (our evil wifi) send deauthentication frame to the victim access point, making them unable to use WiFi.

**Example**

In this excample, i am using my own WiFi for testing purpose.
Run 
```
sudo aireplay-ng --deauth 100 -a E8:81:75:CB:3F:D4 -D wlan0
``` 
You can accesss specify host that you want to disconnect with **-c** following by their MAC address.
![image](https://github.com/user-attachments/assets/a5457737-c7ff-4019-98c7-34895dba72e8)

The result is i was not able to connect to my WiFi.

**Before the command execution:**
![image](https://github.com/user-attachments/assets/6cb5b7f1-5dfc-4abb-8a98-40ee36a2aa09)

**After the command execution:**
![image](https://github.com/user-attachments/assets/3e670553-db33-49cb-a3e8-1583f2a4d280)

**WiFi automatically switched to available WiFi:**
![image](https://github.com/user-attachments/assets/b5cd14e0-a754-478f-a150-470707451967)

WiFi Password Cracking
---
We can use **.cap** files which we obtained when our rogue access point went wild. We can use Hashcat to crack password!


**References:**
---
https://predatech.co.uk/capturing-and-cracking-wpa-wpa2-wifi-passwords/
https://github.com/ricardojoserf/wifi-pentesting-guide
