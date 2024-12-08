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

The result shows that there is issues related to buffer overflow vulnerability when calling **pthread_mutex_lock** function, Null Pointer Dereference and Stack Memory Exhaustion

![image](https://github.com/user-attachments/assets/a177e661-bd07-45d0-8aa8-4e3aab4b2cb6)

![image](https://github.com/user-attachments/assets/9c63ccf8-1374-4e7e-8f6e-24d9e6bee6c2)

![image](https://github.com/user-attachments/assets/c3a37d49-45a2-4bf2-9064-de3c30bdc18a)




