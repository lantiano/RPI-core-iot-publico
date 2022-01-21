import os
import sys
from datetime import datetime, timedelta
import time

directorioActual = os.getcwdb()
Year = time.strftime('%Y')
mes = time.strftime('%m')

def mesActualfuntion(m):

        switcher = {
            "01": 'Enero',
            "02": 'Febrero',
            "03": 'Marzo',
            "04": 'Abril',
            "05": 'Mayo',
            "06": 'Junio',
            "07": 'Julio',
            "08": 'Agosto',
            "09": 'Septiembre',
            "10": 'Octubre',
            "11": 'Noviembre',
            "12": 'Diciembre', }
        return switcher.get(m, "Invalid Month of Year")

mesActualCarpeta = mesActualfuntion(mes)
path = os.path.join(Year, mesActualCarpeta)
#path =  Year +'/'+ mesActualCarpeta
os.makedirs(path)