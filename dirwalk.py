#operating system library
import os
#regex searching library
import re

import shutil

#original Starting Point
path = os.getcwd()

os.chdir('../')
os.chdir('../')
os.chdir('Downloads/')

newpath = os.getcwd()

print(f"{path}\n{newpath}")

#print('Hello World, "how are you"?')

i = input("What files are you looking for? ")

for (root, dirs, files) in os.walk('.', topdown=True):
    for name in files:
        file = os.path.join(root, name)
        size = os.path.getsize(file)
        match = re.search(str(i), file)
        
        if match:
            print('file {} size: {} bytes'.format(file, size))
            src_path = file
            dest_path = '/home/ryszard/Documents/UI'
            shutil.move(src_path, dest_path)
            
    #for name in dirs:
     #   print(os.path.join(root, name))


"""
dog = "dog"

def walker():
    print ("Pick a path")
    x = input("Where do you want to go? ")

    
def tree(x):
    print("Along the way you found a path to {}".format(x))


walker()
tree(dog)
"""

