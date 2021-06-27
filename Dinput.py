from data import *
from time import *
import serial

ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

def dron_input(x):
    if x == 'UI:UP':
        Dron_input = 1
    if x == 'UI:DOWN':
        Dron_input = 2
    if x == 'UI:FORWARD':
        Dron_input = 3
    if x == 'UI:BACK':
        Dron_input = 4
    if x == 'UI:RIGHT':
        Dron_input = 5
    if x == 'UI:LEFT':
        Dron_input = 6
    if x == 'UI:UP1':
        Dron_input = 7
    if x == 'UI:DOWN1':
        Dron_input = 8
    if x == 'UI:UP2':
        Dron_input = 9
    if x == 'UI:DOWN2':
        Dron_input = 10
    if x == 'UI:Start':
        Dron_input = 11
    if x == 'UI:Stop':
        Dron_input = 12
    return Dron_input
while True:
    ser.flush()
    while True:
        ser.write(b"{}\n".format(dron_input(Dron_data.RWN_Data('r1'))))
    time.sleep(1)

