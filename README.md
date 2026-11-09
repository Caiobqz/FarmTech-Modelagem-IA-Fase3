# FarmTech Solutions — Modelagem de IA (Fase 3)

Projeto acadêmico de análise exploratória e modelagem preditiva para recomendação de culturas agrícolas utilizando Machine Learning.

## Estrutura do repositório

```text
FarmTech-Modelagem-IA-Fase3/
├── dados/
│   └── README.md
├── notebooks/
│   ├── README.md
│   └── rascunho_modelagem_ia.ipynb
├── scripts/
│   └── diagnostico_pre_modelagem.py
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

## Identificação da atividade

- **Instituição:** FIAP
- **Fase:** 3
- **Capítulo:** 11 — Modelagem de IA
- **Prazo informado:** 11/11/2026
- **Integrantes do grupo:**
  - Caio Barros Queiroz — RM 576443
  - Paulo Vitor — RM 575580
  - Kauê Araujo — RM 576394
  - Julliana Silva Furtado — RM 576914
  - Cleidimar — RM 576009

> **Registro acadêmico:** os nomes e RMs foram informados pelo aluno; os nomes completos de Paulo Vitor e Cleidimar não foram verificados diretamente na base da FIAP.

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

O notebook principal está em `notebooks/rascunho_modelagem_ia.ipynb` e contém:
1. Carregamento e validação dos dados;
2. Análise exploratória e descritiva;
3. Pelo menos cinco visualizações com interpretação;
4. Comparação do perfil de três culturas;
5. Treinamento e avaliação de cinco algoritmos de classificação;
6. Discussão dos resultados, pontos fortes e limitações.

O notebook possui células de código executadas e explicações em Markdown. O aluno confirmou a entrega acadêmica em 09/11/2026.

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
- [x] Notebook com estatísticas, cinco gráficos, comparação de culturas e divisão treino/teste executados na PR #1
- [x] Notebook executado integralmente e saídas preservadas na versão final (validação isolada)
- [x] Notebook integrado: 38 células, 15 de código executadas sem erros, com cinco classificadores e métricas
- [x] Resultados técnicos conferidos em ambiente isolado em 09/11/2026 (Random Forest: 438/440, F1 macro 0,9955)
- [x] Textos acadêmicos revisados tecnicamente; a aprovação individual de cada integrante não foi auditada
- [x] Envio à FIAP informado como concluído pelo aluno em 09/11/2026 (comprovante não acessado)

## Validação do dataset em 08/11/2026

O arquivo recebido foi verificado por leitura real de CSV: **2.200 registros**, **8 colunas**, **22 culturas**, **100 registros por cultura**, **0 valores ausentes** e **0 duplicatas integrais**. A consistência de tipos, a finitude dos valores numéricos e faixas físicas elementares também foram conferidas. Consulte [dados/README.md](dados/README.md) para o SHA-256, alcance da validação e nota de procedência.

O notebook integrado na PR #1 contém **38 células (15 de código)**, todas as células de código executadas com o CSV real, oito visualizações com saídas salvas, cinco classificadores e métricas. O modelo selecionado pela validação cruzada no treino foi Random Forest; no teste obteve 438/440 acertos (acurácia de 99,55%, F1 macro 0,9955). **As interpretações e a conclusão foram redigidas e revisadas tecnicamente.** A PR #1 foi integrada à `main`; o CSV público não foi alterado nem publicado. A aprovação individual do grupo não foi verificada.

## Versão de entrega — 09/11/2026

O notebook integrado foi reexecutado integralmente com o CSV fornecido, sem erros e com as saídas salvas. O arquivo `notebooks/rascunho_modelagem_ia.ipynb` foi incorporado à `main` pela PR #1. O checklist histórico de conferência está em [docs/CONFERENCIA_FINAL_2026-11-09.md](docs/CONFERENCIA_FINAL_2026-11-09.md). O CSV não foi publicado no GitHub.

## Encerramento

- A PR #1 foi integrada à `main` em 09/11/2026.
- O aluno confirmou que entregou a atividade à FIAP em 09/11/2026.
- O notebook do GitHub possui 38 células e 15 células de código com resultados executados; repositório sem CSV por restrição de redistribuição.

## Atualização do Capítulo 11 — 09/11/2026 (correção de entrega)

O enunciado oficial exige nome e RM no nome do arquivo, perfil de solo e clima para três culturas, cinco gráficos e cinco algoritmos. A versão atualizada para consulta pública está em:

- [notebooks/CaioBarrosQueiroz_RM576443_fase3_cap11.ipynb](notebooks/CaioBarrosQueiroz_RM576443_fase3_cap11.ipynb) — **41 células, 16 de código executadas, sem erros salvos**, com uma seção de perfil empírico (mediana e quartis) para arroz, milho e café.

**Diferença importante:** esta é a versão pública, que carrega o CSV original de forma local (`dados/`, pasta do notebook ou diretório pai). O arquivo individual preparado para **submissão privada à FIAP** tem uma cópia compactada dos dados anexada ao próprio notebook, para permitir a reexecução sem arquivos adicionais. **Essa cópia privada não foi publicada no GitHub**, pois não foi confirmada a autorização de redistribuição pública do CSV.

Em 09/11/2026, a versão individual foi executada isoladamente em uma pasta vazia, com 16/16 células de código sem erros. A substituição efetiva do arquivo no portal depende de confirmação do aluno.
