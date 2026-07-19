# Text Files
# .txt .docx .log


# Binary files
# .mp4 , .mp3 ,.mov ,.png ,.jpeg etc

# Reading writting and closing files
# --------------------------------------------------------
# open("filename",'mode') # by default mode is in read

file = open("demo.txt","r") # r for read and w for write
print(file)

# | Mode | Meaning      | Description                              |
# | ---- | ------------ | ---------------------------------------- |
# | `r`  | Read         | Opens file for reading (default)         |
# | `w`  | Write        | Creates file or overwrites existing file |
# | `a`  | Append       | Adds data at the end of file             |
# | `x`  | Create       | Creates new file, error if file exists   |
# | `b`  | Binary       | Used for binary files (images, etc.)     |
# | `t`  | Text         | Text mode (default)                      |
# | `+`  | Read + Write | Both read and write                      |




data = file.read() # to read entire file
print(data)
print(type(data))

file.close() # better practice to close the file afetr processing

file = open("demo.txt","r") 
data = file.read(10) #reading 1st 10 characters
print(data)

data1 = file.readline() # to read one line at once
print(data1)
file.close()


# Important point Here 
# Here there is a pointer that read the file if we did file.read() then pointer read whole file and points to blank (end of file) now.
# so after reading again it prints blank characters
# for file.readLine() pointe now points to new line


# Writting a file
# In W and A mode if file doesn't exixt then python automatically creates a new one

file = open("demo.txt","w")
file.write("I am Ansuman Badatya") 
file.close()

# Appending 

file = open("demo.txt","a")
file.write("Preparing for NEET") 
file.write("\n Preparing for NEET") # for next line
file.close()


# With open
# it automatically closes the file after its scope ends no need to explicitly close file
with open("demo.txt","a+") as f:
    data = f.read()
    print(data)
    
    
# Deleting the file
# it uses the os module

import os
os.remove('demo.txt')