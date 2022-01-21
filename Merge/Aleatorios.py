import random
from threading import Timer


class Simulacion_Datos(object):

    def __init__(self):

        self.c =""

    def datosRandom(self):
        
        r1 = str(random.randint(0, 10))
        r2 = str(random.randint(8, 18))
        r3 = str(random.randint(7, 15))
        r4 = str(random.randint(4, 10))
        r5 = str(random.randint(9, 11))
        r6 = str(random.randint(10, 16))
        r7 = str(random.randint(7, 19))
        r8 = str(random.randint(4, 18))
        self.c = r1 + "+" + r2 + "+" + r3 + "+" + r4 + "+" + r5 + "+" + r6 + "+" + r7 + "+" + r8
    
        return self.c

    def Contador(self):
        
        datos = self.datosRandom()
        t = Timer(1, datos)
        t.start()
        # wait for time completion
        t.join()


#prueba = Simulacion_Datos()

#test1 = prueba.datosRandom()
#print(test1)


