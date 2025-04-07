import os
from text_to_speech import output_pyttsx3

file = open('Input_Text.txt', 'r', encoding='utf-8')
file2 = open('example.txt', 'w', encoding='utf-8')
line = file.readline()
i=0
while line:
    line = line.strip()  # Remove leading/trailing whitespace characters
    if line:  
        i+=1
        #替代空格为制表符
        line = line.replace(' ', '')
        #去除特殊符號
        line = line.lstrip()
        print(line, end=' ')
        print(i, end=' ')
        output_pyttsx3(line, str(i))
        file2.write(f"{line}\n")
    else:
        # Print a newline character for empty lines
        print()
    line = file.readline()  # Read the next line
file.close()
file2.close()
