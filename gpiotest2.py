import RPi.GPIO as GPIO
import time
from socket import *

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

def init():
    GPIO.setup(12,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)

 

def avancer ():
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1/2)

    GPIO.output(12, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)


def reculer():
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(1/2)

    GPIO.output(16, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)

def reculerDroite():
    GPIO.output(16, GPIO.HIGH)
    time.sleep(1/5)
    GPIO.output(16, GPIO.LOW)


def reculerGauche():
    GPIO.output(22, GPIO.HIGH)
    time.sleep(1/5)
    GPIO.output(22, GPIO.LOW)
    


def tournerdroite():
 
    GPIO.output(12, GPIO.HIGH)

    time.sleep(1/5)

    GPIO.output(12, GPIO.LOW)

    


def tournergauche():
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1/5)

    GPIO.output(18, GPIO.LOW)


def stop():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    


