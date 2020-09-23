import threading
import os
import math
import time
from datetime import datetime
# import RPi.GPIO as GPIO

arr = []

# def motorswitch(bo, pin):
#     GPIO.output(bo)
#     time.sleep(.1)

def timenow():
    return (datetime.now().strftime("%H:%M:%S"))

def calc(type, bo, n):
    for i in range(n):
        bo = not bo
        arr.append([i, type, bo, timenow()])
        time.sleep(.1)

    arr.append([5, type, False])


def stepsame(count, type, bo, t):
    print("working {}".format(count))
    arr.append([count, type, bo, timenow()])
    time.sleep(t)

def all(bo):
    x = threading.Thread(target=stepsame, args=(-1, "xOff", bo, .5,))
    x.start()

    y = threading.Thread(target=stepsame, args=(-1, "yOff", bo, .5,))
    y.start()

    z = threading.Thread(target=stepsame, args=(-1, "zOff", bo, .5,))
    z.start()

    x.join()
    y.join()
    z.join()
    

# x = threading.Thread(target=calc, args=("x", False, 3,))
# x.start()

# y = threading.Thread(target=calc, args=("y", False, 3,))
# y.start()

# z = threading.Thread(target=calc, args=("y", False, 3,))
# z.start()

# x.join()
# y.join()
# z.join()

# count = 0
# while count < 1:
#     x = threading.Thread(target=stepsame, args=(count, "x1", True,))
#     x.start()

#     y = threading.Thread(target=stepsame, args=(count, "y1", True,))
#     y.start()

#     z = threading.Thread(target=stepsame, args=(count, "z1", False,))
#     z.start()

#     x.join()
#     y.join()
#     z.join()

#     all(False)

#     x = threading.Thread(target=stepsame, args=(count, "x1", False,))
#     x.start()

#     y = threading.Thread(target=stepsame, args=(count, "y1", True,))
#     y.start()

#     z = threading.Thread(target=stepsame, args=(count, "z1", True,))
#     z.start()

#     x.join()
#     y.join()
#     z.join()

#     all(False)

#     x = threading.Thread(target=stepsame, args=(count, "x1", True,))
#     x.start()

#     y = threading.Thread(target=stepsame, args=(count, "y1", False,))
#     y.start()

#     z = threading.Thread(target=stepsame, args=(count, "z1", True,))
#     z.start()

#     x.join()
#     y.join()
#     z.join()

#     all(False)

#     count += 1


i = 1
while i < 2:

    all(False)

    arr.append([i, "x2", True, timenow()])
    arr.append([i, "y2", False, timenow()])
    arr.append([i, "z2", False, timenow()])


    all(False)
    

    x = threading.Thread(target=stepsame, args=(i, "x2", True, 2,))
    x.start()

    y = threading.Thread(target=stepsame, args=(i, "y2", True, 2,))
    y.start()

    z = threading.Thread(target=stepsame, args=(i, "z2", False, 2,))
    z.start()

    x.join()
    y.join()
    z.join()

    all(False)

    x = threading.Thread(target=stepsame, args=(i, "x2", True, 1,))
    x.start()

    y = threading.Thread(target=stepsame, args=(i, "y2", True, 1,))
    y.start()

    z = threading.Thread(target=stepsame, args=(i, "z2", True, 1,))
    z.start()

    x.join()
    y.join()
    z.join()

    all(False)

    x = threading.Thread(target=stepsame, args=(i, "x2", False, 4,))
    x.start()

    y = threading.Thread(target=stepsame, args=(i, "y2", True, 4,))
    y.start()

    z = threading.Thread(target=stepsame, args=(i, "z2", True, 4,))
    z.start()

    x.join()
    y.join()
    z.join()

    all(False)

    arr.append([i, "x2", False, timenow()])
    arr.append([i, "y2", False, timenow()])
    arr.append([i, "z2", True, timenow()])

    all(False)

    i += 1

# i = 1

# while i < 4:

#     arr.append([i, "x", True, timenow()])
#     arr.append([i, "y", False, timenow()])


#     arr.append([i, "x", False, timenow()])
#     arr.append([i, "y", False, timenow()])

#     arr.append([i, "x", True, timenow()])
#     arr.append([i, "y", False, timenow()])

#     x = threading.Thread(target=stepsame, args=(i, "x1", False, 10,))
#     x.start()

#     y = threading.Thread(target=stepsame, args=(i, "y1", True, 10,))
#     y.start()

#     x.join()
#     y.join()

#     x = threading.Thread(target=stepsame, args=(i, "x2", True, 10,))
#     x.start()

#     y = threading.Thread(target=stepsame, args=(i, "y2", False, 10,))
#     y.start()

#     x.join()
#     y.join()

#     arr.append([i, "x", False, timenow()])
#     arr.append([i, "y", False, timenow()])

#     i += 1


prev = 1
for i in arr:   
    if i[0] != prev:
        print("\n\n")
    print(i)    
    prev = i[0]

    