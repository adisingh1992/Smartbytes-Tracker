###########################################################################################################
##IMPORTED LIBRARIES
###########################################################################################################

from bs4 import BeautifulSoup
from datetime import date
from time import sleep
import requests
import dbus
import re

###########################################################################################################
##NOTIFY FUNCTION FROM DBUS LIBRARY (NOT-MY-CODE)
###########################################################################################################

def notify(summary, body='', app_name='', app_icon='', timeout=10000, actions=[], hints=[], replaces_id=0):
	_bus_name = 'org.freedesktop.Notifications'
	_object_path = '/org/freedesktop/Notifications'
	_interface_name = _bus_name

	session_bus = dbus.SessionBus()
	obj = session_bus.get_object(_bus_name, _object_path)
	interface = dbus.Interface(obj, _interface_name)
	interface.Notify(app_name, replaces_id, app_icon,summary, body, actions, hints, timeout)

###########################################################################################################
##ACCESSING THE WEBPAGE AND PARSING THE HTML
###########################################################################################################

while (True):
	today = date.today().day
	if (today > 25 or today < 11):
		r = requests.get('http://122.160.230.125:8080/planupdate/')
		raw_html = BeautifulSoup(r.text, "lxml")

		search_term = "You are left with only"
		node = raw_html.find(string=re.compile(search_term))

		data_left = node.next_sibling.get_text()

		msg = "Start saving...!! You are low on data, Only "+ data_left +" left."

		notify(msg)
	sleep(3600)

###########################################################################################################
###########################################################################################################
