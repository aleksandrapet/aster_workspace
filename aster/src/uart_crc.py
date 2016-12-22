import serial
import json
import time
import os

POLYNOMIAL = 0x11021
PRESET = 0xFFFF
counter = 0

global ser
ser = serial.Serial(

    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

ser.flushInput()

if ser.isOpen():
    print "ser is open"
    ser.write("C")

while 1:
    print "vo while"
    time.sleep(1)


    def _initial(c):
        crc = 0
        c = c << 8
        for j in range(8):
            if (crc ^ c) & 0x8000:
                crc = (crc << 1) ^ POLYNOMIAL
            else:
                crc = crc << 1
            c = c << 1
        return crc


    _tab = [_initial(i) for i in range(256)]


    def _update_crc(crc, c):
        cc = 0xff & c

        tmp = (crc >> 8) ^ cc
        crc = (crc << 8) ^ _tab[tmp & 0xffff]
        crc = crc & 0xffff
        return crc


    def crc(str):
        crc = PRESET
        for c in str:
            crc = _update_crc(crc, ord(c))
        return crc


    def crcb(*i):
        crc = PRESET
        for c in i:
            crc = _update_crc(crc, c)
        return crc


    def ser_read():

        global P  # position
        global H  # HWID
        global I  # PatientID
        global N  # Name
        global S  # Surname
        global L  # BufferLenght
        global B  # Battery
        global A1
        global A2
        global C
        global T
        global json_input
        global crc_2
        global crc_input
        global counter
        global decoded

        raw_input = ser.readline()
        # print len(raw_input)
        # print "Vlez na seriska porta:", raw_input
        #		for input in raw_input.split("}"):
        #			if input == '':
        #				break
        input = raw_input.split(" ")
        # print input
        json_input = input[0]
        decoded = json.loads(input[0])

        crc_2 = input[1]
        crc_input = crc_2.encode("hex")
        # print crc_input
        # print "JSON paket:", json_input

        c = crc(json_input)
        crc_json = hex(c)[2:]
        # print "CRC:", crc_json
        print "----------------------"
        if crc_json == crc_input and counter == 0:
            ser.write("A")
            print "A"
            pos_1 = decoded['P']
            print "Position:", pos_1
            hw_id = decoded['H']
            print "HardwareID:", hw_id
            p_id = decoded['I']
            print "PatientID:", p_id
            name = decoded['N']
            print "Name:", name
            surn = decoded['S']
            print "Surname:", surn
            leng = decoded['L']
            print "Buffer lenght:", leng
            bat = decoded['B']
            print "Battery:", bat
            al_1 = decoded['A1']
            print "Alarm1:", al_1
            al_2 = decoded['A2']
            print "Alarm2:", al_2
            pos_2 = decoded['P']
            print "Position:", pos_2
            counter = 1


        elif crc_json == crc_input and counter == 1:

            pos_2 = decoded['P']
            print "Position:", pos_2
            t = decoded['T']
            print "Temperature:", t
            co2 = decoded['C']
            print "CO2:", co2
            counter = 0
            ser.write("A")


        else:
            print "N"
            ser.write("N")
        return


    ser_read()