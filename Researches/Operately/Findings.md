Researched by: Suphawith Phusanbai (Security Researcher)

**Operately v0.1.0**

Every startup needs to align on goals, run projects, track KPIs, and standardize processes. However, figuring out the right systems that tie everything together is tough, and keeping them in order, even tougher.

That’s why we’re building Operately: to give startups and SMBs the tools to become a high-performance organization with 10x less effort.

This project is in alpha and may experience significant changes.

**Finding**

-No rate limiting 

**Details**

**Updated on Sep 10**

-Operately doesn't utilize traditional javascript tag. The javascript resource is being called through **/assets/app-741d8c0f04754f324e315d53e4ff3083.js**

-In appearance tab, when trying to change the theme, the application sends API request which is **/api/v2/update_profile** along with following data **id** and **theme** requried in JSON. The theme parameter has 3 options: **light**, **dark** and **system**. If the value inside theme parameter isn't one of them, the app won't render the correct color. resulting in white default background.
-The **id** is string with some kind of token after the username (For some reason, the token didn't change after re-login)
![image](https://github.com/user-attachments/assets/d089ece3-bd24-4e5e-8a64-38d7cb327252)

-The unique identifier or token can be found at http://localhost/whitehathacker-0bgk/people/ after intercepting the request. Every times the earlier URL request is being used, the **/api/v2/get_person** resource will be used. This API request reveals the real value of ID.










