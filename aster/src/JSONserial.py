import serial
import json
import time
import os
import psycopg2
import logging 


#t_plate=0
#t_1=0
#c_1=0
#t_2=0
#c_2=0
#t_3=0
#c_3=0
#t_4=0
#c_4=0
#t_5=0
#c_5=0
#t_6=0
#c_6=0
#t_7=0
#c_7=0
#t_8=0
#c_8=0
ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)
ser.flushInput()

	
def ser_read():
        #ser = serial.Serial("/dev/ttyAMA0", 115200,timeout=0.7)
        #ser.flushInput()

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
        raw_input=ser.readline()
		#print raw_input
		#con=psycopg2.connect("dbname='pi' user='pi' host='localhost' password='pi'")
		#cur=con.cursor()
        # try:
		for json_input in raw_input.split("}"):
			if json_input == '':
			#logging.warning('WARNING')
				break
			decoded = json.loads(json_input+"}")
			t_plate=decoded['T_plate_avg']
			t_1=decoded['T_1']
			c_1=decoded['CO2_1']
			t_2=decoded['T_2']
			c_2=decoded['CO2_2']
			t_3=decoded['T_3']
			c_3=decoded['CO2_3']
			t_4=decoded['T_4']
			c_4=decoded['CO2_4']
			t_5=decoded['T_5']
			c_5=decoded['CO2_5']
			t_6=decoded['T_6']
			c_6=decoded['CO2_6']
			t_7=decoded['T_7']
			c_7=decoded['CO2_7']
			t_8=decoded['T_8']
			c_8=decoded['CO2_8']
			#T_time=time.time()
			#t= time.strftime("%Y-%m-%d %H:%M:%S")
			#print t
			print("--------------------------------------------------------------------------------------------------------------")
                #except (ValueError, KeyError, TypeError):
                        #print "ERROR"
	
			#query="INSERT INTO Data(T_plate, T_1, C_1, T_2, C_2, T_3, C_3, T_4, C_4, T_5, C_5, T_6, C_6, T_7, C_7, T_8, C_8, TIME) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"       
                	#cur.execute(query, (t_plate, t_1, c_1, t_2, c_2, t_3, c_3, t_4, c_4, t_5, c_5, t_6, c_6, t_7, c_7, t_8, c_8,t))
			#logging.info('Inserting into base sucessfull')
			#logging.warning('vo baza')
		#con.commit()
		#cur.close()
		#con.close()
		
        return t_plate, t_1, c_1, t_2, c_2, t_3, c_3, t_4, c_4, t_5, c_5, t_6, c_6, t_7, c_7, t_8, c_8

	
