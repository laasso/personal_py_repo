import os

#1.1 Eliminar Carpeta
#   2.1 Encontrar Carpet
#       2.2 Pedir Carpeta
#       2.2.2 Comprobar que ruta existe
#   3.1 Eliminar Carpeta
#       3.1.2 Eliminar Contenido
#       3.1.3 Comprobar Si dentro de la carpeta hay otra carpeta
#       3.1.4liminar Carpeta

class EliminarCarpeta():
    def Start(self):
        folder: str = self.RutaCarpeta()
    
    def RutaCarpeta(self):
        folder: str = input("Ruta: ")
        return folder
    
    def CheckRuta(self):
        folder:str = self.RutaCarpeta()
        if os.path.exists(folder) == True:
            return True
        else: 
            return False
        
    