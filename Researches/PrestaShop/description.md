**Background**

According to the OWASP Framework, CSV Injection, also known as Formula Injection, occurs when websites embed untrusted input inside CSV files.
When a spreadsheet program such as Microsoft Excel or LibreOffice Calc is used to open a CSV, any cells starting with =, +, - and @ will be interpreted by the software as a formula.

Source: https://owasp.org/www-community/attacks/CSV_Injection 

**Summary**

A vulnerability in PrestaShop version 8.2.1 in which it allows attackers to inject malicious formulas into the exported CSV file through the "Get My Data to CSV" function due to insufficient input validation in Alias parameter from "Update your address" function. 

**Impact**

Maliciously crafted formulas can be used for three key attacks:

- Hijacking the user’s computer by exploiting vulnerabilities in the spreadsheet software, such as CVE-2014-3524.
- Hijacking the user’s computer by exploiting the user’s tendency to ignore security warnings in spreadsheets that they downloaded from their own website.
- Exfiltrating contents from the spreadsheet, or other open spreadsheets.

**Step to reproduce**

1 Login into a customer account
2 Navigate to Home > Your Account and select "Addresses" menu
3 Create a new address with alias value as shows in the following image > fill out mandatory fields and save form.

![image](https://github.com/user-attachments/assets/c38ebf9f-12e8-4993-b622-fc69dfde397a)

4 Navigate to GDPR - Personal data menu > Get My Data To CSV. 
5 Open the exported CSV file in which the malicious formula that was injected into the cell will be triggered. 

![image (1)](https://github.com/user-attachments/assets/b439ed57-8f99-467e-af58-7a31e8f545ba)

**Remediation**

The researcher found that the system is not allowed "=" to be included in Alias value for security reasons. However, to ensure that the input is sanitized and CSV file is safe to open:
Wrap each cell field in double quotes

1 Prepend each cell field with a single quote
2 Escape every double quote using an additional double quote
3 Add "+", "-", "@" or any special characters in the blacklist. 

In addition, the researcher recorded a PoC video for demonstration in the below private YouTube link.

Poc video: https://youtu.be/PbYDA4d9pAc
