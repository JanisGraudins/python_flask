FILE_NAME = "data.txt"

def pievienot(saraksts):
    f = open(FILE_NAME, 'a', encoding="utf-8")
    f.write(saraksts + '\n')
    f.close()

def lasitRindinas():
    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        rindinas = f.readlines()

    return rindinas