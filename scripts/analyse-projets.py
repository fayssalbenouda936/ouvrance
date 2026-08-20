#!/usr/bin/env python3
"""Vue par projet (dossier de destination) du journal fal.

Regroupe les appels par "chantier" (template ou cadeau livre) et par famille de
modele, pour separer le cout d'une experience maitre du bruit d'exploration.
"""
import json, os, collections, statistics, sys

RACINE = "/home/fayssal/projetCadeau"
JOURNAL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, "outils/.fal-journal.jsonl")
rows = [json.loads(l) for l in open(JOURNAL) if l.strip()]


def est_video(m):
    return m.endswith("image-to-video") or m.endswith("reference-to-video")


def chantier(d):
    fs = d.get("fichiers") or []
    if not fs:
        return "(aucun fichier)"
    p = fs[0]
    parts = p.split("/")
    if p.startswith("apps/gifts/_templates/"):
        return "template:" + parts[3]
    if p.startswith("apps/gifts/"):
        return "cadeau:" + parts[2]
    if p.startswith("promo/"):
        return "promo:" + parts[1]
    return "autre:" + os.path.dirname(p)


def famille(m):
    if "seedance-2.5" in m:
        return "seedance-2.5"
    if "seedance/v1.5/pro" in m:
        return "seedance-1.5-pro"
    if "seedance/v1/lite" in m:
        return "seedance-1-lite"
    if "seedance-2.0" in m:
        return "seedance-2.0"
    if "nano-banana" in m:
        return "nano-banana-pro"
    if "seedream" in m:
        return "seedream"
    return m


g = collections.defaultdict(lambda: collections.defaultdict(list))
for r in rows:
    g[chantier(r)][famille(r["modele"])].append(r)

print("=" * 90)
print("APPELS PAR CHANTIER x FAMILLE DE MODELE")
print("=" * 90)
for ch in sorted(g, key=lambda c: -sum(len(v) for v in g[c].values())):
    tot = sum(len(v) for v in g[ch].values())
    print()
    print("### %s   (%d appels)" % (ch, tot))
    for fam, rs in sorted(g[ch].items(), key=lambda kv: -len(kv[1])):
        fich = sum(len(r["fichiers"]) for r in rs)
        pres = sum(1 for r in rs for f in r["fichiers"] if os.path.exists(os.path.join(RACINE, f)))
        sec_video = sum(int(r["entree"].get("duration", 0) or 0) for r in rs if est_video(r["modele"]))
        imgs = sum(int(r["entree"].get("num_images", 1) or 1) for r in rs if not est_video(r["modele"]))
        extra = ("%d s video" % sec_video) if sec_video else ("%d images" % imgs)
        wall = sum(r["secondes"] for r in rs)
        print("   %-18s appels %3d | fichiers %3d | restants %3d | %-14s | %6.0f s machine"
              % (fam, len(rs), fich, pres, extra, wall))

print()
print("=" * 90)
print("SEEDANCE 2.5 - DETAIL COMPLET (le modele de reference pour les maitres)")
print("=" * 90)
s25 = [r for r in rows if "seedance-2.5" in r["modele"]]
tot_sec = 0
for r in sorted(s25, key=lambda r: r["quand"]):
    e = r["entree"]
    f = r["fichiers"]
    pres = [x for x in f if os.path.exists(os.path.join(RACINE, x))]
    tot_sec += int(e.get("duration", 0) or 0)
    nrefs = len(e.get("image_urls", []) or ([e["image_url"]] if e.get("image_url") else []))
    print("%s | %-14s | %2ss %5s aud=%s | %d ref | %6.1fs | %s | %s"
          % (r["quand"][:16], r["modele"].split("/")[-1], e.get("duration"), e.get("resolution"),
             e.get("generate_audio"), nrefs, r["secondes"], "GARDE" if pres else "JETE",
             f[0] if f else "-"))
print()
print("total secondes de video Seedance 2.5 demandees : %d s" % tot_sec)
gardes = [r for r in s25 if any(os.path.exists(os.path.join(RACINE, x)) for x in r["fichiers"])]
print("appels dont la sortie est encore sur disque    : %d / %d" % (len(gardes), len(s25)))
print("secondes gardees                               : %d s"
      % sum(int(r["entree"].get("duration", 0) or 0) for r in gardes))
print("temps machine total Seedance 2.5               : %.0f s (%.1f h)"
      % (sum(r["secondes"] for r in s25), sum(r["secondes"] for r in s25) / 3600))

print()
print("=" * 90)
print("FICHES PERSONNAGES - tous les appels dont le prefixe contient 'fiche'")
print("=" * 90)
fiches = [r for r in rows if "fiche" in r["prefixe"].lower()]
for r in sorted(fiches, key=lambda r: r["quand"]):
    e = r["entree"]
    pres = sum(1 for x in r["fichiers"] if os.path.exists(os.path.join(RACINE, x)))
    print("%s | %-28s | n=%s %s | %5.1fs | %d/%d sur disque | %s"
          % (r["quand"][:16], r["modele"].split("fal-ai/")[-1], e.get("num_images"),
             e.get("aspect_ratio"), r["secondes"], pres, len(r["fichiers"]), r["prefixe"]))
print()
print("appels fiches : %d | images demandees : %d | encore sur disque : %d"
      % (len(fiches),
         sum(int(r["entree"].get("num_images", 1) or 1) for r in fiches),
         sum(1 for r in fiches for x in r["fichiers"] if os.path.exists(os.path.join(RACINE, x)))))

print()
print("=" * 90)
print("ANIMATION-CADEAU (la carte animee) - tous les appels")
print("=" * 90)
ac = [r for r in rows if any("animation-cadeau" in f for f in r["fichiers"])]
byfam = collections.Counter(famille(r["modele"]) for r in ac)
print("appels : %d  %s" % (len(ac), dict(byfam)))
for r in sorted(ac, key=lambda r: r["quand"]):
    e = r["entree"]
    pres = sum(1 for x in r["fichiers"] if os.path.exists(os.path.join(RACINE, x)))
    d = e.get("duration")
    print("%s | %-24s | %-22s | %s | %5.1fs | %d/%d"
          % (r["quand"][:16], famille(r["modele"]), r["prefixe"],
             ("%ss %s" % (d, e.get("resolution"))) if d else ("n=%s" % e.get("num_images")),
             r["secondes"], pres, len(r["fichiers"])))

print()
print("=" * 90)
print("TAILLE DES SORTIES ENCORE SUR DISQUE (pour le dimensionnement R2)")
print("=" * 90)
tail = collections.defaultdict(lambda: [0, 0])
for r in rows:
    fam = famille(r["modele"])
    for f in r["fichiers"]:
        p = os.path.join(RACINE, f)
        if os.path.exists(p):
            tail[fam][0] += 1
            tail[fam][1] += os.path.getsize(p)
for fam, (n, o) in sorted(tail.items(), key=lambda kv: -kv[1][1]):
    print("  %-18s %3d fichiers  %8.1f Mo  moyenne %6.2f Mo"
          % (fam, n, o / 1e6, o / 1e6 / n))
