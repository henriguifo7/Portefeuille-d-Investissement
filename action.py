from actif import Actif

class Action(Actif):

    def __init__(self, nom, prix_achat, prix_actuel, dividende, quantite):
        super().__init__(nom)
        self.prix_achat = prix_achat
        self.prix_actuel = prix_actuel
        self.dividende = dividende
        self.quantite = quantite

    def valeur_actuelle(self):
        return self.prix_actuel * self.quantite

    def calculer_rendement(self):
        gain = (self.prix_actuel - self.prix_achat) * self.quantite
        dividendes = self.dividende * self.quantite
        return gain + dividendes

    def to_dict(self):
        return {
            "type": "action",
            "nom": self.nom,
            "prix_achat": self.prix_achat,
            "prix_actuel": self.prix_actuel,
            "dividende": self.dividende,
            "quantite": self.quantite
        }