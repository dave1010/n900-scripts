#!/usr/bin/python
import location
import gobject

# from happy_n900_user
# via http://talk.maemo.org/showthread.php?t=47301

def on_error(control, error, data):
    print "location error: %d... quitting" % error
    data.quit()

def on_changed(device, data):
    if not device:
        return
    if device.fix:
        if (device.fix[1] & 
location.GPS_DEVICE_LATLONG_SET) and (device.fix[1] & 
location.GPS_DEVICE_TIME_SET) and not (device.status 
& location.GPS_DEVICE_STATUS_NO_FIX):
            print "%f, %f" % device.fix[4:6]
            data.stop()

def on_stop(control, data):
    #print ""
    data.quit()

def start_location(data):
    data.start()
    return False

loop = gobject.MainLoop()
control = location.GPSDControl.get_default()
device = location.GPSDevice()
control.set_properties(preferred_method=location.METHOD_USER_SELECTED,
                       
preferred_interval=location.INTERVAL_DEFAULT)

control.connect("error-verbose", on_error, loop)
device.connect("changed", on_changed, control)
control.connect("gpsd-stopped", on_stop, loop)

gobject.idle_add(start_location, control)

loop.run()
