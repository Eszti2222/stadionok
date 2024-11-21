class Stadion:
    def __init__(self,nev:str="",varos:str="",csapatok_szama:int=0,elso_merk:str="",utolso_merk:str=""):
        self.nev=nev
        self.varos=varos
        self.csapatok_szama=int(csapatok_szama)
        self.elso_merk=elso_merk
        self.utolso_merk=utolso_merk

    def __str__(self):
        return (f"Stadion neve: {self.nev}\n"
                f"Város: {self.varos}\n"
                f"Csapatok száma: {self.csapatok_szama}\n"
                f"Első mérkőzés: {self.elso_merk}\n"
                f"Utolsó mérkőzés: {self.utolso_merk}")
    
