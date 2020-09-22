import threading
import os
import math
import time

arr = []

def calc(type, bo):
    for i in range(5):
        bo = not bo
        arr.append([i, type, bo])
        time.sleep(.1)

threads = []

x = threading.Thread(target=calc, args=("x", False,))
x.start()

y = threading.Thread(target=calc, args=("y", False,))
y.start()

x.join()
y.join()

x = threading.Thread(target=calc, args=("x1", False,))
x.start()

y = threading.Thread(target=calc, args=("y1", True,))
y.start()

x.join()
y.join()

x = threading.Thread(target=calc, args=("x1", False,))
x.start()

y = threading.Thread(target=calc, args=("y1", True,))
y.start()

x.join()
y.join()

for i in arr:
    print(i)