from action import Action
from obligation import Obligation
from crypto import Crypto

class ActifFactory:

    @staticmethod
    def creer_actif(type_actif, **donnees):
        type_actif = type_actif.lower()

        if type_actif == "action":
            return Action(
                donnees["nom"],
                donnees["prix_achat"],
                donnees["prix_actuel"],
                donnees["dividende"],
                donnees["quantite"]
            )

        elif type_actif == "obligation":
            return Obligation(
                donnees["nom"],
                donnees["valeur_nominale"],
                donnees["taux_interet"],
                donnees["duree"]
            )

        elif type_actif == "crypto":
            return Crypto(
                donnees["nom"],
                donnees["prix_achat"],
                donnees["prix_actuel"],
                donnees["quantite"]
            )

        else:
            raise ValueError("Type d'actif inconnu")