#!/bin/sh
if [ `dbus-send --system --type=method_call --print-reply --dest=com.nokia.phone.net /com/nokia/phone/net Phone.Net.get_selected_radio_access_technology | awk '/b/ {print $2}'` -eq 1 ]; then
dbus-send --system --type=method_call --dest=com.nokia.phone.net /com/nokia/phone/net Phone.Net.set_selected_radio_access_technology byte:0
dbus-send --type=method_call --dest=org.freedesktop.Notifications /org/freedesktop/Notifications org.freedesktop.Notifications.SystemNoteInfoprint string:"Network mode is set to Dual"
else
dbus-send --system --type=method_call --dest=com.nokia.phone.net /com/nokia/phone/net Phone.Net.set_selected_radio_access_technology byte:1
dbus-send --type=method_call --dest=org.freedesktop.Notifications /org/freedesktop/Notifications org.freedesktop.Notifications.SystemNoteInfoprint string:"Network mode is set to 2G"
fi

