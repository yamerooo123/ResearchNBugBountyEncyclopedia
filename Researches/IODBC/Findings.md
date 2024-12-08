<h1>IODBC</h1>

It is a database API before the SQL statement from user input sends to the database, it has to pass the database API first. 

![image](https://github.com/user-attachments/assets/83b01071-8429-474d-a68a-bbdb61e2e1f3)


**Buffer Overflow Testing**
---

1. Set up the environment for testing [HERE](https://github.com/yamerooo123/ResearchNBugBountyEncyclopedia/blob/main/Researches/IODBC/Prep.md)

2. Install **CWE_checker**. It is a static analysis tool that using Ghidra and other tools. [HERE](https://github.com/fkie-cad/cwe_checker) or via Docker
```
docker pull ghcr.io/fkie-cad/cwe_checker:latest
```
Then run the following command to test **iodbctest**
```
docker run --rm -v /usr/bin/iodbctest:/input ghcr.io/fkie-cad/cwe_checker /input
```

**Output**
---

