import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st

st.title("Visualizador de Dados de Ações")
ticker = st.text_input("Digite o ticker da ação (ex: PETR4.SA):").strip().upper()
periodo = st.number_input("Digite o periodo em anos", min_value=1, value=1, step=1)

if ticker:
    try:
        periodoy = f"{int(periodo)}y"
        data = yf.download(ticker, period=periodoy)

        if not data.empty:
            st.subheader(f"Dados para {ticker}")
            st.dataframe(data)
        else:
            st.warning(f"Nenhum dado encontrado para o ticker '{ticker}' para o último ano.")

    except Exception as e:
        st.error(f"Ocorreu um erro ao buscar dados para '{ticker}': {e}")

else:
    st.info("Por favor, digite um ticker de ação para visualizar seus dados.")