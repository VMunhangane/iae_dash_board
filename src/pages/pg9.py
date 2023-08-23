import dash
from dash import dcc, html, callback, Output, Input, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc

# To create meta tag for each page, define the title, image, and description.
dash.register_page (__name__,
                    path = '/acerca_do_INE', #  is home page and it represents the url
                    name = "Acerca do INE", # name of page, commonly used as name of link
                    title= 'Acerca do INE',  # title that appears on browser's tab
                    #image='pg1.png',  # image in the assets folder
                    description="Informações acerca do  Instituto Nacional de Estatística (INE)"

                    )

# page 1 data 
# Temos que carregar a base com a informação da síntese
# df = px.data.gapminder()

card_content = [
    dbc.CardHeader("Instituto Nacional de Estatística (INE)", style = {"fontsize":'8px', "textAlign": "left"}),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
               "O Instituto Nacional de Estatística (INE) é órgão executivo central do Sistema Estatístico Nacional (SEN)\
                 que tem por objectivo a notação, apuramento, coordenação e difusão da informação estatística oficial do País.\
                O Instituto Nacional de Estatística subordina-se ao Conselho de Ministros. (in Lei nº 7/96 de Julho).",
                className="card-text",style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right',\
                                               "text-justify": "inter-word", "color":"black", 'textAlign': 'justify'}
            ),
        ]
    ),
]

card_content1 = [
    dbc.CardHeader("Sistema Estatístico Nacional (SEN)", style = {"fontsize":'8px', "textAlign": "left"}),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
                "É o conjunto orgânico integrado pelas instituições a quem compete o exercício da actividade estatística oficial.",
                className="card-text",style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right',\
                                               "text-justify": "inter-word", "color":"black", 'textAlign': 'justify'}
            ),
        ]
    ),
]

card_content2 = [
    dbc.CardHeader("Actividade estatística oficial", style = {"fontsize":'8px', "textAlign": "left"}),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
                 "Por actividade estatística oficial entende-se, o conjunto de métodos, técnicas e procedimentos de concepção,\
                recolha, tratamento, análise e difusão de informação estatística oficial de interesse nacional, de que se destaca\
                a realização de recenseamentos, inquéritos correntes e eventuais, a elaboração das contas nacionais e de indicadores\
                económicos, sociais e demográficos, bem como a realização de estudos, análises e investigação aplicada.",
                className="card-text",style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right',\
                                               "text-justify": "inter-word", "color":"black", 'textAlign': 'justify'}
            ),
        ]
    ),
]


card_content3 = [
    dbc.CardHeader("Autoridade estatística", style = {"fontsize":'8px', "textAlign": "left"}),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
               "O princípio da autoridade estatística consiste no poder conferido ao Instituto Nacional de Estatística de, no exercício\
                 das actividades estatísticas, realizar inquéritos com obrigatoriedade de resposta nos prazos que forem fixados, bem como\
                 efectuar todas as diligências necessárias à produção das estatísticas.",
                className="card-text",style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right',\
                                               "text-justify": "inter-word", "color":"black", 'textAlign': 'justify'}
            ),
        ]
    ),
]

card_content4 = [
    dbc.CardHeader("Segredo estatístico", style = {"fontsize":'8px', "textAlign": "left"}),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
               "O princípio do segredo estatístico consiste na obrigação do INE de proteger os dados estatísticos individuais, relativos a pessoas\
                singulares ou colectivas recolhidos para produção de estatística, contra qualquer utilização não estatística e divulgação não autorizada,\
                visando salvaguardar a privacidade dos cidadãos, preservar a concorrência entre os agentes económicos e garantir aconfiança dos\
                inquiridos. (Lei nº 7/96 de 5 de Julho)",
                className="card-text",style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right',\
                                               "text-justify": "inter-word", "color":"black", 'textAlign': 'justify'}
            ),
        ]
    ),
]

card_content5 = [
    dbc.CardHeader("Esclarecimentos aos utilizadores", style = {"fontsize":'8px', "textAlign": "left"}),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
               "Devido aos arredondamentos, os totais podem não corresponder à soma das parcelas.",
                className="card-text",style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right',\
                                               "text-justify": "inter-word", "color":"black", 'textAlign': 'justify'}
            ),
        ]
    ),
]

card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(src="/assets/logo.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Endereço", style = {"fontsize":'8px', "textAlign": "left"}, className="card-title"),
                            html.P(
                                "Av. 24 de Julho, n° 1989, C. Postal 493 Maputo\
                                Maputo - Moçambique\n\
                                Telefones: + 258 21 30 55 41\n\
                                Fax: 258 21 30 55 41\n\
                                E-Mail: info@ine.gov.mz\n\
                                Homepage: www.ine.gov.mz",
                                # "below as a natural lead-in to additional "
                                # "content. This content is a bit longer.",
                                className="card-text",style = {'font-family': 'cursive', 'font-size': '10px', 'justifyContent': 'right' }
                            ),
                            # html.Small(
                            #     "Last updated 3 mins ago",
                            #     className="card-text text-muted",
                            # ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px"},
)



row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color="light", outline=True)),
        dbc.Col(dbc.Card(card_content1, color="light", outline=True)),
        #dbc.Col(dbc.Card(card_content, color="info", outline=True)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content2, color="light", outline=True)),
        dbc.Col(dbc.Card(card_content3, color="light", outline=True)),
       
        #dbc.Col(dbc.Card(card_content, color="danger", outline=True)),
    ],
    className="mb-4",
)

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content4, color="light", outline=True)),
        dbc.Col(dbc.Card(card_content5, color="light", outline=True)),
        html.Br()
    ]
)

layout = html.Div([card, row_1 , html.Br(), row_2, html.Br(), row_3,  html.Br(), html.Br()])

