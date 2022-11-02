from machine import I2C
from machine import Pin
from machine import sleep
import tm1637
import mpu6050
import sys

#Initialisering af I2C objekt
I2C = I2C(scl=Pin(22), sda=Pin(21))
mpu = mpu6050.accel(I2C)
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))
tm.number(0)
val = mpu.get_values()
oppreist = val['AcZ']
tackling = 0
tackling = tackling + 1

#Initialisering af mpu6050 objekt

while True:
    val = mpu.get_values()
    oppreist = val['AcZ']
    while oppreist < 10000:
        val = mpu.get_values()
        Z = val['AcZ']
        while Z < 16000:
            tm.number(tackling)
            tackling = tackling + 1
            break
    print(val['AcZ'])
    sleep(2000)




