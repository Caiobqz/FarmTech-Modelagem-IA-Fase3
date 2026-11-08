# Checklist de execução e entrega

## Antes da análise
- [x] Capítulo 11 informado pelo aluno em 08/11/2026; confirmar detalhes formais no portal da FIAP antes da submissão.
- [ ] Adicionar o CSV à pasta `dados/`.
- [ ] Registrar a fonte, a licença e o contexto da base.
- [ ] Reexecutar no notebook a validação de colunas, dimensões, tipos, ausências, duplicatas e classes (resultados anteriores relatados: 2.200 linhas, 8 colunas, 22 classes, sem ausentes/duplicatas integrais).

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
| Rascunho do notebook | Parcialmente implementado | 19 células; importação e checagem inicial codificadas, sem execução |
| Estatísticas anteriores do dataset | Relatado, não validado nesta sessão | Resumo de validação anterior do aluno |
| CSV no GitHub | Ausente | Pasta `dados/` contém apenas README |
| EDA, 5 gráficos, 3 culturas | Planejado | Código ainda não implementado |
| 5 classificadores e métricas | Planejado | Código ainda não implementado |
| Notebook executado e entrega FIAP | Pendente | Evidências não disponíveis |

**Definições de estado:** Planejado = descrito, sem implementação; Implementado = existe no repositório; Executado = rodou com dados reais e gerou saída; Validado = execução e resultados foram revisados.

**Prazo informado pelo aluno:** 11/11/2026. Priorizar análise e modelagem antes de refinamentos extras.
