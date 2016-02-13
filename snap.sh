#!/bin/bash

DATE=`date +"%Y%m%d-%H%M"`
raspistill -o /home/pi/Pictures/$DATE.jpg
