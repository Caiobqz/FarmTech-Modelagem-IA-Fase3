# FarmTech — Comparação técnica inicial de três culturas

**Estado:** cálculos **executados** sobre `Atividade_Cap11_produtos_agricolas(2).csv`; interpretações acadêmicas **pendentes de revisão do aluno**.

**Identificação do CSV utilizado (SHA-256):** `54a5a6e5408668e668667efc50de2fc867c1b875e0431b4f54dd331b0a109a4e`.

Foram selecionadas `coffee` (café), `maize` (milho) e `rice` (arroz). Cada cultura tem **100 registros**. As médias e desvios-padrão foram calculados com pandas sobre os dados recebidos, sem gerar ou alterar linhas.

## Valores médios observados

| Cultura | N | P | K | Temperatura (°C) | Umidade (%) | pH | Precipitação (mm, período não especificado) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Café | 101,20 | 28,74 | 29,94 | 25,54 | 58,87 | 6,79 | 158,07 |
| Milho | 77,76 | 48,44 | 19,79 | 22,39 | 65,09 | 6,25 | 84,77 |
| Arroz | 79,89 | 47,58 | 39,87 | 23,69 | 82,27 | 6,43 | 236,18 |

## Desvios-padrão observados

| Cultura | N | P | K | Temperatura | Umidade | pH | Precipitação |
|---|---:|---:|---:|---:|---:|---:|---:|
| Café | 12,35 | 7,28 | 3,25 | 1,50 | 5,84 | 0,42 | 25,70 |
| Milho | 11,95 | 8,01 | 2,94 | 2,68 | 5,45 | 0,41 | 15,55 |
| Arroz | 11,92 | 7,90 | 2,95 | 2,03 | 1,42 | 0,77 | 34,29 |

**Interpretação metodológica:** essas estatísticas descrevem observações do CSV. Não equivalem a necessidades ideais de cultivo ou a recomendações universais de aplicação de fertilizantes. Não há informação suficiente sobre método, região, época ou unidades específicas de N/P/K para converter essas médias em dose de manejo.

## Atividade reservada ao aluno no notebook

1. Explicar **duas diferenças relevantes** de solo (N, P, K, pH) entre as três culturas, com números.
2. Explicar **duas diferenças de clima** (temperatura, umidade, chuva) e indicar alguma sobreposição.
3. Diferenciar média observada de recomendação agronômica.
4. Registrar essas explicações em Markdown na seção **6. Comparação de três culturas**.

## Como reproduzir os cálculos

Após adicionar o CSV localmente, execute na raiz do projeto:

```powershell
python scripts/diagnostico_pre_modelagem.py "dados/Atividade_Cap11_produtos_agricolas(2).csv"
```

O script também valida a divisão treino/teste, mas **não treina modelos**.
