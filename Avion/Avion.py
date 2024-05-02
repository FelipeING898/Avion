from Silla import Silla

class Avion:
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas=[]
        self.sillasEconomicas=[]
        #false es clase ejecutiva y true clase Economica
        self.AsignacionSillasEjectuvias()
        self.AsignacionSillasEconomicas()
        
    def AsignacionSillasEjectuvias(self):

        for i in range(self.SILLAS_EJEUTIVAS):
            if ((i+1)%2)==0:
                self.sillaEjecutivas.append(Silla((i+1), False, 'pasillo'))
            else:
                self.sillaEjecutivas.append(Silla((i+1), False, 'ventana'))