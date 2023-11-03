import time
from prettytable import PrettyTable
from file_system_extended_v8 import FileSystem

command_history = []
table = PrettyTable()
def print_database_contents(fs):
    """Print the contents of the database table."""
    contents = fs.list_directory()
    table.field_names = [" id","Filename"," File Type" ,"File Size ", "Owner","Permissions","Modification Time"]
    for item in contents:
        table.add_row([item[0],  item[2] , item[3]  ,item[4] , item[5] , item[7] , item[8]])
    print(table)
    table.clear_rows()

def demo_command(fs, inp):
    global command_history
    print(f">>> {' '.join(inp)}")
    command_history.append(inp[0])
    time.sleep(1.5)
    if inp[0] == "ls -lah":
        contents = fs.list_directory()
        table.field_names = [" id","Filename"," File Type" ,"File Size ", "Owner","Permissions","Modification Time"]
        for item in contents:
            table.add_row([item[0],  item[2] , item[3]  ,item[4] , item[5] , item[7] , item[8]])
        print(table)
        table.clear_rows()
    elif inp[0] == "mkdir":
        fs.create_directory(fs.current_directory, inp[1])
        print(f"Directory {inp[1]} created!")
    elif inp[0] == "cd":
        fs.change_directory(inp[1])
        print(f"Changed directory to {inp[1]}")
    elif inp[0] == "pwd":
        print(fs.current_working_directory())
    elif inp[0] == "mv":
        fs.move(inp[1], inp[2])
        print(f"Moved {inp[1]} to {inp[2]}")
    elif inp[0] == "cp":
        fs.copy(inp[1], inp[2])
        print(f"Copied {inp[1]} to {inp[2]}")
    elif inp[0] == "rm -rf":
        fs.delete_directory(inp[1])
        print(f"Deleted directory {inp[1]}")
    elif inp[0] == "chmod":
        fs.change_permissions(inp[1], inp[2])
        print(f"Changed permissions of {inp[1]} to {inp[2]}")
    elif inp[0] == "history":
        print("Command History: ",command_history)
    elif inp[0] == "touch":
        fs.create_file(inp[1])
        print("File created successfully")
    elif inp[0] == "rm":
        fs.delete_file(inp[1])
        print("File deleted successfully")


def main():
    fs = FileSystem("my_database.db")
    li=[["ls -lah"],
    ["mkdir", "repo1/"],
    ["ls -lah"],
    ["cd", "repo1/"],
    ["pwd"],
    ["cd", ".."],
    ["pwd"],
    ["touch","demo.txt"],
    ["ls -lah"],
    ["mv", "demo.txt", "demo1.txt"],
    ["ls -lah"],
    ["cp", "demo1.txt", "demo2.txt"],
    ["ls -lah"],
    ["mkdir", "repo2/"],
    ["ls -lah"],
    ["rm -rf", "repo2/"],
    ["ls -lah"],
    ["history"]]
    for i in li:
        demo_command(fs,i)
        input()
        time.sleep(1.5)
    
    # Print the contents of the database table
    print_database_contents(fs)
    


    fs.close()

if __name__ == "__main__":
    main()
