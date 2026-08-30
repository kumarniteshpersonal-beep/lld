from manager import FileSystemManager

class FileSystemDemo:
    @staticmethod
    def main():
        fsm = FileSystemManager()

        # parent must exist before child - create step by step now
        fsm.create_path("/hld")
        fsm.create_path("/hld/fundamental")
        fsm.create_path("/hld/fundamental/cap.txt")
        fsm.create_path("/hld/fundamental/imp")
        fsm.display() # display all the entities in root folder
        fsm.display("/hld") # everything inside hld folder
        fsm.display("/hld/fundamental")

        # negative case: parent missing -> should fail now instead of silently creating
        print("expect False (parent missing):", fsm.create_path("/no/such/parent/file.txt"))
        # negative case: invalid path format
        print("expect False (invalid path):", fsm.create_path("/hld//bad"))
        # negative case: already exists
        print("expect False (already exists):", fsm.create_path("/hld/fundamental"))

        # delete and display
        fsm.delete_path("/hld/fundamental")
        fsm.display()

        # set and get content of file - recreate parents step by step
        fsm.create_path("/hld/fundamental")
        fsm.create_path("/hld/fundamental/cap.txt")
        fsm.set_content("/hld/fundamental/cap.txt","cap theorem details")
        print(fsm.get_content("/hld/fundamental/cap.txt"))
        fsm.display()
        

FileSystemDemo.main()