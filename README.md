# PyRPG
Moteur RPG style Zelda1 fait en Python.

Le moteur n'est qu'au début de son dévelopement donc j'ai glissé quelques fichiers pour faire des tests.
Le but est de rendre le tout fonctionnel tout en essayant de garder une facilité de navigation dans le code afin d'etre utilisé en tant qu' RPG Maker (mais en Python).

/!\ Afin que PyRPG soit utilisable, veillez à installez les modules 'keyboard' et 'pygame' à l'aide du terminal et de la commande 'pip' /!\
    Installer Pygame: 'pip install pygame'
    Installer Keyboard: 'pip install keyboard'

/!\ Actuellement, la convertion du fichier principale 'main.py' en exécutable (.exe) se fait avec le terminal. /!\
    Vous aurez besoin d'ouvrir le terminal et d'y écrire 'pip install cx-Freeze'.
    Ensuite, rendez-vous au dossier de PyRPG à l'aide de la commande 'cd' suivis du chemin complet du dossier PyRPG.
    Pour finir, entrez 'python to_exe.py build' et laissez le programme transformer le fichier 'main.py' en exe.
    Une fois finis, accédez au dossier 'exe' venant d'être créé dans le dossier de PyRPG ainsi qu'au dossier 'exe_...' s'y trouvant et y attrapez le fichier main.exe ainsi que le dossier 'lib' placez les dans le dossier-racine de PyRPG.
    Ensuite, vous pourrez utiliser l'exécutable.
    /!\ Si vous modifiez ou ajoutez des fichiers, veillez à reproduire la démarche de création de l'exécutable si vous souhaitez encore utilisez l'exécutable. /!\
