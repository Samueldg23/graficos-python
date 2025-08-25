import matplotlib.pyplot as plt

# Quantidades fixas para todos os testes
quantidades = [100000, 160000, 220000, 280000, 340000, 
               400000, 460000, 520000, 580000, 640000, 700000]

# Resultados (seis listas diferentes)
teste1 = [3, 2.67, 4, 4, 5, 4.67, 5, 5.33, 5.33, 7.33, 7]
teste2 = [3364, 8446.33, 15825.67, 25856, 38723.67, 56675.67, 73222.67, 95292.67, 121156.33, 144801.33, 177415]
teste3 = [1712.33, 4368, 7144.67, 13457.67, 19878.33, 28208.33, 32583.33, 47125, 58504.67, 72076.33, 75177.67]
teste4 = [3, 3, 3.33, 4, 4.67, 4.33, 5, 6, 6.67, 6.67, 7]
teste5 = [2450.67, 6095.67, 11349, 18477, 27249, 39417, 50247.67, 65064, 81184.33, 98374.67, 120811]
teste6 = [11661.33, 30058.33, 56572.33, 93203.33, 136220.67, 189999.67, 251888.33, 322201.33, 398261, 493085.67, 588799.33]

# Plot
plt.figure(figsize=(12,7))

plt.plot(quantidades, teste1, marker="o", label="Cres_Rep")
plt.plot(quantidades, teste2, marker="o", label="Dec_Rep")
plt.plot(quantidades, teste3, marker="o", label="Ale_Rep")
plt.plot(quantidades, teste4, marker="o", label="Cres")
plt.plot(quantidades, teste5, marker="o", label="Dec")
plt.plot(quantidades, teste6, marker="o", label="Ale ")

plt.title("Comparação dos Algoritmos")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Tempo (ms)")
plt.legend()
plt.grid(True)

plt.savefig("comparacao.png", dpi=200, bbox_inches="tight")
plt.show()
