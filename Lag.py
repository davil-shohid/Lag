#! /usr/bin/env python 2.7.17
version = 1.0
import os
import sys
import time
def Clear ():
	os.system('clear')
def Figlet ():
	os.system('pkg install figlet')
	os.system('pip install lolcat')
def Volume ():
	t = "100"
	v = " \033[36;1mVolume \033[34;1m=\033[32;1m"
	im = (v + t)
	os.system('termux-volume music 100 ')
	print ('\033[31m Music' + im)
	os.system('termux-volume alarm 100 ')
	print ('\033[31m Alarm' + im)
	os.system('termux-volume notification 100 ')
	print ('\033[31m Notification' + im)
	os.system('termux-volume ring 100 ')
	print ('\033[31m Ring' + im)
	os.system('termux-volume system 100 ')
	print ('\033[31m System' + im)
	os.system('termux-volume call 100 ')
	print ('\033[31m Call' + im)
	Figlet ()
def All ():
	os.system('chmod +x n.sh ./n.sh')
	os.system('./n.sh')

def Davil ():
	print ('\033[36m')
	os.system('figlet -f big D A V I L | lolcat')
Volume ()
def Bannar ():
	print ('\033[31m')
	os.system('figlet -f big W E L C O M E | lolcat')
Clear ()
Davil ()
password= input ('\033[30;1musername : \033[32m')
username= input('\033[30;1mpassword : \033[32m') 
Clear ()
Bannar ()
print ('\033[33mwait....')
time.sleep(2)
Clear ()
print ("\033[35;1m  \033[33;1mhttp://t.me/Davil_Shohid_A\033[0m")
All ()
