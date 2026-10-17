from matplotlib import pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

bars = plt.bar(ismlar, ballar, color="red")
plt.bar_label(bars)
plt.title("O'quvchilar natijalari tahlili")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")
plt.grid(True)

print(f"Eng yuqori ball: {max(ballar)}")
print(f"Eng past ball: {min(ballar)}")
ortacha = max(ballar)/len(ballar)
print("Ortacha ball: ", ortacha)

plt.savefig("oquvchilar_natijasi.png")

# Eng yuqori ball = Aziza 95 ball
# Eng past ball = Jasur 73 ball