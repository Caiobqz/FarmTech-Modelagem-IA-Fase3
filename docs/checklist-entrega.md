# Checklist de execução e entrega

## Antes da análise
- [x] Capítulo 11 informado pelo aluno em 08/11/2026; confirmar detalhes formais no portal da FIAP antes da submissão.
- [x] Receber e validar localmente o CSV fornecido; manter o arquivo fora do GitHub até confirmar permissão de republicação.
- [ ] Colocar uma única cópia do CSV na pasta local `dados/` para executar o notebook.
- [ ] Confirmar procedência exata, autorização de republicação e contexto geográfico; referência compatível no Kaggle, sem identidade do arquivo comprovada.
- [x] Validar o CSV real fora do notebook: 2.200 linhas, 8 colunas, 22 classes, sem ausentes/duplicatas integrais; verificar tipos e faixas básicas.
- [x] Executar as duas primeiras células de código em Jupyter isolado e salvar suas saídas no notebook; reexecutar no computador do aluno antes da entrega.

## Análise exploratória
- [ ] Calcular estatísticas descritivas.
- [ ] Criar pelo menos cinco gráficos diferentes.
- [ ] Escrever uma interpretação própria para cada gráfico.
- [ ] Escolher três culturas e justificar a seleção.
- [ ] Comparar as características observadas sem transformar médias em recomendações universais.

## Modelagem
- [ ] Definir X e y.
- [ ] Criar treino e teste com estratificação.
- [ ] Evitar vazamento de dados usando pipelines.
- [ ] Treinar cinco algoritmos diferentes.
- [ ] Comparar accuracy, precision, recall e F1-score.
- [ ] Analisar matriz de confusão e limitações.

## Entrega
- [ ] Executar todas as células do notebook na ordem.
- [ ] Remover erros e saídas desatualizadas.
- [ ] Conferir explicações em Markdown.
- [ ] Confirmar nome do arquivo, RM, fase e capítulo.
- [ ] Conferir o arquivo final no portal antes de enviar.

## Situação verificada em 08/11/2026

| Item | Estado | Evidência |
|---|---|---|
| Estrutura do repositório | Implementado | Arquivos conferidos na branch `main` |
| Rascunho do notebook | Parcialmente executado | 19 células; primeiras duas células de código executadas com o CSV real e saídas salvas; demais cinco células de código sem execução |
| Estrutura e consistência do CSV | Validado externamente ao notebook | Arquivo real lido em 08/11/2026; ver `dados/README.md` |
| CSV no GitHub | Ausente | Pasta `dados/` contém apenas README |
| EDA, 5 gráficos, 3 culturas | Planejado | Código ainda não implementado |
| 5 classificadores e métricas | Planejado | Código ainda não implementado |
| Notebook integralmente executado e entrega FIAP | Pendente | Apenas as duas primeiras células de código têm evidências de execução |

**Definições de estado:** Planejado = descrito, sem implementação; Implementado = existe no repositório; Executado = rodou com dados reais e gerou saída; Validado = execução e resultados foram revisados.

**Prazo informado pelo aluno:** 11/11/2026. Priorizar análise e modelagem antes de refinamentos extras.
