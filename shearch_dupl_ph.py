""" Programme de Suppression de Photos en Doublons
    Créé par : Aurélien Roger
    Le 29/11/2019
    V1.0.1
    Version de Python : 3.8.0

    (\_/)   (\_/)
    (x_0)   (0_x)
    C(")(")(")(")Ͻ
"""

import glob
import os

print("Ou souhaitez vous chercher les photos en doublons") # where are shearch duplicate photos ?  
choix_chemin = input(r"") # input path of the folder where do you want shearch duplicate. The "r" after quote is for path of windows
chemin = choix_chemin
files = glob.glob(chemin, recursive=True)
liste_image = []
liste_doublon = ["(1)", "(2)", "(3)", "(4)", "(5)"] # this list is for content in name.

for f in files:
    if f.endswith(".JPG") or f.endswith(".JPEG"): # Shearch and selected just .jpg or Jpeg in the folder
        if os.path.isfile(f):
            for i in liste_doublon:
                if i in f:
                    os.remove(f)
                    print(f"{f} SUPPRIMEE")
        else:
            pass
        if "Copie" in f: #if there is no (1) or (2) etc...  shearch if "Copie" in name
            if os.path.isfile(f):
                os.remove(f)
                print(f"{f} SUPPRIMEE")
            else:
                pass

print("Programme terminée")
print("Nettoyage du printemps effectué")