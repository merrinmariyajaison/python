
import os
parent_dir = "C:\\DIRECTORY"
print("1. Create Subdirectory \n2. List Directory\n3. Search file\n4. Remove file\nEnter choice : ")
ch = int(input())
if ch == 1:
    sub_dir = input()
    path = os.path.join(parent_dir,sub_dir)
    os.mkdir(path)
    print("Directory created")
elif ch == 2:
    list_dir = os.listdir(parent_dir)
    print("Files in ",parent_dir," : ")
    print(list_dir)
elif ch == 3:
    res = []
    filename = input("Enter the .py filename ")
    if filename.endswith('.py'):
        for root, dir, files in os.walk(parent_dir):
            if filename in files:
                res.append(os.path.join(root, filename))
        print(res)
    else:
        print("Not a .py file")
elif ch == 4:
    filename = input("Enter the file to remove : ")
    os.remove(filename)
else:
    print("Invalid Option")
