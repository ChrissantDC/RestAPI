import sys
import glob
import hashlib
import pathlib
import os
import json

# a ={"name": "John", "age": 31, "Salary": 25000}
# b = json.dumps(a)
# print(b)

#  Sample output in cmd: python PycharmProjects\Exercise2\main.py  C:\Users\delac\PycharmProjects\Exercise2 E.csv
from configparser import ConfigParser

print(f"The name of the script is: {sys.argv[0]}")
folder_path = (r"" + sys.argv[1])

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

file_path = []
txt_files = []
files_size = []
sha1 = []
md5 = []


# STEP 1: Get files and store them to array
# STEP 2: Get path of each file from the array
# STEP 3: Get file name
# STEP 4: Get Sha1
# STEP 5: Get md5
# STEP 6: Follow the format and POST via REST API

def get_file():
    # This function will list down the file names in an array

    for text_file in glob.glob(folder_path + "\*.txt"):
        # For some reason, if I make this *.*, a problem with hashing occurs. I will ask for help regarding this
        txt_files.append(text_file)


def print_path(path):
    # This function will collect the paths of the file
    file_path.append(str(pathlib.Path(path).parent.resolve()))


def hash_file(filename):
    # This function returns the SHA-1 hash
    # of the file passed into it

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as hashfile:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = hashfile.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    sha1.append(h.hexdigest())
    return h.hexdigest()


def file_size(filename):
    file_name = os.path.getsize(filename)
    files_size.append(file_name)
    return file_name


def get_md5(filename):
    with open(filename, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    md5.append(file_hash.hexdigest())  # to get a printable str instead of bytes


get_file()
for file in txt_files:
    print_path(file)
    file_size(file)
    hash_file(file)
    get_md5(file)

# text = input("prompt ")
# print("you entered " + text)
# with open(input("Enter Desired File Name: "), "w") as Test_Write:
completeName = os.path.join(folder_path, sys.argv[2])

with open(completeName, "w") as Test_Write:
    first_column = "Parent path \t filename \t filesize \t sha1 \t md5"
    row = ""
    i = 0
    for i in range(len(txt_files)):
        row += file_path[i] + ",\t" + txt_files[i] + ",\t" + str(files_size[i]) + ",\t" + sha1[i] + ",\t" + md5[
            i] + "\n"
    json.dump(row, Test_Write)

final_value = row
print(final_value)
