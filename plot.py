import matplotlib.pyplot as plt

quantidades = [100000, 160000, 220000, 280000, 340000, 400000,
               460000, 520000, 580000, 640000, 700000]

resultados = [3, 3, 3.33, 4, 4.67, 4.33, 5, 6, 6.67, 6.67, 7]

plt.figure(figsize=(10,6))
plt.plot(quantidades, resultados, marker="o", linestyle="-")

plt.title("Crescente Insertion")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Resultado (ms)")
plt.grid(True)

plt.show()

plt.savefig("grafico.png", dpi=200, bbox_inches="tight")