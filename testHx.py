from machine import SPI, I2C, Pin
#from hx711_spi import *
from hx711 import *
import mqtt_publisher as mq
import network

from utime import ticks_ms, ticks_diff, sleep, sleep_ms

#========== Strain Gauge Communication =======
pin_OUT = Pin(21, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK = Pin(22, Pin.OUT)

hx = HX711(pin_SCK, pin_OUT)
hx.OFFSET = 12.9 # -150000
hx.set_gain(128)
sleep_ms(50)
scale = 25000.0
#===============================================
def getdata():
    for i in range(10):
        data = hx.read()/scale
        print(data - hx.OFFSET) 
        sleep(1)
      #  lcd.putstr("Strain Gauge " +"\n")
      #  lcd.putstr(str(data)+"\n")
        return data 
#=========== WIFI ==========================
def connect_to_network():
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
   #print(sta_if.scan())
    while (sta_if.isconnected) is False:
        sta_if.connect("Kikidoodle_Network", "Bottle$TORE101!")
        sleep(1)
        print("Network Connected: ", sta_if.isconnected())

    print("Network Connected: ", sta_if.isconnected())


if __name__=="__main__":
    connect_to_network()
    print("NOT CALIBRATED!")
    data = getdata()
    mq.publish(data)
    