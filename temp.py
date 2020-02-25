import serial
import numpy as np

ser = serial.Serial('COM3', baudrate = 115200, timeout = None)  

if ser.isOpen():
    print ('Open: ' + ser.name)
    data = ser.read_all()    
    len(data)
    print (data)
    for s in data:
        print(s)
        
            
        
data = [ 1, 32, 55, 4, 8, 6, 4, 3, 45, 55, 55 ]
def sendData():
    def endTransmission():
        for i in data:
            if (data = 4):
                print ('End of transmission')
    

sendData()

#from ASCII values to characters
data =[1, 32, 55, 2, 87, 69, 76, 67, 79, 77, 69, 3, 53, 65, 4, 1, 49, 52, 2, 90, 77, 101, 116, 101, 114, 52, 119, 32, 118, 32, 52, 46,
 50, 32, 67, 79, 82, 66, 73, 3, 55, 57, 4]
characters = [chr(ascii) for ascii in data]
''.join(characters)

#from characters to ASCII values
s = '\x01 7\x02WELCOME\x035A\x04\x0114\x02ZMeter4w v 4.2 CORBI\x0379\x04'
ASCII = [ord(c) for c in s]