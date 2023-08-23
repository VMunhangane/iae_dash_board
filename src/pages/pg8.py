import dash
import pandas as pd
import numpy as np
from dash import dcc, html, callback, Output, Input, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

# To create meta tag for each page, define the title, image, and description.
dash.register_page (__name__,
                    path = '/ficha_tecnica', #  is home page and it represents the url
                    name = "Ficha técnica", # name of page, commonly used as name of link
                    title= 'Ficha técnica',  # title that appears on browser's tab
                    #image='pg1.png',  # image in the assets folder
                    description="Ficha técnica do Índice de actividade económica"

                    )

df_contagem = pd.read_csv('indices_89_90_91.csv', low_memory=False, encoding="iso-8859-1", dtype= {'CAE': np.object_})
df_contagem = df_contagem[df_contagem["Categoria"] == "Índices"]

ultimo_ano = df_contagem["Ano"].unique().max()

ultimo_mes = df_contagem[df_contagem["Ano"] == ultimo_ano]["Mês"].unique().max()
if ultimo_mes == 1:
    nome_mes =  "janeiro"
elif ultimo_mes == 2:
    nome_mes = "fevereiro"
elif ultimo_mes == 3:
    nome_mes = "março"
elif ultimo_mes == 4:
    nome_mes = "abril"
elif ultimo_mes == 5: 
    nome_mes = "maio"
elif ultimo_mes == 6:
    nome_mes = 'junho'
elif ultimo_mes == 7:
    nome_mes = 'julho'
elif ultimo_mes == 8:
    nome_mes= 'agosto'
elif ultimo_mes == 9:
    nome_mes= 'setembro'
elif ultimo_mes == 10:
    nome_mes= 'outubro'
elif ultimo_mes == 11:
    nome_mes= 'novembro'
elif ultimo_mes == 12:
    nome_mes= 'dezembro'

titulo_message = f'Índice de Actividades Económicas - {nome_mes} de {ultimo_ano}'


# Vamos configurar o layout
layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([dcc.Markdown("""
                            ##### Índices de Actividades Económicas - Brochura de publicação Mensal
                            ###### © 2023 Instituto Nacional de Estatística""")       
                                ])
                    ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12),


            ]   
                ),

    html.Hr(),

    dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div([dcc.Markdown("""
                            ###### Presidência \n
                            * Eliza Mónica Ana Magaua\n 
                            Presidente
                            """)       
                                ])
                    ], xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),

                dbc.Col(
                    [
                        html.Div([dcc.Markdown("""
                            ###### Ficha técnica\
                            """)       
                                ]),
                        
                        html.Div([dcc.Markdown("""
                            ###### Título:
                            """),
                            titulo_message
                                   
                                ]),
                        
                        html.Div([dcc.Markdown("""
                            ###### Editor\n
                            Instituto Nacional de Estatística\n
                            Direcção de Estatísticas Sectoriais e de Empresas\n
                            Av. 24 de Julho, n° 1989, C. Postal 493 Maputo\n
                            Maputo - Moçambique\n
                            Telefones: + 258 21 30 55 41\n
                            Fax: 258 21 30 55 41\n
                            E-Mail: info@ine.gov.mz\n
                            Homepage: www.ine.gov.mz\n
                            """)       
                                ]),

                        html.Div([dcc.Markdown("""
                            ###### Coordenação e direcção\n
                            * Adriano Matsimbe\n
                            Director Nacional Adjunto de Estatísticas Sectoriais e de Empresas\n 
                            """)       
                                ]),
                        html.Div([dcc.Markdown("""
                            * Armando Tsandzana\n
                            Director Nacional Adjunto de Estatísticas Sectoriais e de Empresas\n
                            """)       
                                ]),

                        html.Div([dcc.Markdown("""
                             ###### Produção\n
                            * Jorge Chemanen\n
                            * Ildefonso Alves\n
                            """)       
                                ]),
                        
                        html.Div([dcc.Markdown("""
                            ###### Análise de qualidade\n
                            * Monasse Nguluve\n
                            * António Ferreira Júnior\n
                            """)       
                                ]),

                        html.Div([dcc.Markdown("""
                            ###### Design e grafismo\n
                            * Mário Chivambo\n
                            * Venâncio Munhangane\n
                            """)       
                                ]),

                        html.Div([dcc.Markdown("""
                            ###### Programador\n
                            * Venâncio Munhangane\n
                            """)       
                                ]),

                        html.Div([dcc.Markdown("""
                            ###### Difusão
                            * Instituto Nacional de Estatística 

                            """)       
                                ]),

                    ], xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
            ],style = {'font-family': 'Source Sans Pro', 'font-size': '11px', 'justifyContent': 'right' }    
                ),
    html.Hr(),

    ]           
                )