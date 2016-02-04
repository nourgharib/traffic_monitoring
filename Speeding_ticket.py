from xbee import XBee
import serial
import sys, os, socket
import time
import threading
from threading import Timer


def violation():
    global seconds
    if access==1:
        print "No Violation"
        seconds=-1
    else:
     print "Violation recorded on car number ",rl_number
     final_number=rl_number
     s.send(final_number)
     seconds=-1
    

#Connect to Xbee com port
serial_port=serial.Serial(18,9600)
xbee1=XBee(serial_port)
#Connect to Xbee com port

###Connect to python insertion server 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5943))
###Connect to python insertion server 
    
seconds=-1
counter=0


while True:
  access=0
  number="" 
  i=0
  seconds=seconds+1
  print seconds

  
  while i<14:
         
       if seconds>=10:
         access=1
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

 
       

  
               
           

   
  
  


       

        
