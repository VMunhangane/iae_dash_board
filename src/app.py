import dash
import pandas as pd
import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc 


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# create an app
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
server = app.server
footer_height = "2000rem", "100rem",
FOOTER_STYLE = {
    "position": "fixed",
    "bottom": 0,
    "left": 0,
    "right": 0,
    #"height": footer_height,
    #"width": "5rem",
    #"padding": "200rem 200rem",
    "background-color": "gray",
},

df_contagem = pd.read_csv('indices_89_90_91.csv', low_memory=False, encoding="iso-8859-1", dtype= {'CAE': np.object_})
df_contagem = df_contagem[df_contagem["Categoria"] == "Índices"]


numero_da_publicacao = df_contagem.shape[0]

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

iae_message = f'Informação do Índice de actividades económicas (IAE) até a publicação Nº {numero_da_publicacao} de {nome_mes} de {ultimo_ano}.'

sidebar = dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(page["name"]),# className = "ms-2"),
            ],
            href=page["path"],
            active= "exact",
        )
        for page in dash.page_registry.values()
    ],
    vertical=False,
    pills=True,
    fill=True,
    justified=True,
    horizontal="center",
    className="bg-light",
)

footer = dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(html.H2("Footer"), style=FOOTER_STYLE
                        ),# className = "ms-2"
                 html.Br(),
                #html.P("INSTITUTO NACIONAL DE ESTATISTICA - Moçambique. 1996-2023"),
            ],
            #href=page["path"],
            #active= "exact",
        )
        #for page in dash.page_registry.values()
    ],
    vertical=False,
    pills=True,
    fill=True,
    justified=True,
    horizontal="center",
    className="bg-light",
)





app.layout = dbc.Container([
    #<a id="portal-logo" title="Instituto Nacional de Estatistica" accesskey="1" href="http://www.ine.gov.mz">
    #<img src="http://www.ine.gov.mz/logo.png" alt="Instituto Nacional de Estatistica" title="Instituto Nacional de Estatistica" height="65" width="172"></a>

#<img src="http://www.ine.gov.mz/logo.png" alt="Instituto Nacional de Estatistica" title="Instituto Nacional de Estatistica" height="65" width="172">



    dbc.Row(
        [
        html.Img(src=app.get_asset_url('rain_sprite_.png'),
                                style = {  "textAlign": "center","width": "95vw",
                                        }
                             
                                        ),#"margin-left": "1vw"'backgroundColor': '#E5ECF6',



        dbc.Col(
                        [
                            
                        #    html.Br(),        
                        #         html.Img(src=app.get_asset_url('logo.png'), 
                        #         style = {"textAlign": "left",  #"layer":"above",
                        #                 "margin-left": "2vw", "margin-dwon": "2vw", "className":"fixed-top",})
                            #dbc.Col(
                               # [
                                # html.Br(),        
                                # html.Img(src=app.get_asset_url('logo.png'), 
                                # style = {"textAlign": "left",  "layer":"above",
                                #         "margin-left": "2vw", "margin-dwon": "2vw", "className":"fixed-top",})

                                # html.Img(src=app.get_asset_url('rain_sprite_.png'),
                                # style = {"textAlign": "center","width": "100vw",
                                #         "layer":"above"}),#"margin-left": "1vw"'backgroundColor': '#E5ECF6',

                               # ],xs=11, sm=12, md=12, lg=12, xl=12, xxl=12,),

                            # dbc.Col(
                            #     [ html.Img(src=app.get_asset_url('logo.png'),
                            #     style = {'backgroundColor': '#E5ECF6',  "textAlign": "left", "position": "fixed",})
                            #     ],xs=11, sm=12, md=12, lg=12, xl=12, xxl=12)
                        
                         ],className="fixed-top", xs=11, sm=12, md=12, lg=12, xl=12, xxl=12)

                         ]),

    dbc.Row(
        [
        
        dbc.Col(





                        [html.H5(iae_message,
                         style = {  "textAlign": "center", 'font-family': 'Source Sans Pro', 'font-size': '16px', "textAlign": "center"} )]
                         ,xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)#'backgroundColor': '#E5ECF6',

                         ],style = {'backgroundColor': "#fff",}, 
                         
                         ),
    


    html.Br(style = {'backgroundColor': '#E5ECF6',}),
    dbc.Row([
        dbc.Col(
            [
                sidebar
            ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12
        )

        
    ],style = {'font-family': 'Source Sans Pro', 'font-size': '15px', "textAlign": "center"} 
        ),


    # definição de uma linha para server de separador
    html.Hr(style = {'size' : '200', 'borderColor':'blue','borderHeight': "200vh", "width": "100%",}),
    
    # O menu com os nomes dos diferentes sectores. 
    dbc.Row([
        dbc.Col(
            [
                dash.page_container
            ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12
        )
    ]),

    # Nota de roda pé
    dbc.Row([
        dbc.Col(
            [
                footer
                
            ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12
        )
    ]),

    # AQ mensagem que vai aparecer na nota de Rodapé
        dbc.Row([
        dbc.Col(
            [
                html.P("INSTITUTO NACIONAL DE ESTATISTICA - Moçambique. 1996-2023",),
                
            ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12,
        )
    ],style = {'font-family': 'Source Sans Pro', 'font-size': '10px', "textAlign": "center"}  
        ),



# definição do estilo do conteudo
],style={
        "background-color": "#fff",#"#CCCCCC",
        #"height": "95vh",
        "width": "95vw",
        #"margin-left": "2vw"
        'font-family': 'Source Sans Pro',  
    }, fluid=True)

if __name__ == "__main__":
    app.run(debug=False)