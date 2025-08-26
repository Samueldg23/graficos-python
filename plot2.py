import matplotlib.pyplot as plt

# Quantidades fixas para todos os testes
quantidades = [100000, 160000, 220000, 280000, 340000, 
               400000, 460000, 520000, 580000, 640000, 700000]

# Resultados (seis listas diferentes)
teste1 = [773, 1957.67, 3718.67, 6034.67, 8989.67, 12601, 16425.67, 21166, 26351, 32485.67, 37915.33]
teste2 = [8314.67, 21351.33, 40540, 68047.33, 101844.67, 141419.33, 185215.33, 234717, 298606.33, 361587, 437308.33]
teste3 = [1505.33, 3534.33, 8047.33, 13179.67, 19679, 27433.33, 35944.33, 45938.33, 57094, 68732.67, 83601.67]
teste4 = [767, 1992.67, 3746.67, 6099.67, 9115.33, 12182, 16542.33, 21130, 26517, 32708, 38748.67]
teste5 = [1582.67, 3904.33, 7858.33, 13003.67, 19477, 26630, 35744.67, 45723.67, 56393, 67600, 82656]
teste6 = [1432.67, 3689, 8028.33, 13199.67, 19389, 27055, 35137.33, 45761.33, 56354.67, 69504, 82117]

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
