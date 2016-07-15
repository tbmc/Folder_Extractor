# Folder Extract

### Fonctionnement
Déplace les fichiers du/des sous-dossiers dans le dossier courant.

### Arguments
* **-R | --recursive** : Déplace tous les fichiers de tous les dossiers et sous-dossiers
* **-rm | --remove** : Supprime les sous-dossiers après en avoir extraits les fichiers voulus
* **-x | --regex + "regex"** : Déplace uniquement les fichiers correspondants à la "regex"
    ```
    Exemple : python FolderExtractor.py -x "(ab)*"
    ```
* **-e | --extension + "ext"** : Déplace uniquement les fichiers correspondant à l'extension "extension" sans le "."
    ```
    Exemple : python FolderExtractor.py -e py
    *Sélectionne uniquement les fichier Python (\*.py)*
    ```