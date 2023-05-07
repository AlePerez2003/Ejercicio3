from registro import Registro
import csv

class Meteorología:

    def __init__(self):
        registro_nulo = Registro(0, 0, 0)
        self.__datos_mes = [[registro_nulo for i in range(24)]for j in range(30)]

    def cargar_tabla(self, un_registro, hora, dia):
        self.__datos_mes[hora-1][dia-1] = un_registro
                
    def leer_archivo(self):
        cabecera = True
        with open("datos_meteorologicos.csv","r") as file:
            reader=csv.reader(file, delimiter=",")
            for fila in reader:
                if cabecera:
                    cabecera = False
                else:                 
                    temperatura = float(fila[2])
                    humedad = float(fila[3])
                    presion = float(fila[4])
                    registro = Registro(temperatura, humedad, presion)
                    self.cargar_tabla(registro, int(fila[0]), int(fila[1]))
        
    def min_temp(self):
        
        hora_min = 0          
        dia_min = 0
        min = self.__datos_mes[0][0].get_temp()
            
        for hora in range(len(self.__datos_mes)):
                
            for dia in range(len(self.__datos_mes[hora])):
                            
                if self.__datos_mes[hora][dia].get_temp() < min:
                                
                    min = self.__datos_mes[hora][dia].get_temp()
                    hora_min = hora
                    dia_min = dia
                            

        return 'Se registró la Menor Temperatura: Dia {} Hora {}:00'.format(dia_min, hora_min)
    
    def max_temp(self):
        
        hora = 0          
        dia = 0
            
        max = self.__datos_mes[0][0].get_temp()
            
        for i in range(len(self.__datos_mes)):
                
            for j in range(len(self.__datos_mes[i])):
                    
                if isinstance(self.__datos_mes[i][j], Registro):
                    
                    if self.__datos_mes[i][j].get_temp() > max:
                        
                        hora = i
                        dia = j                    
                        max = self.__datos_mes[i][j].get_temp()
            
        return 'Se registró la Mayor Temperatura: Dia {} Hora {}:00'.format(dia, hora)
    
    def min_hum(self):
        
        hora = 0          
        dia = 0
                 
        min = self.__datos_mes[0][0].get_hum()
            
        for i in range (len(self.__datos_mes)):
                
            for j in range (len(self.__datos_mes[i])):
                    
                if (self.__datos_mes[i][j].get_hum() < min):
                        
                    hora = i
                    dia = j                    
                    min = self.__datos_mes[i][j].get_hum()
                        
            return 'Se registró la Menor Humedad: Dia {} Hora {}:00'.format(dia, hora)
    
    def max_hum(self):
        
        hora = 0          
        dia = 0
        max = self.__datos_mes[0][0].get_hum()
            
        for i in range (len(self.__datos_mes)):
                
            for j in range (len(self.__datos_mes[i])):
                    
                if (self.__datos_mes[i][j].get_hum() > max):
                        
                    max = self.__datos_mes[i][j].get_hum()
                    hora = i
                    dia = j

            return 'Se registró la Mayor Humedad: Dia {} Hora {}'.format(dia, hora)
    
    def min_presion(self):
        
        hora = 0          
        dia = 0
        min = self.__datos_mes[0][0].get_presion()
            
        for i in range (len(self.__datos_mes)):
                
            for j in range (len(self.__datos_mes[i])):
                    
                if (self.__datos_mes[i][j].get_presion() < min):
                        
                    min = self.__datos_mes[i][j].get_presion()
                    hora = i
                    dia = j

            return 'Se registró la Menor Presión: Dia {} Hora {}'.format(dia, hora)
    
    def max_presion(self):

        max = self.__datos_mes[0][0].get_presion()
        hora = 0          
        dia = 0      
        for i in range (len(self.__datos_mes)):
            
            for j in range (len(self.__datos_mes[i])):
                
                if (self.__datos_mes[i][j].get_presion() > max):

                    max = self.__datos_mes[i][j].get_presion()
                    hora = i
                    dia = j
        
        return 'Se registró la Mayor Presión: Dia {} Hora {}'.format(dia, hora)
    
    def temp_prom(self):
        acum = 0
        
        for hora in range(len(self.__datos_mes)):
            
            for dia in range(len(self.__datos_mes[hora])):
                
                acum += self.__datos_mes[hora][dia].get_temp()
            print('En la hora {} la temperatura promedio es de {}°'.format(hora, acum/31))
            acum=0
            
    def mostrar_dia(self, dia):
        print('Hora - Temperatura - Humedad - Presion')
        for hora in range(24):
            print('{}'.format(hora+1), self.__datos_mes[hora][dia])
            
    def opcion1(self):
        print(self.min_temp())
        print(self.max_temp())
        print(self.min_hum())
        print(self.max_hum())
        print(self.min_presion())
        print(self.max_presion())
        
    def opcion2(self):
        self.temp_prom()
        
    def opcion3(self):
        dia = int(input('Ingrese el dia a mostrar datos'))
        self.mostrar_dia(dia)
    
    def mostrar_menu(self):
        print('1: Mostrar para el mayor y menor valor de cada variable el día y la hora')
        print('2: Indicar temperatura promedio mensual de cada hora')
        print('3: Mostrar el registro de cada hora de un Día específico')
        print('0: finalizar operación')
        
    def menu(self):
        self.mostrar_menu()
        cod = int(input('Ingrese el codigo'))
        while cod != 0:
            if cod == 1:
                self.opcion1()
            elif cod == 2:
                self.opcion2()
            elif cod == 3:
                self.opcion3()
            else:
                print('Codigo incorrecto')
            self.mostrar_menu()
            cod = int(input('Ingrese el codigo'))