<h1>Dragon Age Origins</h1>

Explore a stunning world, make complex moral choices, and engage in bone-crushing combat against massive and terrifying creatures. The Ultimate Edition includes Dragon Age: Origins, Dragon Age: Origins - Awakening and all nine content packs.
Steam link: https://store.steampowered.com/app/47810/Dragon_Age_Origins__Ultimate_Edition/

Findings:
---
Unquoted Service Path

**Details**
---

PowerUp.ps1 shows that there is a vulnerability in **DAUpdaterSVC** which is a service used for downloading game contents.

![image](https://github.com/user-attachments/assets/81c30774-1a05-4148-9ab7-b79aa10a57ac)

Furthermore, by default, the service file allows users to modify the path.
![image](https://github.com/user-attachments/assets/21b55fc8-6c4b-432b-bc76-403e5150f1b5)

Manual testing found that unprivileged users have Full Access privileges on this service. This misconfiguration is potentially vulnerable to unquoted service path. The attackers can abuse this to gain RCE or privilege escalation.

![image](https://github.com/user-attachments/assets/608637dc-ba15-4b12-9880-0c9f11afeed6)

In order to exploit, this i crafted .exe file which containing the following commands.

![image](https://github.com/user-attachments/assets/242cfb65-7da7-4b59-87b1-bbe210347dc6)

Then compiled it to .exe file
![image](https://github.com/user-attachments/assets/caaff9a5-2e9e-4570-937f-b993d6092dbe)

For the last preparation step, move the maliciois file to destination path.

![image](https://github.com/user-attachments/assets/872cfae9-8bbd-420b-bbe5-5e80c140de3f)

Before exploiting the vulnerability

![image](https://github.com/user-attachments/assets/5c39435e-bad3-4734-bedc-cd8188ef7507)

After exploiting the vulnerability

![image](https://github.com/user-attachments/assets/15fd20ca-77c3-451f-9873-42630f3d8b21)
