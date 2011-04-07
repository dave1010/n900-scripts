#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Automatic device unlock based on current WLAN AP
#By Olli Laasonen 6.4.2011

#Libraries
######################################################
import gobject, dbus, os, sys
gobject.threads_init()
from dbus.mainloop.glib import DBusGMainLoop
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

#Classes
######################################################
class AutoUnlocker:
	def  __init__(self):
		self.ssids=["44g", "Base", "Wolc"] #Put your SSID
		self.bus = dbus.bus.BusConnection("unix:path=/var/run/dbus/system_bus_socket")
		self.object = self.bus.get_object('com.nokia.mce', '/com/nokia/mce/request')
		self.interface = dbus.Interface(self.object, dbus_interface='com.nokia.mce.request')
 
	def start(self): #Check for events
		self.bus.add_signal_receiver(self.unlock, path='/com/nokia/mce/signal', dbus_interface='com.nokia.mce.signal', signal_name='tklock_mode_ind')
		gobject.MainLoop().run()

	def unlock(self, tklock): #Unlock device
		if self.interface.get_devicelock_mode() == "locked" and tklock == "unlocked":
			ssid = os.popen("/sbin/iwgetid | awk -F'\"' '{print $2}'")
			ssid = ssid.readline()
			if ssid[0:-1] in self.ssids:
				#TODO: Do this with python..
				os.system("dbus-send --system --type=method_call --dest=com.nokia.system_ui /com/nokia/system_ui/request com.nokia.system_ui.request.devlock_close string:'com.nokia.mce' string:'/com/nokia/mce/request' string:'com.nokia.mce.request' string:'devlock_callback' uint32:'0'")

#Run
######################################################
if __name__ == "__main__":
	#First fork
	try: 
		pid = os.fork() 
		if pid > 0:
			sys.exit(0) 
	except OSError, e: 
		sys.exit(1)
	#Enviroment
	os.chdir("/") 
	os.setsid() 
	os.umask(0)
	#Second fork 
	try: 
		pid = os.fork() 
		if pid > 0:
			sys.exit(0) 
	except OSError, e: 
		sys.exit(1)
	#Start 
	daemon = AutoUnlocker()
	daemon.start()

