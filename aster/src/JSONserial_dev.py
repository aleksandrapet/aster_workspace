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

	
def ser_read():

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


		t_plate=37.00
		t_1=36.9
		c_1=5.0
		t_2=37.00
		c_2=5.0
		t_3=37.01
		c_3=5.0
		t_4=37.03
		c_4=5.0
		t_5=37.0
		c_5=5.0
		t_6=36.90
		c_6=5.0
		t_7=37.00
		c_7=5.0
		t_8=37.00
		c_8=5.0

		return (t_plate, t_1, c_1, t_2, c_2, t_3, c_3, t_4, c_4, t_5, c_5, t_6, c_6, t_7, c_7, t_8, c_8)
