# Dados

Coloque nesta pasta o arquivo CSV utilizado no trabalho.

## Arquivo esperado

O enunciado menciona `produtos_agricolas.csv`. A base de referência localizada durante a pesquisa possui nome original `Crop_recommendation.csv`. Não renomeie nem declare uma origem FIAP sem confirmar que o conteúdo é o mesmo.

Antes de usar a base, confira:
- colunas `N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall` e `label`;
- quantidade de linhas e classes;
- valores ausentes, duplicados e tipos;
- origem, licença e contexto geográfico dos dados.

Se a base vier do Kaggle, registre a fonte real e suas limitações no notebook. Não use aqui arquivos de outras atividades que tenham estrutura ou objetivo diferentes.

## Validação técnica executada em 08/11/2026

Arquivo analisado **localmente**, anexado pelo aluno: `Atividade_Cap11_produtos_agricolas(2).csv`. Não foi publicado neste repositório.

| Verificação | Resultado executado |
|---|---:|
| Registros | 2.200 |
| Colunas | 8 |
| Variáveis numéricas | 7 |
| Classes de cultura (`label`) | 22 |
| Registros por cultura | 100 (todas as classes) |
| Valores ausentes | 0 |
| Linhas totalmente duplicadas | 0 |
| Valores numéricos infinitos | 0 |
| Nutrientes negativos | 0 |
| Umidade fora de 0–100% | 0 |
| pH fora de 0–14 | 0 |
| Precipitação negativa | 0 |

Colunas conferidas: `N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall`, `label`.

**SHA-256 da versão recebida:** `54a5a6e5408668e668667efc50de2fc867c1b875e0431b4f54dd331b0a109a4e`

A verificação acima é **executada e validada quanto à estrutura e consistência básica**, não é prova de representatividade nem de adequação agronômica.

### Origem e republicação

O arquivo foi disponibilizado ao aluno como material de aula. O conjunto público [Crop Recommendation Dataset (Atharva Ingle, Kaggle)](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) apresenta estrutura, tamanho e classes compatíveis, e a página pública informa licença **Apache 2.0**. **Isso não estabelece identidade exata de versão nem a cadeia de origem do arquivo recebido.** Antes de disponibilizar o CSV publicamente, confirmar se é uma cópia inalterada e seguir os termos aplicáveis. O conjunto público informa ter sido construído a partir de fontes referentes à Índia; não extrapolar resultados para o Brasil sem validação local.

**Uso recomendado:** mantenha o CSV em `dados/` apenas na máquina de execução. O `.gitignore` bloqueia `dados/*.csv` para evitar publicação acidental.

**Reprodução no notebook:** pendente. A célula de validação foi implementada, mas ainda não há saída executada registrada no `.ipynb`.
