import serial
import json
import time
import os
import psycopg2
import logging

global ser
#ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)
#ser.flushInput()

class HWWarmService():

    def __init__(self):
        pass

    def openContact(self):
        a = {'contact': 1}
        json_out = json.dumps(a)
        print(json_out)
        ser.write(json_out)

    def closeContact(self):
        a = {'contact': 0}
        json_out = json.dumps(a)
        print(json_out)
        ser.write(json_out)


    def ser_read(self):
        while True:
            global t_plate
            global t_1
            global c_1
            global t_2
            global c_2
            global t_3
            global c_3
            global t_4
            global c_4
            global t_5
            global c_5
            global t_6
            global c_6
            global t_7
            global c_7
            global t_8
            global c_8
            raw_input = ser.readline()
            # print raw_input
            # try:
            for json_input in raw_input.split("}"):
                if json_input == '':
                    # logging.warning('WARNING')
                    break
                decoded = json.loads(json_input + "}")
                t_plate = decoded['T_plate_avg']
                t_1 = decoded['T_1']
                c_1 = decoded['CO2_1']
                t_2 = decoded['T_2']
                c_2 = decoded['CO2_2']
                t_3 = decoded['T_3']
                c_3 = decoded['CO2_3']
                t_4 = decoded['T_4']
                c_4 = decoded['CO2_4']
                t_5 = decoded['T_5']
                c_5 = decoded['CO2_5']
                t_6 = decoded['T_6']
                c_6 = decoded['CO2_6']
                t_7 = decoded['T_7']
                c_7 = decoded['CO2_7']
                t_8 = decoded['T_8']
                c_8 = decoded['CO2_8']

            return t_plate, t_1, c_1, t_2, c_2, t_3, c_3, t_4, c_4, t_5, c_5, t_6, c_6, t_7, c_7, t_8, c_8
