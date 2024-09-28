CVE Submitted: 

**Product: Operately v0.1.0**

Open-source application repository: https://github.com/operately/operately

**Finding:**

Remote Code Execution (RCE) through Unrestricted File Upload in Discussion

**Impact:**

Remote Command Execution

**Details:**

The file upload function in the Discussions tab allows privileged users to upload files without validating file extensions or content types. Users who download and execute the malicious attached
file in the Discussion tab will send the connection back to an attacker machine, leading to the compromise of the machine

Unrestricted File Upload: The application does not restrict file types or extensions, allowing any files to be uploaded. This poses a risk if an attacker uploads a file that contains malicious code.

**Testing Scenario (Privileged User):**

![image](https://github.com/user-attachments/assets/c3e40e90-2099-4763-8d0a-00bfe9cb4bb8)

**Mitigation:**

Implement validation checks on file uploads to restrict file types and extensions. Use a whitelist to allow only safe file types and ensure that file contents are properly inspected before processing.


**Notes:**
Proof of Concept (PoC): https://youtu.be/rCYIohrQdxM
