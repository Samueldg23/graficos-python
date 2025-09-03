# -*- coding: utf-8 -*-
# TODOS OS ALGORITMOS EM UM ÚNICO GRÁFICO (com legendas de cores, repetição e ordem)
# Requisitos: pandas, matplotlib

import io
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter

# =========================
# CONFIGURAÇÕES RÁPIDAS
# =========================
TITLE = "Desempenho dos Algoritmos — Todas as Séries"
X_LABEL = "Tamanho do arquivo (itens)"
Y_LABEL = "Tempo (ms)"

USE_LOG_Y = False          # True deixa Y em escala log
FORMAT_MILHAR_X = True     # 100.000 no eixo X
OUT_PNG = Path("todos_algoritmos_um_grafico.png")
OUT_PDF = Path("todos_algoritmos_um_grafico.pdf")

# =========================
# DADOS EMBUTIDOS
# =========================
ALGORITHMS = {
    "Bubble Sort": """Tamanho,Cres_Rep,Dec_Rep,Ale_Rep,Cres,Dec,Ale
100000,2,5947,11590,2,2451,11661
160000,2,15133,29972,2,6096,30058
220000,2,28524,57256,2,11349,56572
280000,1,46279,91302,2,18477,93203
340000,2,68146,134965,3,27249,136221
400000,2,93916,188919,3,39417,190000
460000,3,124070,250789,2,50248,251888
520000,3,158246,322756,3,65064,322201
580000,4,197231,403829,4,80218,398261
640000,5,241573,483522,4,97943,489941
700000,5,289267,580031,4,117913,581970
""",

    "Insertion Sort": """Tamanho,Cres_Rep,Dec_Rep,Ale_Rep,Cres,Dec,Ale
100000,3,3022,1544,2,3077,1626
160000,3,7730,3896,3,7709,3910
220000,4,14894,7220,3,14756,7246
280000,4,24867,13317,4,23875,12387
340000,5,35297,19788,5,35101,18456
400000,5,49583,24371,4,50182,24250
460000,5,66935,32583,5,67149,32096
520000,5,85368,47125,6,87524,42340
580000,7,108594,57759,7,107317,51840
640000,7,132422,72076,7,130918,63344
700000,8,160955,75178,7,158083,76481
""",

    "Selection Sort": """Tamanho,Cres_Rep,Dec_Rep,Ale_Rep,Cres,Dec,Ale
100000,773,8251,1505,767,1583,1433
160000,1958,21228,3524,1993,3904,3689
220000,3719,40540,7249,3747,7858,6569
280000,6035,65716,13180,6097,12891,10987
340000,8990,98280,19447,9115,19477,19110
400000,12532,135025,26767,12182,26510,26836
460000,16414,177478,34132,16542,35745,34843
520000,21166,220622,45031,21130,45113,44461
580000,26328,276288,55737,26517,51068,54939
640000,32347,335242,68137,32708,60918,68406
700000,37915,402328,80929,38749,73461,79314
""",

    "Merge Sort": """Tamanho,Cres_Rep,Dec_Rep,Ale_Rep,Cres,Dec,Ale
100000,15,13,18,14,13,16
160000,22,19,31,20,17,31
220000,25,25,36,24,20,35
280000,28,32,41,26,26,44
340000,31,34,50,30,27,49
400000,34,37,60,34,34,56
460000,36,43,65,43,39,65
520000,43,51,75,47,41,73
580000,47,53,82,52,44,78
640000,54,55,86,56,49,89
700000,57,59,94,61,52,93
""",

    "Quick Sort": """Tamanho,Cres_Rep,Dec_Rep,Ale_Rep,Cres,Dec,Ale
100000,8,11,21,7,11,20
160000,14,15,24,10,14,24
220000,18,17,26,15,19,29
280000,20,18,31,15,22,32
340000,19,20,35,17,21,36
400000,21,21,40,19,22,41
460000,24,23,42,21,27,49
520000,26,26,48,22,27,51
580000,28,25,56,27,30,54
640000,30,29,62,31,32,60
700000,34,30,66,33,33,65
""",

    "Heap Sort": """Tamanho,Cres_Rep,Dec_Rep,Ale_Rep,Cres,Dec,Ale
100000,12,15,18,13,14,15
160000,16,19,22,17,19,20
220000,22,24,28,26,24,31
280000,24,28,35,30,27,38
340000,27,34,44,36,29,42
400000,32,38,53,40,35,49
460000,37,43,60,42,42,56
520000,42,45,66,45,50,66
580000,46,50,76,49,54,75
640000,50,55,83,53,58,78
700000,53,60,92,57,64,87
"""
}

# =========================
# AUXILIARES
# =========================
def thousands_ptbr(val: float) -> str:
    try:
        return f"{int(val):,}".replace(",", ".")
    except:
        return str(val)

def read_algo_df(csv_text: str) -> pd.DataFrame:
    df = pd.read_csv(io.StringIO(csv_text.strip()))
    exp = ["Tamanho","Cres_Rep","Dec_Rep","Ale_Rep","Cres","Dec","Ale"]
    missing = [c for c in exp if c not in df.columns]
    if missing:
        raise ValueError(f"Faltam colunas {missing}. Esperado: {exp}")
    return df[exp].sort_values("Tamanho")

order_to_marker = {
    "Cres_Rep": ("Crescente (Rep)", "^-"),
    "Dec_Rep":  ("Decrescente (Rep)", "s-"),
    "Ale_Rep":  ("Aleatório (Rep)", "o-"),
    "Cres":     ("Crescente (Sem Rep)", "^--"),
    "Dec":      ("Decrescente (Sem Rep)", "s--"),
    "Ale":      ("Aleatório (Sem Rep)", "o--"),
}

# =========================
# PLOT
# =========================
fig, ax = plt.subplots(figsize=(12.5, 7.5))
handles_algos = []

for algo, csv_text in ALGORITHMS.items():
    df = read_algo_df(csv_text)
    color = None
    for j, key in enumerate(["Cres_Rep","Dec_Rep","Ale_Rep","Cres","Dec","Ale"]):
        label, style = order_to_marker[key]
        marker = style[0]
        lstyle = style[1:]
        if j == 0:
            line, = ax.plot(df["Tamanho"], df[key], linestyle=lstyle, marker=marker,
                            label=f"{algo} — {label}")
            color = line.get_color()
        else:
            ax.plot(df["Tamanho"], df[key], linestyle=lstyle, marker=marker, color=color,
                    label=f"{algo} — {label}")
    handles_algos.append(Line2D([0],[0], color=color, lw=2, label=algo))

# Legenda 1: Algoritmos (cores)
leg_alg = fig.legend(handles=handles_algos, title="Algoritmos",
                    loc="upper center", bbox_to_anchor=(0.5, 0.98),
                    ncol=3, frameon=True)

# Legenda 2: Repetição (traços)
handles_rep = [
    Line2D([0],[0], color="black", lw=2, linestyle="-",  label="Com repetição"),
    Line2D([0],[0], color="black", lw=2, linestyle="--", label="Sem repetição"),
]
leg_rep = ax.legend(handles=handles_rep, title="Repetição", loc="upper left", frameon=True)
ax.add_artist(leg_rep)

# Legenda 3: Ordem (marcadores)
handles_ordem = [
    Line2D([0],[0], color="black", lw=0, marker="^", label="Crescente"),
    Line2D([0],[0], color="black", lw=0, marker="s", label="Decrescente"),
    Line2D([0],[0], color="black", lw=0, marker="o", label="Aleatório"),
]
leg_ord = ax.legend(handles=handles_ordem, title="Ordem Inicial", loc="upper right", frameon=True)

# Título/Eixos
ax.set_title(TITLE)
ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
ax.grid(True, linestyle=":")

if USE_LOG_Y:
    ax.set_yscale("log")
if FORMAT_MILHAR_X:
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: thousands_ptbr(x)))

fig.tight_layout(rect=[0, 0, 1, 0.90])

fig.savefig(OUT_PNG, dpi=200, bbox_inches="tight")
fig.savefig(OUT_PDF, bbox_inches="tight")
print(f"OK: {OUT_PNG.resolve()}")
print(f"OK: {OUT_PDF.resolve()}")
