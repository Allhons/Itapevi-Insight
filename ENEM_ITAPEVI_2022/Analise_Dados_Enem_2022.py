import folium
import pandas as pd
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
  st.set_page_config(layout="wide",
                   page_title="Análise de Dados do Enem 2022",
                   page_icon="Itapevi_insights.ico")

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
  with st.container():
      ("---")
      st.markdown("## Análise dos Dados do Enem de 2022")
      st.write("""
              Está análise foi feita a partir do dados do Enem de 2022, não utilizamos os dados do Enem de 2023 pois ainda não foram divulgados pelo [INEP](https://www.gov.br/inep/pt-br).\\
              \\
              Está análise tem o intuito de mostrar como os estudantes de Itape estão se saindo coms os estudantes das cidades vizinhas!\\
              E tambem mostra o perfil dos estudantes que optam pelo Enem para ingressar no Ensino Superior!
              """)
      
  with st.container():
    ("---")
    TP_FAIXA_ETARIA = {"Menores de 17 anos":1,"17 anos":2,"18 anos":3,"19 anos":4,"20 anos":5,"21 anos":6,"22 anos":7, "23 anos": 8, "24 anos": 9, "25 anos": 10,
                      "Entre 26 e 30 anos": 11, "Entre 31 e 35 anos": 12, "Entre 36 e 40 anos": 13, "Entre 41 e 45 anos": 14, "Entre 46 e 50 anos": 15,
                      "Entre 51 e 55 anos": 16, "Entre 56 e 60 anos": 17, "Entre 61 e 65 anos": 18, "Entre 66 e 70 anos": 19, "Maior de 70 anos": 20}

    TP_SEXO = {'Feminino':'F', 'Masculino': 'M'}

    TP_ESTADO_CIVIL = {"Não informado": 0, "Solteiro(a)": 1, "Casado(a)/Mora com companheiro(a)": 2,
                      "Divorciado(a)/Desquitado(a)/Separado(a)": 3, "Viúvo(a)": 4}

    TP_COR_RACA = {'Não declarado': 0,
                  'Branca': 1,
                  'Preta': 2,
                  'Parda': 3,
                  'Amarela': 4,
                  'Indígena': 5,
                  'Não dispõe da informação': 6}

    TP_ST_CONCLUSAO = {'Já concluí o Ensino Médio': 1, 
                      'Estou cursando e concluirei o Ensino Médio em 2021': 2,
                      'Estou cursando e concluirei o Ensino Médio após 2021': 3,
                      'Não concluí e não estou cursando o Ensino Médio': 4}

    TP_ANO_CONCLUIU = {'Não informado': 0, '2021': 1, '2020': 2, '2019': 3, '2018': 4, '2017': 5, '2016': 6, '2015': 7, '2014': 8,
                      '2013': 9, '2012': 10, '2011': 11, '2010': 12, '2009': 13, '2008': 14, '2007': 15, "Antes de 2007": 16}

    TP_ESCOLA = {'Não Respondeu': 1, 'Pública': 2, 'Privada': 3}

    TP_ENSINO = {"Ensino Regular": 1, "Educação Especial - Modalidade Substitutiva": 2}

    IN_TREINEIRO = {'Não': 0,'Sim':1}

    TP_DEPENDENCIA_ADM_ESC={'Federal': 1, 'Estadual': 2, 'Municipal': 3, 'Privada': 4}

    TP_LOCALIZACAO_ESC = {'Urbana': 1, 'Rural': 2}

    TP_PRESENCA_LC ={"Presente": 1, "Faltou": 0}

    TP_PRESENCA_MT = {"Presente": 1, "Faltou": 0}

    TP_SIT_FUNC_ESC = {'Em atividade': 1, 'Paralisada': 2, 'Extinta': 3, 'Escola extinta em anos anteriores.': 4}

    TP_STATUS_REDACAO	= {'Sem problemas': 1, 'Anulada': 2, 'Cópia Texto Motivador': 3, 'Em Branco': 4, 'Fuga ao tema': 6,
                          'Não atendimento ao tipo textual': 7,'Texto insuficiente': 8, 'Parte desconectada': 9}

    Q001 = Q002= {'Nunca estudou.': 'A',
                  'Não completou a 4ª série/5º ano do Ensino Fundamental.': 'B',
                  'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.': 'C',
                  'Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.': 'D',
                  'Completou o Ensino Médio, mas não completou a Faculdade.': 'E',
                  'Completou a Faculdade, mas não completou a Pós-graduação.': 'F',
                  'Completou a Pós-graduação.': 'G',
                  'Não sei.': 'H'}

    TP_LINGUA = {'Inglês': 0, 'Espanhol': 1}

    Q003 = Q004 = {'Grupo 1': 'A', 'Grupo 2': 'B', 'Grupo 3': 'C', 'Grupo 4': 'D', 'Grupo 5': 'E', 'Não sei': 'F'}

    Q005 = {'1 - 5':[1,2,3,4,5],
            '6 - 10':[6,7,8,9,10],
            '11 - 15':[11,12,13,14,15],
            '16 - 20':[16,17,18,19,20]}

    Q006 = {
    'Nenhuma Renda': ['A'],
    'R$ 1.100,00 - R$ 2.750,00.': ['B','C','D','E'],
    'R$ 2.750,01 - R$ 6.600,00.': ['F','G','H','I'],
    'R$ 6.600,01 - R$ 11.000,00.': ['J','K','L','M'],
    'R$ 11.000,01 - Acima de R$ 22.000,00.': ['N','O','P','Q']
    }

    dicionarios_cols = {
        'TP_FAIXA_ETARIA':TP_FAIXA_ETARIA,
        'TP_SEXO':TP_SEXO,
        'TP_ESTADO_CIVIL':TP_ESTADO_CIVIL,
        'TP_COR_RACA':TP_COR_RACA,
        'TP_ST_CONCLUSAO':TP_ST_CONCLUSAO,
        'TP_ANO_CONCLUIU':TP_ANO_CONCLUIU,
        'TP_ESCOLA':TP_ESCOLA,
        'IN_TREINEIRO':IN_TREINEIRO,
        'TP_DEPENDENCIA_ADM_ESC':TP_DEPENDENCIA_ADM_ESC,
        'TP_LOCALIZACAO_ESC':TP_LOCALIZACAO_ESC,
        'TP_SIT_FUNC_ESC':TP_SIT_FUNC_ESC,
        'TP_LINGUA': TP_LINGUA,
        'TP_STATUS_REDACAO': TP_STATUS_REDACAO,
        'Q001':Q001,
        'Q002':Q002,
        'Q003':Q003,
        'Q004':Q004}

    df = pd.read_excel('ENEM_ITAPEVI_2022/Enem 2022 Grupo.xlsx')
    Itapevi_df = pd.read_excel('ENEM_ITAPEVI_2022/Itapevi enem 2022.xlsx')

    df_presentes = df.loc[(df['TP_PRESENCA_CN']  == 1) & (df['TP_PRESENCA_CH'] == 1)]
    df_presentes_itapevi = Itapevi_df.loc[(df['TP_PRESENCA_CN']  == 1) & (Itapevi_df['TP_PRESENCA_CH'] == 1)]

    def valores_em_texto(val,colunas):
      dict_temporario = dicionarios_cols[colunas]
      for chave, valor in dict_temporario.items():
        if valor == val:
          return chave

    def faixa_Q5_Q6(val,coluna):
      for chave,valor in coluna.items():
        if val in valor:
          return chave

    str_colunas = ['TP_FAIXA_ETARIA','TP_SEXO','TP_ESTADO_CIVIL','TP_COR_RACA','TP_ST_CONCLUSAO','TP_ANO_CONCLUIU','TP_ESCOLA','IN_TREINEIRO',
                  'TP_DEPENDENCIA_ADM_ESC','TP_LOCALIZACAO_ESC','TP_STATUS_REDACAO','TP_LINGUA','TP_SIT_FUNC_ESC','Q001','Q002','Q003','Q004']

    nov_df = df_presentes[:]
    nov_df_itapevi = df_presentes_itapevi[:]
    for colunas in str_colunas:
      nov_df[colunas] = df_presentes[colunas].apply(valores_em_texto,args=(colunas,))
      nov_df_itapevi[colunas] = df_presentes_itapevi[colunas].apply(valores_em_texto,args=(colunas,))

    nov_df['Q005'] = nov_df['Q005'].apply(faixa_Q5_Q6,args=(Q005,))
    nov_df['Q006'] = nov_df['Q006'].apply(faixa_Q5_Q6,args=(Q006,))
    nov_df_itapevi['Q005'] = nov_df_itapevi['Q005'].apply(faixa_Q5_Q6,args=(Q005,))
    nov_df_itapevi['Q006'] = nov_df_itapevi['Q006'].apply(faixa_Q5_Q6,args=(Q006,))

    def tabela_notas(data):
        locais = ['GERAL','Cotia','Carapicuíba', 'Itapevi','Jandira','Osasco','Barueri']
        dict_med = {}

        for i in locais:
            if i == 'GERAL':
                municipio = data
            else:
                municipio = data.loc[data['NO_MUNICIPIO_ESC'] == i]
            dict_med[i] = [municipio.iloc[:,27].mean(),
                            municipio.iloc[:,28].mean(),
                            municipio.iloc[:,29].mean(),
                            municipio.iloc[:,30].mean(),
                            municipio.iloc[:,33].mean()]

            df_medias_notas = pd.DataFrame(data= dict_med,index=['Natureza','Humanas','Linguagem','Matematica','Redacao'])
            df_medias_notas = df_medias_notas.applymap('{:.2f}'.format)
            df_medias_notas = df_medias_notas.astype('float64')
        return df_medias_notas
      
    cor_destaque = "rgb(00, 33, 47)"
    cor_claro = "rgb(33, 249, 208)"
    cor_tema = "rgb(0, 143, 199)"
    cor_destoante = "rgb(46, 66, 74)"
    cor_escuro = "rgb(00, 69, 94)"

    textos_graficos = {
    'TP_FAIXA_ETARIA': ['Faixa etária Enem 2022','Idade'],
    'TP_SEXO': ['Sexo dos candidatos Enem 2022','Sexo'],
    'TP_COR_RACA': ['Etnias candidatos Enem 2022','Etinia'],
    'TP_ESCOLA': ['Tipo de escola do Ensino Médio Enem 2022','Tipos de escola'],
    'NO_MUNICIPIO_ESC':['Município das escolas dos candidatos Enem 2022','Município'],
    'TP_DEPENDENCIA_ADM_ESC': ['Dependência administrativa (Escola) Enem 2022','Região Administrativa'],
    'TP_LINGUA':['Língua Estrangeira selecionada Enem 2022','Língua Estrangeira'],
    'TP_STATUS_REDACAO':['Status da redação Enem 2022','Status redação'],
    'Q001':['Escolaridade Paterna Enem 2022', 'Escolaridade Pai'],
    'Q002':['Escolaridade Materna Enem 2022','Escolaridade Mãe'],
    'Q003':['Grupo de Ocupação Paterna Enem 2022', 'Ocupação Pai'],
    'Q004':['Grupo de Ocupação Materna Enem 2022', 'Ocupação Mãe'],
    'Q005':['Quantidade de pessoas que moram na<br>residência do candidato Enem 2022', 'Membros da Família'],
    'Q006':['Renda Familiar','Renda']
    }


    def create_graf_pizza(SERIE):
      cores_array_pizza = [cor_destaque] * len(SERIE.index)
      cores_array_pizza[1] = cor_claro
      if len(SERIE.index) == 3:
        cores_array_pizza[2] = cor_escuro

      fig_pie = go.Figure()
      
      if isinstance(SERIE, pd.Series):
          serie_name = SERIE.name
      else:
          serie_name = "Série"
                
      if serie_name in textos_graficos:
        title = f"<b>{textos_graficos[serie_name][0]}</b>"
        hover_text = textos_graficos[serie_name][1]
      else:
        title = f"<b>{serie_name}</b>"
        hover_text = "Quantidade: %{y}"

      fig_pie.add_trace(go.Pie(values=SERIE.values,
                              labels= SERIE.index,
                              marker_colors=cores_array_pizza))

      fig_pie.update_traces(hole=.5,
                            customdata = np.stack( (SERIE.index, SERIE.values), axis=-1),
                            hovertemplate= f'<b>{hover_text}:'+'</b> %{customdata[0][0]}<br><b>Quantidade: %{customdata[0][1]}</b>',
                            textfont_size=16,)

      fig_pie.update_layout(title=title,
                            title_x=0.5,
                            title_font = {"size": 20,"family":"Tahoma,sans serif"},
                            width=500,
                            height=500)

      return fig_pie

    def tamanho_zoom(SERIE):
      maior = max(SERIE) * 1.07
      return maior

    def gerador_graf(SERIE):
      if len(SERIE.index) <= 3:
        return create_graf_pizza(SERIE)
      else:
        if isinstance(SERIE, pd.Series):
          serie_name = SERIE.name
        else:
          serie_name = "Série"
                
        if serie_name in textos_graficos:
          title = f"<b>{textos_graficos[serie_name][0]}</b>"
          hover_text = textos_graficos[serie_name][1]
        else:
          title = f"<b>{serie_name}</b>"
          hover_text = "Quantidade: %{y}"
        
        cores_array = [cor_destoante] * len(SERIE.index)
        cores_array[0] = cor_destaque
        cores_array[1] =cor_escuro
        cores_array[2] = cor_claro
        #marker_colors=[cor_destaque,cor_claro]
        layout_zoom = go.Layout(yaxis=dict(range=[0, tamanho_zoom(SERIE)]))
        GRAF_SERIE = go.Figure(layout=layout_zoom)

        GRAF_SERIE.add_trace(go.Bar(x=SERIE.index,
                                              y=SERIE.values,
                                              text=SERIE.values,
                                              textposition='outside',
                                              textfont_size=16,
                                              marker_color= cores_array
                                              ))

        GRAF_SERIE.update_layout(title=title,
                                          title_x= 0.5,
                                          template= 'plotly_white',
                                          title_font = {"size": 20,"family":"Tahoma,sans serif"})

        # GRAF_SERIE.update_xaxes(title_font=dict(size=18))
        GRAF_SERIE.update_yaxes(visible=False, showticklabels=False)

        GRAF_SERIE.update_traces(customdata = np.stack( (SERIE.index, SERIE.values), axis=-1),
                                hovertemplate= f'<b>{hover_text}:'+'</b> %{customdata[0]}<br><b>Quantidade: %{customdata[1]}</b>')

        GRAF_SERIE.update_xaxes(tickfont_size=16)

        return GRAF_SERIE

    def graf_notas_esc(data,titulo):
      fig_notas = go.Figure(layout= go.Layout(yaxis=dict(range=[0,1000])))
      palheta = [cor_destaque,cor_claro,cor_tema,cor_destoante,cor_escuro]
      nome_materias = ['Natureza','Humanas','Linguagem','Matematica','Redacao']
      for i in range(len(data.index)):
          fig_notas.add_trace(go.Bar(x=data.loc[nome_materias[i]].index,
                                      y=data.loc[nome_materias[i]].values,
                                      text=data.loc[nome_materias[i]].values,
                                      textposition='outside',
                                      textfont_size=116,
                                      name= nome_materias[i],
                                      marker_color=palheta[i]))


      fig_notas.update_layout(title=f"<b>{titulo}</b>",
                              title_x= 0.1,
                              template= 'plotly_white',
                              title_font = {"size": 20,"family":"Tahoma,sans serif"},
                              bargap=0.20,
                              bargroupgap=0.1)

      fig_notas.update_yaxes(visible=False, showticklabels=False)

      fig_notas.update_traces(customdata = np.stack( (data.columns, data.loc['Natureza'].values,data.loc['Humanas'].values,data.loc['Linguagem'].values,data.loc['Matematica'].values,data.loc['Redacao'].values), axis=-1),
                              hovertemplate= '<b>Município</b> %{customdata[0]}<br><b>Nota Natureza: %{customdata[1]}</b><br><b>Nota Humanas: %{customdata[2]}</b><br><b>Nota Linguagem: %{customdata[3]}</b><br><b>Nota Matemática: %{customdata[4]}</b><br><b>Nota Redação: %{customdata[5]}</b>')

      fig_notas.update_xaxes(tickfont_size=16)

      return fig_notas
      
    st.markdown("## Comparando Itapevi com outras cidades")
    df_medias_notas = tabela_notas(df_presentes)
    st.write("**Média das notas dos Municípios da Zona Oeste de São Paulo:**")
    df_medias_notas
    nota_geral = graf_notas_esc(df_medias_notas,"Média Notas Gerais do Enem 2022")
    col1, col2 = st.columns(2)
    col1.plotly_chart(nota_geral)
    ("")
    st.write("**Média das notas das Escolas Privadas da Zona Oeste de São Paulo:**")
    df_medias_notas_priv = tabela_notas(nov_df.loc[nov_df['TP_ESCOLA'] == "Privada"])
    df_medias_notas_priv
    nota_parti = graf_notas_esc(df_medias_notas_priv,"Média Notas Escolas Particulares do Enem 2022")
    col3, col4 = st.columns(2)
    col3.plotly_chart(nota_parti)
    ("")
    st.write("**Média das notas das Escolas Públicas da Zona Oeste de São Paulo:**")
    df_medias_notas_publi = tabela_notas(nov_df.loc[nov_df['TP_ESCOLA'] == "Pública"])
    df_medias_notas_publi
    nota_pub = graf_notas_esc(df_medias_notas_publi,"Média Notas Escolas Públicas do Enem 2022")
    col5, col6 = st.columns(2)
    col5.plotly_chart(nota_pub)

  with st.container():
    ("---")
    st.markdown("## Presença dos Candidatos de Itapevi-SP")
    col1, col2 = st.columns(2)
    dia1 = gerador_graf(Itapevi_df['TP_PRESENCA_LC'].value_counts())
    dia1.update_layout(title="<b>Presença 1° dia Prova</b>")
    col1.plotly_chart(dia1)
    
    dia2 = gerador_graf(Itapevi_df['TP_PRESENCA_MT'].value_counts())
    dia2.update_layout(title="<b>Presença 2° dia Prova</b>")
    col2.plotly_chart(dia2)
    
  with st.container():
    ("---")
    st.title("Candidatos que compareceram aos 2 dias do ENEM 2022")

  with st.container():
    ("---")
    st.markdown("## Faixa Etária candidados Itapevi")
    col1, col2 = st.columns(2)
    idade = gerador_graf(nov_df_itapevi['TP_FAIXA_ETARIA'].value_counts())
    idade.update_layout(title="<b>Faixa Etária Enem 2022 Itapevi</b>")
    col1.plotly_chart(idade)
    
  with st.container():
    ("---")
    st.markdown("## Quantidade de Pessoas que Moram na sua Residência")
    col1, col2 = st.columns(2)
    residencia = gerador_graf(nov_df_itapevi['Q005'].value_counts())
    residencia.update_layout(title="<b>Quantida de Pessoas que Moram com o Candidato</b>")
    col1.plotly_chart(residencia)
    
  with st.container():
    ("---")
    st.markdown("## Renda Familiar")
    col1, col2 = st.columns(2)
    graf_renda = gerador_graf(nov_df_itapevi['Q006'].value_counts())
    graf_renda.update_layout(title="<b>Renda Familiar</b>", xaxis=dict(tickmode='array',tickvals=[0,1,2,3,4],ticktext =['R&#36; 1.100,00 até<br>R&#36; 2.750,00.', 'R&#36; 2.750,01 até<br>R&#36; 6.600,00.','R&#36; 6.600,01 até<br>R&#36; 11.000,00.', 'R&#36; 11.000,01<br>Acima de R&#36; 22.000,00.','Nenhuma Renda'],tickfont_size=14))
    col1.plotly_chart(graf_renda)
    
  with st.container():
    ("---")
    st.markdown("## Língua Estrangeira Escolhida")
    col1, col2 = st.columns(2)
    lingua = gerador_graf(nov_df_itapevi['TP_LINGUA'].value_counts())
    lingua.update_layout(title="<b>Língua Estrangeira Enem 2022 Itapevi</b>")
    col1.plotly_chart(lingua)

  with st.container():
    ("---")
    st.markdown("## Tipo de Escola dos Participantes")
    col1, col2 = st.columns(2)
    tipo_esc = gerador_graf(nov_df_itapevi['TP_ESCOLA'].value_counts())
    tipo_esc.update_layout(title="<b>Tipo de escola dos Participantes Enem 2022</b>")
    col1.plotly_chart(tipo_esc)
    
  with st.container():
    ("---")
    st.markdown("## Status Redação")
    col7, col8 = st.columns(2)
    graf_redacao = gerador_graf(nov_df_itapevi['TP_STATUS_REDACAO'].value_counts())
    graf_redacao.update_layout(title="<b>Status da Redação Enem 2022</b>", xaxis=dict(tickmode='array',tickvals=[0,1,2,3,4,5,6,7],ticktext =['Sem problemas', 'Em Branco', 'Fuga ao tema', 'Texto insuficiente','Parte<br>desconectada', 'Cópia Texto<br>Motivador','Não atendimento<br>ao tipo textual', 'Anulada'],tickfont_size=14))
    col7.plotly_chart(graf_redacao)  
    
  with st.container():
    ("---")
    st.markdown("## Escolaridade Paterna e Materna dos Candidatos")
    col1, col2 = st.columns(2)
    lista_escolaridade_familiar = ["Até Ensino médio","Até Faculdade","Pós-graduado","Até o fundamental","Até o 5°<br>do fundamental","Não sabe","Não completou<br>5° do fundamental","Nunca estudou"]
    graf_q001 = gerador_graf(nov_df_itapevi['Q001'].value_counts())
    graf_q001.update_layout(title="<b>Escolaridade Paterna</b>", xaxis=dict(tickmode='array',tickvals=[0,1,2,3,4,5,6,7],ticktext =lista_escolaridade_familiar,tickfont_size=14))
    col1.plotly_chart(graf_q001)
    
    col3, col4 =st.columns(2)
    graf_q002 = gerador_graf(nov_df_itapevi['Q002'].value_counts())
    graf_q002.update_layout(title="<b>Escolaridade Materna</b>",xaxis=dict(tickmode='array',tickvals=[0,1,2,3,4,5,6,7],ticktext =lista_escolaridade_familiar,tickfont_size=14))
    col3.plotly_chart(graf_q002)
    
  with st.container():
    ("---")
    st.markdown("## Grupo de Ocupação dos Pais dos Candidatos")
    st.write("""
            **O grupo de ocupação adotado pelo Enem se utiliza de cinco categorias, as divisões são:**\\
              **Grupo 1:** Trabalhadores de campo;\\
              **Grupo 2:** Prestador de serviço sem necessidade de estudo técnico;\\
              **Grupo 3:** Prestador de serviço com necessidade de estudo técnico;\\
              **Grupo 4:** Profissionais com ensino superior ou microempreendedores;\\
              **Grupo 5:** Profissionais com ensino superior da alta especialização e médios a grandes empreendedores.
              """)
    col13, col14 = st.columns(2)
    ocu_pat = gerador_graf(nov_df_itapevi['Q003'].value_counts())
    ocu_pat.update_layout(title="<b>Grupo de Ocupação Paterna</b>")
    col13.plotly_chart(ocu_pat)
    
    col15, col16 = st.columns(2)
    ocu_mat = gerador_graf(nov_df_itapevi['Q004'].value_counts())
    ocu_mat.update_layout(title="<b>Grupo de Ocupação Materna</b>")
    col15.plotly_chart(ocu_mat)
    
  with st.container():
    ("---")
    
if __name__ == "__main__":
    run()
