#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import thread
import time
def print_time( threadName, delay):
   word = '输入想输出的音频,输入想输出的音频,输入想输出的音频,2.5元一斤'
   cmd = "ilang "+word
   os.system(cmd)
#word = raw_input('输入想输出的音频')
#print(word)
#reload9(sys)
#sys.s9etdefaultcoding("utf-8")
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
except:
   print "Error: unable to start thread"
 
print 'jddjdj'
time.sleep(20)