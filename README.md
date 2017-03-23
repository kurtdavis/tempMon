

sudo apt-get update

# Common tools
sudo apt-get install git vim


### Temp sensor installs
# Add line to  /boot/config.txt
sudo echo "dtoverlay=w1-gpio" >> /boot/config.txt

# Add the python lib:
sudo pip install w1thermsensor


### Display installs
# Add SPI line to /boot/config.txt
echo "dtparam=spi=on" >> /boot/config.txt

# Add i2c for display (could be done with gui:  sudo raspi-config )
 #  sudo apt-get install python-smbus
 #  sudo apt-get install i2c-tools
 #  
 #  sudo echo "dtparam=i2c_arm=on" >> /boot/config.txt
 #  sudo echo "dtparam=i2c1=on" >> /boot/config.txt
 #  sudo echo "i2c-bcm2708" >> /etc/modules
 #  sudo echo "i2c-dev" >> /etc/modules

# Add display drivers/image drawing stuff.
sudo apt-get install build-essential python-dev python-pip
sudo pip install RPi.GPIO
sudo apt-get install python-imaging python-smbus

# Pull repo and install SSD1306 chipset python drivers
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install

# If errors from repo state, need to force install again after pull
# sudo python setup.py install --force


### Add Dropbox uploader script

sudo apt-get install -y curl
cd ~
git clone https://github.com/andreafabrizi/Dropbox-Uploader.git
cd Dropbox-Uploader
chmod a+x dropbox_uploader.sh
sudo cp dropbox_uploader.sh /usr/local/bin/dropbox_uploader




### Add motion detection... need to setup kernel for video4linux 2 api
sudo echo "bcm2835_v4l2" >> /etc/modules
# to check: ls -l /dev/video*
#   assert: /dev/video0
#  if fail: sudo modprobe bcm2835_v4l2

sudo apt-get install -y motion
# fix perms for motion image store:
sudo mkdir /var/lib/motion
sudo chown motion:motion /var/lib/motion

#   vim /etc/motion/motion.conf
## update these lines:
##   
##   # Image width (pixels). Valid range: Camera dependent, default: 352
##   width 1280
##    
##   # Image height (pixels). Valid range: Camera dependent, default: 288
##   height 720
##   
##   threshold 3000
##   minimum_motion_frames 2
##   ffmpeg_output_movies off
##   
##   # Command to be executed when a picture (.ppm|.jpg) is saved (default: none)
##   # To give the filename as an argument to a command append it with %f
##   on_picture_save dropbox_uploader -f /home/pi/.dropbox_uploader upload %f "Cloud Cam/"

# start motion on boot
#   vim /etc/default/motion
## update the 'no' to 'yes'
## 
##    start_motion_daemon=yes

sudo systemctl enable motion
sudo systemctl restart motion


# to inspect motion's captures:
sudo journalctl -u motion

# Allow motion to read the dropbox settings:
sudo groupadd dropbox -g777
sudo usermod -aG dropbox pi
sudo usermod -aG dropbox motion
chmod g+r .dropbox_uploader
sudo chown pi:dropbox .dropbox_uploader




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
