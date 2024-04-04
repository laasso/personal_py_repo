import os

ruta_fitxer: str = input("Intridueix la ruta de l'arxiu que vols canviar el nom")

ArxiuSEnseEtensio = os.path.splitext(ruta_fitxer)

os.rename(ruta_fitxer,ArxiuSEnseEtensio[0])

directori = os.listdir("/home/lasso/github/personal_py_repo/UF3/teoria/CanviNom")
print(directori)



