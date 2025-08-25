import matplotlib.pyplot as plt

quantidades = [100000, 160000, 220000, 280000, 340000, 400000,
               460000, 520000, 580000, 640000, 700000]

resultados = [1.67, 2, 2, 1.67, 2.67, 3, 2.33, 3, 3.67, 3.67, 4]

plt.figure(figsize=(10,6))
plt.plot(quantidades, resultados, marker="o", linestyle="-")

plt.title("Crescente Bubble")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Resultado (ms)")
plt.grid(True)

plt.show()

plt.savefig("grafico.png", dpi=200, bbox_inches="tight")