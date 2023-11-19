# -*- coding: utf-8 -*-

import textract
import os

def IDSniffer(fichier):
    try:
        # Convertion fichier en txt (voir extensions de fichiers supportés)
        text = str(textract.process(fichier))
        # Nettoyage des non-breaking spaces
        text = text.replace("\\xc2\\xa0", " ")
        # Recherche des termes dans le tableau mdp
        for m in mdp:
            if m.upper() in text or m.capitalize() in text or m in text:
                global nb
                nb += 1
                return "- ID found in file : "+fichier 
        return 1
    except Exception as e:
        return 1

if __name__ == "__main__":
    fichier = open("results.txt", "w")
    extensions = ["csv", "docx", "doc", "gif", "jpg", "json", "html", "msg", "odt", "pdf", "png", "pptx", "txt", "xlsx", "xls"]
    mdp = ["mdp:", "mdp :", "mdp=", "mdp =", "mdp est",
        "mot de passe:", "mot de passe :", "mot de passe=", "mot de passe =", "mot de passe est",
        "pwd:", "pwd :", "pwd=", "pwd =", "pwd is", 
        "password:", "password :", "password=", "password =", "password is",
        "identifiant:", "identifiant :", "identifiant=", "identifiant =", "identifiant est",
        "login:", "login :", "login=", "login =", "login is",
        "identifiants:", "identifiants :", "identifiants=", "identifiants =", "identifiants sont",  
        "credentials:", "credentials :", "credentials=", "credentials =", "credentials are",
        "creds:", "creds :", "creds=", "creds =", "creds are"]
    racine = os.getcwd()
    nb = 0
    # Boucle pour tous les dossiers du repertoire
    for root, dirs, files in os.walk(racine):
        for file in files:
            try:
                # Traitement des fichiers avec la bonne extension
                ext = file.split('.')[-1]
                if ext in extensions:
                    result = IDSniffer(os.path.abspath(root+"\\"+file))
                    if (result != 1):
                        fichier.write(result+"\n")
            except Exception as e:
                print("Last open file : "+file)
                print("Exception returned : "+e)  
    print("Successfully finished !")
    print(nb, "files found with potential ids")
    fichier.close()

    # Ajout du nombre de fichiers trouves
    f = open("results.txt", "r")
    total = str(nb) + " files found with potential ids :\n\n" + f.read()
    f.close()
    newFichier = open("results.txt", "w")
    newFichier.write(total)
    newFichier.close()
               

# Notes : si "antiword CheminVersUnFichier" (commande pour fichiers .doc) donne "failed with exit code 127" il faut ajouter :
# C:\Program Files\Git\mingw64\bin au PATH Windows car antiword a besoin d'extracteurs qui utilisent bash