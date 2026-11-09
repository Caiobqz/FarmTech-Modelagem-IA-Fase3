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
- [ ] Escrever uma interpretação própria para cada gráfico.
- [x] Culturas escolhidas: arroz, milho e café. Justificativa de escolha: comparar perfis contrastantes observados no dataset; inserir explicação autoral em Markdown.
- [x] Tabela de médias e desvios das três culturas executada e sincronizada; interpretação acadêmica do aluno pendente.

## Modelagem
- [x] Definir X (sete variáveis) e y (22 culturas) no notebook.
- [x] Executar treino/teste estratificado: 1.760/440 registros e 80/20 por classe.
- [x] Escalonamento dentro de pipelines e validação cruzada somente no treino, verificado no notebook integrado.
- [x] Cinco algoritmos integrados e treinados com 1.760 exemplos (teste: 440).
- [x] Comparação executada com acurácia, precisão macro, recall macro, F1 macro e CV estratificada no treino.
- [x] Matriz de confusão e relatório detalhado gerados para o modelo selecionado pela CV.
- [ ] Aluno interpretar a matriz, explicar os dois erros do Random Forest e discutir limitações do dataset.

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
- [ ] Redigir e revisar interpretações dos 5 gráficos, da comparação das 3 culturas e das métricas.
- [ ] Finalizar conclusão e referências; conferir integrantes/RMs e formato final da submissão.
