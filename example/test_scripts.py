import pyautogui
import os
import time


def convert_command(command):
    if "start simulation" in command:
        return "mpirun -n 1 ~parafem/p121 p121-demo"
    elif "stop simulation" in command:
        return "putsa"
    elif "increase stiffness" in command:
        return "villous"
    else:
        return "error"

path = '/Users/alexbrown/Desktop/Vosk/vosk-api/python/example/listfile.txt'
last_updated = os.path.getctime(path)
first = True
f = open("listfile.txt", "r")
time.sleep(3)
while True:
    c_time = os.path.getctime(path)

    if not first:
        if c_time == last_updated:
            print("no change")
        else:
            print("change")
            f = open("listfile.txt", "r")
            last_updated = c_time
            line = f.readline()
            if not line:
                break
            fortran_command = convert_command(line.lower().strip())
            print("new command = " + fortran_command)
            if fortran_command == "error":
                continue
            else:
                pyautogui.write(fortran_command)
                pyautogui.press('enter')
    elif first:
        first = False
        line = f.readline()
        if not line:
            break
        fortran_command = convert_command(line.lower().strip())
        pyautogui.write(fortran_command)
        pyautogui.press('enter')
    f.close()
    time.sleep(2)

    
   
    
   

