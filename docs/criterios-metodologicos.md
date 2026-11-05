# Critérios metodológicos

Este documento registra cuidados para que a análise seja tecnicamente defensável. Ele não substitui a leitura do enunciado nem as decisões justificadas no notebook.

## Problema

A coluna `label` representa uma classe categórica. Portanto, trata-se de classificação, não de regressão.

## Separação dos dados

- Separar treino e teste antes de ajustar transformações ou modelos.
- Usar estratificação para preservar a proporção das classes.
- Ajustar escalonadores somente nos dados de treino, preferencialmente dentro de `Pipeline`.
- Não usar o conjunto de teste para escolher repetidamente hiperparâmetros ou modelos.

## Métricas

Acurácia isolada pode esconder erros por classe. Apresentar precision, recall e F1-score por classe e médias macro/weighted quando pertinente. Explicar o que cada métrica significa no contexto do problema.

## Comparabilidade

Os modelos devem ser avaliados com a mesma divisão de treino/teste. Se houver ajuste de hiperparâmetros, realizá-lo apenas no treino, por validação cruzada.

## Limitações

A base de referência identificada na pesquisa é associada a condições agrícolas da Índia. Mesmo que os modelos obtenham métricas elevadas, isso não comprova desempenho em fazendas brasileiras. A generalização exige dados locais, validação agronômica e avaliação em condições reais.

## Interpretação

Distinguir:
- associação observada no dataset;
- desempenho preditivo no conjunto de teste;
- recomendação agronômica aplicável no mundo real.

Essas três coisas não são equivalentes.
