#!/bin/sh
xset -dpms # disable DPMS (Energy Star) features.
xset s off # disable screen saver
xset s noblank # don't blank the video device
unclutter -idle 0.5 -root &

#matchbox-window-manager &
#midori -e fullscreen -a http://192.168.0.111/screen/screen_800x480.php

DISPLAY=":0" python /home/pi/buttonWatch.py & # start the button script too
/usr/bin/chromium-browser --check-for-update-interval=31536000 --noerrdialogs --disable-infobars --kiosk http://192.168.0.111/screen/screen_800x480.php &
