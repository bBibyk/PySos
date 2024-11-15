print("pysos")
from UserInterface import UserInterface

def main():
    ui = UserInterface()

    while True:
        print("\n--- Menu ---")
        print("1. Créer une nouvelle personne")
        print("2. Supprimer une personne")
        print("3. Créer une relation d'amitié")
        print("4. Supprimer une relation d'amitié")
        print("5. Afficher les personnes")
        print("6. Sauvegarder les données")
        print("7. Quitter")
        print("8. Charger les données")
        print("9. Produire diagramme")
        choix = input("Votre choix : ")

        if choix == "1":
            ui.create_person()
        elif choix == "2":
            ui.delate_person()
        elif choix == "3":
            ui.create_link()
        elif choix == "4":
            ui.delate_link()
        elif choix == "5":
            print(ui)
        elif choix == "6":
            ui.save()
            print("Données sauvegardées avec succès !")
        elif choix == "7":
            print("Au revoir...")
            break
        elif choix == "8":
            ui.load()
            print("Chargement des données...")
        elif choix == "9":
            ui.make_diagram()
            print("Le diagramme a été produit.")
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
