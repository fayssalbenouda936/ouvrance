#!/usr/bin/env python3
"""Sonde les mp4 produits sans ffprobe : lit les atomes MP4 (mvhd, tkhd, stsd).

Renvoie duree reelle, dimensions de la piste video, presence d'une piste audio
et poids. Sert a verifier la resolution facturee et a dimensionner R2.
"""
import os, glob, struct, sys

RACINE = "/home/fayssal/projetCadeau"
CIBLES = [
    "apps/gifts/_templates/animation-cadeau/essais-decors/films/*.mp4",
    "apps/gifts/_templates/animation-cadeau/public/films/*.mp4",
    "apps/gifts/_templates/combat-3d/cinematique/essais-2.5/*.mp4",
    "apps/gifts/_templates/combat-3d/films/*.mp4",
    "apps/gifts/_templates/combat-3d/films/precedents-18-plans/*.mp4",
    "apps/gifts/_templates/combat-3d/rushes/*.mp4",
    "apps/gifts/illies-crevette/rushes/*.mp4",
]


def atomes(buf, debut, fin):
    """Itere (type, debut_contenu, fin_contenu) sur les atomes d'un intervalle."""
    i = debut
    while i + 8 <= fin:
        taille = struct.unpack(">I", buf[i:i + 4])[0]
        typ = buf[i + 4:i + 8]
        entete = 8
        if taille == 1:
            taille = struct.unpack(">Q", buf[i + 8:i + 16])[0]
            entete = 16
        elif taille == 0:
            taille = fin - i
        if taille < entete:
            return
        yield typ, i + entete, min(i + taille, fin)
        i += taille


CONTENEURS = {b"moov", b"trak", b"mdia", b"minf", b"stbl", b"edts"}


def parcours(buf, debut, fin, trouve):
    for typ, d, f in atomes(buf, debut, fin):
        trouve(typ, d, f)
        if typ in CONTENEURS:
            parcours(buf, d, f, trouve)


def sonde(chemin):
    taille = os.path.getsize(chemin)
    with open(chemin, "rb") as fh:
        buf = fh.read()
    res = {"octets": taille, "duree": 0.0, "w": None, "h": None, "audio": False}

    def visite(typ, d, f):
        if typ == b"mvhd":
            ver = buf[d]
            if ver == 1:
                echelle = struct.unpack(">I", buf[d + 20:d + 24])[0]
                duree = struct.unpack(">Q", buf[d + 24:d + 32])[0]
            else:
                echelle = struct.unpack(">I", buf[d + 12:d + 16])[0]
                duree = struct.unpack(">I", buf[d + 16:d + 20])[0]
            if echelle:
                res["duree"] = duree / echelle
        elif typ == b"tkhd":
            ver = buf[d]
            # tkhd : entete(4) + [v1: 8+8+4+4+8 | v0: 4+4+4+4+4] + 16 + matrice(36)
            base = d + 4 + (32 if ver == 1 else 20) + 16 + 36
            larg = struct.unpack(">I", buf[base:base + 4])[0] / 65536.0
            haut = struct.unpack(">I", buf[base + 4:base + 8])[0] / 65536.0
            if larg and haut:
                res["w"], res["h"] = int(round(larg)), int(round(haut))
        elif typ == b"hdlr":
            if buf[d + 8:d + 12] == b"soun":
                res["audio"] = True

    parcours(buf, 0, len(buf), visite)
    return res


motifs = sys.argv[1:] or CIBLES
for motif in motifs:
    fichiers = sorted(glob.glob(os.path.join(RACINE, motif)))
    if not fichiers:
        continue
    print()
    print("### " + motif)
    tot_o = tot_d = 0
    for p in fichiers:
        i = sonde(p)
        tot_o += i["octets"]
        tot_d += i["duree"]
        print("   %-34s %4sx%-4s %6.2f s %7.2f Mo audio=%s"
              % (os.path.basename(p), i["w"], i["h"], i["duree"],
                 i["octets"] / 1e6, "oui" if i["audio"] else "non"))
    print("   -> %d fichiers | %.1f s cumulees | %.1f Mo | debit moyen %.2f Mo/s"
          % (len(fichiers), tot_d, tot_o / 1e6, (tot_o / 1e6 / tot_d) if tot_d else 0))
