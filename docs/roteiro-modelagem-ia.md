# Roteiro de implementação — Fase 3, Capítulo 11

**Objetivo:** apoiar o aluno a concluir o **único notebook de entrega**, sem substituir as justificativas e a avaliação crítica que ele precisa saber defender.

## Estado em 08/11/2026

- **Executado localmente pelo aluno (evidência por capturas na conversa):** validação do CSV, estatísticas descritivas, histograma de temperatura, boxplot de pH, scatterplot de temperatura × precipitação, heatmap de correlação e barras de nutrientes por cultura.
- **A confirmar:** presença das cinco **interpretações em células Markdown** e a versão mais recente do `.ipynb` salvo em disco.
- **GitHub `main`:** contém rascunho com as duas primeiras células de código executadas. **Não contém ainda os cinco gráficos locais**.
- **Preparado nesta branch:** tabela comparativa das 3 culturas, script de diagnóstico, divisão estratificada e este roteiro.
- **Pendente de implementar pelo aluno com orientação:** seções 6 a 10 do notebook, cinco modelos e avaliação.

## Primeiro: sincronizar o notebook do PC sem perder gráficos

1. No Jupyter, salve o notebook com `Ctrl+S`.
2. Encontre o arquivo `notebooks/rascunho_modelagem_ia.ipynb` **na pasta local que está usando**.
3. Anexe esse `.ipynb` à conversa para revisão. **Não substitua pelo arquivo do GitHub**, pois a `main` ainda não contém os cinco gráficos.
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

- [ ] `.ipynb` local atualizado com as cinco visualizações e interpretações.
- [ ] Tabela e explicação de comparação das 3 culturas.
- [ ] Células de modelagem realmente executadas.
- [ ] Métricas reais e discussão, sem vazamento de dados.
- [ ] Notebook reexecutado da primeira à última célula, sem erros, com outputs salvos.
- [ ] Identificação, RM, capítulo, nome do arquivo e entrega no portal FIAP conferidos.
