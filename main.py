import umqtt_robust2 as mqtt
from machine import Pin, ADC, I2C
from time import sleep
import ssd1306

analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)

i2c =I2C(-1,scl=Pin(26), sda=Pin(27))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)

# oled.fill(0)
# oled.text ("test"(50, 50))
# oled.show

def battery_percentage():
    analog_val = analog_pin.read()
    volts = (analog_val * 0.00086)*5
    battery_percentage = (volts/2)*100-320
    print("The battery persentage is:", battery_percentage, "%")
    sleep(1)
    return battery_percentage

    mqtt.web_Print(battery_percentage())

while True:
    oled.fill(0)
    bat = "battery:"+ str(battery_percentage())+"%"
    oled.text(bat,25,30)
    oled.show()
    sleep(5)

while True:
    try:
                    
        sleep(0.5)
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""            
        mqtt.syncWithAdafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        print(".", end = '') # printer et punktum til shell, uden et enter        
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()