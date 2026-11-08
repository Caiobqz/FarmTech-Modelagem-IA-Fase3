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

O CSV da atividade, recebido como `Atividade_Cap11_produtos_agricolas(2).csv`, foi verificado localmente em 08/11/2026, mas **não está versionado** em `dados/`. A origem primária/condições de redistribuição precisam ser confirmadas antes de publicá-lo. A estrutura validada corresponde às colunas:

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
- [x] CSV recebido e auditado localmente; sem publicação até confirmar procedência e licença
- [x] Validação técnica externa ao notebook executada com o CSV real em 08/11/2026
- [ ] Validação reproduzida pelo aluno no notebook e saídas salvas
- [ ] Notebook desenvolvido e executado
- [ ] Resultados revisados
- [ ] Entrega acadêmica conferida

## Validação do dataset em 08/11/2026

O arquivo recebido foi verificado por leitura real de CSV: **2.200 registros**, **8 colunas**, **22 culturas**, **100 registros por cultura**, **0 valores ausentes** e **0 duplicatas integrais**. A consistência de tipos, a finitude dos valores numéricos e faixas físicas elementares também foram conferidas. Consulte [dados/README.md](dados/README.md) para o SHA-256, alcance da validação e nota de procedência.

O notebook em `notebooks/rascunho_modelagem_ia.ipynb` possui 19 células. A importação e a validação inicial foram **implementadas**, mas **a execução com saídas salvas no notebook permanece pendente**. Estatísticas interpretadas, gráficos, treinamento e conclusão serão desenvolvidos pelo aluno durante a orientação.
