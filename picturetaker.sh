#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 320x240 --jpeg 80 -D 3 -S 13 /home/pi/poochpics/$DATE.jpg

find /home/pi/poochpics/*.jpg -mtime +1 -exec rm {} \;
