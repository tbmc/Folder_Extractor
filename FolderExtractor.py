
import os, sys


def extract_folder(dir, base_dir=os.getcwd(), recursive=False):
    """
    Permet de déplacer tous les fichiers d'un dossier dans un autre dossier
    :param dir: Dossier dans lequel chercher les fichiers
    :param base_dir: Dossier dans lequel déplacer les fichiers trouvés
    :param recursive: Chercher dans tous les sous dossier et pas uniquement dans le dossier courrant
    """
    for n in os.listdir(dir):
        print(dir + "/" + n)
        if os.path.isfile(dir + "/" + n):
            if base_dir != dir:
                os.rename(dir + "/" + n, base_dir + "/" + n)
        elif recursive:
            extract_folder(dir + "/" + n, base_dir, recursive)


def print_help():
    a = """
Voici les quelques commandes utiles :
Recursive : Extrait dans le dossier courant, tous les dossiers ainsi que tous les sous-dossiers

    """
    print(a)

arguments = {
    "recursive": False,
}

def arguments_helper():
    l = len(sys.argv)
    error = False
    if l > 1:
        for arg in sys.argv:
            if arg == sys.argv[0]:
                continue
            arg = arg.lower()
            if arg in arguments:
                arguments[arg] = not arguments[arg]
            else:
                error = True
    return error


if __name__ == "__main__":
    print("Extract Folder")
    error_arg = arguments_helper()
    if error_arg:
        print_help()
    else:
        base = os.getcwd()
        extract_folder(base, base, arguments["recursive"])



