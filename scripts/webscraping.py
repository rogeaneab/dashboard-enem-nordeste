# =============================================================
# Projeto: Análise de Desempenho e Indicadores Socioeducativos
#          do ENEM na Região Nordeste
# Disciplina: Tratamento e Análise de Dados
# Faculdade Princesa do Oeste – FPO
# =============================================================
# Descrição:
# Este script demonstra como automatizar a coleta de dados
# do ENEM disponibilizados pelo INEP (Instituto Nacional de
# Estudos e Pesquisas Educacionais Anísio Teixeira).
#
# Nota: Os dados utilizados neste projeto foram obtidos
# manualmente pelo portal oficial do INEP:
# https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem
# =============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL da página de microdados do ENEM no portal do INEP
URL_INEP = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem"

# Estados da Região Nordeste
ESTADOS_NORDESTE = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]

def coletar_links_inep(url):
    """
    Acessa a página do INEP e coleta os links disponíveis
    para download dos microdados do ENEM.
    """
    print("Acessando portal do INEP...")
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        links = []
        for a in soup.find_all("a", href=True):
            if "enem" in a["href"].lower() and a["href"].endswith(".zip"):
                links.append(a["href"])
        
        print(f"{len(links)} link(s) encontrado(s).")
        return links
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o portal: {e}")
        return []

def filtrar_nordeste(df, coluna_uf="CO_UF_ESC"):
    """
    Filtra o DataFrame mantendo apenas os registros
    dos estados da Região Nordeste.
    """
    print("Filtrando dados da Região Nordeste...")
    df_nordeste = df[df[coluna_uf].isin(ESTADOS_NORDESTE)]
    print(f"{len(df_nordeste)} registros encontrados para o Nordeste.")
    return df_nordeste

def salvar_dados(df, caminho="dados/dataset_original.csv"):
    """
    Salva o DataFrame coletado em formato CSV.
    """
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    df.to_csv(caminho, index=False, encoding="utf-8-sig")
    print(f"Dados salvos em: {caminho}")

if __name__ == "__main__":
    print("=" * 55)
    print("Coleta de Dados — ENEM Região Nordeste")
    print("Fonte: INEP — Microdados do ENEM")
    print("=" * 55)
    
    links = coletar_links_inep(URL_INEP)
    
    if links:
        print("\nLinks disponíveis para download:")
        for link in links:
            print(f"  - {link}")
    else:
        print("\nNenhum link encontrado automaticamente.")
        print("Acesse manualmente: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem")
    
    print("\nScript finalizado.")
    print("Os dados foram coletados manualmente e tratados no Power BI.")
