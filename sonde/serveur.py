#!/usr/bin/env python3
"""Sert la sonde sur le réseau local et recueille les relevés qu'elle renvoie.

    python3 sonde/serveur.py [port]

POST /releve enregistre le rapport dans docs/recherche/releves/. C'est ce qui
évite de recopier un JSON depuis un téléphone tenu à bout de bras.
"""
import json, re, sys, datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

RACINE = Path(__file__).resolve().parent
RELEVES = RACINE.parent / "docs" / "recherche" / "releves"


def ardoise(texte, repli):
    texte = re.sub(r"[^\w.-]+", "-", (texte or "").strip()).strip("-")
    return texte or repli


class Sonde(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(RACINE), **kw)

    def do_POST(self):
        if self.path.rstrip("/") != "/releve":
            self.send_error(404)
            return
        taille = int(self.headers.get("Content-Length", 0))
        brut = self.rfile.read(taille)
        try:
            rapport = json.loads(brut)
        except json.JSONDecodeError as e:
            self.send_error(400, f"JSON illisible : {e}")
            return
        meta = rapport.get("meta", {})
        nom = "{}-{}.json".format(
            ardoise(meta.get("appareil"), "appareil"),
            ardoise(meta.get("app"), "app"),
        )
        chemin = RELEVES / nom
        RELEVES.mkdir(parents=True, exist_ok=True)
        if chemin.exists():  # un second passage n'écrase pas le premier
            horodate = datetime.datetime.now().strftime("%H%M%S")
            chemin = RELEVES / f"{chemin.stem}-{horodate}.json"
        chemin.write_text(json.dumps(rapport, ensure_ascii=False, indent=1), encoding="utf-8")
        corps = json.dumps({"ecrit": chemin.name}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)
        print(f"  ← relevé reçu : {chemin.name} ({taille} octets)")

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"Sonde servie sur le port {port} — relevés écrits dans {RELEVES}")
    ThreadingHTTPServer(("0.0.0.0", port), Sonde).serve_forever()
