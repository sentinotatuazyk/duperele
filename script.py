import time
import random
lista = []
print("Tworzenie listy")
start0 = time.time()
for i in range(10000000):
    liczba =  random.randint(0, 999999999)
    lista.append(liczba)
end0 = time.time()
print("#################")
print("Stortowanie")
start1 = time.time()
lista.sort()
end1 = time.time()

czas = end0 - start0 + end1 - start1
print("#################")
print("Czas tworzenia listy: ", end0 - start0)
print("Czas sortowania: ", end1 - start1)
print("Czas ogolny: ", czas)

