#socket
import socket
#local
from message import message 

"""Config Port destino"""
UDP_IP="192.168.24.100"
UDP_PORT = 9600
""""Config port local"""
UDP_IP_LOCAL = "192.168.24.236"
UDP_PORT_LOCAL = 4023
#message
MESSAGE = B"hola te saludo desde python tu mensaje fue: "

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((UDP_IP_LOCAL,UDP_PORT_LOCAL))

def main():
 while True:
     data, adress =sock.recvfrom(1024)
     print("received message: ",data)
    

if __name__=="__main__":
    print(message.welcome)
    main()


