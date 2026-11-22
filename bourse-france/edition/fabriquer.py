"""Regénérer d’un seul geste les livrables client et les ressources vendeur."""
from zipfile import ZipFile, ZIP_DEFLATED
import atelier
import livret
import panorama
import tableur
from commun import GUIDE, PANORAMA, DOCX, XLSX, KIT, VENTE


def archive(chemin, fichiers):
    with ZipFile(chemin, 'w', compression=ZIP_DEFLATED, compresslevel=9) as z:
        for p in fichiers:z.write(p, arcname=p.name)

if __name__ == '__main__':
    livret.make();panorama.make();atelier.make();tableur.make()
    archive(KIT,[GUIDE,PANORAMA,DOCX,XLSX])
    archive(VENTE/'Ressources-Chariow.zip',[VENTE/'Fiche-Chariow.md',VENTE/'Visuel-Chariow.png',VENTE/'Extrait-gratuit.pdf'])
