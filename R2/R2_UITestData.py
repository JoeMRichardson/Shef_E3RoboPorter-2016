
import serial
import time
import random
import numpy as np

def testFunction():

    viewerCon.write("#")  # 0
    # Time
    viewerCon.write(time.ctime() + ',')
    # Ultrasonic data
    viewerCon.write(str(random.randint(0 ,200)) + ",")  # 1
    viewerCon.write(str(random.randint(0 ,200)) + ",")
    viewerCon.write(str(random.randint(0 ,200)) + ",")
    viewerCon.write(str(random.randint(0 ,200)) + ",")
    viewerCon.write(str(random.randint(0 ,200)) + ",")
    viewerCon.write(str(random.randint(0 ,200)) + ",")  # 6
    # motor speeds
    # demanded motor speeds
    viewerCon.write(str(random.randint(0 ,50)) + ",")  # 7
    viewerCon.write(str(random.randint(0 ,50)) + ",")
    # actual speeds
    viewerCon.write(str(random.randint(0 ,50)) + ",")  # 9
    viewerCon.write(str(random.randint(0 ,50)) + ",")
    # POSITIONS
    # target
    viewerCon.write(str(100) + ",")  # 11
    viewerCon.write(str(100) + ",")
    # Porter_global
    viewerCon.write(str(random.randint(0 ,500)) + ",")  # 13
    viewerCon.write(str(random.randint(0 ,500)) + ",")
    # Porter_local
    viewerCon.write(str(random.randint(0 ,500)) + ",")  # 15
    viewerCon.write(str(random.randint(0 ,500)) + ",")
    # porterOrientation
    viewerCon.write(str(random.uniform(-np.pi ,np.pi)) + ",")  # 17
    # AHRS # FOR VALIDATION ONLY
    # yaw
    viewerCon.write(str(random.uniform(-np.pi ,np.pi)) + ",")  # 18

    # thread life status
    viewerCon.write(str(True) + ",")  # 19
    # current lock

    # safety staus
    viewerCon.write(str(True) + ",")  # 20
    # obstruction status
    viewerCon.write(str(True) + ",")  # 21
    # data status
    viewerCon.write(str(True))  # 22

    viewerCon.write("\n")


try:
    viewerCon = serial.Serial('COM7', 19200)
    viewerCon.open()
    vCon = True
except Exception as e:
    print(str(e))

while True:
    try:
        testFunction()
        time.sleep(1)
    except Exception as e:
        print (str(e))

