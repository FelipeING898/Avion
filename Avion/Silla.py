class Silla: 
    CLASE = {
        'eje':'Ejecutiva',
        'eco':'Economica'    
    }
    UBICACION = {
        'ventana':'Venmtana',
        'centro':'Centro',
        'pasillo':'Pasillo',
    }
    #ARREGLOS, CONTENEDORES CON [] Y OBJETOS, JSON CON {}:
    
    def __init__(self, pNumero, pClase, pUbicacion):
        # self.__numero = pNumero
    # #Operador ternario 1 - pClase es booleano(true o false)
        # self.__clase == (self.CLASE['eje'], self.CLASE.['eco'])[pClase]
        # if pUbicacion == 'ventana':
        #     self.__ubicacion = self.UBICACION['ventana']
        # elif pUbicacion == 'centro':
        #     self.__ubicacion = self.UBICACION['centro']
        # elif pUbicacion == 'pasillo':
        #     self.__ubicacion = self.UBICACION['pasillo']
        # else:
        #     self.__ubicacion = None

            #self.__pasajero = None
        #Operador ternario 2 - pClase es booleano(true o false)
        #self.__clase = (self.CLASE.eco if pClase == 'economica' else self.CLASE.eje)
        self.__pasajero = None
        self.setNumero(pNumero)
        self.setNumero(pNumero)
        self.setClase(pClase)
        self.setUbicacion(pUbicacion)

    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero

    def desasignarPasjaero(self):
        self.__numero = None
        self.__pasajero = None
    
    def sillaAsignada(self):

        # return(False, True)[self.__numero is None]
        return False if self.__numero == None else True
    
    def getNumero(self):
        return self.__numero
    
    def setNumero(self, pNumero):
        self.__numero = pNumero
    
    def getClase(self):
        return self.__clase
    
    def setClase(self, pClase):
        self.__clase = (self.CLASE['eje'], self.CLASE['eco'])[pClase]
    
    def getUbicacion(self):
        return self.__ubicacion

    def setUbicacion(self, pUbiacion):
        if pUbicacion == 'ventana':
            self.__ubicacion = self.UBICACION['ventana']
        elif pUbiacion == 'centro':
            self.__ubicacion = self.UBICACION['centro']
        elif pUbiacion == 'pasillo':
            self.__ubicacion = self.UBICACION['pasillo']
        else:
            self.__ubicacion = None 
    
    
    def getPasajero(self):
        return self.__pasajero