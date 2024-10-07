**Problem: JWT token allows a blank password to verify a signature.**

JWT JSON Data Construction

![image](https://github.com/user-attachments/assets/08890eb7-d562-4dcb-b32e-dfb89975f1de)

**jwt.RegisteredClaims** = For customed types. It performs standard verification.

Checking for **Authorization** in the request. This **Authorization** is used for storing JWT token
![image](https://github.com/user-attachments/assets/279c9a5e-2414-4a9f-ae72-411783709be1)

**Conditions:**
1. If Authorization(token) is missing, return HTTP error 401. |checked|
