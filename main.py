from Stadion import Stadion
import faljbeolvas

stadion=faljbeolvas.beolvas("stadionok.txt",[])
for i in range(0,len(stadion),1):
  
    print(f"Első stadion neve: {stadion[0]}")