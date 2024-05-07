import os

ruta_fitxer: str = input("Intridueix la ruta de l'arxiu que vols canviar el nom")

ArxiuSEnseEtensio = os.path.splitext(ruta_fitxer)

os.rename(ruta_fitxer,ArxiuSEnseEtensio[0])

directori_actual = os.getcwd()

print(directori_actual)

directori = os.listdir(directori_actual)
print(directori)



