# Verificação técnica — 08/11/2026

## Escopo

Arquivo recebido pelo aluno como `Atividade_Cap11_produtos_agricolas(2).csv`, fornecido para a atividade de Modelagem de IA (FIAP, Fase 3, Capítulo 11).

A verificação foi realizada **com a cópia anexada na conversa, não com dados publicados neste repositório**.

## Integridade e dados

- SHA-256: `54a5a6e5408668e668667efc50de2fc867c1b875e0431b4f54dd331b0a109a4e`.
- Formato: CSV UTF-8, cabeçalho legível.
- Dimensões: 2.200 linhas × 8 colunas.
- Tipos: `N`, `P`, `K` inteiros; `temperature`, `humidity`, `ph`, `rainfall` reais; `label` texto.
- 22 culturas; todas com 100 linhas cada.
- Ausências: 0; duplicatas completas: 0; linhas com atributos repetidos (sem `label`): 0.
- Valores numéricos não finitos: 0.
- Faixas básicas: nenhum nutriente negativo, nenhuma umidade fora de 0–100%, nenhum pH fora de 0–14 e nenhuma precipitação negativa.

Esses testes verificam **consistência estrutural básica**, não autenticidade do conjunto, qualidade experimental, generalização ou aplicabilidade agronômica.

## Teste isolado da rotina de leitura

A rotina de descoberta e leitura do CSV inserida no rascunho do notebook foi reproduzida em ambiente local com o arquivo real, sem executar as seções futuras de análise e modelagem.

| Cenário | Resultado |
|---|---|
| Notebook iniciado a partir da raiz do projeto, CSV em `dados/` | Leitura correta; 2.200 × 8; 22 classes |
| Notebook iniciado a partir de `notebooks/`, CSV em `../dados/` | Leitura correta; 2.200 × 8; 22 classes |
| CSV não encontrado | `FileNotFoundError` conforme esperado |
| Duas cópias do CSV | `ValueError` para evitar escolha silenciosa |

**Limite:** o arquivo completo `.ipynb` ainda não foi executado e salvo com saídas; o teste descrito acima é da lógica de leitura em isolamento.

## Proveniência

A página pública [Crop Recommendation Dataset — Atharva Ingle, Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) descreve 2.200 linhas, 22 culturas, campos compatíveis e licença Apache 2.0, mas não foi demonstrada igualdade binária com o anexo. A autorização de redistribuição do arquivo recebido deve ser confirmada antes de torná-lo público. Não publicar o CSV por padrão.

## Etapas acadêmicas pendentes

1. Executar no Jupyter a célula de carregamento e salvar as saídas.
2. Calcular e interpretar estatísticas descritivas.
3. Criar cinco gráficos com explicações escritas.
4. Comparar três culturas escolhidas e justificar os critérios.
5. Preparar dados, treinar cinco classificadores e avaliar métricas sem vazamento treino/teste.
6. Concluir, registrar limitações, executar o notebook integralmente e conferir a submissão em 11/11/2026.

**Estados:** validação externa do CSV = executado/validado; rotina de leitura = implementada/testada isoladamente; execução integral do notebook = pendente; análises e modelos = planejados.
