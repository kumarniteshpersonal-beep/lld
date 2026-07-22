# Composite Pattern lets clients treat individual objects (leaves) and groups of objects (composites) uniformly by organizing them into a tree structure through a common interface.
from abc import ABC, abstractmethod

# component - abstract class
class FileSystemComponent(ABC):
    def __init__(self,name: str):
        self.name = name
    
    @abstractmethod
    def display(self, indent=0):
        pass

# leaf component
class File(FileSystemComponent):
    def display(self, indent=0):
        print(" "*indent + self.name)

# container / composite component
class Folder(FileSystemComponent):
    def __init__(self,name: str):
        super().__init__(name)
        self.children = []
    
    def display(self, indent=0):
        print(" "*indent + self.name)
        for _component in self.children:
            _component.display(indent+2)
    
    def add_file_component(self,file: FileSystemComponent):
        self.children.append(file)

# client code
root = Folder("root")
folder1 = Folder("folder1")
file_in_folder1 = File("file1.1")
folder2 = Folder("folder2")
file_in_folder2 = File("file2.1")
root.add_file_component(folder1)
folder1.add_file_component(file_in_folder1)
folder1.add_file_component(folder2)
folder2.add_file_component(file_in_folder2)
root.display()

