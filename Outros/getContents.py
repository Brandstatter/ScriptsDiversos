import os
import shutil

def getCont():
    dir = 'C:/Program Files (x86)/Steam/steam/steamapps/workshop/content/211820'
    dest = 'D:/Github/StarHelper/mods'
    oldDir = dir
    u = 0
    for file in os.listdir(dir):
        print(file)
        dir += "/" + file
        u += 1 
        for i in os.listdir(dir):
            if i.endswith('.pak'):
                print(i)
                src = dir + "/" + i
                shutil.copy2(src, dest)
                fileN = str(u) + '.pak'

                oldFile = os.path.join(dest, i)
                newFile = os.path.join(dest, fileN)
                print(u)
                os.rename(oldFile, newFile)
                dir = oldDir