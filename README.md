# Pico_Universal_E-Paper_HAT_Software

Universal ePaper HAT is based on the Raspberry Pi Pico W which can be attached to any sizes of E-Paper screens ranging from 2.9", 4.2", 5.83" & 7.5".
It has dual clips - on top and bottom side of the HAT to attach a display of any dimensions.
<img src="https://github.com/sbcshop/Pico_Universal_E-Paper_HAT_Software/blob/main/images/universal_epaper_hat.gif" />

This Universal ePaper HAT is equipped with additional GPIO pins which can be programmed as per user's requirements.This universal HAT is compatible with both Raspberry Pi Pico and Raspberry Pi Pico W. Comes with a pair of Female Header Pins which can be soldered, if needed, to access additional devices.
<img src="https://github.com/sbcshop/Pico_Universal_E-Paper_HAT_Software/blob/main/images/universal_epaper_hat_pinout.png" />

## Getting Started guide
### 1. Step to install boot Firmware in Pico W
   - Follow this steps only if you need to install firmware for your Pico W, then you can follow the tutorial [here](https://github.com/sbcshop/PiCoder-Software/blob/main/README.md#1-how-to-install-boot-firmware-in-picoder-kit)

### 2. Testing Pico W
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect EnkPi with a laptop/PC using a micro USB cable and the micro USB port on Pico W present on EnkPi.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/Pico_Universal_E-Paper_HAT_Software/blob/main/examples/onboard_ledBlink.py), then click on the green run button to make your script run. 
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up Pico and it should run your script, go to step 3. 
    
### 3. How to move your script on Pico W
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as main.py
      <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr1.jpg" />
      <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr2.jpg" />
      <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr3.jpg" />
      <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr4.jpg" />

### Example Codes
   Depending upon which E-paper you are using, Follow corresponding tutorial to work with E-paper
   - [Click Here](https://github.com/sbcshop/EnkPi_2.9_Software) - to use with 2.9" E-paper
   - [Click Here](https://github.com/sbcshop/EnkPi_4.2_Software) - to use with 4.2" E-paper
   - [Click Here](https://github.com/sbcshop/EnkPi_5.83_Software) - to use with 5.83" E-paper
   - [Click Here](https://github.com/sbcshop/EnkPi_7.5_Software) - to use with 7.5" E-paper
   
   Now you are ready to try out your own codes, **_Happy Coding!_**

## Documentation
  * [MicroPython getting started for RPI](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related Products
   ![EnkPi2_9]()
   * [EnkPi 2.9"](https://shop.sb-components.co.uk/products/enkpi?variant=40474297401427) - EnkPi with 2.9" E-paper display size
   
   ![EnkPi4_2]() 
   * [EnkPi 4.2"](https://shop.sb-components.co.uk/products/enkpi?variant=40474297434195) - EnkPi with 4.2" E-paper display size
   
   ![EnkPi5_83]()
   * [EnkPi 5.83"](https://shop.sb-components.co.uk/products/enkpi?variant=40474297466963) - EnkPi with 5.83" E-paper display size
 
   ![EnkPi7_5]()
   * [EnkPi 7.5"](https://shop.sb-components.co.uk/products/enkpi?variant=40474297499731) - EnkPi with 7.5" E-paper display size
 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>

