import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np




def main():
    st.image('capa app.jpg')

    selecao = st.sidebar.radio(
    "Selecione a opção:",
    ("Página inicial", "Guia do aplicativo", "Análises da Tuberculose", "Contato"))
    if selecao!="Contato":
        st.title("Situação da Tuberculose no Paraná de 2001 a 2021")

    url="incidencia_tb_mun.csv"
    dados=pd.read_csv(url)
    incidencia_pr=pd.read_csv("incidencia_pr.csv")

    if selecao=="Página inicial": 
        st.header("Introdução")
        st.markdown("""A Tuberculose (TB) é a doença infecciosa creditada pelo maior número de mortes anuais anteriormente à pandemia COVID-19,
            mas com a situação pandêmica, fez-se necessário a avaliação do impacto deste novo vírus na notificação de casos de TB. 
            """)
        st.subheader("Objetivo")
        st.markdown("""Desta forma, o objetivo deste trabalho foi avaliar a série histórica de casos de TB no PR, com ênfase no impacto da pandemia de COVID-19 na notificação de novos casos de TB.
             Posteriormente as analises, a criação desse aplicativo foi realizada afim de tornar visível e acessível à população através de números 
             e gráficos a notificação dos casos de TB no Paraná e seus municípios.""")

        st.subheader("Equipe executora")
        st.markdown("**Beatriz Ignácio Pinel**, João Vitor Perez de Souza e Rosilene Fressatti Cardoso ")
    if selecao=="Guia do aplicativo": 
        st.markdown("O modo de usar esse aplicativo é bem simples!")
        
        st.markdown("""Essa é a tela inicial. """)
        
        st.markdown("""Aqui você encontra um resumo do projeto e a equipe executora!""") 
        
        st.markdown("""Na região **indicada pela seta**, você pode navegar pelas páginas do app.""")   
        
        st.image('primeira_tela.png')

        st.markdown("""Na página \"Análises da Tuberculose\", você pode **selecionar (ou digitar) o nome de um município do Paraná**.""")
        
        st.markdown("""Ao selecionar o nome, você poderá ver um resumo da Incidência e número de casos de TB registrado!""")
        

        st.markdown("""Outra opção é que você pode também baixar os gráficos ao clicar no **botão indicado!**""")
        
        st.image('terceira_tela.png')

        st.markdown("""Na página \"Contato\", você encontra as informações da equipe executora desse projeto.""")
        
        st.markdown("""Se você gostou e quer saber mais, entre em contato com a gente!""")    
        
        st.image('quarta_tela.png')


    if selecao=="Análises da Tuberculose": 


        def filtrar_tabelar(banco,municipio):
            banco_mun=banco.query('ID_MN_RESI_MAP == @municipio')
            return banco_mun

        def plotar_graficos(banco,municipio):
            fig, ax=plt.subplots(1,2, figsize=(12,4))
            ax[0].plot(banco['NU_ANO'].astype(str), banco['INCIDENCIA'],label=f'Incidência {municipio}')
            ax[0].set_xticklabels(banco["NU_ANO"].astype(str),rotation=90);
            ax[0].set_ylabel("Casos por 100 mil habitantes",  fontsize=13)

          #incidencia_pr
            ax[0].plot(incidencia_pr['NU_ANO'].astype(str), incidencia_pr['INCIDENCIA'],label="Incidência PR")
            ax[0].legend()
            ax[0].set_title("Incidência de TB",fontsize=15)
            ax[0].legend(loc=(0,-0.35))
            ax[1].bar(banco['NU_ANO'].astype(str), banco['CASOS'])
            ax[1].set_xticklabels(banco["NU_ANO"].astype(str),rotation=90);
            ax[1].set_ylabel("Número", fontsize=13)
            ax[1].set_title("Casos absolutos de TB", fontsize=15)
            fig.suptitle(f'Panorama da Tuberculose em {municipio} de 2001 à 2021',fontsize=18,y=-0.2)
            fig.savefig('Gráfico.png', dpi=300, bbox_inches="tight")
            return fig


        def filtra_plota(banco, municipio):
            banco_mun=filtrar_tabelar(banco, municipio)
            fig = plotar_graficos(banco_mun,municipio)

            return fig

        municipios = dados["Município"].unique()

        option = st.selectbox(
         'Selecione o município de interesse:',
         municipios)
        st.write("Essa foi sua opção", option)

        fig = filtra_plota(dados, option)
        

        st.pyplot(fig)

        with open("Gráfico.png", "rb") as file:
            btn = st.download_button(
             label="Baixar imagem",
             data=file,
             file_name="Gráfico.png",
             mime="image/png"
           )
    if selecao=="Contato":
        st.header("Contato")
        st.subheader("Beatriz Ignácio Pinel")
        st.markdown("Aluna do 4° ano de Biomedicina - UEM")
        st.markdown("email: ra112880@uem.br")
        st.subheader("João Vitor Perez de Souza")
        st.markdown("Doutorando no PBF - UEM")
        st.markdown("email: pg54174@uem.br")
        st.subheader("Rosilene Fressatti Cardoso")
        st.markdown("Professora no DAB - UEM")

        st.markdown("email: rfcardoso@uem.br")

    

if __name__ == "__main__":
    main()