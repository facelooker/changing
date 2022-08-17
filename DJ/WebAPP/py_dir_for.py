import os

# g = os.walk('G:\zeng\Videos\wqeqeq')
# for path, dir_list, file_list in g:
#     for dir_name in dir_list:
#         print(os.path.join(path, dir_name))
#     for file_name in file_list:
#         print(os.path.join(path, file_name))
# dir = os.istdir('G:\zeng')
# d = os.listdir('G:\zeng\Videos')
# dir = os.path.isdir('G:\zeng')

# print(d)
import os

def dirlist(path, allfile):
     filelist = os.listdir(path)
     for filename in filelist:
          filepath = os.path.join(path, filename)
          if os.path.isdir(filepath):
               dirlist(filepath, allfile)
          else:
               allfile.append(filepath)
          return allfile

print (dirlist("G:\zeng\Videos\wqeqeq", []))

from glob import glob
from os import path

def dirlist(parent, allfile):
     pattern = path.join(parent, '*', '*.wav')
     return glob(pattern)
# if __name__ == '__main__':
#     # dir = os.path.isdir('G:\zeng')
#     files = []
#     dir_exc('G:\zeng\Videos',files)
#     print(files)



