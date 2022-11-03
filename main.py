from machine import Pin, ADC, I2C
from time import sleep
import umqtt_robust2 as mqtt
import gps_funktion
import ssd1306
import adafruit_gps_main
# import imu_funktion

analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)

i2c =I2C(-1,scl=Pin(26), sda=Pin(27))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)

def battery_percentage():
    analog_val = analog_pin.read()
    volts = (analog_val * 0.00086)*5
    battery_percentage = (volts/2)*100-320
    print("The battery persentage is:", battery_percentage, "%")
    return battery_percentage
        
while True: 
    oled.fill(0)
    bat = "battery:"+ str(battery_percentage())+"%"
    oled.text(bat,15,30)
    oled.show()
    mqtt.web_Print(battery_percentage())
    sleep(4)
    adafruit_gps_main.gpsData()
    sleep(4)