#!/usr/bin/env python3
"""Assemble les captures en planches lisibles. Recadre sur le sujet : à 6 m dans
un cadre 9:16, un garde occupe 1 % de l'image, et une planche pleine page ne
montre rien."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

CAP = Path(__file__).resolve().parent.parent / 'captures'


def planche(nom, fichiers, boite, titre_par=None, colonnes=None):
    x0, y0, x1, y1 = boite
    vign = [(f, Image.open(CAP / f).convert('RGB').crop(boite)) for f in fichiers]
    l, h = x1 - x0, y1 - y0
    n = colonnes or len(vign)
    lignes = (len(vign) + n - 1) // n
    out = Image.new('RGB', (l * n, (h + 18) * lignes), (14, 14, 16))
    d = ImageDraw.Draw(out)
    for i, (f, im) in enumerate(vign):
        cx, cy = (i % n) * l, (i // n) * (h + 18)
        out.paste(im, (cx, cy))
        d.text((cx + 4, cy + h + 4), (titre_par or (lambda s: s))(f), fill=(190, 200, 210))
    out.save(CAP / nom)
    print(nom, out.size)


ALBEDOS = ['0-02', '0-04', '0-06', '0-08', '0-1', '0-13', '0-16', '0-22', '0-3', '0-45']
planche('planche-albedo.png',
        [f'garde-alb-do-{a}.png' for a in ALBEDOS],
        (170, 260, 270, 460), colonnes=5,
        titre_par=lambda f: 'albédo ' + f[15:-4].replace('-', ','))

planche('planche-origines-recadre.png',
        ['fond.png', 'garde-origine.png', 'garde-palette.png',
         'banc-origine.png', 'banc-palette.png',
         'sculpture-origine.png', 'sculpture-palette.png'],
        (150, 250, 290, 470), colonnes=7,
        titre_par=lambda f: f[:-4])

planche('planche-plafond-de-faces.png',
        [f'bronze-{n}-tris-2-m.png' for n in (15000, 4000, 2000, 1000, 500)],
        (150, 230, 290, 430), colonnes=5,
        titre_par=lambda f: f.split('-')[1] + ' tris')
