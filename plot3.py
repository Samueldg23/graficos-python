# -*- coding: utf-8 -*-
# Gera UM gráfico (Heap Sort) a partir da tabela colada.
# Requisitos: pandas, matplotlib

import io
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# =========================
# CONFIGURAÇÕES RÁPIDAS
# =========================
ALGO_NAME   = "Heap Sort"                  # Título do gráfico e base do nome do arquivo
X_LABEL     = "Tamanho do arquivo (itens)" # Texto do eixo X
Y_LABEL     = "Tempo (ms)"                 # Texto do eixo Y

SHOW_LEGEND = True                         # Mostrar legenda?
LEGEND_LOC  = "best"                       # "best", "upper left", "lower right", etc.
LEGEND_NCOL = 2                            # Nº de colunas na legenda

DASHED_FOR_NO_REP = True                   # Tracejado para séries "sem repetição"
FORMAT_THOUSANDS_X = True                  # Milhares no eixo X como 100.000
FORMAT_THOUSANDS_Y = False                 # Ative se quiser formatação de milhares no Y

# =========================
# SUA TABELA (colada abaixo)
# Cabeçalho esperado: Tamanho,Cres_Rep,Dec_Rep,Ale_Rep,Cres,Dec,Ale
# =========================
DATA_TEXT = """Tamanho	Cres_Rep	Dec_Rep	Ale_Rep	Cres	Dec	Ale
100000	12	15	18	13	14	15
160000	16	19	22	17	19	20
220000	22	24	28	26	24	31
280000	24	28	35	30	27	38
340000	27	34	44	36	29	42
400000	32	38	53	40	35	49
460000	37	43	60	42	42	56
520000	42	45	66	45	50	66
580000	46	50	76	49	54	75
640000	50	55	83	53	58	78
700000	53	60	92	57	64	87
"""

# =========================
# CÓDIGO (não precisa alterar)
# =========================
EXPECTED = ["Tamanho","Cres_Rep","Dec_Rep","Ale_Rep","Cres","Dec","Ale"]

def thousands_ptbr():
    return FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", "."))

def load_df_from_text(text: str) -> pd.DataFrame:
    df = pd.read_csv(io.StringIO(text), sep=None, engine="python")
    missing = [c for c in EXPECTED if c not in df.columns]
    if missing:
        raise ValueError(f"Colunas ausentes: {missing}. Esperado: {EXPECTED}")
    df = df[EXPECTED].copy()
    for col in EXPECTED:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.sort_values("Tamanho").reset_index(drop=True)
    return df

def plot_one(df: pd.DataFrame, algo: str):
    fig, ax = plt.subplots(figsize=(11.69, 8.27))  # A4 paisagem

    # Com repetição (linhas contínuas)
    ax.plot(df["Tamanho"], df["Cres_Rep"], marker="o", label="Crescente (Rep)")
    ax.plot(df["Tamanho"], df["Dec_Rep"],  marker="o", label="Decrescente (Rep)")
    ax.plot(df["Tamanho"], df["Ale_Rep"],  marker="o", label="Aleatório (Rep)")

    # Sem repetição (tracejado opcional)
    ls = "--" if DASHED_FOR_NO_REP else "-"
    ax.plot(df["Tamanho"], df["Cres"], linestyle=ls, marker="o", label="Crescente (Sem Rep)")
    ax.plot(df["Tamanho"], df["Dec"],  linestyle=ls, marker="o", label="Decrescente (Sem Rep)")
    ax.plot(df["Tamanho"], df["Ale"],  linestyle=ls, marker="o", label="Aleatório (Sem Rep)")

    ax.set_title(algo)
    ax.set_xlabel(X_LABEL)
    ax.set_ylabel(Y_LABEL)
    ax.grid(True, linestyle=":")

    if SHOW_LEGEND:
        ax.legend(loc=LEGEND_LOC, ncol=LEGEND_NCOL, fontsize=9)

    if FORMAT_THOUSANDS_X:
        ax.xaxis.set_major_formatter(thousands_ptbr())
    if FORMAT_THOUSANDS_Y:
        ax.yaxis.set_major_formatter(thousands_ptbr())

    fig.tight_layout()
    return fig

def main():
    df = load_df_from_text(DATA_TEXT)
    fig = plot_one(df, ALGO_NAME)

    slug = ALGO_NAME.lower().replace(" ", "_")
    out_png = Path(f"grafico_{slug}.png")
    out_pdf = Path(f"grafico_{slug}.pdf")
    fig.savefig(out_png, dpi=200, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")
    print(f"OK: {out_png.resolve()}")
    print(f"OK: {out_pdf.resolve()}")

if __name__ == "__main__":
    main()
