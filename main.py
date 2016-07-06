
import os


def extract_folder(dir, base_dir=os.getcwd(), recursive=False):
    for n in os.listdir(dir):
        print(dir + "/" + n)
        if os.path.isfile(dir + "/" + n):
            if base_dir != dir:
                os.rename(dir + "/" + n, base_dir + "/" + n)
        elif recursive:
            extract_folder(dir + "/" + n, base_dir, recursive)





if __name__ == "__main__":

    print("Salut tout le monde")
    base = 'B:\\The.Big.Bang.Theory.S07.PROPER.VOSTFR.HDTV.XviD-ATeam'
    extract_folder(base, base, True)
