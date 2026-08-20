#!/usr/bin/env python3
"""Analyse du journal append-only `.fal-journal.jsonl` du depot legacy.

Lecture seule. Compte les appels par modele, mesure les durees, distingue
les sorties encore presentes sur disque des essais jetes.

Usage: python3 scripts/analyse-journal.py [chemin-du-journal]
"""
import json, sys, os, collections, statistics, re

RACINE = "/home/fayssal/projetCadeau"
JOURNAL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, "outils/.fal-journal.jsonl")

rows = [json.loads(l) for l in open(JOURNAL) if l.strip()]


def est_video(m):
    return m.endswith("image-to-video") or m.endswith("reference-to-video")


def est_image(m):
    return "nano-banana" in m or "seedream" in m


def sortie(d):
    return d.get("fichiers") or []


def existe(f):
    return os.path.exists(os.path.join(RACINE, f))


print("=" * 78)
print("1. VOLUMETRIE GLOBALE")
print("=" * 78)
print("appels journalises : %d" % len(rows))
print("periode            : %s -> %s" % (min(r["quand"] for r in rows), max(r["quand"] for r in rows)))
tot_s = sum(r["secondes"] for r in rows)
print("temps machine total: %.0f s = %.2f h" % (tot_s, tot_s / 3600))

print()
print("=" * 78)
print("2. APPELS PAR MODELE (avec unites facturables)")
print("=" * 78)
par_modele = collections.defaultdict(list)
for r in rows:
    par_modele[r["modele"]].append(r)

for m, rs in sorted(par_modele.items(), key=lambda kv: -len(kv[1])):
    n = len(rs)
    fich = sum(len(sortie(r)) for r in rs)
    presents = sum(1 for r in rs for f in sortie(r) if existe(f))
    secs = [r["secondes"] for r in rs]
    if est_video(m):
        dur = sum(int(r["entree"].get("duration", 0) or 0) for r in rs)
        res = collections.Counter(str(r["entree"].get("resolution")) for r in rs)
        audio = sum(1 for r in rs if r["entree"].get("generate_audio"))
        unite = "%d s de video demandees | resolutions %s | audio on: %d" % (dur, dict(res), audio)
    elif est_image(m):
        imgs = sum(int(r["entree"].get("num_images", 1) or 1) for r in rs)
        unite = "%d images demandees" % imgs
    else:
        unite = "-"
    print()
    print(m)
    print("  appels %3d | fichiers produits %3d | encore sur disque %3d" % (n, fich, presents))
    print("  duree appel  med %6.1fs  moy %6.1fs  min %.1fs  max %.1fs  total %.0fs"
          % (statistics.median(secs), statistics.mean(secs), min(secs), max(secs), sum(secs)))
    print("  " + unite)

print()
print("=" * 78)
print("3. VIDEO - DETAIL APPEL PAR APPEL")
print("=" * 78)
print("%-20s %-46s %4s %6s %5s %7s %11s  prefixe" % ("quand", "modele", "dur", "res", "aud", "s", "sur disque"))
for r in sorted((r for r in rows if est_video(r["modele"])), key=lambda r: r["quand"]):
    e = r["entree"]
    f = sortie(r)
    dispo = "%d/%d" % (sum(1 for x in f if existe(x)), len(f))
    print("%-20s %-46s %4s %6s %5s %7.1f %11s  %s"
          % (r["quand"][:19], r["modele"], e.get("duration"), e.get("resolution"),
             e.get("generate_audio"), r["secondes"], dispo, r["prefixe"]))

print()
print("=" * 78)
print("4. GROUPES DE PLANS (prefixe normalise) - mesure du taux d'essais")
print("=" * 78)


def racine_prefixe(p):
    p = re.sub(r"\d+$", "", p)
    p = re.sub(r"[-_]?(v|essai|retry|bis)$", "", p)
    return p.rstrip("-_") or p


for famille, pred in (("VIDEO", est_video), ("IMAGE", est_image)):
    print()
    print("--- %s ---" % famille)
    g = collections.defaultdict(list)
    for r in rows:
        if pred(r["modele"]):
            g[racine_prefixe(r["prefixe"])].append(r)
    for k, rs in sorted(g.items(), key=lambda kv: -len(kv[1])):
        presents = sum(1 for r in rs for f in sortie(r) if existe(f))
        tot = sum(len(sortie(r)) for r in rs)
        print("  %-34s appels %3d  fichiers %3d  sur disque %3d" % (k, len(rs), tot, presents))

print()
print("=" * 78)
print("5. EMPREINTES DUPLIQUEES (meme entree relancee = re-roll pur)")
print("=" * 78)
emp = collections.Counter(r["empreinte"] for r in rows)
dups = {k: v for k, v in emp.items() if v > 1}
print("appels avec une empreinte deja vue : %d sur %d" % (sum(v - 1 for v in dups.values()), len(rows)))
for k, v in sorted(dups.items(), key=lambda kv: -kv[1])[:15]:
    ex = next(r for r in rows if r["empreinte"] == k)
    print("  %s x%d  %s  %s" % (k, v, ex["modele"], ex["prefixe"]))

print()
print("=" * 78)
print("6. SORTIES ENCORE PRESENTES vs JETEES (global)")
print("=" * 78)
tot_f = sum(len(sortie(r)) for r in rows)
pres_f = sum(1 for r in rows for f in sortie(r) if existe(f))
print("fichiers produits selon le journal : %d" % tot_f)
print("encore presents sur disque         : %d  (%.0f %%)" % (pres_f, 100 * pres_f / tot_f))
print("disparus / supprimes               : %d  (%.0f %%)" % (tot_f - pres_f, 100 * (tot_f - pres_f) / tot_f))

print()
print("=" * 78)
print("7. REPARTITION PAR DOSSIER DE DESTINATION")
print("=" * 78)
dossiers = collections.Counter()
for r in rows:
    for f in sortie(r):
        dossiers[os.path.dirname(f)] += 1
for d, c in dossiers.most_common(40):
    print("  %4d  %s" % (c, d))
