from actif import Actif

class Obligation(Actif):

    def __init__(self, nom, valeur_nominale, taux_interet, duree):
        super().__init__(nom)
        self.valeur_nominale = valeur_nominale
        self.taux_interet = taux_interet
        self.duree = duree

    def valeur_actuelle(self):
        """
        La valeur actuelle d'une obligation correspond à sa valeur nominale.
        """
        return self.valeur_nominale

    def calculer_rendement(self):
        """
        Rendement basé sur les intérêts cumulés.
        """
        return self.valeur_nominale * self.taux_interet * self.duree

    def to_dict(self):
        """
        Convertit l'objet en dictionnaire pour la sauvegarde JSON.
        """
        return {
            "type": "obligation",
            "nom": self.nom,
            "valeur_nominale": self.valeur_nominale,
            "taux_interet": self.taux_interet,
            "duree": self.duree
        }