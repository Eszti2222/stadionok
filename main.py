from Stadion import Stadion
import faljbeolvas
import feladatok

stadion=faljbeolvas.beolvas("stadionok.txt",[])
for i in range(0,len(stadion),1):
  
    print(f"Első stadion neve: {stadion[0]}")

""""print("1. Összesen hány stadion van New Yorkban? ")
newyork_db=feladatok.elso(stadion)
print(f"Összesen {newyork_db} db stadion van New York-ban.\n")

print("2. Mennyi az összes csapatszám? ")
ossz_csapatszam=feladatok.masodik(stadion)
print(f"Az összes csapatszám: {ossz_csapatszam}.\n")

print("3. listázd ki azokat a stadionokat, amelyekben  1900.01.01 előtt volt az első mérkőzésük!")
elso_merk_1900_elott_lista=feladatok.harmadik(stadion)
print(f"Az 1900-nál korábbi mérkőzések:\n {elso_merk_1900_elott_lista}.\n")"""

print("4. Hány olyan stadion van, amelyben 200 óta nem volt mérkőzés?")
db=feladatok.negyedik(stadion)
print(f"{db} olyan stadion van, emelyben nem volt mérkőzés 2000 óta.\n")

"""print("5. Összesen hány csapat játszott Buffalo - ban?")
feladatok.otodik()"""