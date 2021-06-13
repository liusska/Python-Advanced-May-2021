import os

try:
    os.remove("my_first_file.txt")
except FileNotFoundError:
    print("File already deleted!")


# option 2:
if os.path.exists("my_first_file.txt"):
    os.remove("my_first_file.txt")
else:
    print("File already deleted!")
