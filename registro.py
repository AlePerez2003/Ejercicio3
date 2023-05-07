class Registro:
    __temperatura: float
    __humedad: float
    __presion: float   
    
    def __init__(self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    
    def __str__(self):
        return f"{self.__temperatura, self.__humedad, self.__presion}"
    
    def get_temp(self):
        return self.__temperatura
    
    def get_hum(self):
        return self.__humedad
    
    def get_presion(self):
        return self.__presion