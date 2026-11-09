# Roteiro de implementação — Fase 3, Capítulo 11

**Objetivo:** apoiar o aluno a concluir o **único notebook de entrega**, sem substituir as justificativas e a avaliação crítica que ele precisa saber defender.

## Estado em 08/11/2026

- **Executado localmente pelo aluno (evidência por capturas na conversa):** validação do CSV, estatísticas descritivas, histograma de temperatura, boxplot de pH, scatterplot de temperatura × precipitação, heatmap de correlação e barras de nutrientes por cultura.
- **Confirmado após upload:** as cinco interpretações estavam ausentes ou incompletas; foram criados campos Markdown marcados como PENDENTE para autoria do aluno.
- **GitHub `main`:** preservada. **PR #1:** notebook revisado com 30 células, cinco gráficos distintos, tabelas descritivas e separação treino/teste executados e saídas salvas.
- **Preparado e testado nesta branch:** tabela comparativa das 3 culturas, script de diagnóstico, divisão estratificada e notebook sincronizado até a Seção 7.
- **Pendente de implementar pelo aluno com orientação:** seções 6 a 10 do notebook, cinco modelos e avaliação.

## Notebook recebido e sincronizado na PR #1 — preservar backup no PC

1. No Jupyter, salve o notebook com `Ctrl+S`.
2. Encontre o arquivo `notebooks/rascunho_modelagem_ia.ipynb` **na pasta local que está usando**.
3. O notebook foi recebido e sua versão corrigida foi sincronizada **na PR #1**, não na `main`. Antes de usar a versão revisada, mantenha backup do arquivo antigo no PC.
4. Compare a execução local antes de atualizar a `main`; nunca use `git reset --hard` neste momento.
5. Mantenha o CSV apenas em `dados/` local; a proteção no `.gitignore` evita commit acidental.

## Seção 6 — Três culturas

Use `rice`, `maize`, `coffee`. Gere uma tabela de médias para N, P, K, `temperature`, `humidity`, `ph`, `rainfall`, apoiando-se no arquivo [comparacao-tecnica-tres-culturas.md](comparacao-tecnica-tres-culturas.md).

**Tarefa de aprendizagem:** escrever suas interpretações em Markdown, sem chamar as médias de necessidades ideais da cultura.

## Seção 7 — Preparação de dados

- **Problema:** classificação multiclasse, porque `label` identifica 22 culturas.
- **X:** as 7 variáveis `N,P,K,temperature,humidity,ph,rainfall`.
- **y:** coluna `label` (não incluir a resposta nas variáveis de entrada).
- Separação recomendada: **80% treino / 20% teste**, `random_state=42`, `stratify=y`.
- Validado com CSV recebido: **1.760 linhas de treino** e **440 linhas de teste**, com **80/20 exemplos por cultura**.
- Qualquer `StandardScaler` deve ser ajustado **somente no treino**, dentro de `Pipeline`.

**Ponto de partida para construir e explicar no Jupyter:**

```python
from sklearn.model_selection import train_test_split
X = dados[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
y = dados["label"]
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
print(X_treino.shape, X_teste.shape)
```

**Exercício:** explique por que `stratify=y` importa e por que não se deve ajustar o escalonador antes da separação.

## Seção 8 — Cinco algoritmos, a implementar com orientação

| Algoritmo | Motivo da escolha | Pipeline |
|---|---|---|
| KNN (`KNeighborsClassifier`) | Vizinhos próximos, sensível à distância | `StandardScaler` + modelo |
| Regressão Logística (`LogisticRegression`) | Referência linear para classificação multiclasse | `StandardScaler` + modelo |
| SVM (`SVC`) | Limites de decisão não lineares | `StandardScaler` + modelo |
| Árvore de Decisão (`DecisionTreeClassifier`) | Regras interpretáveis, risco de sobreajuste | Modelo sem escalonamento |
| Random Forest (`RandomForestClassifier`) | Combina árvores, reduz variância | Modelo sem escalonamento |

**O aluno implementa:** importações dos cinco estimadores, parâmetros razoáveis, `fit` em `X_treino, y_treino`, e `predict` para validação. O assistente revisa cada etapa. Não há resultados de acurácia neste documento.

## Seção 9 — Métricas e escolha

- Para todos os modelos usar a **mesma divisão**.
- `accuracy`, `precision_macro`, `recall_macro` e `f1_macro` para comparar 22 classes; `classification_report` e matriz de confusão para examinar erros por cultura.
- Se houver seleção de hiperparâmetros ou modelo preferido, faça-a por **validação cruzada apenas no treino** (por exemplo `StratifiedKFold`). Reserve o conjunto de teste para a avaliação final.
- Nunca inventar métricas nem atribuir desempenho ao algoritmo sem execução.
- **Tarefa do aluno:** explicar os falsos positivos/falsos negativos de pelo menos uma cultura e identificar a principal limitação do conjunto.

## Seção 10 — Conclusão

Depois de executar os cinco algoritmos, escrever: problema estudado, principais achados das análises, comparação numérica dos modelos, limitações de representatividade da base, e proposta de validação com amostras agrícolas reais.

## Definição de pronto para envio à FIAP

- [x] Notebook com cinco visualizações e saídas salvas na PR #1.
- [ ] Aluno redigir interpretações de cada gráfico em Markdown.
- [x] Tabela comparativa das três culturas executada.
- [ ] Aluno redigir explicação da comparação das culturas.
- [x] Células de modelagem realmente executadas e verificadas.
- [x] Métricas reais e pipelines contra vazamento gerados.
- [ ] Aluno revisar/discutir os resultados de avaliação.
- [x] Notebook reexecutado da primeira à última célula de código, sem erros, com outputs salvos.
- [ ] Reexecutar novamente a versão definitiva após as alterações finais de Markdown.
- [ ] Identificação, RM, capítulo, nome do arquivo e entrega no portal FIAP conferidos.

## Atualização em 09/11/2026 (substitui as pendências históricas de 08/11)

O notebook foi integrado e reexecutado por completo, com cinco modelos, comparação das culturas, interpretações e conclusão redigidas. Foram removidas as marcações provisórias repetidas, preservadas as atribuições e os registros de apoio de IA. Permanecem **pendentes de aprovação humana** os nomes completos, a revisão crítica dos textos e o envio à FIAP. Consulte [CONFERENCIA_FINAL_2026-11-09.md](CONFERENCIA_FINAL_2026-11-09.md). A PR #1 permanece em rascunho sem merge.
