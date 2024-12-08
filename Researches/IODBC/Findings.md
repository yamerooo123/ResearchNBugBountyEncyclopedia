<h1>IODBC</h1>

It is a database API before the SQL statement from user input sends to the database, it has to pass the database API first. 

![image](https://github.com/user-attachments/assets/83b01071-8429-474d-a68a-bbdb61e2e1f3)


**Buffer Overflow Testing**
---

1. Set up the environment for testing [HERE](https://github.com/yamerooo123/ResearchNBugBountyEncyclopedia/blob/main/Researches/IODBC/Prep.md)

2. Install **CWE_checker**. It is a static analysis tool that combining Ghidra and other tools. [HERE](https://github.com/fkie-cad/cwe_checker) or via Docker
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

4. Next, we will perform binary analysis using GDB.

Run the following command
```
gdb /usr/bin/iodbctest
```
![image](https://github.com/user-attachments/assets/22d03d5f-4668-4921-b6c9-ca1d15d3d10c)

5. Set breakpoints. Breakpoint in debugger means we want to pause(like freeze) the program when one or more particular functions are being called. In this case we found that buffer overflow occurs where **pthread_mutex_lock** is being used.
```
break pthread_mutex_lock
break strcpy
```
![image](https://github.com/user-attachments/assets/56ec5e56-c86a-482a-9455-848d307a8eae)

6.Then run the debugger.

**Output**
---
```
(gdb) run
Starting program: /usr/bin/iodbctest
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
iODBC Demonstration program
This program shows an interactive SQL processor

Breakpoint 1, ___pthread_mutex_lock (mutex=0x555555652460 <iodbcdm_global_lock>) at ./nptl/pthread_mutex_lock.c:77
77      ./nptl/pthread_mutex_lock.c: No such file or directory.
(gdb)
```

As you can see that, **iodbctest** called **libthread_db.so.1** and then printed out some string. Then the first breakpoint crashes in the 77th line in **./nptl/pthread_mutex_lock.c**. Since this is a binary without sourcecode which is why GDB couldnt find pthread_mutex_lock.c

Inspecting memory and stack ( in the picture below is "stack". But before it becomes a stack, it was a buffer such as a string)
```
x/32x $sp
```
![image](https://github.com/user-attachments/assets/d6685e79-8787-4e32-9b77-6f7b69b7bfb3)



