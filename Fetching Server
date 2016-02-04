import sys
from threading import Thread
from time import gmtime, strftime, localtime
import socket
import MySQLdb

allClients=[]

class Client(Thread):
    
    def __init__(self,clientSocket):
                Thread.__init__(self)
                self.sockfd = clientSocket #socket client
                self.name = ""
                self.nickName = ""

              
                
    
    def newClientConnect(self): 
     counter_for_main=0
      
     while True:
         
          while True:
              
                try:
                  name= self.sockfd.recv(2048)
                  password=self.sockfd.recv(2048)
                  i=0
                  
                  while (i<login_length):
                                                          
                   if name==rowx[i][0] and password==rowx[i][1]:
                      login_response=("\n1")
                      self.sockfd.send(login_response)
                      counter_for_main=counter_for_main+1
                      
                      if counter_for_main==2:

                          self.main_menu()
                          counter_for_main=0
                      break
                   
                   else:
                     i=i+1
                
                   if i==login_length:
                    login_response="\nError101:Wrong username or password"
                    self.sockfd.send(login_response)
                    i=i+1
                    i=0
                    break

                  break
                                         
                except ValueError:
                       self.sockfd.send("\nError201:That is not a valid Name or Password")
          #              self.sockfd.close()
        
   
        
    def main_menu(self):
        
         while True:
         
          while True:
              
            try:
                car_num=self.sockfd.recv(2048)
                i=0

                number_of_tickets=0;
                array_tickets=[]
                if "logout"==car_num:
                 #Back to log_in Menu
                 self.newClientConnect()

    
               
                else:
         
                  
                  while (i<ticket_length):
                      
                   
                   if car_num==rowy[i][2]:

                      ticket_info="\nvehicule number: %s xbee_module: %s             vehicule_type: %s                      ticket_type: %s                              ticket_date: %s                            ticket_time: %s                        ticket_street: %s                             ticket_fine: %s                                  Date: %s        "%(rowy[i][2],rowy[i][1],rowy[i][3],rowy[i][4],rowy[i][5],rowy[i][6],rowy[i][7],rowy[i][8],strftime("%a, %d %b %Y %H:%M:%S", localtime()))                                          
                      self.sockfd.send(ticket_info)
                     
                      paid_or_unpaid=self.sockfd.recv(2048)

                      if paid_or_unpaid=="unpaid":
                          b=0
                          break
                      elif paid_or_unpaid=="paid":          
                          officer_name=self.sockfd.recv(2048)
                          x.execute("UPDATE ticket_to_be_printed SET payment='paid' WHERE vehicule_n='%s'"%(rowy[i][2]))
                          conn.commit()
                          z.execute("DELETE FROM ticket_to_be_printed WHERE payment='paid'")
                          conn.commit()
                          f.execute("SELECT cash FROM login WHERE name='%s'"%(officer_name))
                          cash1=f.fetchall()
                          cash=cash1[0][0]
                          cash=int(rowy[i][8])+int(cash)
                          cash=str(cash)
                          f.execute("UPDATE login SET cash='%s' WHERE name='%s'"%(cash,officer_name))
                          conn.commit()
                          
                          break
                      else:
                          break
                
                   else:
                    i=i+1
                     
                   if i==ticket_length:
                    login_response="\nError102:No tickets on this car        press paid or unpaid to go back"
                    self.sockfd.send(login_response)
                    anything=self.sockfd.recv(2048)
                    i=i+1
                    i=0
                    break
                
             
                  break
                                         
            except ValueError:
                       self.sockfd.send("\nError202:That is not a valid Car Number")
        
        
     
    def run(self):
                allClients.append(self.sockfd)

                decider=self.sockfd.recv(2048)              
                if decider=="main":
                    self.main_menu()
                else:
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
        serversocket.bind(('',5936))
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
    x=conn.cursor()
    x.execute("SELECT *  FROM login")
    rowx = x.fetchall()
    x.execute("SELECT COUNT(*) FROM login")
    length=x.fetchall()
    login_length=length[0][0]
    z=conn.cursor()
    f=conn.cursor()                                   
    y=conn.cursor()
    y.execute("SELECT *  FROM ticket_to_be_printed")
    rowy = y.fetchall()
    y.execute("SELECT COUNT(*) FROM ticket_to_be_printed")
    length2=y.fetchall()
    ticket_length=length2[0][0]
    
    print ("Connected to the Database")

    
    

    #Server Accepting New Clients:    
    while True:
        (clientSocket, address) = serversocket.accept()
        print 'New connection from ', address
        ct = Client(clientSocket)
        ct.start()

__all__ = ['allClients','Client']

