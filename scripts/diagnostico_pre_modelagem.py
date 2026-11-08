"""Verifica dataset e prepara uma divisão de treino/teste, sem treinar modelos.

Uso (a partir da raiz do projeto):
    python scripts/diagnostico_pre_modelagem.py "dados/Atividade_Cap11_produtos_agricolas(2).csv"

O arquivo CSV permanece local, não deve ser publicado sem conferir a licença.
"""
from pathlib import Path
import argparse
import hashlib

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

VARIAVEIS = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
CULTURAS = ["rice", "maize", "coffee"]


def executar(caminho: Path) -> None:
    if not caminho.is_file():
        raise FileNotFoundError(f"CSV não encontrado: {caminho}")
    dados = pd.read_csv(caminho)
    esperadas = set(VARIAVEIS + ["label"])
    if set(dados.columns) != esperadas:
        raise ValueError(
            f"Colunas inválidas. Faltando: {sorted(esperadas - set(dados.columns))}; "
            f"extras: {sorted(set(dados.columns) - esperadas)}"
        )
    for coluna in VARIAVEIS:
        dados[coluna] = pd.to_numeric(dados[coluna], errors="raise")
    if dados.isna().any().any():
        raise ValueError("Há valores ausentes.")
    if not np.isfinite(dados[VARIAVEIS].to_numpy()).all():
        raise ValueError("Há valores numéricos não finitos.")
    if dados.duplicated().any():
        raise ValueError("Há linhas completamente duplicadas.")
    if not set(CULTURAS).issubset(set(dados["label"].unique())):
        raise ValueError("Falta ao menos uma das três culturas selecionadas.")

    arquivo_hash = hashlib.sha256(caminho.read_bytes()).hexdigest()
    print(f"Arquivo local: {caminho.name}")
    print(f"SHA-256: {arquivo_hash}")
    print(f"Dimensões: {dados.shape}, classes: {dados['label'].nunique()}")
    print("\nMédias das três culturas (valores observados):")
    medias = (
        dados.loc[dados["label"].isin(CULTURAS)]
        .groupby("label")[VARIAVEIS].mean().round(2)
    )
    print(medias.to_string())
    print("\nDesvios-padrão das três culturas:")
    desvios = (
        dados.loc[dados["label"].isin(CULTURAS)]
        .groupby("label")[VARIAVEIS].std().round(2)
    )
    print(desvios.to_string())

    # A coluna categórica label é o alvo, e não deve entrar nas entradas X.
    X = dados[VARIAVEIS]
    y = dados["label"]
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\nTreino: {X_treino.shape[0]} registros; teste: {X_teste.shape[0]} registros")
    print("Quantidade por classe (treino):", sorted(y_treino.value_counts().unique()))
    print("Quantidade por classe (teste):", sorted(y_teste.value_counts().unique()))
    print("Nenhum modelo treinado ou selecionado por este diagnóstico.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path, help="Caminho para o CSV local")
    parametros = parser.parse_args()
    executar(parametros.csv)
