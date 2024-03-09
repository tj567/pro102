import os
import shutil

from_dir = "C:/Users/tommy/Downloads/C102_assets-main/C102_assets-main"
to_dir = "C:/python_stuff/class102/asset_storage"

list_of_files = os.listdir(from_dir)

valid_types = ['.docx', '.txt', '.pdf','.doc']

for file in list_of_files:
    name, extension = os.path.splitext(file)
    if extension == "":
        continue
    if extension in valid_types:
        path1 = from_dir + "/" + file
        path2 = to_dir + "/" + "img_files"
        path3 = to_dir + "/" + "img_files" + "/" + file
        if os.path.exists(path2):
            print("moving " + file + "...")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving " + file + "...")
            shutil.move(path1,path3)
    

    
