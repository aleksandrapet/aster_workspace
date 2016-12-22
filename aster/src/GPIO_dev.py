import RPi.GPIO as GPIO
import sys
import os

GPIO.setmode(GPIO.BCM)



GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
if GPIO.input(12):
	print("PIN 12 HIGH")
else:
	print("PIN 12 LOW")
	

GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
if GPIO.input(16):
	print("PIN 16 HIGH")
else:
	print("PIN 16 LOW")

GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
if GPIO.input(20):
	print("PIN 20 HIGH")
else:
	print("PIN 20 LOW")

GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
if GPIO.input(21):
	print("PIN 21 HIGH")
else:
	print("PIN 21 LOW")

GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
if GPIO.input(18):
	print("PIN 18 HIGH")
else:
	print("PIN 18 LOW")

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
if GPIO.input(23):
	print("PIN 23 HIGH")
else:
	print("PIN 23 LOW")

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
if GPIO.input(24):
	print("PIN 24 HIGH")
else:
	print("PIN 24 LOW")

GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
if GPIO.input(25):
	print("PIN 25 HIGH")
else:
	print("PIN 25 LOW")
