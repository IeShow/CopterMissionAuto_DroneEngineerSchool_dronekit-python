from dronekit import connect, TimeoutError, VehicleMode, LocationGlobal
import time
import math



def get_distance_metres(aLocation1, aLocation2):
    """
    Returns the ground distance in metres between two LocationGlobal objects.
    This method is an approximation, and will not be accurate over large distances and close to the 
    earth's poles. It comes from the ArduPilot test code: 
    https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
    """
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5


vehicle = connect('127.0.0.1:14551', wait_ready=True, timeout=60)


targetlocation=LocationGlobal(35.514063, 138.744247, vehicle.location.global_frame.alt)

for i in range(10):
    print(" Armed: %s" % vehicle.armed)    # settable
    print(vehicle.velocity)
    print(vehicle.location.global_relative_frame)
    print(get_distance_metres(vehicle.location.global_frame, targetlocation))
    print(get_distance_metres(vehicle.location.global_frame, targetlocation) * 10.0)
    print(" Global Location: %s" % vehicle.location.global_frame)
    print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
    print(" Local Location: %s" % vehicle.location.local_frame)
    print("GLx",float(str(vehicle.location.global_frame).split(":")[1].split(",")[0].split("=")[1]))
    print("GLy",float(str(vehicle.location.global_frame).split(":")[1].split(",")[1].split("=")[1]))
    print("GLz",float(str(vehicle.location.global_frame).split(":")[1].split(",")[2].split("=")[1]))
    time.sleep(1)