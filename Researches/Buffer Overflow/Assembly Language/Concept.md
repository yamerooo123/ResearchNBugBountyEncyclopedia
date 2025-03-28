<h1>Assembly Language</h1>

-It is a low-level language that allow human to interact with the computer since the computer knows only 1 or 0.

-This instruction can be inject to the computer memory

<h1>Computer Architecture</h1>


![image](https://github.com/user-attachments/assets/1405d948-696e-4fe6-86e8-b433cc91205b)

Normally, data is sent to cache or RAM. This is where data are being stored. Then, from cache, data will be sent to CPU (Central Processing Unit) in which the CPU will call for a pointer to give an order where data will be sent to.



HIGH LEVEL vs LOW LEVEL
---
![alt text](HLvsLL.png)

Example of Assembly code

```
mov rax, 1
mov rdi, 1
mov rsi, message
mov rdx, 12
syscall

mov rax, 60
mov rdi, 0
syscall
```

The shellcode would look like this or we can call it hex code.

```
48 c7 c0 01
48 c7 c7 01
48 8b 34 25
48 c7 c2 0d
0f 05

48 c7 c0 3c
48 c7 c7 00
0f 05
```

then the computer changes the shellcode into binary

```
01001000 11000111 11000000 00000001
01001000 11000111 11000111 00000001
01001000 10001011 00110100 00100101
01001000 11000111 11000010 00001101 
00001111 00000101

01001000 11000111 11000000 00111100 
01001000 11000111 11000111 00000000 
00001111 00000101
```

Tip: Java operates similarly to assemly. To make it easier to understand.
```
Java Bytecode > shell code or machine code using Java runtime > binary
```

<h1>CPU Components</h1>

CPU or Computer Processing Unit has 3 components:

-Control Unit (CU)

-Arithmetic/Logic Unit (ALU) = For calculatio tasks

-Registers = fastest 

![alt text](image.png)

Clock Speed & Clock Cycle
---

Each cycle is equal to one instruction. Modern CPU have multiple cores. This means that CPU can process multiple instructions at a time. 
![image](https://github.com/user-attachments/assets/00d38bdf-704a-4533-8dae-aaa9e1e41d70)

How CPU works?
---
![image](https://github.com/user-attachments/assets/22f84e60-f41f-44c1-9e2f-385bef1dcadc)

**Instruction	Description**

1. Fetch	Takes the next instruction's address from the Instruction Address Register (IAR), which tells it where the next instruction is located.
2. Decode	Takes the instruction from the IAR, and decodes it from binary to see what is required to be executed.
3. Execute	Fetch instruction operands from register/memory, and process the instruction in the ALU or CU.
4. Store	Store the new value in the destination operand.

MEMORY
---

Memory in CPU have 2 types.

1. Cache - Pretty fast and faster than RAM
2. RAM - is bigger than cache 

When programs are running. it send intructions to storage > RAM to prepare for CPU since storage couldn't handle both things at the same time. 

RAM
---

There are 4 components in RAM.

1. Stack - Has a Last-in First-out (LIFO) design and is fixed in size. Data in it can only be accessed in a specific order by push-ing and pop-ing data.
2. Heap - Has a hierarchical design and is therefore much larger and more versatile in storing data, as data can be stored and retrieved in any order. However, this makes the heap slower than the Stack.
3. Data - Has two parts: Data, which is used to hold variables, and .bss, which is used to hold unassigned variables (i.e., buffer memory for later allocation).
4. Text - Main assembly instructions are loaded into this segment to be fetched and executed by the CPU.

<h1>IO/Storage</h1>

This storage gives command to input/output devices using **bus interfaces**. This bus interface uses electric to communicate with CPU which convert to binary later. Storage is the slowest because it stores permanent information such as OS files.

|  Component | Speed | Size |
| ------------- | ------------- | -------- |
| Registers  | Fastest | Bytes |
| L1 Cache  | Fastest, other than Registers | Kilobytes |
|  RAM | Much slower than all of the above  | Megabytes |
| L2 Cache  | Very fast |Megabytes |
|  L3 Cache | Fast, but slower than the above | Gigabytes-Terabytes |
| Storage  | Slowest  | Terabytes and more |

Processor Specific
---
Each processor understands a different set of instructions. For example, while an Intel processor based on the 64-bit x86 architecture may interpret the machine code 4883C001 as add rax, 1, an ARM processor translates the same machine code as the biceq r8, r0, r8, asr #6 instruction. As we can see, the same machine code performs an entirely different instruction on each processor.

Assembly
---
An example of Assembly code.
```
         global  _start

         section .data
message: db      "Hello HTB Academy!"

         section .text
_start:
         mov     rax, 1
         mov     rdi, 1
         mov     rsi, message
         mov     rdx, 18
         syscall

         mov     rax, 60
         mov     rdi, 0
         syscall
```

All those lines just to print out "Hello HTB Academy". -_-

Assembly code explanation
---
![image](https://github.com/user-attachments/assets/bb3f7ee4-7f63-4925-9cd4-bbe1448d9dff)

NASM
---

It is a tool for assembling code. 

**Example:**

**Assemble a file**

We write a new Assembly file using test.s and paste the code in it. After that we assemble it usiing nasm where we want the output file aS ELF64 so that we can run it in Linux OS.
```
nasm -f elf64 test.s
```

We will obtain test.o which has been assembled. However, we cannot use this yet. we need to link it using ld. This is pretty similar to GCC.
```
ld -o test test.o
```
![image](https://github.com/user-attachments/assets/b06ad7bf-47fb-475b-aea9-3e07ceac52b1)

We successfully created an Assembly file!

![image](https://github.com/user-attachments/assets/fb64f4d4-1f78-47f3-8643-ed3f3b6559c3)

**Disassemble a file**

To disassemble a file, use the following tool & command

```
objdump -d test_asm -m intel
```

Note: The reason we specify intel is because we are going to disassemble the file using intel syntax. Remember each CPU architecture has different syntax!

![image](https://github.com/user-attachments/assets/76bd48d6-68ce-489b-9380-183e8b027f01)

or this if you want to see only text
```
objdump -sj .data test_asm 
```

![image](https://github.com/user-attachments/assets/4c328682-dfd0-4527-8531-867c29199586)

GNU Debugger(GDB) + GEF
---
GEF is an extension for GDB. It is used for reverse engineering.

To use it with GDB.
```
wget -O ~/.gdbinit-gef.py -q https://gef.blah.cat/py
echo source ~/.gdbinit-gef.py >> ~/.gdbinit
```


Now try to open the Assembled file with GDB.

![image](https://github.com/user-attachments/assets/a99a0477-e562-4c81-8c71-82e71316eb6a)

In GDB, there are many commands that should help us in reverse engineering. 

For example, to figure out how many labels or variables in this file. We can use this
```
info variable
```

![image](https://github.com/user-attachments/assets/7e7b93dc-a012-4f77-bb4a-f7a3c87265f6)

In GDB, we should focus on these functions as these are important for us to reverse engineering!

| Step | Desc. | 
| ------------- | ------------- | 
| Break  | Setting breakpoints at various points of interest | 
| Examine  | Running the program and examining the state of the program at these points | 
| Step  | Moving through the program to examine how it acts with each instruction and with user input |
| Modify | Modify values in specific registers or addresses at specific breakpoints, to study how it would affect the execution |

**In a nutshell:**

Break or b => Stop where you want to investigae let say buffer overflow. Don't forget to add "*"!
```
b *0x401005
```

In case you want to unset breakpoints, you can simply **info breakpoints** and then delete 1 or any breakpoint you want to remove.

![image](https://github.com/user-attachments/assets/e5cf47ba-9d6a-41b6-8f66-b5027e8be751)


Run or r => to run our program or start the program again

![image](https://github.com/user-attachments/assets/55f0b319-9edd-48e3-ae3d-06d71fc48522)

Continue or C => If you wanna continue after breakpoints

Next, we will examine the process!

Examine or x ADDRESS => This examine each address

Next is to inspect address line by line

![image](https://github.com/user-attachments/assets/cf3e1d6c-2360-4dbb-a237-56f1485f659b)

Modify => Here come the fun part! We gonna modify address!

Let's set breakpoint at this address
```
break *0x401019
```
to modify address use
```
patch string 0x402000 "Patched!\\x0a"
```
Result
---

```
gef➤  break *0x401019

Breakpoint 1 at 0x401019
gef➤  r
gef➤  patch string 0x402000 "Patched!\\x0a"
gef➤  set $rdx=0x9
gef➤  c

Continuing.
Patched!
```

In conclusion:
---
First we run GDB, then we set breakpoints before address we want to overwrite. Finally you use GEF function such as patch to overwrite address to manipulate memory!

