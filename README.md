# Análise de Desempenho e Indicadores Socioeducativos do ENEM na Região Nordeste

## 👥 Integrantes
- Rogeane Alves Bezerra
- Heitor Alves Cavalcante
- Miguel Pereira de Sousa Neto

**Instituição:** Faculdade Princesa do Oeste – FPO  
**Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas  
**Disciplina:** Tratamento e Análise de Dados  
**Professor:** Adeilson Sales Aragão

---

## 📌 Descrição do Tema e Objetivo

Este projeto analisa o desempenho dos participantes do ENEM 2024 nos nove estados da Região Nordeste do Brasil, cruzando indicadores de desempenho escolar com o Índice de Desenvolvimento Humano (IDH) de cada estado.

O objetivo é identificar padrões socioeducativos, comparar o desempenho entre os estados e visualizar a distribuição geográfica dos inscritos por meio de um dashboard analítico interativo construído no Power BI.

---

## 🗂️ Estrutura do Repositório

```
dashboard-enem-nordeste/
├── scripts/
│   └── webscraping.py              # Script de coleta de dados do portal INEP
├── apresentacao/
│   └── pitch_deck.pdf              # Apresentação em formato pitch
└── README.md
```

> ⚠️ Os arquivos de dados e o dashboard (.pbix) não estão no repositório pois ultrapassam o limite de tamanho do GitHub (100MB). Acesse pelo link abaixo:

---

## 📁 Arquivos no Google Drive

🔗 [Acessar todos os arquivos do projeto no Google Drive](https://drive.google.com/drive/folders/1epfSySUw6gT0PwcBiTN5a5w7l08uUGsp?usp=sharing)

O Drive contém:
- `dataset_original.csv` — Dados brutos extraídos do INEP
- `dataset_tratado.csv` — Dados tratados e filtrados para o Nordeste
- `projeto_final.pbix` — Dashboard interativo no Power BI

---

## 📥 Fontes de Dados

- **INEP — Microdados do ENEM 2024**  
  Disponível em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

- **IBGE — Índice de Desenvolvimento Humano (IDH) por Estado**  
  Utilizado para cruzamento com os dados de desempenho do ENEM

---

## 🖥️ Como Abrir o Dashboard

1. Instale o **Power BI Desktop** (gratuito): https://powerbi.microsoft.com/pt-br/desktop/
2. Baixe o arquivo `projeto_final.pbix` pelo link do Google Drive acima
3. Abra o Power BI Desktop
4. Vá em **Arquivo → Abrir** e selecione o arquivo `.pbix`
5. O dashboard possui 3 páginas navegáveis: **Visão Geral**, **Análise Geográfica** e **Análise Detalhada**

---
## 📸 Principais Visuais

### Página 1 — Visão Geral
- KPIs: Total de Inscritos (4 milhões), Média Nota Redação (624,59), Percentual de Presença (100%)
- Evolução da média de redação por ano
- Total de inscritos por estado

### Página 2 — Análise Geográfica
- Mapa coroplético com IDH por estado
- Mapa de bolhas com distribuição geográfica dos inscritos

### Página 3 — Análise Detalhada
- Tabela de detalhamento por estado
- Gráfico de dispersão: relação entre IDH e total de inscritos
- Top 3 estados com maior IDH e Bottom 3 com menor IDH

---

## 💡 Principais Insights Encontrados

1. **Ceará possui o maior IDH do Nordeste (735)**, seguido por Rio Grande do Norte (731) e Pernambuco (727)
2. **Piauí possui o menor IDH da região (697)**, seguido por Maranhão (687) e Alagoas (683)
3. A **média da nota de redação no Nordeste foi de 624,59** no ENEM 2024
4. O **percentual de presença na redação foi de 100%** entre os inscritos analisados
5. A distribuição geográfica mostra **maior concentração de inscritos nos estados litorâneos** do Nordeste
6. Estados com maior IDH tendem a apresentar melhores indicadores educacionais, evidenciando a relação entre desenvolvimento humano e desempenho no ENEM

