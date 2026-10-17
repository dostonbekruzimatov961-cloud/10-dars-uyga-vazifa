from matplotlib import pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, color="red", marker="o")
plt.plot(testlar, guruh_b, color="orange", marker="*")

plt.title("Ikki guruh natijalarini taqqoslash")
plt.xlabel("Testlar")
plt.ylabel("guruhlar ballari")
plt.grid(True)
plt.legend()

plt.show()
