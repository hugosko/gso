Labo 5: application python utilisant un service d'API public

Description
Ce programme python permet d'afficher une blague en utilisant la librairie requests

Table des matières
- [Pré-requis]
- [Installation]
- [Utilisation]


[Pré-requis]

Avant de commencer, assurez-vous d’avoir installé :
- Python 3.10 ou plus
- pip
- (Optionnel) Docker si vous utilisez une version conteneurisée.


[Installation]

Avec Docker
1: Cloner le projet 
- git clone https://github.com/hugosko/ue19-lab-05.git

2: Construire l'image Docker
- docker build -t mon-projet .

Sans Docker
1: Cloner le projet 
- git clone https://github.com/hugosko/ue19-lab-05.git

2: Installer les dépendances
- pip install -r requirements.txt


[Utilisation]

Avec Docker
- docker run mon-projet

Sans Docker
- python app.py
