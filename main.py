import time
from dronekit import connect, TimeoutError, VehicleMode, LocationGlobal
from mission_tool import*
import math


# 2点間距離判定[m]
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


# ミッションのロード
import_mission_filename = 'copter2plane_ver01.waypoints'
#export_mission_filename = 'exportedmission.txt'

#Upload mission from file
upload_mission(import_mission_filename, vehicle)
print("mission upload finish")

# 離陸
try:
    vehicle.wait_for_mode("GUIDED")
    vehicle.wait_for_armable()
    vehicle.arm()
    time.sleep(1)
    vehicle.wait_simple_takeoff(10, timeout=60)
    # vehicle.wait_simple_takeoff(20,0.5,15)
    print("Takeoff is over altitude 20m")

except TimeoutError as takeoffError:
    print("Takeoff is timeout!!!")
    # フェールセーフコード


# 目標位置オブジェクト作成
targetlocation=LocationGlobal(35.514063, 138.744247, vehicle.location.global_frame.alt)

# Autoモードへ変更
vehicle.mode = VehicleMode("AUTO")
print("Auto mode start")

# 着陸判定(Autoの判定と同じか広く設定)
goledist_th = 1.5 # [m]
while True:
    currentlocatin = vehicle.location.global_frame
    dist = get_distance_metres(currentlocatin, targetlocation)
    print("move", dist)
    if dist <= goledist_th:
        vehicle.mode = VehicleMode("LAND")
        break
    time.sleep(1)
print("Landing")
# disarmedをチェックして着陸確認
while vehicle.armed: 
    print("Armed", vehicle.armed)
    time.sleep(1)
print("Armed", vehicle.armed)
print("finish")
