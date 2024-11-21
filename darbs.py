# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus robežās no 101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.

import random

for _ in range(100): # Izvēlās 100 nejaušus skaitļus 
    random_skaitlis = random.randint(100, 501)# Nejauši skaitļi no 101 līdz 500 
    print(random_skaitlis) # Izvada 100 skaitļus 

