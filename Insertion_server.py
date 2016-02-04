import sys
from threading import Thread
from time import gmtime, strftime, localtime
import socket
import MySQLdb
import shlex
import random

allClients=[]

class Client(Thread):
    
    def __init__(self,clientSocket):
                Thread.__init__(self)
                self.sockfd = clientSocket #socket client
                self.name = ""
                self.nickName = ""

              
                
    
    def newClientConnect(self): 
     
      
     while True:
         
          while True:

                try:
                    
                   allClients.append(self.sockfd)
                   number= self.sockfd.recv(2048)
                   num=random.random()*100
                   num=int(round(num,0))
                   info=shlex.split(number)
                   ticket_date=strftime("%d %b %Y", localtime())
                   ticket_time=strftime("%H:%M:%S", localtime())
                   vehicle_num=info[0]
                   vehicle_type=info[1]
                   xbee_num=info[2]
                   ticket_type=info[3]
                   ticket_street=info[4]
                   ticket_fine=info[5]
                   payment=info[6]

                   y.execute("INSERT INTO ticket_to_be_printed(number,xbee_n,vehicule_n,vehicule_type,ticket_type,ticket_date,ticket_time,ticket_street,ticket_fine,payment) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(num,xbee_num,vehicle_num,vehicle_type,ticket_type,ticket_date,ticket_time,ticket_street,ticket_fine,payment))
                   conn.commit()
                   
                   print "done"
                   
        
                except ValueError:
                       self.sockfd.send("\nError201:That is not a valid Name or Password")
          #              self.sockfd.close()
        
   
        
     
    def run(self):
                allClients.append(self.sockfd)
                self.newClientConnect()
                while True:
                        buff = self.sockfd.recv(2048)
                        if buff.strip() == 'quit':
                             self.sockfd.close()
                             break # Exit when break
                        else:
                            self.sendAll(buff)

    
#Main
if __name__ == "__main__":
    #Server Connection to socket:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    try:
        serversocket.bind(('',5943))
    except ValueError,e:
        print e
    serversocket.listen(5)
    print ("Server Started")
    print ("Connecting to the Database...")    

    #Server Connection to MySQL:
    conn = MySQLdb.connect (host = "localhost",
                           user = "root",
                           passwd = "",
                           db = "traffic_monitoring")
    
    y=conn.cursor()    
    print ("Connected to the Database")

    
    

    #Server Accepting New Clients:    
    while True:
        (clientSocket, address) = serversocket.accept()
        print 'New connection from ', address
        ct = Client(clientSocket)
        ct.start()

__all__ = ['allClients','Client']


