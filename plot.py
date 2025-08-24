import matplotlib.pyplot as plt

quantidades = [100000, 160000, 220000, 280000, 340000, 400000,
               460000, 520000, 580000, 640000, 700000]

resultados = [2, 1.66, 1.66, 2, 1.66, 2, 2.33, 3, 4, 3.66, 4]

plt.figure(figsize=(10,6))
plt.plot(quantidades, resultados, marker="o", linestyle="-")

plt.title("Crescente com Repetição Bubble")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Resultado (ms)")
plt.grid(True)

plt.show()

plt.savefig("grafico.png", dpi=200, bbox_inches="tight")