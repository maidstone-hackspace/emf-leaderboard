### Author: Maidstone Hackspace
### License: MIT
### Appname: whats my ip
### Description: whats my ip


import wifi
import ugfx
import pyb
import time
import buttons
from http_client import *
import json
import math
	
def mainscreen():
	ugfx.area(0,0,ugfx.width(),ugfx.height(),0x0000)
	ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)	
	ugfx.text(30,30,"Whats My IP",ugfx.YELLOW)
	ugfx.text(40,75,"Press [A] to continue",ugfx.YELLOW)
	return

def getdata():
	server = 'badge.emf.camp'
	#url = 'http://'+server+':9002/schedule'
	#url = 'http://hackspace-leaderboard-scollins.c9users.io/schedule'
	url = 'http://api.ipify.org/'
	resp = get(url).text
	ugfx.area(0,0,ugfx.width(),ugfx.height(),0x0000)
	while True:
		ugfx.text(30,30,resp,ugfx.WHITE)
	return json.loads(resp)

#Check and Connect to WiFi
if wifi.is_connected():
	pass
else:
	wifi.connect()

#Init GFX and Buttons
ugfx.init()
buttons.init()

#Main Screen
mainscreen()
while True:
	if buttons.is_triggered('BTN_A'):
		getdata()
	if buttons.is_triggered('BTN_B'):
		mainscreen()
		
		
	
 
