import matplotlib.pyplot as plt

quantidades = [100000, 160000, 220000, 280000, 340000, 400000,
               460000, 520000, 580000, 640000, 700000]

resultados = [8314.67, 21351.33, 40540, 68047.33, 101844.67, 141419.33, 185215.33, 234717, 298606.33, 361587, 437308.33]

plt.figure(figsize=(10,6))
plt.plot(quantidades, resultados, marker="o", linestyle="-")

plt.title("Decrescente com Repetição Selection")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Resultado (ms)")
plt.grid(True)

plt.show()

plt.savefig("grafico.png", dpi=200, bbox_inches="tight")