#!/usr/bin/env python

import math
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import Image
import ImageDraw
import ImageFont

from cageDisplay.facts import diskUsage
from cageDisplay.facts import ipaddr

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))


# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()


image = Image.new('1', (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Draw an ellipse.
draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
x += shape_width+padding
# Draw a rectangle.
draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
x += shape_width+padding
# Draw a triangle.
draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
x += shape_width+padding
# Draw an X.
draw.line((x, bottom, x+shape_width, top), fill=255)
draw.line((x, top, x+shape_width, bottom), fill=255)
x += shape_width+padding

# Draw the image buffer.
disp.image(image)
disp.display()

myDisk = diskUsage.diskUsage();
print myDisk.quickCheck()




# Load default font.
font = ImageFont.load_default()

# Define text and get total width.
text = 'SSD1306 ORGANIC LED DISPLAY.'
maxwidth, unused = draw.textsize(text, font=font)




disp.clear() # This clears the display but only when there is a led.display() as well!

# led.draw_text2(x-axis, y-axis, whatyouwanttoprint, size) < Understand?
# So led.drawtext2() prints simple text to the OLED display like so:

upstairsStr = 'Upstairs: ' + '93deg'
targetStr   = 'target:   ' + '71deg'

# Draw text.
# draw.text((x, y), c, font=font, fill=255)

draw.text((0,0),myDisk.quickCheck(),2)
draw.text((85,0),'HI',4)
draw.text((2,16),upstairsStr,1)
draw.text((2,25),targetStr,1)
disp.image(image)
disp.display()

exit

time.sleep(6.1)








# Set animation and sine wave parameters.
amplitude = height/4
offset = height/2 - 4
velocity = -2
startpos = width

# Animate text moving in sine wave.
print 'Press Ctrl-C to quit.'
print 'IP: ' + ipaddr.getNetIp()
pos = startpos
while True:
	# Clear image buffer by drawing a black filled box.
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	# Enumerate characters and draw them offset vertically based on a sine wave.
	x = pos
	for i, c in enumerate(text):
		# Stop drawing if off the right side of screen.
		if x > width:
			break
		# Calculate width but skip drawing if off the left side of screen.
		if x < -10:
			char_width, char_height = draw.textsize(c, font=font)
			x += char_width
			continue
		# Calculate offset from sine wave.
		y = offset+math.floor(amplitude*math.sin(x/float(width)*2.0*math.pi))
		# Draw text.
		draw.text((x, y), c, font=font, fill=255)
		# Increment x position based on chacacter width.
		char_width, char_height = draw.textsize(c, font=font)
		x += char_width
	# Draw the image buffer.
	disp.image(image)
	disp.display()
	# Move position for next frame.
	pos += velocity
	# Start over if text has scrolled completely off left side of screen.
	if pos < -maxwidth:
		pos = startpos
	# Pause briefly before drawing next frame.
	time.sleep(0.1)
