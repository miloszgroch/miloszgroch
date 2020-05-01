import os
from pathlib import Path

def Liczenie(path):
    for folder,folders,files in os.walk(path):
        for file in files:
            if file[-3:]=='.py':
                linijek=0
                with open(Path(folder)/file,'r') as f:
                    for line in f:
                        linijek+=1
                print("Pliki Python:",files)
                print("Linijek Kodu:",linijek)

def test():
    Liczenie(input("Podaj scieżke do zliecznie plików python/linijek kodu"))

if __name__ == ' __main__':
    test()
