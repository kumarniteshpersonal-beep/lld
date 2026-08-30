from file_system_node import FileSystemNode, File, Folder

class FileSystemManager:
    def __init__(self):
        self.root = Folder("")
    
    def _is_file(self, split: str) -> bool:
        if "." in split:
            return True
        return False
    
    def _is_valid_path(self, path: str) -> bool:
        if not path or not path.startswith("/"):
            return False
        if path == "/":
            return True
        if path.endswith("/"):
            return False
        splitted_path = path[1:].split("/")
        if any(segment == "" for segment in splitted_path):
            return False
        return True

    def create_path(self, path: str) -> bool:
        if not self._is_valid_path(path):
            print(f"invalid path: {path}")
            return False
 
        print(f"creating path: {path}")
        splitted_path = path[1:].split("/")
        parent_segments, last_segment = splitted_path[:-1], splitted_path[-1]
        temp = self.root
 
        # parent must already exist - do NOT auto-create intermediate folders
        for split in parent_segments:
            next_map = temp.get_next_node_map()
            if split not in next_map:
                print(f"parent path does not exist: {split}")
                return False
            temp = next_map[split]
            if isinstance(temp, File):
                print(f"cannot create path inside a file: {temp.name}")
                return False
 
        next_map = temp.get_next_node_map()
        if last_segment in next_map:
            print(f"path already exists: {path}")
            return False
 
        next_map[last_segment] = File(last_segment) if self._is_file(last_segment) else Folder(last_segment)
        return True
    
    def delete_path(self, path: str) -> bool:
        if not self._is_valid_path(path) or path == "/":
            print(f"invalid path: {path}")
            return False
 
        splitted_path = path[1:].split("/")
        parent_path = "/" + "/".join(splitted_path[:-1]) if len(splitted_path) > 1 else "/"
        last_segment = splitted_path[-1]
 
        parent_node = self.find_node(parent_path)
        if parent_node is None or last_segment not in parent_node.get_next_node_map():
            print(f"path not found: {path}")
            return False
 
        print(f"deleting path: {path}")
        del parent_node.get_next_node_map()[last_segment]
        return True
            
    def find_node(self,path) -> FileSystemNode | None:
        if not self._is_valid_path(path):
            return None
        splitted_path = [] if path=="/" else path[1:].split("/")
        temp = self.root
        
        for split in splitted_path:
            if split not in temp.get_next_node_map():
                return None
            temp = temp.get_next_node_map()[split]
        
        return temp
    
    def get_content(self, path: str) -> str | None:
        if not self._is_valid_path(path) or path == "/":
            print(f"invalid path: {path}")
            return None
        # find the node
        temp = self.find_node(path)
        # return the content of the last identified node
        if isinstance(temp,File):
            return temp.get_content()

        return None
    
    def set_content(self,path: str,content: str) -> bool:
        if not self._is_valid_path(path) or path == "/":
            print(f"invalid path: {path}")
            return False
        
        # find the node
        temp = self.find_node(path)
        # set the content
        if isinstance(temp, File):
            print(f"setting content to file: {temp.name}")
            temp.set_content(content)
            return  True
        
        return False

    def display(self, path: str = "/"):
        node = self.find_node(path)
        if not node:
            return
        node.display()
        print("-----------------")