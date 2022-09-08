import os
from datetime import datetime

file_name = "./guests.txt"
if os.path.exists(file_name):
    print(os.path.isfile(file_name))
    print(os.path.isdir(file_name))
    print(os.path.abspath(file_name))
    print(os.path.getsize(file_name))
    modif_time = os.path.getmtime(file_name)
    print(datetime.fromtimestamp(modif_time).strftime("%Y-%m-%d"))
else:
    print("File not found!")

print(os.getcwd())
dir_name = "./newdir/"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
print(os.listdir("./"))

current_dir = os.getcwd()
relative_parent = os.path.dirname(current_dir)
print(os.path.abspath(relative_parent))
