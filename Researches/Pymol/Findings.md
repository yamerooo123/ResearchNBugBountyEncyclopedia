**Research by Suphawith Phusanbai**

<h1>Pymol</h1>

Open-source foundation of the user-sponsored PyMOL molecular visualization system.

GitHub repo: https://github.com/schrodinger/pymol-open-source

**Tested on:**

Distributor ID: Ubuntu

Description:    Ubuntu 22.04.5 LTS

Release:        22.04

Codename:       jammy

<h1>Findings</h1>

1. RCE through the Run Script function

<h3>Description</h3>

This vulnerability should be described as design limitation as the fucntion is work as it intended but possessed a serious issue if the feature is used for malicious activities. However, this issue has raise the same vulnerability suggested in CVE-2019–9193 and CVE-2023-28311.

**CVE-2019–9193** allows authenticated users to gain RCE through SQL statement.

**CVE-2023-28311** allows attackers to embed VBS script which is a Microsoft office feature. Once the victim opens the file, the VBS script automatically executes the script, leadning to RCE.

<h1>Details</h1>

The software implements serveral dangerous Python functions without input sanitization. For instance, a file with PYM file extension is treated the same as a Python, allowing the attackers to insert a malicious PYM file with reverse shell payload. This could potentially lead to RCE.

<h1>Testing scenario</h1>

1. Prepare a malicoius PYM file. Inside the file is a reverser shell payload

![image](https://github.com/user-attachments/assets/9674c700-e754-45aa-9450-98e558aff4d3)

2.  Select Run Script

![image](https://github.com/user-attachments/assets/fedfaade-c25d-4f1e-b68d-68cf163db4ec)

3. Run a listening port

4. Select a malicious file to execute RCE

![image](https://github.com/user-attachments/assets/4c6afb1c-7e31-46e1-9e77-7ae8f489cc22)

5. Result

![image](https://github.com/user-attachments/assets/0bf3564c-d652-4519-a8b5-aac6d935c980)


