#
# Serial COM Port receive message event handler
# 8/17/2017, Dale Gambill
# When a line of text arrives from the COM port terminated by a \n character, this module will pass the message to
# the function specified by the instantiator of this class.
#
import serial
import sys
import threading


class SerialPort:
    
    def __init__(self):
        
        self.comportName = ""
        self.baud = 0
        self.timeout = None
        self.ReceiveCallback = None
        self.isopen = False
        self.receivedMessage = None
        self.serialport = serial.Serial()


    def __del__(self):
        try:
            if self.serialport.is_open():
                self.serialport.close()
        except:
            print("Destructor error closing COM port: ", sys.exc_info()[0] )

    def RegisterReceiveCallback(self, aReceiveCallback):
        self.ReceiveCallback = aReceiveCallback
        try:
            threading.Thread(target=self.SerialReadlineThread).start()
            #_thread.start_new_thread(self.SerialReadlineThread, ())
        except:
            print("Error starting Read thread: ", sys.exc_info()[0])

    def SerialReadlineThread(self):
        while True:
            try:
                if self.isopen:
                    self.receivedMessage = self.serialport.readline()
                    if self.receivedMessage != "":
                        self.ReceiveCallback(self.receivedMessage)
                        #return self.receivedMessage
            except:
                print("Error reading COM port: ", sys.exc_info()[0])

    def IsOpen(self):
        return self.isopen

    def Open(self,portname, baudrate, timeout = None):
        if not self.isopen:
            # serialPort = 'portname', baudrate, bytesize = 8, parity = 'N', stopbits = 1, timeout = None, xonxoff = 0, rtscts = 0)
            self.serialport.port = portname
            self.serialport.baudrate = baudrate
            try:
                self.serialport.open()
                self.isopen = True
                #print("Puerto Abierto")
            except:
                print("Error opening COM port: ", sys.exc_info()[0])
            

    def Close(self):
        if self.isopen:
            try:
                self.serialport.close()
                self.isopen = False
            except:
                print("Close error closing COM port: ", sys.exc_info()[0])

    def Send(self, newmessage):
        if self.isopen:
            try:
                # Ensure that the end of the message has both \r and \n, not just one or the other
                #newmessage = message.strip()
                #newmessage += '\r\n'
                self.serialport.write(newmessage.encode('utf-8'))
            except:
                print("Error sending message: ", sys.exc_info()[0] )
            else:
                return True
        else:
            return False

        # serial data callback function
    def OnReceiveSerialData(self, message):
        try:
            str_message = message.decode("utf-8")
            #textbox.insert('1.0', str_message)
            if str_message is not None:
                #print(str_message)
                return str_message
        except Exception as e:
            raise e

    def Read(self):
        #while True:
        try:
            if self.isopen:
                self.receivedMessage = self.serialport.readline()
                if self.receivedMessage is not None:
                    #print(str_message)
                    self.receivedMessage = self.receivedMessage.decode("utf-8")
                    #print(self.receivedMessage)
                    return self.receivedMessage
                    
                # if self.receivedMessage != "":
                #     self.receivedMessage = receivedMessage.decode("utf-8")
                #     return str_message
        except:
            print("Error reading COM port: ", sys.exc_info()[0])
    
    def handleMessage(self, info_incoming):

        if info_incoming is not None:
            endOfLineIndex = info_incoming.index("~")
            #print(endOfLineIndex)                                               
        
            if (endOfLineIndex > 0):
                #print(info_incoming[0:endOfLineIndex])
                #print("Data Received = " + info_incoming)
                dataLength = len(info_incoming)
              
                if info_incoming[0] == '#':

                    sensor0 = info_incoming[1: 5]                     #get sensor value from string between indices 1-5
                    sensor1 = info_incoming[6: 10]                    #same again...
                    sensor2 = info_incoming[11: 15]
                    sensor3 = info_incoming[16: 20]

                    print("Sensor 0 Voltage = " + sensor0 + "V")             #update the textviews with sensor values
                    print("Sensor 1 Voltage = " + sensor1 + "V")
                    print("Sensor 2 Voltage = " + sensor2 + "V")
                    print("Sensor 3 Voltage = " + sensor3 + "V")
                
                info_incoming =""                         #clear all string data           
            