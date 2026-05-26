from abc import ABC, abstractmethod

class Actif(ABC):
    """
    Classe abstraite représentant un actif financier.
    Toutes les classes filles (Action, Obligation, Crypto)
    doivent implémenter les méthodes abstraites.
    """

    def __init__(self, nom):
        self._nom = nom  # encapsulation

    @property
    def nom(self):
        return self._nom

    @abstractmethod
    def calculer_rendement(self):
        """
        Calcule le rendement de l'actif.
        """
        pass

    @abstractmethod
    def valeur_actuelle(self):
        """
        Retourne la valeur actuelle de l'actif.
        """
        pass

    @abstractmethod
    def to_dict(self):
        """
        Convertit l'actif en dictionnaire pour la sauvegarde JSON.
        """
        pass