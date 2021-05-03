import os
import time

path = '/Users/alexbrown/Desktop/Vosk/vosk-api/python/example/listfile.txt'

# Get the ctime of last
# for the specified path
c_time = os.path.getctime(path)
print("ctime since the epoch:", c_time)
  
# convert the ctime in
# seconds since epoch
# to local time
local_time = time.ctime(c_time)
print("ctime (Local time):", local_time)


