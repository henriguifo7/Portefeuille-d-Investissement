import json
from factory import ActifFactory


class Portefeuille:

    def __init__(self):
        self.actifs = []

    # Ajouter un actif
    def ajouter_actif(self, actif):
        self.actifs.append(actif)

    # Supprimer un actif par nom
    def supprimer_actif(self, nom):
        self.actifs = [a for a in self.actifs if a.nom != nom]

    # Calculer la valeur totale du portefeuille
    def valeur_totale(self):
        return sum(actif.valeur_actuelle() for actif in self.actifs)

    # Calculer le rendement global
    def rendement_global(self):
        return sum(actif.calculer_rendement() for actif in self.actifs)

    # Simulation du marché
    def simuler_marche(self, variation):
        """
        variation = pourcentage (+5, -3, etc.)
        """
        for actif in self.actifs:
            if hasattr(actif, "prix_actuel"):
                actif.prix_actuel *= (1 + variation / 100)

    # Affichage du résumé
    def afficher_resume(self):
        print("\n📊 Résumé du portefeuille")
        print("--------------------------------")

        for actif in self.actifs:
            print(
                f"{actif.nom} | Valeur actuelle: {actif.valeur_actuelle():.2f} | Rendement: {actif.calculer_rendement():.2f}"
            )

        print("--------------------------------")
        print(f"💰 Valeur totale : {self.valeur_totale():.2f}")
        print(f"📈 Rendement global : {self.rendement_global():.2f}")

    # Sauvegarde JSON
    def sauvegarder(self, fichier="portefeuille.json"):
        data = [actif.to_dict() for actif in self.actifs]

        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print("💾 Portefeuille sauvegardé")

    # Chargement JSON
    def charger(self, fichier="portefeuille.json"):
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.actifs = []

        for item in data:
            type_actif = item.pop("type")
            actif = ActifFactory.creer_actif(type_actif, **item)
            self.actifs.append(actif)

        print("📂 Portefeuille chargé")