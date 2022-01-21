import time
import threading
import signal
import RPi.GPIO as GPIO

#Sending the data thorugh UART 
#UART PINOUT
#Rx -> GPIO15
#Tx -> GPIO14
#StatusInternetConn -> GPIO

class ThreadStatus(threading.Thread):
 
    def __init__(self, seg_queue):  
        threading.Thread.__init__(self)
        self.seg_queue = seg_queue
        
        # the input buttons
        up = 7
        down = 8


        #Setting up the GPIO Pins
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        #Setting up the Button Inputs
        GPIO.setup(up, GPIO.IN)
        GPIO.setup(down, GPIO.IN)
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()
 
        # ... Other thread setup code here ...
 
    def run(self):
        print('Thread #%s 2' % self.ident)
        self.serialPort = SerialPort()
        self.serialPort.Open("/dev/ttyAMA0",115200)
        tiempo = Temperizadores()
        escritura = handleCSV()
        datos = Database()
        query = "INSERT INTO energia (`dia`,`Segundo`, `hora`,`corriente`, `voltaje`, `potencia`,`milisegundo`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        while not self.shutdown_flag.is_set():
            # ... Job code here ...
            
            
            # ... Clean shutdown code here ...
        print('Thread #%s stopped' % self.ident)
 
 
class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    pass
 
 
def service_shutdown(signum, frame):
    print('Caught signal %d' % signum)
    raise ServiceExit
 
 