from matplotlib import pyplot
 
kunlar = [1, 2, 3, 4, 5, 6, 7]
harorat = [18, 20, 17, 23, 25, 22, 27]

pyplot.plot(kunlar, harorat, marker="o")

pyplot.title("Haftalik haroratlar")
pyplot.xlabel("Hafta kunlari")
pyplot.ylabel("Temperatura (°C)")

pyplot.grid(True)

pyplot.show()