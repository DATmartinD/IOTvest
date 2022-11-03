from imu import MPU6050  # https://github.com/micropython-IMU/micropython-mpu9x50
import time
from machine import Pin, I2C
import tm1637

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)
tackling = 0
 
# Temperature display

def imu.funktion()
    # reading values
    
    tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))
    tm.number(0)
    
    acceleration = imu.accel
    gyroscope = imu.gyro  
    print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2),
           "z: ", round(acceleration.z,2))

# data interpretation (acceleromet er)

    if abs(acceleration.x) >= 1 or abs(acceleration.z) >= 0.8:
         
         tackling = tackling + 1
         tm.number(tackling)
         while (acceleration.y) >= 1: 
             time.sleep(1)

#HVIS faldstatus er false og accl vørdien  på x aksen er faldet fald status er true