billetes = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
tipo_billetes = []
n = len(billetes)

total = 128

cantidad_min_billetes = 0

i = n - 1  

while total > 0 and i >= 0:
    if total >= billetes[i]:
        total -= billetes[i]
        tipo_billetes.append(billetes[i])
        cantidad_min_billetes += 1
    else:
        i -= 1  

print(f"Cantidad total minima de billetes: {cantidad_min_billetes}")

for billete in tipo_billetes:
    print(billete)
