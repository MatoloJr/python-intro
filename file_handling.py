#it is how python let's you interact with files on your computer like saving a file
#handles opening and closing a file safely
#always use with to avoid leaving files open
#confirm whether a file exists before writing to prevent errors
#use import os and os.path.exists(notes.txt)
#use append mode for big files

#file creation and writing
with open("notes.txt", "w") as file: #open creates a file named notes.txt and w represents the ability to write on it
    file.write("welcome homie")#file.write writes the specified text into the above created file

#file reading
with open("notes.txt", "r") as file:#here the file is opened and the r is for viewing the content of the specified file
    content = file.read()#file.read reads the file content
    print(content)#it outputs the file contents

#append text without overwriting
with open("notes.txt", "a") as file:#the 'a' starts a new line
    file.write("\nhow's school life")#the \n moves the content specified to it's own independent line
with open("notes.txt", "r") as file:
    contents = file.read()
    print(contents)

#reading files line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())#strip remove white spaces or extra spaces

#read all lines into a list
with open("notes.txt", "r") as file:
    lines = file.readlines()#read the all the lines and put them into a list
    print(lines)

#save a new note to a file
with open("notes.txt", "a") as file:
    notes = input("Enter a new note: ")#accepting user input
    file.write(f"\n{notes}")#saving the user input to the above specified file

#reads and displays all notes
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

#clearing the file content
#with open("notes.txt", "w") as file:
#    file.write("")#to clear the specified file above