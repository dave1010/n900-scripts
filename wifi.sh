#!/bin/sh

# toggle wifi
# from http://wiki.maemo.org/Desktop_Command_Execution_Widget_scripts#Enable.2Fdisable_Wi-Fi

out=`ifconfig wlan0`
if [ $? -eq "0" ] ; then
if [ `echo "$out" | grep -c RUNNING` -gt "0" ] ; then
run-standalone.sh dbus-send --system --dest=com.nokia.icd /com/nokia/icd_ui com.nokia.icd_ui.disconnect boolean:true
fi
ifconfig wlan0 down
rmmod wl12xx
run-standalone.sh dbus-send --type=method_call --dest=org.freedesktop.Notifications /org/freedesktop/Notifications org.freedesktop.Notifications.SystemNoteInfoprint string:'Wi-Fi disabled'
exit 2
else
modprobe wl12xx
wl1251-cal
stop wlancond
start wlancond
ifconfig wlan0 up
run-standalone.sh dbus-send --system --type=method_call --dest=com.nokia.icd_ui /com/nokia/icd_ui com.nokia.icd_ui.show_conn_dlg boolean:false
exit 0
fi

