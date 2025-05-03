import time
import random
lista = []
for i in range(10000000):
    liczba =  random.randint(0, 999999999)
    lista.append(liczba)
start = time.time()
lista.sort()
end = time.time()

czas = end - start
print("Czas sortowania: ", czas)
