import time
import threading
import signal
from manejo_csv import *
from Aleatorios import *
from testtimer import *

try:
    import queue
except ImportError:
    import queue as queue

class ThreadRandom(threading.Thread):

    def __init__(self):
        
        threading.Thread.__init__(self)
    
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()

        # ... Other thread setup code here ...
       
    def run(self):
        print('Thread #%s 1' % self.ident)

        ValoresSimulados = Simulacion_Datos()
        escritura = handleCSV()
    
        while not self.shutdown_flag.is_set():
            # ... Job code here ...
            
            while True:

                t = Timer(1, ValoresSimulados.datosRandom)
                t.start()
                t.join()
                escritura.escribe(ValoresSimulados.c)

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

