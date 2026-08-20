#!/usr/bin/env python3
"""Chiffre le journal fal aux tarifs publics fal.ai releves le 20/08/2026.

Le journal ne consigne AUCUN montant : il consigne le modele, l'entree et les
fichiers produits. Tout montant ci-dessous est donc RECALCULE en appliquant les
formules de facturation publiees par fal.ai aux parametres mesures dans le
journal. On distingue :
  - MESURE  : nombre d'appels, duree demandee, resolution, fichiers  -> journal
  - ESTIME  : le prix unitaire                                       -> fal.ai

Tarifs releves le 2026-08-20 (voir docs/recherche/couts-production.md pour les
URL et le niveau de confiance de chaque ligne).
"""
import json, os, collections, sys

RACINE = "/home/fayssal/projetCadeau"
JOURNAL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, "outils/.fal-journal.jsonl")
USD_EUR = 0.854  # 1 USD ~= 0.854 EUR, source secondaire, confiance moyenne

# --- Dimensions de sortie effectivement mesurees sur les mp4 produits ---------
DIMS = {
    ("seedance-2.5", "720p"): (720, 1280),   # mesure sur les mp4 : 720x1280
    ("seedance-2.5", "480p"): (496, 864),    # grille fal 9:16 480p
    ("seedance-1", "720p"): (704, 1248),     # mesure sur les rushes : 704x1248
    ("seedance-1", "1080p"): (1056, 1872),   # non mesure (aucun fichier restant)
    ("seedance-2.0", "720p"): (720, 1280),
    ("seedance-2.0", "480p"): (496, 864),
    ("minimax", "768P"): (768, 1376),        # non mesure
}


def dims(fam, res):
    for (f, r), v in DIMS.items():
        if fam.startswith(f) and r == res:
            return v
    return (720, 1280)


def famille(m):
    if "seedance-2.5" in m:
        return "seedance-2.5"
    if "seedance/v1.5/pro" in m:
        return "seedance-1.5-pro"
    if "seedance/v1/lite" in m:
        return "seedance-1.0-lite"
    if "seedance-2.0/fast" in m:
        return "seedance-2.0-fast"
    if "seedance-2.0/mini" in m:
        return "seedance-2.0-mini"
    if "nano-banana" in m:
        return "nano-banana-pro"
    if "seedream" in m:
        return "seedream"
    if "minimax" in m:
        return "minimax-h3"
    if "tripo" in m:
        return "tripo3d"
    return m


def cout_usd(d):
    """Renvoie (bas, haut, note) en USD pour un appel journalise."""
    m, e = d["modele"], d["entree"]
    fam = famille(m)
    dur = int(e.get("duration", 0) or 0)
    res = e.get("resolution")

    if fam == "seedance-2.5":
        w, h = dims(fam, res)
        tok = w * h * dur * 24 / 1024
        c = tok * 0.0214 / 1000  # refs image non facturees, pas de remise 0.6
        return c, c, "formule tokens publiee"

    if fam == "seedance-1.5-pro":
        w, h = dims("seedance-1", res)
        tok = w * h * 24 * dur / 1024
        avec = bool(e.get("generate_audio"))
        c = tok * (2.4 if avec else 1.2) / 1e6
        return c, c, "1,2 $/M sans audio, 2,4 $/M avec"

    if fam == "seedance-1.0-lite":
        w, h = dims("seedance-1", res)
        tok = w * h * 24 * dur / 1024
        # bas  : reroutage vers Seedance 1.0 Pro Fast, 1,00 $/M (tarif d'aujourd'hui)
        # haut : tarif lite historique, 1,80 $/M
        return tok * 1.0 / 1e6, tok * 1.8 / 1e6, "endpoint deprecie, fourchette 1,00-1,80 $/M"

    if fam == "seedance-2.0-fast":
        return dur * 0.2419, dur * 0.2419, "0,2419 $/s a 720p"

    if fam == "seedance-2.0-mini":
        # variante non documentee publiquement : bornee par le token standard (bas)
        # et par le tarif fast (haut)
        w, h = dims("seedance-2.0", res)
        tok = w * h * dur * 24 / 1024
        return tok * 0.014 / 1000 * 0.5, dur * 0.2419, "variante mini non tarifee publiquement"

    if fam == "nano-banana-pro":
        n = int(e.get("num_images", 1) or 1)
        prix = 0.30 if str(e.get("resolution")).upper() == "4K" else 0.15
        c = n * prix
        return c, c, "0,15 $/image (1K-2K), 0,30 $ en 4K"

    if fam == "seedream":
        n = int(e.get("num_images", 1) or 1)
        if d["fichiers"]:
            return n * 0.03, n * 0.03, "0,03 $/image (v4)"
        return 0.0, n * 0.03, "appel sans fichier produit : facture ou non, inconnu"

    if fam == "minimax-h3":
        return 0.20, 0.80, "tarif non releve : fourchette large"

    if fam == "tripo3d":
        return 0.05, 0.30, "tarif non releve : fourchette large"

    return 0.0, 0.0, "inconnu"


rows = [json.loads(l) for l in open(JOURNAL) if l.strip()]
for r in rows:
    r["_fam"] = famille(r["modele"])
    r["_bas"], r["_haut"], r["_note"] = cout_usd(r)
    r["_garde"] = any(os.path.exists(os.path.join(RACINE, f)) for f in r["fichiers"])


def chantier(d):
    fs = d["fichiers"]
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
    return "hors-depot (scratchpad)"


def bloc(titre, sel):
    sel = list(sel)
    if not sel:
        return
    b = sum(r["_bas"] for r in sel)
    h = sum(r["_haut"] for r in sel)
    print("  %-42s %3d appels  %7.2f - %7.2f $   %6.2f - %6.2f EUR"
          % (titre, len(sel), b, h, b * USD_EUR, h * USD_EUR))
    return b, h


print("=" * 96)
print("A. COUT RECALCULE PAR FAMILLE DE MODELE (tarifs publics fal.ai, releve 2026-08-20)")
print("=" * 96)
for fam in sorted({r["_fam"] for r in rows}, key=lambda f: -sum(r["_haut"] for r in rows if r["_fam"] == f)):
    sel = [r for r in rows if r["_fam"] == fam]
    bloc(fam, sel)
TB = sum(r["_bas"] for r in rows)
TH = sum(r["_haut"] for r in rows)
print("  " + "-" * 92)
print("  %-42s %3d appels  %7.2f - %7.2f $   %6.2f - %6.2f EUR"
      % ("TOTAL DU JOURNAL", len(rows), TB, TH, TB * USD_EUR, TH * USD_EUR))

print()
print("=" * 96)
print("B. COUT PAR CHANTIER")
print("=" * 96)
ch = collections.defaultdict(list)
for r in rows:
    ch[chantier(r)].append(r)
for c in sorted(ch, key=lambda c: -sum(r["_haut"] for r in ch[c])):
    print()
    print("### " + c)
    for fam in sorted({r["_fam"] for r in ch[c]}, key=lambda f: -sum(r["_haut"] for r in ch[c] if r["_fam"] == f)):
        bloc("  " + fam, [r for r in ch[c] if r["_fam"] == fam])
    bloc("  = sous-total", ch[c])

print()
print("=" * 96)
print("C. GARDE vs JETE (sortie encore presente sur disque ou non)")
print("=" * 96)
for etat, pred in (("GARDE (fichier encore present)", lambda r: r["_garde"]),
                   ("JETE  (fichier absent du disque)", lambda r: not r["_garde"])):
    bloc(etat, [r for r in rows if pred(r)])

print()
print("=" * 96)
print("D. LES DEUX CINEMATIQUES SEEDANCE 2.5 SERVIES (combat-3d ouverture + fin)")
print("=" * 96)
s25_combat = [r for r in rows if r["_fam"] == "seedance-2.5" and any("combat-3d" in f for f in r["fichiers"])]
for r in sorted(s25_combat, key=lambda r: r["quand"]):
    print("   %s  %-16s %2ss %s  %6.2f $" % (r["quand"][:16], r["prefixe"], r["entree"]["duration"],
                                             r["entree"]["resolution"], r["_haut"]))
bloc("= total des 3 appels 2.5 du combat", s25_combat)
print()
print("   -> 50 s de cinematique servie (ouverture 30 s + fin 20 s), 1 essai de fin jete")

print()
print("=" * 96)
print("E. LA CARTE ANIMEE (template animation-cadeau)")
print("=" * 96)
ac = [r for r in rows if any("animation-cadeau" in f for f in r["fichiers"])]
bloc("nano-banana-pro (decors, papiers, ecritures)", [r for r in ac if r["_fam"] == "nano-banana-pro"])
bloc("seedance-2.5 (films)", [r for r in ac if r["_fam"] == "seedance-2.5"])
bloc("= total carte animee", ac)
s25ac = [r for r in ac if r["_fam"] == "seedance-2.5"]
retenu = [r for r in s25ac if "film2h" in r["prefixe"]]
print()
print("   film servi : public/films/depliage.mp4 = film2h-bordure (10 s)")
print("   cout du SEUL rendu retenu            : %6.2f $ (%5.2f EUR)"
      % (sum(r["_haut"] for r in retenu), sum(r["_haut"] for r in retenu) * USD_EUR))
print("   cout des 8 autres essais 2.5         : %6.2f $ (%5.2f EUR)"
      % (sum(r["_haut"] for r in s25ac if r not in retenu),
         sum(r["_haut"] for r in s25ac if r not in retenu) * USD_EUR))
print("   ratio essais / retenu                : %.1f x" %
      (sum(r["_haut"] for r in s25ac) / sum(r["_haut"] for r in retenu)))

print()
print("=" * 96)
print("F. FICHES PERSONNAGES (prefixe contenant 'fiche')")
print("=" * 96)
fi = [r for r in rows if "fiche" in r["prefixe"].lower() and r["_fam"] == "nano-banana-pro"]
bloc("appels 'fiche' (2 personnages, illies + crevette)", fi)
print("   images demandees : %d | encore sur disque : %d"
      % (sum(int(r["entree"].get("num_images", 1) or 1) for r in fi),
         sum(1 for r in fi for f in r["fichiers"] if os.path.exists(os.path.join(RACINE, f)))))
perso = [r for r in fi if r["prefixe"].startswith("illies-fiche")]
bloc("dont le seul personnage 'illies' (7 passes)", perso)
