<h1>QUELEA</h1>

<h3>About</h3>

Open source projection software for churches.

Link: https://github.com/quelea-projection/Quelea

**Finding**

Default Password: quelea

![image](https://github.com/user-attachments/assets/c9bea1bd-997e-4663-b1fb-08aeb0425cea)


**Technology stack:**

-OpenJDK 

-Log4J v. 2.21.1 

**Details**


1. When saves file as Schedule, the file extension will be converted to **.qsch** (Quelea Schedule). 

![image](https://github.com/user-attachments/assets/ed0f19a8-c428-40c2-bef9-a22d55dc61d1)
![image](https://github.com/user-attachments/assets/b6a0307b-9385-48ff-ae2e-02c3fb736c08)

Upon inspecting the file type, it shows that the file is ZIP file containing "**.xml**"

![image](https://github.com/user-attachments/assets/6e03732a-5d1f-46d7-bbc7-5062b17eabd5)
![image](https://github.com/user-attachments/assets/2b73be6a-588a-4e2f-9a4d-644785431418)

The information in .XML contains Schedule configuration in "schedule" tag.

![image](https://github.com/user-attachments/assets/e46920be-911a-47d2-b928-badaf7ed9c80)

The below table shows how Quelea stored each file in XML

| File   | Format tag          |
|--------------|-------------|
| PowerPoint      | filepresentation    |
| Website link       | url    |
| Video       | filevideo    |
| Timer       | timer    |
| Timer title       | name    |
| Duration       | Time    |
| PDF       | filepdf    |
| Image       | fileimage   |

2. The following function is used to save file as **.qsch** using **import org.quelea.services.utils.QueleaProperties;**

![image](https://github.com/user-attachments/assets/32b8dd57-d123-407e-a1f6-eda59a984290)


<h2><b>ScheduleSaver.java source code summary</b></h2><br />
<br />

1. it creates a panel for a user to choose where to save using javafx

2. it checks for the file extension. 

3. it checks for existing file. If there is already the existing file, it asks for a permission to overwrite.

4. if conditions are met, it saves the file else show an error.

<h2><b>QueleaProperties Save Schedule File As .qsch</b></h2><br />
<br />

![image](https://github.com/user-attachments/assets/58b3dcd1-e799-4860-81a5-ff80b7af43c4)

<h2><b>QueleaProperties Save Song File As .qsp</b></h2><br />
<br />

![image](https://github.com/user-attachments/assets/91d3c716-c764-4d9f-ba19-0a4c2cdcff84)

**Note: Media files are specified in absolute path. This means that if it couldn't retrieve files that specified in the path, it won't return the file and display error window**  

![image](https://github.com/user-attachments/assets/80a5c20a-9de5-4bab-b411-b60360913fda)

![image](https://github.com/user-attachments/assets/87132ec4-e081-4f39-b0a4-b6756e7863d1)


