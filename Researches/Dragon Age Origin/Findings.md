<h1>Dragon Age Origins</h1>

<h3>Game</h3>

Explore a stunning world, make complex moral choices, and engage in bone-crushing combat against massive and terrifying creatures. The Ultimate Edition includes Dragon Age: Origins, Dragon Age: Origins - Awakening and all nine content packs.

Steam link: https://store.steampowered.com/app/47810/Dragon_Age_Origins__Ultimate_Edition/

**Findings:**

Unquoted Service Path 

**Details**

PowerUp.ps1 shows that there is a vulnerability in **DAUpdaterSVC** which is a service used for downloading game contents.

![image](https://github.com/user-attachments/assets/81c30774-1a05-4148-9ab7-b79aa10a57ac)

Furthurmore, by default, the service file allows users to modify the path.

![image](https://github.com/user-attachments/assets/21b55fc8-6c4b-432b-bc76-403e5150f1b5)

Manual testing found that unprivileged users have Full Access privileges on this service. This misconfiguration is potentially vulnerable to unquoted service path. The attackers can abuse this to gain RCE.

![image](https://github.com/user-attachments/assets/608637dc-ba15-4b12-9880-0c9f11afeed6)



