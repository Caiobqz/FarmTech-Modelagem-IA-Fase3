# Checklist de execução e entrega

## Antes da análise
- [x] Capítulo 11 informado pelo aluno em 08/11/2026; confirmar detalhes formais no portal da FIAP antes da submissão.
- [x] Receber e validar localmente o CSV fornecido; manter o arquivo fora do GitHub até confirmar permissão de republicação.
- [x] CSV foi carregado no ambiente Jupyter do aluno, conforme resultados compartilhados na conversa. Manter uma cópia local em `dados/` e não publicar no GitHub.
- [ ] Confirmar procedência exata, autorização de republicação e contexto geográfico; referência compatível no Kaggle, sem identidade do arquivo comprovada.
- [x] Validar o CSV real fora do notebook: 2.200 linhas, 8 colunas, 22 classes, sem ausentes/duplicatas integrais; verificar tipos e faixas básicas.
- [x] Executar as duas primeiras células de código em Jupyter isolado e salvar suas saídas no notebook; reexecutar no computador do aluno antes da entrega.

## Análise exploratória
- [x] Estatísticas descritivas executadas e sincronizadas no notebook da PR #1.
- [x] Cinco gráficos distintos executados com CSV real e sincronizados na PR #1.
- [x] Rascunhos das interpretações dos Gráficos 1–5 inseridos no notebook, com apoio de IA.
- [ ] **Grupo deve revisar e aprovar** interpretações, números e redação de todos os cinco gráficos antes da entrega.
- [x] Culturas escolhidas: arroz, milho e café. Justificativa de escolha: comparar perfis contrastantes observados no dataset; inserir explicação autoral em Markdown.
- [x] Tabela comparativa de médias e desvios e rascunho de interpretação de arroz, milho e café disponíveis na PR #1.
- [ ] Grupo revisar e aprovar comparação de solo e clima.

## Modelagem
- [x] Definir X (sete variáveis) e y (22 culturas) no notebook.
- [x] Executar treino/teste estratificado: 1.760/440 registros e 80/20 por classe.
- [x] Escalonamento dentro de pipelines e validação cruzada somente no treino, verificado no notebook integrado.
- [x] Cinco algoritmos integrados e treinados com 1.760 exemplos (teste: 440).
- [x] Comparação executada com acurácia, precisão macro, recall macro, F1 macro e CV estratificada no treino.
- [x] Matriz de confusão e relatório detalhado gerados para o modelo selecionado pela CV.
- [x] Rascunho de interpretação de matriz de confusão e dos dois erros do Random Forest inserido.
- [ ] Grupo validar a discussão das métricas e limitações, com base nas saídas.

## Entrega
- [x] Executar todas as células do notebook na ordem no ambiente de validação isolado em 09/11 (15/15). Reexecutar no PC se o grupo editar o conteúdo.
- [x] Ausência de exceções verificada em 09/11; saídas salvas no arquivo reexecutado.
- [x] Revisão técnica das explicações em Markdown concluída e marcadores de rascunho removidos.
- [ ] Aprovação crítica da redação e da conclusão pelo grupo.
- [x] Cinco integrantes e RMs incluídos; fase e capítulo identificados.
- [ ] Nomes completos de Paulo Vitor, Juliana e Cleidimar e nomenclatura oficial do arquivo confirmados com a FIAP.
- [ ] Conferir o arquivo final no portal antes de enviar.

## Situação verificada em 08/11/2026

| Item | Estado | Evidência |
|---|---|---|
| Estrutura do repositório | Implementado | Arquivos conferidos na branch `main` |
| Notebook na PR #1 | Tecnicamente executado, interpretação pendente | 38 células, 15 células de código executadas, 8 imagens de gráficos; sem erros |
| Estrutura e consistência do CSV | Validado externamente ao notebook | Arquivo real lido em 08/11/2026; ver `dados/README.md` |
| CSV no GitHub | Ausente | Pasta `dados/` contém apenas README |
| EDA e 5 gráficos | Sincronizados | Notebook na PR #1, execução com CSV real |
| Três culturas | Cálculos executados; interpretação pendente | `docs/comparacao-tecnica-tres-culturas.md` |
| Preparação técnica de ML | Testada isoladamente | Script de diagnóstico e split estratificado 80/20: 1.760/440 |
| 5 classificadores e métricas | Executados e verificados | CV escolheu Random Forest; teste: 438/440 acertos, F1 macro 0,9955 |
| Notebook integralmente executado e entrega FIAP | Execução técnica concluída; entrega pendente | Interpretar 5 gráficos, comparar culturas, revisar conclusão, autoria e regras do portal |

**Definições de estado:** Planejado = descrito, sem implementação; Implementado = existe no repositório; Executado = rodou com dados reais e gerou saída; Validado = execução e resultados foram revisados.

**Prazo informado pelo aluno:** 11/11/2026. Priorizar análise e modelagem antes de refinamentos extras.

## Preparação complementar em branch de revisão (08/11/2026)

- [x] Script de diagnóstico para conferência de médias, desvios, classes e divisão treino/teste criado sem treinar modelos.
- [x] Critérios para cinco algoritmos e avaliação sem vazamento registrados em `docs/roteiro-modelagem-ia.md`.
- [x] Receber notebook local do aluno, auditar, corrigir duplicação, restaurar Gráfico 3 e sincronizar em PR #1, preservando a `main`.
- [x] Integrar cinco modelos, executar e validar todas as 15 células de código no CSV original.
- [x] Rascunhos de cinco interpretações, comparação, métricas, importância das variáveis e conclusão adicionados à PR #1.
- [ ] Revisar criticamente, adaptar e aprovar redação final pelo grupo.
- [x] Proposta de conclusão registrada para revisão.
- [ ] Aprovar conclusão e referências; conferir integrantes/RMs e formato final da submissão.

## Estado posterior — 09/11/2026: versão candidata à entrega

- [x] Correções de apresentação, rascunhos removidos do notebook principal, preservada a declaração de apoio de IA nas atribuições.
- [x] Notebook reexecutado integralmente com o CSV real; 38 células, 15 de código, 8 saídas gráficas, **zero erros**.
- [x] Modelo selecionado no treino: Random Forest; teste: 438/440, acurácia 99,55% e F1 macro 0,9955.
- [x] Checklist completo para conferência do grupo: `docs/CONFERENCIA_FINAL_2026-11-09.md`.
- [ ] Grupo aprovar os textos, conferir nomes completos, regras da FIAP e enviar o `.ipynb` pelo portal.
- [ ] Confirmar recibo de submissão. PR #1 continua em rascunho, sem merge.
