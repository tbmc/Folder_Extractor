import os
import shutil
import re
import argparse


def extract_folder(dossier, base_dir=os.getcwd(), recursive=False, ext=False, regex=False):
    """
    Permet de déplacer tous les fichiers d'un dossier dans un autre dossier
    :param dossier: Dossier dans lequel chercher les fichiers
    :param base_dir: Dossier dans lequel déplacer les fichiers trouvés
    :param recursive: Chercher dans tous les sous dossier et pas uniquement dans le dossier courrant
    :param ext:
    :param regex:
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


def get_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-R", "--recursive", action="store_true",
                        help="Extrait depuis le dossier courant ainsi que tous \
                        les sous dossiers")
    argument_parser.add_argument("-rm", "--remove", action="store_true",
                        help="Supprime les sous dossiers après en avoir extrait \
                                 les fichiers")
    argument_parser.add_argument("-x", "--regex", type=str,
                        help="Déplace uniquement les fichiers correspondants \
                            à la regex")
    argument_parser.add_argument("-e", "--extension", type=str,
                        help="Déplace uniquement les fichiers ayant l'extension \
                                 passée en paramètre")
    return argument_parser

if __name__ == "__main__":
    print("Extract Folder")
    parser = get_parser()
    args = parser.parse_args()
    print(args)

    print("Déplacelement en cours...")

    base = os.getcwd()
    extract_folder(base, base, recursive=args.recursive, ext=args.extension, regex=args.regex)

    if args.remove:
        remove_sub_folder(base)

    print("Fini")



