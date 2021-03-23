import os
from datetime import datetime

# print(dir(os))
print(os.getcwd())
os.chdir('/home/saroj/icon')
os.makedirs('OS-demo-2/Sub-Dir-1')
print(os.listdir())
os.removedirs('OS-demo-2/Sub-Dir-1')

mod_time = os.stat('sms').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path: ',dirpath)
    print('Directories:',dirnames)
    print('Files:', filenames)
    print()

print(os.environ.get('HOME'))
print(os.listdir(os.environ.get('HOME')))

file_path = os.path.join( os.environ.get('HOME') , 'test.txt')
print(file_path)
print(dir(os.path))