from flask import Flask,render_template
import socket 
import sys
import time

app = Flask(__name__)


## end of imports ###

### init ###
host = socket.gethostname()
port = 8080
def begin():
    s = socket.socket()
   
#print(" server will start on host : ", host)
    
#print("Port:",port)
    s.bind((host,port))
#print("")
#print(" Server done binding to host and port successfully")
#print("")
#print("Server is waiting for incoming connections")
#print("")
    s.listen(1)
    conn, addr = s.accept()
#print(addr, " Has connected to the server and is now online ...")
#print("")
    while 1:
                message = input(str(">> "))
                message = message.encode()
                conn.send(message)
            #print("message has been sent...")
            #print("")
                incoming_message = conn.recv(1024)
                incoming_message = incoming_message.decode()
            #print(" Client : ", incoming_message)
            #print("")


@app.route("/")
def home():
    return render_template('home.html',host=host,port=port)
