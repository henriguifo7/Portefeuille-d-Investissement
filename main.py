from portefeuille import Portefeuille
from factory import ActifFactory

portefeuille = Portefeuille()

def separateur (titre: str):
    print(f"\n{'_' * 65}")
    print(f"{titre}")
    print(f"{'_' * 65}")


a1 = ActifFactory.creer_actif(
    "action",
    nom="apple",
    prix_achat=40.000,
    prix_actuel=50.000,
    dividende=2,
    quantite=10
)

c1 = ActifFactory.creer_actif(
    "crypto",
    nom="Bitcoin",
    prix_achat=20000,
    prix_actuel=25000,
    quantite=0.1
)

o1 = ActifFactory.creer_actif(
    "obligation",
    nom="oat",
    valeur_nominale=1000,
    taux_interet=0.03,
    duree=5
)


print("\nAvant simulation :")
portefeuille.afficher_resume()

portefeuille.simuler_marche(+5)

print("\nAprès simulation :")

portefeuille.ajouter_actif(a1)
portefeuille.ajouter_actif(c1)
portefeuille.ajouter_actif(o1)
portefeuille.supprimer_actif("oat")
portefeuille.afficher_resume()

print(f" portefeuille après suppression : {len(portefeuille.actifs)} actifs")
portefeuille.afficher_resume()