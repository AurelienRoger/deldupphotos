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

print("Ou souhaitez vous chercher les photos en doublons")
choix_chemin = input(r"")
chemin = choix_chemin
files = glob.glob(chemin, recursive=True)
liste_image = []
liste_doublon = ["(1)", "(2)", "(3)", "(4)", "(5)"]

for f in files:
    if f.endswith(".JPG") or f.endswith(".JPEG"):
        if os.path.isfile(f):
            for i in liste_doublon:
                if i in f:
                    os.remove(f)
                    print(f"{f} SUPPRIMEE")
        else:
            pass
        if "Copie" in f:
            if os.path.isfile(f):
                os.remove(f)
                print(f"{f} SUPPRIMEE")
            else:
                pass

print("Programme terminée")
print("Nettoyage du printemps effectué")