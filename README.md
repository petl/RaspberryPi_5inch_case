# Raspberry Pi 5inch touch LCD case

3D model of a case for the Raspberry Pi 2,3,4 with a 5' touch LCD and four buttons.


![Final Work](https://github.com/petl/RaspberyyPi_5inch_case/blob/master/Photos/IMG_20200413_133427.jpg)
The Final setup in its natural habitat with the weather, central heating and public transport monitor open. 

More in depth explaination here: https://quiescentcurrent.com/blog/post.php?p_id=61

## Hardware

I've used a Raspberry Pi 2, but a Pi 3 or 4 should also work. 

The LC-Display is a 5 inch resistive touchscreen, which can be bought for around 25$ form [ebay](https://www.ebay.at/itm/5-Inch-800x480-HDMI-Touch-LCD-Screen-Display-For-Raspberry-Pi-3-Pi2-Model-B-A/201703903207) or [amazon](https://www.amazon.de/Resistive-Touch-Screen-Display-interface/dp/B071CKFTJH/). 

The fours buttons are 12mm types, [ebay](https://www.ebay.at/itm/Mini-12mm-wasserdicht-Momentan-ON-OFF-Push-Button-runden-SchaRSDE/312865346056) is also your friend here, but any electronic component supplier has those. 

## 3D printed parts

The parts are drawn in solid edge and exported as is usual as stl. You can slice them yourself or just take a look at my design skills. 

Especially the LCD it quite a perfect fit on my lulzbot mini, maybe you have to play around a bit with the settings. 

The four screws are meant to be M3 x 20, if you don't have those just use any reasonably sized ones. They are responsible for holding in the LCD by applying pressure to the back of the raspberry, I've applied some sticky foam tape on the back cover so the Pi can't wiggle around, but without should also be fine.  

![Rendering Front](https://github.com/petl/RaspberryPi_5inch_case/blob/master/Renderings/Screen-Raspi_5inch_front_v0_front.bmp)


## Software

The raspberry can use the touchscreen more or less natively. If you're unsure about how to setup up your pi, use this [insctructables.com](https://www.instructables.com/id/Setting-Up-an-800X400-5inch-HDMI-LCD-for-Raspberry/).

I've added three files: 

* buttonWatch.py: This is a small Python script used to detect pressed buttons and translate them into virtual keyboard presses in order to operate the chromium / chrome webbrowser. The script can right now scroll down, up, go ho the homepage and go back. The buttons are mapped to four free pins (6,13,19,26) on the RPi header. You need to install pyntput with:
>  pip install pynput


* startChromium.sh: Starts the buttonWatch.py and then chromium browser in Kiosk mode. It disables the mouse pointer and a few things so it looks nice while idling.

* autostart: this file is just the windowmanager autostart procedure and should be copied to .config/lxsession/LXDE-pi/autostart so it gets run when the pi has finished booting up. It basically starts the wifi and then the chromium browser. 

The whole blog post with more pictures is [here](https://quiescentcurrent.com/blog/post.php?p_id=61).

