import socket
import time
 
bufferSize          = 128

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(10.0)

myList = []

# Send to server using created UDP socket
while True:
    try:
        start = time.time()
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        t = time.time()
        myList.append(t, msgFromServer)
        print(myList)
        print("\n\n Wait for new message")
        end = time.time()
        elapsed = end - start
        print(f'{msgFromServer[0]} {msgFromServer[1]} {elapsed}')
    except socket.timeout:
        print('REQUEST TIMED OUT')
        exit()