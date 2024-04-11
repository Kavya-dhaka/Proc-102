import os
import shutil

from_dir = "C:/Users/rkdha/Downloads"
to_dir = "C:/Users/rkdha/Documents"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extention = os.path.splitext(i)
    print(name)
    print(extention)

    if extention == "":
        continue
    if extention in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "Document_files"
        path3 = to_dir + "/" + "Document_files" + i

        if os.path.exists(path2):
            print("Moving " + i + ".....")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving" + i + ".....")
            shutil.move(path1, path3)
