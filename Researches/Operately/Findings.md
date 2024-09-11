Researched by: Suphawith Phusanbai (Security Researcher)

**Operately v0.1.0-alpha**

Every startup needs to align on goals, run projects, track KPIs, and standardize processes. However, figuring out the right systems that tie everything together is tough, and keeping them in order, even tougher.

That’s why we’re building Operately: to give startups and SMBs the tools to become a high-performance organization with 10x less effort.

This project is in alpha and may experience significant changes.

Open-source project repo: https://github.com/operately/operately

**Finding**

-No rate limiting(reported) 

-Remote Code Execution(RCE) through unrestricted file upload in Discussion(reported)

**Impact: Remote Command Execution, Denial of service and resource exhaustion**

**Details**

**Updated on Sep 10**

-Operately uses API to call for CSS resources. The javascript resource is being called through **/assets/app-741d8c0f04754f324e315d53e4ff3083.js**

-In appearance tab, when trying to change the theme, the application sends API request which is **/api/v2/update_profile** along with following data **id** and **theme** requried in JSON. The theme parameter has 3 options: **light**, **dark** and **system**. If the value inside theme parameter isn't one of them, the app won't render the correct color. resulting in white default background.
-The **id** is string with some kind of token after the username (For some reason, the token didn't change after re-login)
![image](https://github.com/user-attachments/assets/d089ece3-bd24-4e5e-8a64-38d7cb327252)

-The unique identifier or token can be found at http://localhost/whitehathacker-0bgk/people/ after intercepting the request. Every times the earlier URL request is being used, the **/api/v2/get_person** resource will be used. This API request reveals the real value of ID.

-The **/api/v2/add_company** POST request has no privilege implemented. Any users can create their own channels. This means an attacker abuse this flaw to trigger resource exhaustion or denial of service.
![image](https://github.com/user-attachments/assets/c7c85093-a6dd-4c0c-9180-39657e5e6120)

**Testing scenario(Authenticated user):**
![image](https://github.com/user-attachments/assets/b7c5bd75-85f3-44c3-9789-e384f34c163e)

**Mitigation:**

The application should create application administrator role to manage all channels to mitigate the risk.


-The application doesn't validate file extension. It allows any types to be uploaded. 
![image](https://github.com/user-attachments/assets/85ad4e27-76c2-43d9-81a4-edabc64c2480)

**Testing scenario(Privileged user)**
![image](https://github.com/user-attachments/assets/c3e40e90-2099-4763-8d0a-00bfe9cb4bb8)

**Mitigation:**

Preliminarily, the function should validate Content type and file extensions by implementing the whitelist to ensure only safe file extensions are allowed to be uploaded.








