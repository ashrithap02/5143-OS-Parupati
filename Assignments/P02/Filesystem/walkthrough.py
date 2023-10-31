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
        fs.create_directory(fs.current_directory, inp[1], "user", "group", "rwxr-xr-x")
        print(f"Directory {inp[1]} created!")
    elif inp[0] == "cd":
        fs.change_directory(inp[1])
        print(f"Changed directory to {inp[1]}")
    elif inp[0] == "pwd":
        print(fs.current_directory)
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
        fs.create_file(inp[1],inp[2],inp[3],inp[4],inp[5])
        print("File created successfully")


def main():
    fs = FileSystem("my_database.db")
    li=[
    ["ls -lah"],
    ["mkdir", "Fruits",],
    ["ls -lah"],
    ["cd", "Fruits"],
    ["ls -lah"],
    ["mkdir", "Apples"],
    ["ls -lah"],
    ["cd", ".."],
    ["ls -lah"],
    ["pwd"],
    ["touch","1","somefile.txt","root","root","rwxr-xr-x"],
    ["mv", "somefile.txt", "bananas"],
    ["ls -lah"],
    ["cp", "bananas/somefile.txt", "somefile/otherfile.txt"],
    ["ls -lah"],
    ["rm -rf", "bananas"],
    ["ls -lah"],
    ["chmod", "somefile.txt", "777"],
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

