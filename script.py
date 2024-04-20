import os
import shutil

from_dir = '/Users/grishka/Downloads';
to_dir = '/Users/grishka/Documents'
list_of_files = os.listdir(from_dir)


for file in list_of_files:
    root, extension = os.path.splitext(file)

    if extension == '':
        continue

    if extension in ['.txt', '.doc', 'docx', 'pdf']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + 'Document_Files'
        path3 = path2 + '/' + file

        print(to_dir, path2)

        
        print('Moving')
        shutil.move(path1, path3)
            
        