from threading import Timer
import threading
import time

class temporiza(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.prueba = ""
    
    def hello(self):
        #print("hello, Timer")
        self.prueba = "hello, Timer"
        #return "hello, Timer"
        #return self.prueba

if __name__ == '__main__':
    tm = temporiza()
    #tm.hello()

    while True:
        t = Timer(3.0, tm.hello)
        t.start()
        print(tm.prueba)
        t.join()