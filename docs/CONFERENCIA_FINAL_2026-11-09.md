# FarmTech — Fase 3, Capítulo 11 | Conferência antes da entrega

**Status:** versão tecnicamente validada em 09/11/2026; **aprovação acadêmica do grupo e envio à FIAP ainda não confirmados**. Prazo informado: **11/11/2026**.

## O que foi realmente testado

- [x] CSV fornecido como material da professora, SHA-256 `54a5a6e5408668e668667efc50de2fc867c1b875e0431b4f54dd331b0a109a4e`.
- [x] Notebook com **38 células (15 de código)**; execução integral de **15/15** células sem exceções no ambiente de validação em 09/11.
- [x] **Cinco gráficos exploratórios** com interpretação; tabelas de comparação de arroz, milho e café.
- [x] **Cinco modelos de classificação** com validação cruzada estratificada somente no treino (80%); teste separado (20%).
- [x] Matrizes/relatório, tabelas de métricas e importância das variáveis; **oito saídas gráficas** salvas no notebook.
- [x] Selecionado por CV no treino: **Random Forest**; em 440 casos de teste, **438 acertos (99,55% de acurácia; F1 macro 0,9955)**. Dois erros: `blackgram → maize` e `rice → jute`.
- [x] Saídas preservadas e rótulos editoriais de rascunho repetidos removidos da versão candidata à entrega.
- [x] Referências qualificam o dataset público do Kaggle apenas como *compatível*, sem afirmar que é o arquivo original da professora.
- [x] CSV não incluído no GitHub nem no arquivo `.ipynb`.

## O que só os integrantes podem confirmar

- [ ] **Grafia e nomes completos:** os registros fornecidos são Caio Barros Queiroz (RM 576443), Paulo Vitor (RM 575580), Kauê Araujo (RM 576394), Juliana (RM 579614) e Cleidimar (RM 576009). *Os nomes completos de Paulo Vitor, Juliana e Cleidimar ainda não foram confirmados*. Verificar no portal da FIAP antes da entrega.
- [ ] Ler os textos sobre cinco gráficos, culturas, métricas e conclusão e aprovar/adaptar com compreensão. A redação teve apoio de IA e os resultados devem ser compreendidos e assumidos pelo grupo.
- [ ] Confirmar o **enunciado e barema completos** no portal, incluindo requisitos de identificação, arquivo e anexos. Não há confirmação atual do portal.
- [ ] Confirmar que a referência de dados está corretamente declarada como arquivo de aula e que não há necessidade de republicar o CSV. A procedência e a licença original **não estão comprovadas**.
- [ ] Abrir a versão **`FarmTech_Fase3_Modelagem_IA_PARA_CONFERENCIA.ipynb`** na pasta local `notebooks/` com uma cópia do CSV em `../dados/`. Reexecutar todas as células após quaisquer edições de nome/texto/código; salvar as saídas e verificar ausência de erros.
- [ ] Confirmar se os demais integrantes precisam enviar individualmente ou se um envio representa o grupo. Não inferir regras da FIAP.
- [ ] Fazer backup e enviar o `.ipynb` correto na atividade **antes do prazo de 11/11/2026**; verificar recibo ou confirmação de submissão no portal.
- [ ] Somente depois da revisão, aprovar a PR #1 ou decidir como sincronizar a `main`. O merge não substitui a submissão na FIAP.

## Perguntas rápidas para o grupo conseguir defender os resultados

1. Por que `stratify=y` mantém 80 exemplos por cultura no treino e 20 no teste?
2. Por que `StandardScaler` fica dentro do pipeline e não é ajustado com o conjunto inteiro?
3. O que é F1 macro, e por que dois erros em 440 casos não garantem generalização para propriedades brasileiras?
4. Por que o Random Forest foi selecionado pela validação cruzada do treino, e não pelos resultados do teste?
5. Qual a diferença entre a média observada de nutrientes e a recomendação agronômica de adubação?

**Nota:** execução técnica não significa aprovação de conteúdo acadêmico nem prova de entrega. O grupo precisa confirmar os itens pendentes.