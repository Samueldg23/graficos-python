# -*- coding: utf-8 -*-
# Um gráfico com 3 séries de memória: Estimada, Usada (Maioria) e Usada (Merge).
# Requisitos: pandas, matplotlib

import io
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path

# =========================
# CONFIGURAÇÕES RÁPIDAS
# =========================
TITLE   = "Uso de Memória — Algoritmos de Ordenação"
X_LABEL = "Tamanho do arquivo (itens)"          # ajuste se quiser
Y_LABEL = "Memória (unidades da planilha)"       # ajuste se quiser
SHOW_LEGEND = True
LEGEND_LOC  = "best"
FORMAT_THOUSANDS_X = True
FORMAT_THOUSANDS_Y = False  # ligue se quiser formatar Y com 100.000

# =========================
# TABELAS COLADAS (pode manter TAB/ESPAÇO/VÍRGULA)
# =========================
DATA_ESTIMADA = """Memória Estimada\tTamanho do Arquivo
390\t100000
625\t160000
859\t220000
1093\t280000
1328\t340000
1562\t400000
1797\t460000
2031\t520000
2266\t580000
2500\t640000
2734\t700000
"""

DATA_USADA_MAIORIA = """Memória Usada\tTamanho do Arquivo
225\t100000
225\t160000
225\t220000
266\t280000
266\t340000
266\t400000
287\t460000
287\t520000
287\t580000
287\t640000
430\t700000
"""

DATA_USADA_MERGE = """Memória Usada\tTamanho do Arquivo
1019\t100000
1249\t160000
1249\t220000
2334\t280000
2314\t340000
2334\t400000
2221\t460000
2314\t520000
4382\t580000
4526\t640000
4546\t700000
"""

# =========================
# CÓDIGO
# =========================
def thousands_ptbr():
    return FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", "."))

def load_xy(text: str, col_y_name: str, col_x_name: str):
    df = pd.read_csv(io.StringIO(text.strip()), sep=None, engine="python")
    # Normaliza nomes de colunas (tira espaços extras)
    df.columns = [c.strip() for c in df.columns]
    if col_y_name not in df.columns or col_x_name not in df.columns:
        raise ValueError(f"Esperado colunas '{col_y_name}' e '{col_x_name}'. Recebi: {list(df.columns)}")
    # Converte para numérico
    df[col_x_name] = pd.to_numeric(df[col_x_name], errors="coerce")
    df[col_y_name] = pd.to_numeric(df[col_y_name], errors="coerce")
    # Ordena por X
    df = df.sort_values(col_x_name).reset_index(drop=True)
    return df[col_x_name].values, df[col_y_name].values

def main():
    x_e, y_e = load_xy(DATA_ESTIMADA, "Memória Estimada", "Tamanho do Arquivo")
    x_m, y_m = load_xy(DATA_USADA_MAIORIA, "Memória Usada", "Tamanho do Arquivo")
    x_q, y_q = load_xy(DATA_USADA_MERGE,   "Memória Usada", "Tamanho do Arquivo")

    # Verificação simples: tamanhos iguais (opcional)
    # Aqui assumimos que os eixos X são equivalentes
    fig, ax = plt.subplots(figsize=(11.69, 8.27))  # A4 paisagem

    # Três séries no mesmo gráfico
    ax.plot(x_e, y_e, marker="o", label="Memória Estimada")
    ax.plot(x_m, y_m, marker="o", label="Memória Usada (Maioria)")
    ax.plot(x_q, y_q, marker="o", label="Memória Usada (Merge)")

    ax.set_title(TITLE)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.grid(True, linestyle=":")

    if SHOW_LEGEND:
        ax.legend(loc=LEGEND_LOC)

    if FORMAT_THOUSANDS_X:
        ax.xaxis.set_major_formatter(thousands_ptbr())
    if FORMAT_THOUSANDS_Y:
        ax.yaxis.set_major_formatter(thousands_ptbr())

    fig.tight_layout()

    # Saídas
    out_png = Path("grafico_memoria.png")
    out_pdf = Path("grafico_memoria.pdf")
    fig.savefig(out_png, dpi=200, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")
    print(f"OK: {out_png.resolve()}")
    print(f"OK: {out_pdf.resolve()}")

if __name__ == "__main__":
    main()
