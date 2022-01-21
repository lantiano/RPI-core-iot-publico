import pandas
import csv
import time
import os
from itertools import islice
from datetime import datetime, timedelta

class handleCSV(object):
    """docstring for handleCVS"""

    def __init__(self):

        self.Year = time.strftime('%Y')
        self.mes = time.strftime('%m')
        self.dia = time.strftime('%d/%m/%Y')
        self.diacsv = time.strftime('%d-%m-%Y')
        self.diaActual = time.strftime('%d-%m-%Y')
        self.mesPasado = time.strftime('%m')
        self.mesActual = time.strftime('%m')
        self.fecha = time.strftime('%d/%m/%Y')
        self.yearActualCarpeta = time.strftime('%Y')
        self.mesActualCarpeta = self.mesActualfuntion(self.mes)
        self.rutaYear = self.yearActualCarpeta + "/"
        self.rutaMes = self.mesActualCarpeta + "/"
        self.ruta = os.path.join(self.rutaYear, self.rutaMes)
        self.directorioActual = os.getcwdb()
        self.NuevoDirectorio()

    def mesActualfuntion(self, m):

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

    def escribe(self, datos):

        txt = datos
        lecExt = txt.split("+")
        mil = int(round(time.time() * 1000))
        time2 = time.strftime('%H:%M:%S')
        x = time.strptime(time2.split(',')[0], '%H:%M:%S')
        segundos = timedelta(hours=x.tm_hour, minutes=x.tm_min,
                             seconds=x.tm_sec).total_seconds()

        

        if len(lecExt) == 8:
            fields = [str(self.dia), str(int(segundos)), str(time2), str(lecExt[0]),
                        str(lecExt[1]), str(lecExt[2]), str(lecExt[3]), str(lecExt[4]),
                        str(lecExt[5]), str(lecExt[6]), str(lecExt[7]), str(mil)]
    
        with open(self.ruta + self.diacsv +'.csv', 'a+', newline='') as f:

            print(fields)
            writer = csv.writer(f)
            writer.writerow(fields)
        
        self.diaActual = self.diacsv
        self.mesPasado = self.mes

    def NuevoDirectorio(self):

        pathActual = str(self.directorioActual, 'utf-8')
        newpathYear = self.yearActualCarpeta
        newpathMonth = self.rutaYear + self.rutaMes
    
        if not os.path.exists(newpathYear):
            os.makedirs(newpathYear)
        if not os.path.exists(newpathMonth):
            os.makedirs(newpathMonth)
            self.writing_csv()
            

    def lecturas(self):

        lista = []
        with open(self.ruta + self.diacsv +'.csv') as csvfile:
            row_count = len(list(csvfile))
            print(row_count)
            #datos = pd.read_csv(self.ruta + self.diacsv +'.csv', nrows=int(row_count))
            datos = pandas.read_csv(
                self.ruta + self.diacsv +'.csv', nrows=int(row_count))
            # print(datos)
            for index, row in islice(datos.iterrows(), int(row_count)-301, int(row_count)):
                z = row.dia, row.seg, row.hora, row.current, row.volta,  row.pot, row.mil
                lista.append(z)
                print(lista)
            return lista

    def read_cvsfile(self):

        with open('employee_data.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f"Column names are {', '.join(row)}")
                    print("Column names are {', '.join(row)}")
                    line_count += 1
                else:
                    #print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.")
                    print(
                        "\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.")
                    line_count += 1
            #print(f"Processed {line_count} lines")
            print("Processed {line_count} lines")

    def pandas_reads_csv(self):

        df = pandas.read_csv('hrdata.csv')
        df_2 = pandas.read_csv('hrdata.csv', index_col='Name')
        df_3 = pandas.read_csv(
            'hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
        df_4 = pandas.read_csv(
            'hrdata.csv',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
        print(df_4)

    def writing_csv(self):
    
        with open(self.ruta + self.diacsv +'.csv') as csvfile:
            employee_writer = csv.writer(csvfile)
            employee_writer.writerow(['dia', 'seg', 'hora', 'P1', 'P2', 'P3', 'P4', 'E1', 'E2', 'E3', 'E4', 'mil'])

    def pandas_to_csv(self):
        df = pandas.read_csv(
            'hrdata.csv',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
        df.to_csv('hrdata_modified.csv')

        df_modified = pandas.read_csv(
            'hrdata_modified.csv',
            index_col='Employee',
            parse_dates=['Hired'],)
        print(df_modified)

    def change_delimiter(self):
        with open('employee_data2.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=":")
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f"Columns are {', '.join(row)}")
                    print("Columns are {', '.join(row)}")
                    line_count += 1
                else:
                    #print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]} and lives in {row[3]}.")
                    print(
                        "\t{row[0]} works in the {row[1]} department, and was born in {row[2]} and lives in {row[3]}.")
                    line_count += 1
            #print(f"Processed {line_count} lines")
            print("Processed {line_count} lines")

    def csv_dictreader(self):
        with open('employee_data.csv') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            line_count = 0
            for row in csv_reader:
                print(row)
                if line_count == 0:
                    #print(f'Columns are {", ".join(row)}')
                    print('Columns are {", ".join(row)}')
                    line_count += 1
                else:
                    #print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.")
                    print(
                        "\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.")
                    line_count += 1
            #print(f"Processed {line_count} lines")
            print("Processed {line_count} lines")

    def csv_dictwriter(self):
        with open('employee_file1.csv', 'w', newline='') as csvfile:
            fieldnames = ['emp_name', 'dept', 'birth_month']
            employee_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            employee_writer.writeheader()
            employee_writer.writerow(
                {'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
            employee_writer.writerow(
                {'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

    def using_quotechar(self):
        with open('employee_data1.csv') as csvfile:
            csv_reader = csv.reader(
                csvfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    #print(f"Columns are {', '.join(row)}")
                    print("Columns are {', '.join(row)}")
                    line_count += 1
                else:
                    #print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]} and lives in {row[3]}.")
                    print(
                        "\t{row[0]} works in the {row[1]} department, and was born in {row[2]} and lives in {row[3]}.")
                    line_count += 1
            #print(f"Processed {line_count} lines")
            print("Processed {line_count} lines")


# if __name__ == "__main__":
# print('Ejecutando como programa principal')


#prueba = handleCSV()

# test1 = prueba.read_cvsfile()
# print(test1)
# test2 = prueba.pandas_reads_csv()
# print(test2)
#test3 = prueba.writing_csv()
#print(test3)
# test4 = prueba.pandas_to_csv()
# print(test4)
# test5 = prueba.change_delimiter()
# print(test5)
# test6 = prueba.csv_dictreader()
# print(test6)
# test7 = prueba.csv_dictwriter()
# print(test7)
# test8 = prueba.using_quotechar()
# print(test8)
#test9 = prueba.lecturas()
# print(test9)
#test14 = prueba.nueva_carpeta()
#test15 = prueba.writing_csv()
#test10 = prueba.writing_csv('27-10-2020')
# print(test10)
#test11 = prueba.nueva_carpeta(2020, 10)
#test13 = prueba.writing_csv(self.diacsv)
#texto = 'segundos+10+temp1+P2+P3+1300+12345'
#test12 = prueba.escribe(texto)
