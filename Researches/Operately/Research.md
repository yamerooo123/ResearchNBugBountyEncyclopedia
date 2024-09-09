Researched by: Suphawith Phusanbai (Security Researcher)

**Operately**

Every startup needs to align on goals, run projects, track KPIs, and standardize processes. However, figuring out the right systems that tie everything together is tough, and keeping them in order, even tougher.

That’s why we’re building Operately: to give startups and SMBs the tools to become a high-performance organization with 10x less effort.

This project is in alpha and may experience significant changes.

**Finding**

**Details**

-Operately doesn't utilize traditional javascript tag. The javascript resource is being caleld through **/assets/app-741d8c0f04754f324e315d53e4ff3083.js**

-In appearance tab, when trying to change the theme, the application sends API request which is **/api/v2/update_profile** along with following data **id** and **theme**. The theme parameter has 3 options: light, dark and system. If the value inside theme parameter isnt one of them, the app won't render the correct color. resulting in white default background.
There is a possibiltiy for the attacker to find broken access control vulnerability in the POST API request to try to change other users theme if the attacker figures out the token that display after the username.
![image](https://github.com/user-attachments/assets/d089ece3-bd24-4e5e-8a64-38d7cb327252)



