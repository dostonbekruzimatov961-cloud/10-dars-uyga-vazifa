import matplotlib.pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color='blue')

plt.title("Kunlik tayyorlanish vaqti va test ballari bog'liqligi", fontsize=14)
plt.xlabel("Kunlik tayyorlanish vaqti (soat)", fontsize=12)
plt.ylabel("Test bali", fontsize=12)

plt.grid(True)

plt.show()