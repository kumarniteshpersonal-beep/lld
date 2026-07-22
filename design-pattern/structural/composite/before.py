# without composite pattern, we need to check the type of each object before performing operations on it

class File:
    def __init__(self, name):
        self.name = name

class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []

    def add_file(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(folder)

def display_folder(folder, indent=0):
    print(" " * indent + folder.name)

    for file in folder.files:
        print(" " * (indent + 2) + file.name)

    for child_folder in folder.folders:
        display_folder(child_folder, indent + 2)

# client code

root = Folder("root")
folder1 = Folder("folder1")
folder2 = Folder("folder2")

file1 = File("file1.1")
file2 = File("file2.1")

root.add_folder(folder1)

folder1.add_file(file1)
folder1.add_folder(folder2)
folder2.add_file(file2)

display_folder(root)

# problems:
# 1. The client code has to check the type of each object (whether it's a file or a folder) before performing operations on it.