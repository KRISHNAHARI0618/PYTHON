import os
import pathlib


print(os.error)

print(os.error(pathlib))

print(os.getcwd())


# Changing the directory
def current_path():
    print(os.getcwd())
    print()

current_path()
os.chdir('../')
current_path()

#Creating the directory
def make_dir():
    os.mkdir('peddireddy')
    return os.getcwd()

result = make_dir()

print(os.geteuid())

print(os.urandom(100))

print("Before Deleting the Peddireddy ")
list1 = os.listdir(os.getcwd())
print(list1)

for i in list1:
    if i == "peddireddy":
        os.removedirs(i)
    if i == "WEB":
        os.rename(i,i.lower())

print("After deleting the Peddireddy")

list1 = os.listdir(os.getcwd())
print(list1)





