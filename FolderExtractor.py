import os
import sys
import shutil
import re


def extract_folder(dossier, base_dir=os.getcwd(), recursive=False, ext=False, regex=False):
    """
    Permet de déplacer tous les fichiers d'un dossier dans un autre dossier
    :param dossier: Dossier dans lequel chercher les fichiers
    :param base_dir: Dossier dans lequel déplacer les fichiers trouvés
    :param recursive: Chercher dans tous les sous dossier et pas uniquement dans le dossier courrant
    """
    reg = False

    if ext:
        reg = re.compile(r"\.{}$".format(ext))
    elif regex:
        reg = re.compile(regex)
    for n in os.listdir(dossier):
        a = "{}/{}".format(dossier, n)
        if os.path.isfile(a):
            if base_dir != dossier:
                if reg and reg.search(n):
                    os.rename(a, base_dir + "/" + n)
        elif recursive:
            extract_folder(a, base_dir, recursive, ext, regex)


def remove_sub_folder(dossier):
    for n in os.listdir(dossier):
        a = "{}/{}".format(dossier, n)
        if os.path.isdir(a):
            shutil.rmtree(a)


def print_help():
    a = """
Voici les quelques commandes utiles :
Recursive : Extrait dans le dossier courant, tous les dossiers ainsi que tous les sous-dossiers
RemoveFolders : Supprime les dossiers après avoir déplacé les fichiers (même si il reste encore des fichiers)
Only regex "regex" : Déplace uniquement les fichiers correspondants à une regex
Only ext "ext" : Déplace uniquement les fichiers correspondants à une certaine extension
    """
    print(a)

arguments = {
    "recursive": False,
    "removefolders": False,
    "regex": False,
    "extension": False,
}


def arguments_helper():
    l = len(sys.argv)
    if l > 1:
        i = 1
        while i < l:
            arg = sys.argv[i]
            arg = arg.lower()
            if arg == "recursive":
                arguments["recursive"] = True
            elif arg == "only":
                arg1 = sys.argv[i+1].lower()
                arg2 = sys.argv[i+2].lower()
                i += 2
                if i + 2 >= l:
                    return "Il manque des arguments avec l'option 'only'"
                if arg1 == "regex":
                    arguments["regex"] = arg2
                elif arg1 == "ext":
                    arguments["extension"] = arg2
                else:
                    return "L'argument après 'only' est une action non gérée : {}".format(arg1)
            elif arg == "removefolders":
                arguments["removefolders"] = True
            else:
                return "Argument inconnu : {}".format(arg)
            i += 1
    return False


if __name__ == "__main__":
    print("Extract Folder")
    error_arg = arguments_helper()
    if error_arg:
        print(error_arg)
        print()
        print_help()
    else:
        base = os.getcwd()
        base = "B:\\BigBangTheoryS07"
        print("En cours...")
        extract_folder(base, base, arguments["recursive"],
                       arguments["extension"], arguments["regex"])
        if arguments["removefolders"]:
            remove_sub_folder(base)
        print("Fini")



