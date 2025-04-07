from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


def main():
    print("\nBienvenue dans le programme de gestion des échecs !")
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    while True:
        print("\nMenu principal :")
        print("1. Créer un joueur")
        print("2. Afficher les joueurs")
        print("3. Créer un tournoi")
        print("4. Reprendre un tournoi en cours")
        print("5. Voir les détails d'un tournoi")
        print("6. Quitter")
        choice = input("Entrez votre choix : ")

        if choice == "1":
            player_controller.create_player()
        elif choice == "2":
            player_controller.display_players()
        elif choice == "3":
            tournament_controller.create_tournament()
        elif choice == "4":
            tournament_controller.resume_tournament()
        elif choice == "5":
            tournament_controller.view_tournament_details()
        elif choice == "6":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
