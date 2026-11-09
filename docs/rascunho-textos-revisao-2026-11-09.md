# FarmTech — Textos acadêmicos para revisão do grupo

**Status:** RASCUNHO, não enviar à FIAP sem revisão. Base: notebook integrado executado e CSV fornecido como material de aula (SHA-256 `54a5a6e5408668e668667efc50de2fc867c1b875e0431b4f54dd331b0a109a4e`).

## O que foi preservado

- 38 células, 15 células de código executadas e 8 saídas gráficas; código, métricas e imagens originais preservados sem alterações.
- Interpretação do Gráfico 1 anterior preservada.
- O conjunto CSV **não** está incluído nesses arquivos.

---

## Gráfico 2 — Distribuição do pH

### Interpretação do Gráfico 2 — Distribuição do pH

> **Rascunho para revisão do grupo (redação assistida por IA):** verificar os dados, ajustar a linguagem e aprovar antes da entrega.

O boxplot mostra que o pH do solo apresenta mediana aproximada de **6,43**, com metade central dos registros entre **5,97 e 6,92** (primeiro e terceiro quartis). Também há observações fora do intervalo esperado pelos limites do boxplot, tanto com pH mais baixo quanto mais alto. Esses pontos são considerados atípicos do ponto de vista estatístico, mas não podem ser classificados automaticamente como erros de medição. Como os dados reúnem **22 culturas diferentes**, a distribuição geral não permite definir uma faixa de pH ideal para todas elas; essa avaliação exigiria uma análise por cultura e informações agronômicas adicionais.

---

## Gráfico 3 — Temperatura e precipitação

### Interpretação do Gráfico 3 — Temperatura × precipitação

> **Rascunho para revisão do grupo (redação assistida por IA):** verificar os dados, ajustar a linguagem e aprovar antes da entrega.

Ao comparar **arroz, milho e café** no gráfico de dispersão, observam-se diferenças mais evidentes na precipitação registrada do que na temperatura, embora existam sobreposições entre as culturas. No conjunto analisado, o **arroz** apresenta precipitação média de **236,18 mm**, seguido pelo **café**, com **158,07 mm**, e pelo **milho**, com **84,77 mm**. As temperaturas médias são **23,69 °C** para arroz, **25,54 °C** para café e **22,39 °C** para milho. A proximidade entre parte das temperaturas mostra que essa variável, isoladamente, não separa completamente as culturas. O gráfico identifica padrões presentes na amostra, mas não comprova causalidade nem define exigências ideais de cultivo; o período de referência da precipitação também não está especificado no CSV.

---

## Gráfico 4 — Correlações

### Interpretação do Gráfico 4 — Mapa de calor

> **Rascunho para revisão do grupo (redação assistida por IA):** verificar os dados, ajustar a linguagem e aprovar antes da entrega.

O mapa de calor apresenta as **correlações lineares** entre as sete variáveis numéricas da base. A associação positiva mais destacada é entre **fósforo (P) e potássio (K)**, com coeficiente aproximado de **+0,74**, indicando que valores maiores de uma dessas variáveis tendem a acompanhar valores maiores da outra no conjunto de dados. A relação entre **nitrogênio (N) e fósforo (P)** é negativa e fraca, aproximadamente **−0,23**. Esses coeficientes não demonstram que uma variável cause alterações na outra. Além disso, por considerar as 22 culturas em conjunto, o mapa pode misturar diferenças entre culturas e ocultar relações específicas que apareceriam em análises separadas.

---

## Gráfico 5 — Nutrientes por cultura

### Interpretação do Gráfico 5 — Nutrientes por cultura

> **Rascunho para revisão do grupo (redação assistida por IA):** verificar os dados, ajustar a linguagem e aprovar antes da entrega.

As médias de **N, P e K** diferem entre as três culturas selecionadas. O **café** apresenta a maior média de nitrogênio (**101,20**), acima do **arroz (79,89)** e do **milho (77,76)**. Para fósforo, o **milho (48,44)** e o **arroz (47,58)** têm médias próximas, enquanto o café apresenta **28,74**. Já o **arroz** possui a maior média de potássio (**39,87**), seguido do **café (29,94)** e do **milho (19,79)**. Portanto, as médias de potássio **não são equivalentes** entre as culturas. Os valores representam registros do dataset, não doses recomendadas de adubação; as unidades específicas dos nutrientes e o contexto de manejo não estão documentados no arquivo.

---

## Comparação de três culturas — solo e clima

## 6. Comparação de três culturas

> **Rascunho para revisão do grupo (redação assistida por IA):** verificar os dados, ajustar a linguagem e aprovar antes da entrega.

Foram selecionados **arroz (`rice`), milho (`maize`) e café (`coffee`)**, com **100 registros por cultura**, para comparar perfis contrastantes de nutrientes do solo e condições climáticas presentes no conjunto de dados. As médias e os desvios-padrão da tabela abaixo descrevem as observações; **não representam condições universalmente ideais de plantio**.

**Solo e nutrientes.** O café apresenta média de **N = 101,20**, acima do arroz (**79,89**) e do milho (**77,76**). Para **K**, a maior média ocorre no arroz (**39,87**) e a menor no milho (**19,79**). O milho possui média de **P = 48,44**, próxima da observada no arroz (**47,58**), mas acima da do café (**28,74**). As médias de **pH** também variam: **6,79** no café, **6,43** no arroz e **6,25** no milho.

**Clima.** O arroz tem maior umidade média (**82,27%**) e precipitação média (**236,18 mm**) na amostra; o café apresenta **58,87%** e **158,07 mm**, e o milho, **65,09%** e **84,77 mm**. A temperatura média é maior no café (**25,54 °C**), seguida por arroz (**23,69 °C**) e milho (**22,39 °C**). Como algumas faixas de temperatura se sobrepõem, a interpretação deve considerar diferentes variáveis em conjunto. O CSV não especifica o período a que se referem os valores de precipitação.

**Limitação da comparação.** As médias refletem somente os registros disponíveis. Sem confirmação da procedência, da região, das unidades exatas de N/P/K e das condições de produção, não é possível convertê-las em recomendações de fertilizantes ou generalizá-las para lavouras brasileiras.

---

## Divisão treino/teste — justificativa

**Justificativa da preparação dos dados — rascunho para revisão do grupo:**

A divisão com `stratify=y` preserva a proporção de cada uma das **22 culturas** no treino e no teste. Como há **100 exemplos por classe**, a separação de **80%/20%** gera **80 exemplos de treinamento e 20 de teste por cultura**. Isso evita que a separação aleatória deixe alguma classe desproporcionalmente representada.

A padronização das variáveis deve ser ajustada apenas sobre os dados de treinamento, pois calcular média e desvio-padrão com o conjunto completo permitiria que informações do teste influenciassem o pré-processamento. O `StandardScaler` é usado dentro de `Pipeline` para que cada partição da validação cruzada aprenda suas transformações somente com a parte de treino.

---

## Discussão dos modelos e erros

### Discussão dos resultados e dos erros

> **Rascunho para revisão do grupo (redação assistida por IA):** verificar os dados, ajustar a linguagem e aprovar antes da entrega.

A seleção do modelo foi realizada pelo **F1 macro médio em validação cruzada estratificada com cinco partições**, utilizando somente os dados de treinamento. O algoritmo selecionado foi o **Random Forest**. Na avaliação final, ele acertou **438 dos 440 exemplos de teste**, alcançando **acurácia de 99,55%** e **F1 macro de 0,9955**. O relatório de classificação e a matriz de confusão revelaram **dois erros**: um registro de **`blackgram`** foi classificado como **`maize`**, e um registro de **`rice`** foi classificado como **`jute`**. Não há evidências suficientes para afirmar que essas duas confusões sejam sistemáticas.

As métricas mostram bom desempenho **nessa divisão específica do dataset**, mas não garantem o mesmo resultado fora da amostra. O conjunto contém 100 registros por cultura e sua procedência primária não foi confirmada; também não há validação independente por região, safra ou propriedade. Acurácia elevada em dados de aula não equivale a validação agronômica nem assegura desempenho em propriedades brasileiras.

---

## Importância das variáveis

### Interpretação da importância das variáveis

> **Rascunho para revisão do grupo (redação assistida por IA):** verificar os dados, ajustar a linguagem e aprovar antes da entrega.

No Random Forest, as maiores importâncias relativas calculadas por redução de impureza foram **precipitação (`rainfall`: 0,2196)** e **umidade (`humidity`: 0,2171)**, seguidas por **potássio (`K`: 0,1808)** e **fósforo (`P`: 0,1513)**. Esse resultado sugere que, nesta base, essas variáveis contribuíram mais para as decisões das árvores. A análise exploratória também mostrou diferenças expressivas de precipitação entre arroz, café e milho. Entretanto, a medida de importância **não demonstra causalidade**, não permite afirmar uma necessidade agronômica universal e pode sofrer vieses do próprio método baseado em árvores.

---

## Conclusão acadêmica — proposta

## 10. Conclusão acadêmica — RASCUNHO PARA REVISÃO DO GRUPO

Este trabalho analisou um conjunto de **2.200 registros de 22 culturas agrícolas** com sete atributos numéricos de solo e clima, buscando compreender padrões nos dados e comparar algoritmos de classificação multiclasse. A análise exploratória mostrou concentração de temperaturas aproximadamente entre **23 °C e 30 °C**, pH mediano de **6,43** e associação positiva entre fósforo e potássio (**r ≈ 0,74**). A comparação de arroz, milho e café revelou diferenças nos nutrientes e nas condições climáticas registradas, especialmente nas médias de precipitação e umidade.

Foram avaliados **Regressão Logística, KNN, Árvore de Decisão, Random Forest e SVM**, mantendo a mesma divisão estratificada de **1.760 registros para treino e 440 para teste**. A seleção por validação cruzada ocorreu somente no treinamento, e o **Random Forest** foi o modelo escolhido. No teste, obteve **99,55% de acurácia** e **F1 macro de 0,9955**, com dois erros de classificação. Esses números indicam bom desempenho neste experimento, sem comprovar que o algoritmo seja necessariamente o melhor em outros conjuntos.

Como limitações, destacam-se a **origem primária ainda não confirmada do CSV**, a ausência de informações completas sobre região, período e coleta dos dados e a falta de avaliação com amostras externas de propriedades agrícolas brasileiras. As saídas do classificador devem ser entendidas como **predições experimentais de classes**, e não como recomendações agronômicas prontas para uso. Uma continuidade apropriada seria testar o método com dados locais, documentados e validados por profissionais da área, além de verificar estabilidade entre diferentes períodos e regiões.

> **Antes da entrega:** o grupo deve revisar criticamente esta conclusão, verificar as referências e conferir as regras de autoria e identificação acadêmica da FIAP.

---

## Checklist de aprovação antes da entrega

- [ ] Revisar o Gráfico 1 já redigido anteriormente.
- [ ] Conferir números e compreensão das interpretações dos Gráficos 2 a 5.
- [ ] Revisar e, se necessário, reformular comparação de arroz, milho e café.
- [ ] Entender e validar divisão estratificada, pipelines, F1 macro e matriz de confusão.
- [ ] Confirmar autoria e contribuições do grupo, nomes/RMs e capítulo/fase exigidos.
- [ ] Verificar enunciado, referências e formato de submissão no portal FIAP.
- [ ] Reexecutar notebook de ponta a ponta no computador antes de entregar; conferir saídas.
- [ ] Enviar `.ipynb` final ao portal e confirmar recebimento antes de 11/11/2026.