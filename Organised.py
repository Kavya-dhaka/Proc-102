import os
import shutil

from_dir = "C:/Users/rkdha/Downloads"
to_dir = "C:/Users/rkdha/Documents"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)
    print(extension)
    print(name)

    if extension == "":
        continue
    if extension in [".jpg", ".png", ".jpeg", ".jfif"]:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "Image_files"
        path3 = to_dir + "/" + "Image_files" + "/" + i

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)