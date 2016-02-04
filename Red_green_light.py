from xbee import XBee
import serial
import sys, os, socket
import time
import threading
from threading import Timer

def violation():
    
    print "Violation recorded on car number ",rl_number
    final_number=rl_number+" x100"+" RL"+" Sala7 Salem"+" 500"+" unpaid"
    s.send(final_number)
    
#Connect to Xbee com port
serial_port=serial.Serial(18,9600)
xbee1=XBee(serial_port)
#Connect to Xbee com port

###Connect to python insertion server 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5943))
###Connect to python insertion server

light="red"
counter=0
while True:    
  number="" 
  i=0     
  while i<14:   #number specifying the violation threshold    
      if light=="red":
           t = Timer(3.0, violation)
           if counter==1:
            t.start()            
      b= serial_port.read()
      counter=1
      t.cancel()                   
      x=str(b) 
      i=i+1
      number=number+x
      rl_number=number

  print rl_number 
       

  
               
           

   
  
  


       

        
