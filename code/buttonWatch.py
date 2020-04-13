###
#Script to detect a pressed button on an raspberry pi and scroll up/down on a chromium webpage
#12.4.2020
#peter@traunmueller.net
###
import RPi.GPIO as GPIO
import time
from pynput.keyboard import Key, Controller


#pins
scrollDN = 26
scrollUP = 19
back = 13
home = 6

#setup
GPIO.setmode(GPIO.BCM)
keyboard = Controller()


#pinmodes
GPIO.setup(scrollDN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(scrollDN, GPIO.FALLING, bouncetime=400)
GPIO.setup(scrollUP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(scrollUP, GPIO.FALLING, bouncetime=400)
GPIO.setup(back, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(back, GPIO.FALLING, bouncetime=800)
GPIO.setup(home, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(home, GPIO.FALLING, bouncetime=800)



def func_scrollDN(argument):
    #print(argument) #outputs the pressed pin number
    print("scrollDN")
    keyboard.press(Key.page_down)
    #time.sleep(0.01)#
    keyboard.release(Key.page_down)
    time.sleep(0.3)#debounce


def func_scrollUP(argument):
    #print(argument) #outputs the pressed pin number
    print("scrollUP")
    keyboard.press(Key.page_up)
    #time.sleep(0.01)#
    keyboard.release(Key.page_up)
    time.sleep(0.3)#debounce


def func_back(argument):
    #print(argument) #outputs the pressed pin number
    print("back")
    keyboard.press(Key.alt_l)#chromium/chrome shortcut for back
    keyboard.press(Key.left)
    #time.sleep(0.01)#
    keyboard.release(Key.alt_l)
    keyboard.release(Key.left)
    time.sleep(0.3)#debounce


def func_home(argument):
    #print(argument) #outputs the pressed pin number
    print("home")
    keyboard.press(Key.alt_l)#chromium/chrome shortcut for go to homepage
    keyboard.press(Key.home)
    #time.sleep(0.01)#
    keyboard.release(Key.alt_l)
    keyboard.release(Key.home)
    time.sleep(0.3)#debounce



GPIO.add_event_callback(scrollDN, func_scrollDN)
GPIO.add_event_callback(scrollUP, func_scrollUP)
GPIO.add_event_callback(back, func_back)
GPIO.add_event_callback(home, func_home)





while True:
    #wait for an interrupt
    time.sleep(0.01)



    keyboard.press(Key.page_up)
    #time.sleep(0.01)#
    keyboard.release(Key.page_up)
    time.sleep(0.3)#debounce
