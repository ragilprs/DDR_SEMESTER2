makanan = ["Nasi uduk", "Nasi goreng", "Ayam geprek"]
minuman = ["Es teh", "Susu", "Mizone"]

print(makanan)
print(minuman)

print(minuman[1])
print(len(minuman))

minuman[1] = "Energen"
print(minuman)
del minuman[1]
print(minuman)
makanan.append("chicken katsu")
print(makanan)