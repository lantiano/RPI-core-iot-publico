import time
import threading
import signal
from serialclass import *
from manejo_csv import *

try:
    import queue
except ImportError:
    import queue as queue

class ThreadSerial(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.contado = 0
        self.corrienteFinal = 0
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()

        # ... Other thread setup code here ...

    def run(self):
        print('Thread #%s 1' % self.ident)
        self.serialPort = SerialPort()
        self.serialPort.Open("COM4",9600)
        #self.serialPort.Open('/dev/serial0', 9600)
        escritura = handleCSV()
        

        while not self.shutdown_flag.is_set():
            # ... Job code here ...

            while True:

                lecturaEsclavo = self.serialPort.Read()
                escritura.escribe(lecturaEsclavo)        

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

