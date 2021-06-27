from time import *
from data import *
import serial

ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

while True:
    ser.flush()
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
    Dron_data.RWN_Data('w2', "RI:{}".format(line))
