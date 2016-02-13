
# Common tools
sudo apt-get install git vim


### Temp sensor installs
# Add line to  /boot/config.txt
echo "dtoverlay=w1-gpio" >> /boot/config.txt

# Add the python lib:
sudo pip install w1thermsensor


### Display installs
# Add SPI line to /boot/config.txt
echo "dtparam=spi=on" >> /boot/config.txt

sudo apt-get update
sudo apt-get install build-essential python-dev python-pip
sudo pip install RPi.GPIO
sudo apt-get install python-imaging python-smbus

# Pull repo and install SSD1306 chipset python drivers
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install


# Documentation and Tutorials
#  ------------------------------------------------------
#  Companion Parts Pack for Adventures in Raspberry Pi
#   Tutorials: [[http://www.adafruit.com/products/1775#tutorials]]
#  Raspberry Pi 2 - Model B - ARMv7 with 1G RAM
#   Tutorials: [[http://www.adafruit.com/products/2358#tutorials]]
#  16mm Illuminated Pushbutton - Red Momentary
#   Tutorials: [[http://www.adafruit.com/products/1439#tutorials]]
#  16mm Illuminated Pushbutton - Green Momentary
#   Tutorials: [[http://www.adafruit.com/products/1440#tutorials]]
#  DS18B20 Digital temperature sensor + extras
#   Tutorials: [[http://www.adafruit.com/products/374#tutorials]]
#  Raspberry Pi Camera Board
#   Tutorials: [[http://www.adafruit.com/products/1367#tutorials]]
#  Premium Female/Male 'Extension' Jumper Wires - 20 x 6"
#   Tutorials: [[http://www.adafruit.com/products/1954#tutorials]]
#  Adafruit GPIO Reference Card for Raspberry Pi Model B
#   Tutorials: [[http://www.adafruit.com/products/2262#tutorials]]
#  Rotary Encoder + Extras
#   Tutorials: [[http://www.adafruit.com/products/377#tutorials]]
#  Adafruit Assembled Pi T-Cobbler Breakout for Raspberry Pi
#   Tutorials: [[http://www.adafruit.com/products/1754#tutorials]]
#  Raspberry Pi Model B+ / Pi 2 Case Lid - Smoke Gray
#   Tutorials: [[http://www.adafruit.com/products/2244#tutorials]]
#  Pi Model B+ / Pi 2 Case Base - Smoke Gray
#   Tutorials: [[http://www.adafruit.com/products/2256#tutorials]]
#  
#  -----

# 
# OLED Display
# https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black
# https://github.com/adafruit/Adafruit_Python_SSD1306
