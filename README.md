# CopterMissionAuto_DroneEngineerSchool_dronekit-python  
Copterの作成されたミッションのロード、離陸、ミッション動作、終了後着陸までを自動動作させるコード。dronekit-pythonで作成。  
## How to use  
```
# SITLを動作
sim_vehicle.py -v ArduCopter --custom-location=35.51150,138.753830,0,0 --map --console
# 別ターミナルでmain.pyを動作
python main.py
```  
スタート位置は動作時のcustom-locationの値を変更することで変更。  
ミッションはミッションプランナーで作成。  
スタート位置と目的地のミッションテキストを作成してミッションプランナーでロードし、  
途中経路を追加することで任意の経路を通るミッションを作成する。  


