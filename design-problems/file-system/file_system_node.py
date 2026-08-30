class FileSystemNode:
    def __init__(self, name: str = ""):
        self.name = name
        self.next_node_map = {}
    
    def get_next_node_map(self):
        return self.next_node_map

    def display(self, indent=0):
        for node_name, node in self.next_node_map.items():
            print(" "*indent+node_name)
            if node:
                node.display(indent+2) # add 2 spaces

class File(FileSystemNode):
    def __init__(self, name: str):
        super().__init__(name)
        self.content = ""
    
    def set_content(self, content: str):
        self.content = content
    
    def get_content(self):
        return self.content

class Folder(FileSystemNode):
    def __init__(self, name: str):
        super().__init__(name)