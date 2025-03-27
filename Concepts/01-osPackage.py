import datetime
import os
from datetime import datetime

# print(dir(os))

print(os.getcwd())
print(os.listdir())

mod_time = os.stat('osPackage.py').st_mtime

print(datetime.fromtimestamp(mod_time))
print(os.walk())
 