# Jeu Démineur

J’ai split mon programme en 4 méthodes : 

# Main : 

Le main consiste à générer le plateau de jeu en appelant la méthode Plateau.getPlateau()

Grace à la valeur du niveau renseignée par le joueur, le Main appelle la méthode Mine.getMines(niveau) et les valeurs des mines sont détérminée.

Avec le plateau de jeu et les mines le main lance le jeu en appelant la méthode Game.play(plateau, mines)

Dans le cas où une partie a été déjà enregistrée par le joueur, le main récupère les mines et le plateau enregistré avec les valeurs des cases entrées auparavant affichées.  

# Plateau : 

La méthode getplateau() génère un Dataframe de 100 case (10 x 10) où les lignes sont représentées par des lettres (A, B,..., J) et les colonnes par des numéros (1, 2,..., 10).

Les valeurs sont disposées aléatoirement dans le Dataframe.

# Mine : 

La méthode getmines(niveau) prend le niveau en entrée et génère une liste d’entiers entre 0 et 99 et de taille égale au niveau. Le niveau maximal est 4.

# Game : 

La méthode play lance la partie de jeu

Le joueur est prié de saisir un caractère parmi les lettres (a,b,..,j) représentant une ligne du plateau. Si aucun caractère n’est entré ou la valeur renseignée n’est pas un caractère compris entre a et j, une exception est levée.

Un numéro de 1 à 10 correspondant à une colonne.

Le détail des variables et fonctions utilisées est sous forme de commentaire dans le programme.

Les valeurs des cases sélectionnées s’ajoutent pour calculer le score atteint.

Avant chaque tour, un enregistrement de la partie est fait sur un fichier savedData.txt 

