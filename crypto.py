from actif import Actif

class Crypto(Actif):

    def __init__(self, nom, prix_achat, prix_actuel, quantite):
        super().__init__(nom)
        self.prix_achat = prix_achat
        self.prix_actuel = prix_actuel
        self.quantite = quantite

    def valeur_actuelle(self):
        return self.prix_actuel * self.quantite

    def calculer_rendement(self):
        return (self.prix_actuel - self.prix_achat) * self.quantite

    def to_dict(self):
        return {
            "type": "crypto",
            "nom": self.nom,
            "prix_achat": self.prix_achat,
            "prix_actuel": self.prix_actuel,
            "quantite": self.quantite
        }