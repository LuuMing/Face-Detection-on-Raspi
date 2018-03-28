# -*- coding: utf-8 -*
from aip import AipSpeech
import numpy as np
import cv2
import RPi.GPIO as GPIO
import pygame
import os
import time
from time import strftime,gmtime
import sys
pygame.init()
pygame.mixer.init()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
APP_ID = '11011621'
API_KEY = 'GtembSekb8DY90BUIFz450Il'
SECRET_KEY = 'b89f0860e948a3e701f9b098f62cc97f'
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
def save_audio(name,result): 
    if not os.path.exists('./audio/'+name+'.mp3'):
        fileObject = open('./audio/'+name+'.mp3', 'w')  
        fileObject.write(client.synthesis(result, 'zh', 1, {'vol': 5}))  
        fileObject.close()  
    return './audio/'+name+'.mp3'
def High():
    GPIO.output(38,True)
    GPIO.output(40,False)
def Low():
    GPIO.output(38,False)
    GPIO.output(40,True)
def play(name):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    time.sleep(3)
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)    
start_detection = save_audio('s_d','启动人脸识别')
captured = save_audio('cap','捕捉到数据')
saved = save_audio('saved','数据已保存')
play(save_audio('init','初始化完成'))
