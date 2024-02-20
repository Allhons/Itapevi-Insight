import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("Datasets\cruzamento_eleitorado-pais_2022_sudeste_sp_itapevi_359.csv")
df_local_votacao = pd.read_csv("Datasets\cruzamento_eleitorado-pais_2022_sudeste_sp_itapevi.csv")
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

fig_idade = px.histogram(df, 
                         x="Eleitorado",
                         y="Faixa etária",
                         color = "Gênero",
                         title= 'Faixa Etária')
col1.plotly_chart(fig_idade, use_container_width=True)

fig_educacao = px.bar(df,
                      x="Escolaridade",
                      y="Eleitorado",
                      color="Gênero",
                      title="Educação")
col3.plotly_chart(fig_educacao, use_container_width=True)
 
fig_local_votacao = px.bar(df_local_votacao,
                           x="Local de votação",
                           y="Eleitorado",
                           title="Local de Votação")
col5.plotly_chart(fig_local_votacao, use_container_width=True)

fig_estado_civil = px.pie(df,
                          values="Eleitorado",
                          names="Estado civil",
                          title="Estado Civil")
col4.plotly_chart(fig_estado_civil, use_container_width=True)

fig_genero = px.pie(df,
                    values="Eleitorado",
                    names="Gênero",
                    title="Gênero",)
col2.plotly_chart(fig_genero, use_container_width=True)