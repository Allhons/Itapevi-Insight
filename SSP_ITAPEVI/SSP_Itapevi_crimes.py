import folium
import pandas as pd
import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(layout="wide",
                   page_title="Mapa Criminal Itapevi",
                   page_icon="SSP_ITAPEVI/Itapevi_insights.ico")

    st.sidebar.image("ENEM_ITAPEVI_2022/Logo_sem_nada.png", caption="")

    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #05AAF1;
        }
        [data-testid=stAppViewBlockContainer]{
            background-color: #FFFFFF;
        }
    </style>
    """, unsafe_allow_html=True)


    with st.container():
        st.subheader("Itapevi Insights", "Itapevi_insights.ico")
        

        st.write("""Seja bem vindo(a) ao Itapevi Insights, aqui nos transformamos dados em informações!!\\
                Caso queira nos conhecer melhor acesse as nossas redes sociais:\\
                ***Instagram***: [Itapevi Insights](https://www.instagram.com/itapevi.insights?igsh=dDAyMXdqN2tpZnJq)\\
                ***Twitter***: [Itapevi Insights](https://x.com/itapevi_insight?s=11)
                """)
        
        st.sidebar.header(" Filtro de Ocorrência para o Gráfico Mapa")

    with st.container():
        ("---")
        st.markdown("## Sumário")
        st.write("""
                1° - Grafico mapa sobre a Segurança publica de Itapevi.\\
                2° - Análise geral dos bairros de Itapevi.
                """)
        
        
    with st.container():
        ("---")
        st.markdown("## Grafico mapa sobre Segurança Pública de Itapevi")
        st.write("""
                Aqui nós criamos um gráfico mapa intuitiuvo e dinâmico.O nosso intuito é que quando as pessoas vejam esse grafico consigam visualizar as regiões onde acontecem os casos.\\
                \\
                Para visuzlizar as Informações no mapa basta filtrar no filtro a esquerda o caso que você deseja ver.\\
                Esse gráfico está alimentado com dados da ultima versão de Dados Criminais divulgados pela SSP de 2023.
                """)
        
        df = pd.read_excel("SSP_ITAPEVI/SSP_itapevi.xlsx")

        df['LATITUDE'] = pd.to_numeric(df['LATITUDE'], errors='coerce') 
        df['LONGITUDE'] = pd.to_numeric(df['LONGITUDE'], errors='coerce')

        df=df.dropna(subset=['LATITUDE'])
        df=df.dropna(subset=['LONGITUDE'])

        ocorrencias =st.sidebar.multiselect("Ocorrência",
                                        options=df["NATUREZA_APURADA"].unique(),
                                        placeholder="Escolha uma ocorrência",
                                        default=None)

        df_filtro = df[df["NATUREZA_APURADA"].isin(ocorrencias)]

        mapa_itapevi = folium.Map(location=[-23.550792893857476, -46.93904384692045],
                        zoom_start=14)

        Grupo_1 = folium.FeatureGroup("APREENSÃO DE ENTORPECENTES").add_to(mapa_itapevi)
        Grupo_2 = folium.FeatureGroup("FURTO - OUTROS").add_to(mapa_itapevi)
        Grupo_3 = folium.FeatureGroup("FURTO DE CARGA").add_to(mapa_itapevi)
        Grupo_4 = folium.FeatureGroup("FURTO DE VEÍCULO").add_to(mapa_itapevi)
        Grupo_5 = folium.FeatureGroup("HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO").add_to(mapa_itapevi)
        Grupo_6 = folium.FeatureGroup("HOMICÍDIO DOLOSO").add_to(mapa_itapevi)
        Grupo_7 = folium.FeatureGroup("LATROCÍNIO").add_to(mapa_itapevi)
        Grupo_8 = folium.FeatureGroup("LESÃO CORPORAL CULPOSA - OUTRAS").add_to(mapa_itapevi)
        Grupo_9 = folium.FeatureGroup("LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO").add_to(mapa_itapevi)
        Grupo_10 = folium.FeatureGroup("LESÃO CORPORAL DOLOSA").add_to(mapa_itapevi)
        Grupo_11 = folium.FeatureGroup("PORTE DE ARMA").add_to(mapa_itapevi)
        Grupo_12 = folium.FeatureGroup("PORTE DE ENTORPECENTES").add_to(mapa_itapevi)
        Grupo_13 = folium.FeatureGroup("ROUBO - OUTROS").add_to(mapa_itapevi)
        Grupo_14 = folium.FeatureGroup("ROUBO DE CARGA").add_to(mapa_itapevi)
        Grupo_15 = folium.FeatureGroup("ROUBO DE VEÍCULO").add_to(mapa_itapevi)
        Grupo_16 = folium.FeatureGroup("TENTATIVA DE HOMICÍDIO").add_to(mapa_itapevi)
        Grupo_17 = folium.FeatureGroup("TRÁFICO DE ENTORPECENTES").add_to(mapa_itapevi)
    
    
        for bairro, lat, lon, caso in zip(df_filtro.BAIRRO, df_filtro.LATITUDE.values, df_filtro.LONGITUDE.values, df_filtro.NATUREZA_APURADA):
    
            if caso == "APREENSÃO DE ENTORPECENTES":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "cannabis", prefix= 'fa', icon_color="lightgreen", color= "darkgreen")
                            ).add_to(Grupo_1)
            
            if caso == "FURTO - OUTROS":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "people-robbery", prefix= 'fa', icon_color="black",  color= "lightgray")
                            ).add_to(Grupo_2)
                
            if caso == "FURTO DE CARGA":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "truck", prefix ='fa', icon_color="black",  color= "lightgray")
                            ).add_to(Grupo_3)
            
            if caso == "FURTO DE VEÍCULO":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "car", prefix= 'fa', icon_color="black",  color= "lightgray")
                            ).add_to(Grupo_4)
            
            if caso == "HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "car-burst", prefix= 'fa',icon_color="red", color= "black")
                            ).add_to(Grupo_5)
                
            if caso == "HOMICÍDIO DOLOSO":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "skull", prefix= 'fa', icon_color="red", color= "black")
                            ).add_to(Grupo_6)
                
            if caso == "LATROCÍNIO":
                folium.Marker([lat, lon],
                                tooltip= "Clique Aqui!",
                                popup= f"{caso}",
                                icon= folium.Icon(icon= "gun", prefix= 'fa', icon_color="red", color= "black")
                                ).add_to(Grupo_7)
                
            if caso == "LESÃO CORPORAL CULPOSA - OUTRAS":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "person-harassing", prefix= 'fa', icon_color="beige", color= "black")
                            ).add_to(Grupo_8)
                
            if caso == "LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "car-burst", prefix= 'fa', icon_color="darkblue",  color= "beige")
                            ).add_to(Grupo_9)
                
            if caso == "LESÃO CORPORAL DOLOSA":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "person-harassing", prefix= 'fa', icon_color="beige",  color= "orange")
                            ).add_to(Grupo_10)
                
            if caso == "PORTE DE ARMA":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "gun", prefix= 'fa', icon_color="darkblue", color= "blue")
                            ).add_to(Grupo_11)
                
            if caso == "PORTE DE ENTORPECENTES":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "joint", prefix= 'fa', icon_color="darkgreen", color= "lightgreen")
                            ).add_to(Grupo_12)
            
            if caso == "ROUBO - OUTROS":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "people-robbery", prefix= 'fa', icon_color="white", color= "black")
                            ).add_to(Grupo_13)
                
            if caso == "ROUBO DE CARGA":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "truck", prefix= 'fa', icon_color="white", color= "black")
                            ).add_to(Grupo_14)
                
            if caso == "ROUBO DE VEÍCULO":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "car", prefix= 'fa', icon_color="white", color= "black")
                            ).add_to(Grupo_15)
                
            if caso == "TENTATIVA DE HOMICÍDIO":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "skull", prefix= 'fa', icon_color="black", color= "darkred")
                            ).add_to(Grupo_16)
    
            if caso == "TRÁFICO DE ENTORPECENTES":
                folium.Marker([lat, lon],
                            tooltip= "Clique Aqui!",
                            popup= f"{caso}",
                            icon= folium.Icon(icon= "cannabis", prefix= 'fa', icon_color="darkgreen", color= "lightgreen")
                            ).add_to(Grupo_17)
            
    
        folium.LayerControl().add_to(mapa_itapevi)
        mapa_itapevi.save("mapa.html")
        st.components.v1.html(open("mapa.html", "r", encoding="utf8").read(), height=600)
        
    with st.container():
        ("---")
        A = st.markdown("## Análise Geral dos Bairros de Itapevi")
            
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col5, col6 =st.columns(2)
            
        ###############################################################################################################################
        contagem_bairros = df['BAIRRO'].value_counts().reset_index().head(30)
        contagem_bairros.columns = ['BAIRRO', 'frequencia']
            
        fig_bairros = px.bar(contagem_bairros,
                            x='BAIRRO',
                            y='frequencia',
                            text_auto="frequencia",
                            title='TOP 30 bairros com mais ocorrências')
        fig_bairros.update_traces ( textfont_size = 12 ,  textangle = 0 ,  textposition = "outside" ,  cliponaxis = False )
        col1.plotly_chart(fig_bairros, use_container_width=True)
            
            ########################################################################################################################
        contagem_casos = df['RUBRICA'].value_counts().reset_index().head(15)
        contagem_casos.columns = ['RUBRICA', 'frequencia']

        fig_casos = px.pie(contagem_casos,
                            values="frequencia",
                            names="RUBRICA",
                            title="Total casos por Rubrica")
        col3.plotly_chart(fig_casos, use_container_width=True)
            ############################################################################################################################
        
        st.sidebar.header(" Filtro de Bairros Para o Gráfico de Casos Agrupados por Bairro")
        bairro_selecionado =st.sidebar.selectbox("BAIRRO",
                                        options=df["BAIRRO"].unique(),
                                        placeholder="Escolha um bairro",
                                        index=None)
        
        df_bairros = df[df["BAIRRO"] == bairro_selecionado]
        contagem_rubricas = df_bairros["RUBRICA"].value_counts()
            
        df_contagem = pd.DataFrame({"Rubrica": contagem_rubricas.index, "Quantidade": contagem_rubricas.values})

        fig = px.bar(df_contagem,
                x="Rubrica",
                y="Quantidade",
                color='Rubrica',
                text_auto="frequencia",
                title=f'Gráfico de Barras de Casos Agrupados por Rubrica - Bairro: {bairro_selecionado}')
        fig.update_traces ( textfont_size = 12 ,  textangle = 0 ,  textposition = "outside" ,  cliponaxis = False )
        col5.plotly_chart(fig)

if __name__ == "__main__":
    run()
