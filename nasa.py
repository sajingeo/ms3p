#!/usr/bin/env python
# coding: utf8
# This extends a Web interface to initialize the grow PODS, this is the code for a local 
# that would receive TCP sockets from the Web2py app, that provides the front interface 
# for GrowPOD, this is a modified from the PI link code from nasa space apps

from socket import *
#import RPi.GPIO as GPIO
import subprocess

SETUP = chr(0)
OUTPUT = chr(1)
LIGHTSON = chr(3)

LIGHTSOFF=chr(4)
FEEDSTART=chr(6)
FILLPOD=chr(7)

proc=0
pid=0

FLAG=False 

#GPIO.setmode(GPIO.BCM)

def gpio_setup(data):
    pin,dir = ord(data[0]),ord(data[1])
    #GPIO.setup(pin,dir)
    print "setup",pin,dir
    return 0

def gpio_output(data):
    pin,val = ord(data[0]),ord(data[1])
    #GPIO.output(pin,val)
    print "out",pin,val
    return 0

def podINIT(data):
    global proc
    global FLAG
    global pid
    patternval=ord(data[0])
    print patternval
    if(FLAG==True):
        print 'killing old guy'
        FLAG=False
	print proc
        proc.kill()
    else:     
        if patternval==4:
            FLAG=True
            print 'spawn feed'
            proc = subprocess.Popen(('./feed.py'))
        elif patternval==5:
            FLAG=True
            print 'spawn lights'
            proc = subprocess.Popen(['./lights.py'])
        elif patternval==5:
        	FLAG=True
            print 'spawn air'
            proc = subprocess.Popen(['./air.py'])
            
    return 0
    
if __name__=='__main__':
    HOST = 'localhost'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind(ADDR)
    serversock.listen(2)

    while 1:
        ret = None
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        data = clientsock.recv(BUFSIZ)
        if data[0] == SETUP:
            print 'entering SETUP'
            ret = gpio_setup(data[1:])
        elif data[0] == OUTPUT:
            print 'entering MODE'
            ret = gpio_output(data[1:])
        elif data[0]== PATTERN:
            print 'entering routine'
            ret=podINIT(data[1:])
        
            
        if  ret:
            clientsock.send(ret)
            clientsock.close()