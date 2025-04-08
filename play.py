import os
from play_mp3 import play_mp3
from datetime import datetime
import random
import string

def get_current_time():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

file = open('example.txt', 'r', encoding='utf-8')
line = file.readline()

file_save = open('play_save.txt', 'r', encoding='utf-8')
line_save = file_save.readline()
save_len=int(line_save.strip())
#查看line全部有幾行
total_lines = sum(1 for _ in open('example.txt', 'r', encoding='utf-8'))
for i in range(total_lines):
    if i > save_len:
        #line去掉/n
        line = line.strip()
        
        for j in range(0, len(line), 10):
            random_words = ''.join(random.choices(string.ascii_letters, k=5))
            random_words1 = ''.join(random.choices(string.ascii_letters, k=5))
            print(get_current_time()+" "+random_words+"/"+line[j:j+10]+"/"+random_words1)
        
        file_mp3=f"./save/{(i+1)}.mp3"
        play_mp3(file_mp3)
        with open('play_save.txt', 'w') as f:
            f.write(f"{i}")
    elif total_lines == (i+1):
        print("已經播放完畢")
        with open('play_save.txt', 'w') as f:
            f.write(f"0")
        #結束程式
        break
    line = file.readline()