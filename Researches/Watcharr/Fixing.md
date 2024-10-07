**Problem: JWT token allows a blank password to verify a signature.**

**Note:**

Developers forced the web app to use JWT_SECRET in Watcharr.json. Theoretically, it should work. But the problem still persists.

![image](https://github.com/user-attachments/assets/f425dc9c-b084-4f97-88a9-21d92acd5050)


**Analysis**

-JWT JSON Data Construction

![image](https://github.com/user-attachments/assets/08890eb7-d562-4dcb-b32e-dfb89975f1de)

**jwt.RegisteredClaims** = For customed types. It performs standard verification.

Checking for **Authorization** in the request. This **Authorization** is used for storing JWT token
![image](https://github.com/user-attachments/assets/279c9a5e-2414-4a9f-ae72-411783709be1)

**Conditions:**

1. If Authorization(token) is missing, return HTTP error 401. &check;

2. Parse the token

3. In line 210th, **return []byte(Config.JWT_SECRET), nil**. This **Config** is **ServerConfig** which read config from **/data** where **Watcharr.json** is being stored. The sourcecode is **Config.go**.
   
