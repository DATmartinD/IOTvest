import umqtt_robust2 as mqtt
import gps_funktion
from machine import Pin
from time import sleep


def gpsData():
        
    try:
        gps_data = gps_funktion.gps_to_adafruit
        print(f"\ngps_data er: {gps_data}")
        

        mqtt.web_Print(gps_data, 'casp262k/feeds/mapfeed/csv')        
        sleep(4)
        
        if len(mqtt.besked) != 0:
            mqtt.besked = ""            
        mqtt.syncWithAdafruitIO()           
        print(".", end = '')     

    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()
