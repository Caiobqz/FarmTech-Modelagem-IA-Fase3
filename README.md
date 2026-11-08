# FarmTech Solutions — Modelagem de IA (Fase 3)

Projeto acadêmico de análise exploratória e modelagem preditiva para recomendação de culturas agrícolas utilizando Machine Learning.

## Estrutura do repositório

```text
FarmTech-Modelagem-IA-Fase3/
├── dados/
│   └── README.md
├── notebooks/
│   └── README.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Identificação da atividade

- **Instituição:** FIAP
- **Fase:** 3
- **Capítulo:** 11 — Modelagem de IA
- **Aluno:** Caio Barros Queiroz — RM 576443
- **Prazo informado:** 11/11/2026

## Objetivo

Analisar dados de nutrientes do solo e condições climáticas para estudar a relação entre essas variáveis e a cultura agrícola indicada (`label`). O trabalho contempla análise exploratória, visualizações, comparação de culturas e avaliação de modelos de classificação.

## Dados

O arquivo CSV da atividade (recebido pelo aluno com o nome `Atividade_Cap11_produtos_agricolas(1).csv`) ainda não está versionado em `dados/`. A origem e a autorização de redistribuição precisam ser verificadas antes de publicá-lo. Antes de qualquer análise, será necessário validar se o arquivo corresponde às colunas esperadas:

- `N`, `P`, `K`
- `temperature`, `humidity`, `ph`, `rainfall`
- `label` (variável-alvo)

**Importante:** não considerar automaticamente qualquer base anterior da FarmTech como equivalente. A base estatística municipal usada em outra atividade possui finalidade e estrutura diferentes.

Consulte [dados/README.md](dados/README.md) para instruções de origem e organização.

## Notebook

O notebook principal ficará em `notebooks/`. Ele deverá conter:
1. Carregamento e validação dos dados;
2. Análise exploratória e descritiva;
3. Pelo menos cinco visualizações com interpretação;
4. Comparação do perfil de três culturas;
5. Treinamento e avaliação de cinco algoritmos de classificação;
6. Discussão dos resultados, pontos fortes e limitações.

O notebook final deverá ser entregue com as células executadas e explicações em Markdown.

## Ambiente

As bibliotecas iniciais estão listadas em [requirements.txt](requirements.txt).

Para instalar:

```bash
python -m pip install -r requirements.txt
```

## Limitações e responsabilidade

As recomendações obtidas por modelos dependem da origem, qualidade e representatividade dos dados. Resultados de uma base de referência não devem ser tratados como recomendação agronômica universal ou como validação para condições brasileiras sem dados locais e avaliação especializada.

## Status

- [x] Repositório inicial criado
- [x] Estrutura de diretórios preparada
- [ ] CSV incluído no repositório (publicação condicionada à origem/licença)
- [ ] Validação do CSV reproduzida no notebook (resultados anteriores relatados, ainda não reexecutados)
- [ ] Notebook desenvolvido e executado
- [ ] Resultados revisados
- [ ] Entrega acadêmica conferida

## Validação anterior do dataset (registro histórico)

Segundo os resultados da verificação anterior relatados pelo aluno: **2.200 registros**, **8 colunas**, **22 culturas**, **100 registros por cultura**, **0 valores ausentes** e **0 linhas totalmente duplicadas**. Esses resultados ainda não foram reexecutados nesta atualização porque o CSV não está disponível no repositório. Veja [dados/README.md](dados/README.md).

O notebook em `notebooks/rascunho_modelagem_ia.ipynb` contém somente a estrutura (19 células). Análises, treinamento, gráficos e conclusões permanecem **planejados**, não executados ou validados.
