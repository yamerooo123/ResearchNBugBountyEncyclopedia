**Researched by Suphawith Phusanbai**

<h1>Microrealestate</h1>

**About**

This is an Open Source Real estate management system that helps landlords to manage their rentals and properties

GitHub repo: https://github.com/microrealestate/microrealestate

**Findings**

-Lack of input validation



**Details**

1. "Name" object doesn't validate input. For example, it allows users to use the name with special letters. 

 ![image](https://github.com/user-attachments/assets/b96d0889-6d5e-414a-96d4-9fb1424f8b99)

As you can see in the picture the website allows users to use **"tester&<script>alert('XSS')</script>"**. Futhurmore, it causes the confusion to the web server leading to ERROR 404

![image](https://github.com/user-attachments/assets/1ac9c54f-d05a-49a2-8ae1-8aa5bcff57a9)

