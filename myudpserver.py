import socket

"""Config Port destino"""
UDP_IP = "192.168.24.100"
UDP_PORT = 9600

""""Config port local"""
UDP_IP_LOCAL = "192.168.24.236"
UDP_PORT_LOCAL = 4023


ICF=B"\x80"
RESERVED=B"\x00"
GATEWAY=B"\x02"
LOCALNETW=B"\x00"
DESTINATIONNODE=B"\x64"
DESTINATION_UNIDAD=B"\x00"
SOURCE_NET=B"\x00"
SORCE_NODE=B"\xec"
SOURCE_UNIDADAREA=B"\x00"
SERVICE_ID=B"\x00"
FINS_HEADER=ICF+RESERVED+GATEWAY+LOCALNETW+DESTINATIONNODE+DESTINATION_UNIDAD+SOURCE_NET+SORCE_NODE+SOURCE_UNIDADAREA+SERVICE_ID

COMMAND_CODE=B"\x01\x01"

MEMORY_DM=B"\x98"
Begginer_Adress=B"\x00\x01"
Begginer_Adress_Bites=B"\x00"
Number_Items=B"\x00\xb4"

COMMAND_DATA=MEMORY_DM+Begginer_Adress+Begginer_Adress_Bites+Number_Items

MESSAGE = FINS_HEADER+COMMAND_CODE+COMMAND_DATA



def SendData():
    try:
        s = socket.socket(socket.AF_INET,
                            socket.SOCK_DGRAM)  
        s.bind((UDP_IP_LOCAL, UDP_PORT_LOCAL))
        s.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    except:
        print("Sending Error!!!\n")

    return s

def ReceiveData(sock):
    print("Receiving data: \n")

    while True:
        data, addr = sock.recvfrom(416)      # buffer size is 4096 bytes
        print ("received message:", data)


if __name__ == "__main__":    
    s = SendData()
    ReceiveData(s)
    print("Termino.!")