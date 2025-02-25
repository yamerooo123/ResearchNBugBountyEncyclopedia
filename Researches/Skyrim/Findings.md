[25 Feb 2025 - Attempt 1 ]
---

1. I went to %USERPROFILE%/Documents/My Games/Skyrim Special Edition/Saves to inspect what file extension is save file is.
---

![alt text](image.png)

2. Upon inspection, the save file extension is .ess which i need to research more.
---
```
PS C:\Users\PC\Downloads> [IO.Path]::GetExtension('C:\Users\PC\Documents\My Games\Skyrim Special Edition\Saves\Autosave1_D2E91592_0_50737963686974_Tamriel_000716_20250224193821_10_1.ess')
.ess
```

3. I decided to inspect the ".ess" file in VSCode
---
![alt text](image-1.png)

As you can see, the content of the file is binary.

4. After some research, i discovered the ".ess" file is The Elder Scrolls Saved Game (.ess). 
---

**.ess file extension:**

```
Source: https://gist.github.com/felipepodesta/e87252275b437133d2f0
```

A little more research helped me understand that the save file is basically C++ file.

```
Source: https://www.reddit.com/r/learnprogramming/comments/1fnsy9/how_do_games_like_skyrim_handle_saves/
```
**C++ variables and clarification:**

```
Source: https://en.uesp.net/wiki/Skyrim_Mod:Save_File_Format
```

Next, what i am thinking right now is to find a disassembler so that I can see what the file actually looks like. I decided to use Ghidra which is a free software for the reverse engineering task.

```
Source: https://github.com/NationalSecurityAgency/ghidra/releases
```









