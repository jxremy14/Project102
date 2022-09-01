from distutils import extension
import os
import shutil

from_dir="C:/Users/class/OneDrive/Desktop/Document_Files"
to_dir="C:/Users/class/Downloads"

listOfFiles=os.listdir(from_dir)
print(listOfFiles)

for file_name in listOfFiles:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension=='':
        continue
    if extension in['.txt','.png','.jpg','.pdf','.doc','.docx']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+"Document_Files"
        path3=to_dir+'/'+"Document_files"+'/'+file_name

        if os.path.exists(path2):
            print("moving"+file_name+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name+"...")
            shutil.move(path1,path3)