#### 5143 - P01
#### Shell project

#### Group members

- Srikanth Yanala
- Sravani Seelam
- Ashritha Parupati

#### Overview:
This Project implements a basic shell in python where it runs most of the commands that a shell does.
When you run shell.py program, it will ask you for prompt where we can give commands like ls, sort, cp, mkdir and so on.
Based on the commands entered, output will be shown on the terminal.

#### Instructions

import all the packages and run shell.py program

For help, type "help" in commandline

# How to run commands

1. ls :

   >> ls : lists all files and directories
   >> ls -a : lists all files including hidden files
   >> ls -h : lists all files with sizes
   >> ls -l : lists all files with modes, sizes, datetime and so on

2. mkdir :

   >> mkdir demo : to create a directory

3. cd :

   >> cd demo : changes to named directory
   C:\Users\ashri\Downloads\Shell\demo
   
4. cd .. : 

   >> cd .. : changes to parent directory
   C:\Users\ashri\Downloads\Shell
   
5. cd ~ :

   >> cd ~ : changes to home directory
   C:\Users\ashri

6. pwd :

   >> pwd : displays the path of current directory
   C:\Users\ashri\Downloads\Shell

7. mv :

   >> mv code1.py code2.py : to rename file1 to file2
   File moved successfully

8. cp :

   >> cp shell.py code1.py : to copy file1 to file2
   File copied successfully
   >> cp shell.py ash\code3.py : to copy file1 to a file2 in other directory
   File copied successfully

9. rm :
     >> rm code1.py : to delete a file
     File deleted successfully
     >> rm -r demo : to delete files in a directory
     Directory deleted successfully

10. rmdir :

    >> rmdir demo : to remove a directory
    Directory removed successfully

11. cat :

    >> cat shell.py : to display a file

12. less :

    >> less shell.py : to display a page of file at a time

13. head :

    >> head shell.py : to display first few lines of file
    >> head shell.py -n 17 : to display first lines of file according to the number given
14. tail :

    >> tail shell.py : to display last few lines of file
    >> tail shell.py -n 13 : to display last lines of file according to the number given

15. grep :

    >> grep "head" keyword : to search a keyword in file and print lines where pattern is found
    >> grep -l head shell.py code1.py : only return file names where the word or pattern is found
    shell.py
    code1.py

  


