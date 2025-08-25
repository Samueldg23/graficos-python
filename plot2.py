import matplotlib.pyplot as plt

# Quantidades fixas para todos os testes
quantidades = [100000, 160000, 220000, 280000, 340000, 
               400000, 460000, 520000, 580000, 640000, 700000]

# Resultados (seis listas diferentes)
teste1 = [2, 1.66, 1.66, 2, 1.66, 2, 2.33, 3, 4, 3.66, 4]
teste2 = [5947, 15248.67, 28556.67, 46504, 68145.67, 93915.67, 124907.67, 158450.33, 197389, 241573.33, 289267.33]
teste3 = [11589.67, 29971.67, 57255.67, 91301.67, 134965, 188919.33, 250789, 322756.33, 403829.33, 489199.67, 590302.33]
teste4 = [1.67, 2, 2, 1.67, 2.67, 3, 2.33, 3, 3.67, 3.67, 4]
teste5 = [2450.67, 6095.67, 11349, 18477, 27249, 39417, 50247.67, 65064, 81184.33, 98374.67, 120811]
teste6 = [11661.33, 30058.33, 56572.33, 93203.33, 136220.67, 189999.67, 251888.33, 322201.33, 398261, 493085.67, 588799.33]

# Plot
plt.figure(figsize=(12,7))

plt.plot(quantidades, teste1, marker="o", label="Cres_Rep")
plt.plot(quantidades, teste2, marker="o", label="Dec_Rep")
plt.plot(quantidades, teste3, marker="o", label="Ale_Rep")
plt.plot(quantidades, teste4, marker="o", label="Cres")
plt.plot(quantidades, teste5, marker="o", label="Dec")
plt.plot(quantidades, teste6, marker="o", label="Ale")

plt.title("Comparação dos Algoritmos")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Tempo (ms)")
plt.legend()
plt.grid(True)

plt.savefig("comparacao.png", dpi=200, bbox_inches="tight")
plt.show()
