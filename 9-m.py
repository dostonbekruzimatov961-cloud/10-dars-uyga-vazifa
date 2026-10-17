from matplotlib import pyplot as plt

mashinalar = ["Nexia", "Captiva", "Cobalt", "Gentra", "Matiz", "Malibu", "Onix"]
benzin_sarfi = [10, 19, 9, 16, 7, 20, 8]

plt.plot(mashinalar, benzin_sarfi, marker="o")
plt.title("Mashinalar benzin sarfi")
plt.xlabel("Avtomobil markasi")
plt.ylabel("Benzin sarfi")
plt.grid(True)

plt.savefig("natija.png")
plt.show()