# test code
from machine import Pin
import framebuf
import utime, time

button1 = Pin(14, Pin.IN, Pin.PULL_UP)
button2 = Pin(15, Pin.IN, Pin.PULL_UP)
button3 = Pin(16, Pin.IN, Pin.PULL_UP)
button4 = Pin(17, Pin.IN, Pin.PULL_UP)

Led = Pin(25, Pin.OUT) # "LED" to select onboard led for Pico
#Led = Pin("LED", Pin.OUT) # "LED" to select onboard led for Pico W

print("Press Buttons to test!!")
while 1:
    val1 = button1.value()
    val2 = button2.value()
    val3 = button3.value()
    val4 = button4.value()
    
    if val1 == 0 :
        print("Bt1 = ", val1)
        print('Switch 1 Pressed\n')
        Led.on()  #To switch on LED
        print("LED is ON")
        
    if val2 == 0 :
        print("Bt2 = ", val2)
        print('Switch 2 Pressed\n')
        Led.on()  #To switch on LED
        print("LED is ON")       
        
    if val3 == 0 :
        print("Bt3 = ", val3)
        print('Switch 3 Pressed\n')
        Led.on()  #To switch on LED
        print("LED is ON") 
        
    if val4 == 0 :
        print("Bt4 = ", val4)
        print('Switch 4 Pressed\n')
        Led.on()  #To switch on LED
        print("LED is ON") 
        
    time.sleep(0.5)
    Led.off() #To switch off LED


