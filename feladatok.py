from Stadion import Stadion
import faljbeolvas
from  datetime import datetime

def elso(stadionok_lista):
    i:int=0
    newyork_db=0
    while(i<len(stadionok_lista)):
        if(stadionok_lista[i].varos=="New York"):
            newyork_db+=1
        i+=1
    return newyork_db

def masodik(stadionok_lista):
    ossz_csapatszam:int=0
    for i in range(0,len(stadionok_lista),1):
        if(stadionok_lista[i].csapatok_szama!=0):
            ossz_csapatszam+=stadionok_lista[i].csapatok_szama
    return ossz_csapatszam

def harmadik(stadionok_lista):
    elso_merk_1900_elott_lista=[]
    
    for i in range(0,len(stadionok_lista),1):
        korabbi_merk=stadionok_lista[i].elso_merk
        datum=datetime.strptime("1900-01-01","%Y-%m-%d")
        if(korabbi_merk<datum):
            elso_merk_1900_elott_lista.append(stadionok_lista[i].nev)
    return elso_merk_1900_elott_lista

def negyedik(stadionok_lista):
    datum=datetime.strptime("2000-01-01","%Y-%m-%d")
    db:int=0
    for i in range(0,len(stadionok_lista),1):
        if(stadionok_lista[i].utolso_merk<datum):
            db+=1
    return db

"""def otodik(stadionok_lista):
    for i in range(0,len(stadionok_lista),1):
        if(stadionok_lista[i].)"""