import dash
import pandas as pd
import numpy as np
from dash import dcc, html, callback, Output, Input, dash_table
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

# To create meta tag for each page, define the title, image, and description.
dash.register_page (__name__,
                    path = '/electricidade', #  is home page and it represents the url
                    name = "Electricidade", # name of page, commonly used as name of link
                    title='Electricidade',  # title that appears on browser's tab
                    #image='pg1.png',  # image in the assets folder
                    description="Índices e variações do sector da Electricidade"

                    )

# Fazer leitura da dataframe do industria
electricidade_df = pd.read_csv('resultados por sector de actividade.csv', low_memory=False, encoding="iso-8859-1",  dtype= {'CAE': np.object_})

electricidade_df = electricidade_df[electricidade_df["Sector de actividade"] == "Electricidade"]

#comercio_df = pd.read_csv('resultados_comercio.csv', low_memory=False, encoding="iso-8859-1")


# melting a dataframe do comercio
electricidade_df_melted = pd.melt(electricidade_df, id_vars =['CAE', 'Descrição do código da CAE',\
                                                    'Distribuição do peso da divisão e grupo',\
                                                    'Nível de codificação', 'Tipo de resultados',\
                                                    'Categoria', 'Ano'],\
                                          value_vars =['Jan', 'Fev', 'Mar', 'Abr',  'Mai', 'Jun',\
                                                         'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
                                          var_name ='Meses', value_name ='Resultado')

# Creating new variable "Mes/Ano"
electricidade_df_melted["Mes/Ano"]= electricidade_df_melted["Meses"]+"-"+[x[2:] for x in electricidade_df_melted["Ano"].astype(str)]

# Funcação para mostrar um grafico vazio
def make_empty_fig():
    fig = go.Figure()
    fig.layout.paper_bgcolor = "#eeeeee" #'#E5ECF6'
    fig.layout.plot_bgcolor = "#eeeeee" #'#E5ECF6'
    return fig

layout = html.Div(
    [
        html.H6('Resultados do índice no sector da electricidade', style = {'font-family': 'Source Sans Pro', 'font-size': '16px',
                                                            'justifyContent': 'right', 'textAlign': 'center',"font-weight": "bold"}),
        dbc.Row(
            [
                dbc.Col([
                        html.H6('Selecione os campos abaixo para poder verificar e analisar os resultados desejados:', 
                                style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),
                        html.Hr(),

                        dbc.Label('Selecione o ano:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify',"font-weight": "bold" }),
                        dcc.Dropdown(id='ano_id_ele', value=electricidade_df["Ano"].max(),
                        placeholder='Anos',
                        multi=False,
                        options=[{'label': ano, 'value': ano}
                                  for ano in electricidade_df["Ano"].unique()]),
                        html.Hr(),

                        
                        dbc.Label('Selecione o tipo de resultados:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),
                        
                        dcc.RadioItems(id='resultados_id_ele', value=list(electricidade_df["Tipo de resultados"].unique())[0], 
                                       options=[{'label': html.Div(tipo,style={'color': '', 'padding-left': 10,\
                                                            'font-family': 'Source Sans Pro', 'font-size': '12px'}), 'value': tipo, }
                                  for tipo in electricidade_df['Tipo de resultados'].unique()], inline=False,
                                  
                                  inputStyle={'cursor': 'pointer'},                                        
                                  labelStyle={"display": "flex", 'padding': '0.5rem', 'margin-left':'5px'}
                                      ),

                        html.Hr(),
                        dbc.Label('Selecione a(s) categoria(s) de resultados:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),

                        dcc.Checklist(id='categoria_id_ele', 
                                       options=[{'label': html.Div(categoria,style={'color': '', 'padding-left': 10,\
                                                            'font-family': 'Source Sans Pro', 'font-size': '12px'}), 'value': categoria, }
                                  for categoria in electricidade_df['Categoria'].unique()], inline=False,
                                  inputStyle={'cursor': 'pointer'}, 
                                  labelStyle={"display": "flex", 'padding': '0.5rem', 'margin-left':'5px'}
                                  ),

                        html.Hr(),
                        dbc.Label('Selecione o nível da CAE-Rev.2 que pretende verificar os resultados:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),

                        dcc.RadioItems(id='nivel_id_ele', #value='Secção', 
                                   options=[{'label': html.Div(categoria,style={'color': '', 'padding-left': 10,\
                                                        'font-family': 'Source Sans Pro', 'font-size': '12px'}), 'value': categoria, }
                              for categoria in list(filter(lambda x: x != "Grupo", electricidade_df['Nível de codificação'].unique()))], inline=False,
                              

                                inputStyle={'cursor': 'pointer'}, 
                                labelStyle={"display": "flex", 'padding': '0.5rem', 'margin-left':'5px'}
                                ),

                        html.Hr(),
                        dcc.Checklist(id='nivel_options_id_ele', className="checklist" ),


                ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2 ),

                dbc.Col(
                        [
                        dbc.Row([

                            dbc.Col(
                                [
                                html.H6('Volume de negócios:', style = {"textAlign": "left", 'font-family': 'Source Sans Pro',"font-size":" 1.2em"}),                                 
                                dcc.Graph(id='ind_var_vvn_c_ele', style={'width': '100%','display': 'inline-block',},
                                config = {'modeBarButtonsToRemove':["zoom2d", "select2d", "lasso2d", "resetscale2d"],
                                'modeBarButtonsToAdd' : ['toImage','pan2d', 'autoScaled2d', 'zoomIn2d', 'zoomOut2d'],
                                    },

                                figure=make_empty_fig())
                                ], align="center"),


                            dbc.Col(
                                [
                                html.H6('Emprego:', style = {"textAlign": "left", 'font-family': 'Source Sans Pro',"font-size":" 1.2em"}),                                 
                                dcc.Graph(id='ind_var_nps_c_ele', style={'width': '100%','display': 'inline-block',},
                                config = {'modeBarButtonsToRemove':["zoom2d", "select2d", "lasso2d", "resetscale2d"],
                                'modeBarButtonsToAdd' : ['toImage','pan2d', 'autoScaled2d', 'zoomIn2d', 'zoomOut2d'],
                                    },

                                figure=make_empty_fig())
                                ], align="center"),
                                    ]),

                        dbc.Row([

                            dbc.Col(
                                [
                                html.H6('Remunerações:', style = {"textAlign": "left", 'font-family': 'Source Sans Pro',"font-size":" 1.2em"}),                                 
                                dcc.Graph(id='ind_var_rem_c_ele', style={'width': '100%','display': 'inline-block',},
                                config = {'modeBarButtonsToRemove':["zoom2d", "select2d", "lasso2d", "resetscale2d"],
                                'modeBarButtonsToAdd' : ['toImage','pan2d', 'autoScaled2d', 'zoomIn2d', 'zoomOut2d'],
                                    },

                                figure=make_empty_fig())
                                ], align="center"),


                            dbc.Col(
                                [
                                html.H6('Horas trabalhadas:', style = {"textAlign": "left", 'font-family': 'Source Sans Pro',"font-size":" 1.2em"}),                                 
                                dcc.Graph(id='ind_var_horas_c_ele', style={'width': '100%','display': 'inline-block',},
                                config = {'modeBarButtonsToRemove':["zoom2d", "select2d", "lasso2d", "resetscale2d"],
                                'modeBarButtonsToAdd' : ['toImage','pan2d', 'autoScaled2d', 'zoomIn2d', 'zoomOut2d'],
                                    },

                                figure=make_empty_fig())
                                ], align="center"),
                                    ])
                        ], align="center", xs=10, sm=10, md=10, lg=10, xl=10, xxl=10
                    )    
            ] ,style = {'font-family': 'Source Sans Pro', 'font-size': '11px', 'justifyContent': 'right' }            
                ),
        html.Hr(),

# Bloco dos comentários:
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label('Descrição do código da CAE consoante o (a):',
                                  style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                        'justifyContent': 'right', "text-justify": "inter-word",
                                        'textAlign': 'justify', "font-weight": "bold"}),

                            html.Div(id='descricao_id_ele'),

                    ],  className='column_left', xs=2, sm=2, md=2, lg=2, xl=2, xxl=2),
                
                dbc.Col(
                    [
                        # Vai ficar a tabela da descrição
                        dash_table.DataTable(id="tabela_descricao_id_ele",
                                  columns=[{"name":i, "id":i,
                                  "selectable":True, 
                                  } for i in electricidade_df[["CAE", "Descrição do código da CAE"]].columns 
                                  ], data= "",                                  

                                  #filter_action= "native",
                                  page_action= "native",
                                  page_current=0,
                                  page_size=6,
                                  #style_cell={"minWidth":100, "maxWidth":100, "width":100, "padding": "0.5px"}, # O estilo sera aplicado em toda tabela
                                  #export_format="csv",
                                  style_cell_conditional=[
                                            {
                                                "if": {"column_id":c},
                                                "textAlign": "left"
                                            } for c in ["CAE", "Descrição do código da CAE"] # O estilo sera aplicado somente nas tabelas escolhidas
                                  ], 
                                  style_data= {
                                        "whiteSpace": "normal",
                                        "height":"auto",
                                        'font-size': '11px',
                                  },
                                  style_as_list_view= True,
                                  style_header={
                                            "backgroundColor": "rgb(230, 230, 230)",
                                            'font-size': '11px',
                                            "fontWeight": "bold",
                                            "border": "0.8px solid black"
                                  },
                                  style_table = { "overflowY":"auto"},#"height": "420px",
                                  #fixed_rows = {"headers": True, },
                                  style_data_conditional=[
                                        {
                                            "if": {"row_index": "odd"},
                                            "backgroundColor": "rgb(248, 248, 248)"
                                        } ]
                                )

                    ], align="center", xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
            ],style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right' }   
                ),
 
        # Uma linha para separar os resultados do VVN com o do NPS
        html.Hr(),#style={"height:2px;border-width:0;color:gray;background-color:gray"}),

# Criação do bloco aonde ira ficar a tabela com a informação dos indices.
        dbc.Row(
            [
                dbc.Col(
                    [

                        html.H6('Selecione os campos abaixo para poder exportar e analisar os dados desejados:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),                        
                        html.Br(),
                        html.Br(), 

                        dcc.Dropdown(id='nivel_id_c_ele',   
                        placeholder='Selecione o nível',
                        multi=False,
                        options=[{'label': nivel, 'value': nivel}
                                  for nivel in electricidade_df["Nível de codificação"].unique()]),
                        
                        html.Br(), 
                        html.Br(), 

                        dcc.Dropdown(id='tipo_resultados_id_c_ele',   
                        placeholder='Selecione o tipo de resultados',
                        multi=False,
                        options=[{'label': tipo_resultados, 'value': tipo_resultados}
                                  for tipo_resultados in electricidade_df['Tipo de resultados'].unique()]),

                        html.Br(),
                        html.Br(), 

                        dcc.Dropdown(id='categoria_id_c_ele',
                        placeholder='Selecione a categoria de resultados',
                        multi=False,
                        options=[{'label': categoria, 'value': categoria}
                                  for categoria in electricidade_df["Categoria"].unique()]),

                        html.Br(),
                        html.Br(), 

                        dcc.Dropdown(id='ano_id_c_ele',
                        placeholder='selecione o ano',
                        multi=False,
                        options=[{'label': ano, 'value': ano}
                                  for ano in electricidade_df["Ano"].unique()]),


                    ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2),
                
                dbc.Col(
                    [
                        dash_table.DataTable(id="tabela_comercio_id_ele",
                                  columns=[{"name":i, "id":i,
                                  "selectable":True, "hideable":True,# "presentation":"dropdown"
                                  }\
                                    for i in list(filter(lambda i: i not in ["Sector de actividade", "Distribuição do peso da divisão e grupo"], electricidade_df.columns))
                                  ], data= electricidade_df.to_dict("records"),                                  

                                  #filter_action= "native",
                                  page_action= "native",
                                  page_current=0,
                                  page_size=12,
                                  #style_cell={"minWidth":100, "maxWidth":100, "width":100, "padding": "0.5px"}, # O estilo sera aplicado em toda tabela
                                  export_format="csv",
                                  style_cell_conditional=[
                                            {
                                                "if": {"column_id":c},
                                                "textAlign": "left"
                                            } for c in ["Categoria", "Tipo de Indices"] # O estilo sera aplicado somente nas tabelas escolhidas
                                  ], 
                                  style_data= {
                                        "whiteSpace": "normal",
                                        "height":"auto",
                                        'font-size': '11px',
                                  },
                                  style_as_list_view= True,
                                  style_header={
                                            "backgroundColor": "rgb(230, 230, 230)",
                                            'font-size': '11px',
                                            "fontWeight": "bold",
                                            "border": "0.8px solid black"
                                  },
                                  style_table = {"height": "420px", "overflowY":"auto"},
                                  #fixed_rows = {"headers": True, },
                                  style_data_conditional=[
                                        {
                                            "if": {"row_index": "odd"},
                                            "backgroundColor": "rgb(248, 248, 248)"
                                        } ]
                                )
                    ], xs=10, sm=10, md=10, lg=10, xl=10, xxl=10),
        
                    html.Hr(),

            ], justify="center", align="left", style = {'font-family':'Source Sans Pro', 'font-size':'11px','justifyContent': 'right' }    
                ),
    ]           
                ),


# @callback(
#     Output('nivel_options_id', 'options'),
#     Input('nivel_id', 'value'))
# def set_cities_options(selected_country):

#     df = comercio_df.copy()
#     df= df[df["Nível de codificação"]==selected_country]
#     return [{'label': categoria, 'value': categoria, } for categoria in df['Descrição do código da CAE'].unique()]


    # print([{'label': i, 'value': i} for i in df[df["Nível de codificação"]==selected_country]['Descrição do código da CAE']])
    # return [{'label': i, 'value': i} for i in df[df["Nível de codificação"]==selected_country]['Descrição do código da CAE'].unique()]



# CallBack das opções do nível da CAE-Rev.2 
@callback(Output('nivel_options_id_ele', 'options'),
                Output('nivel_options_id_ele', 'inline'),
                Output('nivel_options_id_ele', 'inputStyle'),
                Output('nivel_options_id_ele', 'labelStyle'),  
                Input('nivel_id_ele', 'value'))

def opcoes_nivel_cae(nivel):
    df = electricidade_df.copy()

    
    # Filtrando a base de dados pelo ano e o tipo de resultados
    df = df[df['Nível de codificação'] == nivel]


    return [{'label': html.Div(categoria,style={'color': '', 'padding-left': 5,\
                                                            'font-family': 'Source Sans Pro', 'font-size': '12px'}), 'value': categoria, }
                                  for categoria in list(df['CAE'].unique())], True, {'cursor': 'pointer'}, {"display": "flex", 'padding': '0.5rem', 'margin-left':'5px', }
    
    
# CallBack dos comentarios-1
@callback(Output('descricao_id_ele', 'children'),
              Input('nivel_id_ele', 'value'),)

def data_dos_comentarios(nivel):
    

    if nivel is None: raise PreventUpdate

    text1= html.H6(nivel, style = {'font-family': 'Source Sans Pro', 'font-size': '13px', 'justifyContent': 'right', "font-weight": "bold" }  )


    return text1,


#CallBack da tabela com a descrição da CAE
@callback(Output("tabela_descricao_id_ele", 'data'),
              Input('nivel_id_ele', 'value'),)

def data_table_update(nivel):
    
    # Copiando a dataset
    df = electricidade_df.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    if nivel is None: raise PreventUpdate
    df = df[df["Nível de codificação"] == nivel]
    df = df[["CAE", "Descrição do código da CAE"]].drop_duplicates() 

    return df.to_dict("records")


# CallBack dos resultados do volume de negócios 
@callback(Output('ind_var_vvn_c_ele', 'figure'),
              Input('ano_id_ele', 'value'),
              Input('resultados_id_ele', 'value'), 
              Input('categoria_id_ele', 'value'),
              Input('nivel_id_ele', 'value'),        
              Input('nivel_options_id_ele', 'value'))

# Resultados do volume de negócios
def resultado_vvn(ano, resultados, categoria, nivel, opcoes):
    
    # Copiando a dataset
    df = electricidade_df_melted.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    df_ = df[(df["Ano"] == ano) & (df['Tipo de resultados'] == resultados) & (df["Nível de codificação"] == nivel)]

    # filtrando a base de dados pela categoria de resultados e pelos sectores de actividade  tipos de indices e indicadores
    # para que tenha somente resultados do Volume de Negócios
    df2 = df_[df_['Categoria'].isin(categoria)]
    df2 = df2[df2["CAE"].isin(opcoes)]

    # filtrando a base de dados para que tenha somente resultados do Volume de Negócios
    df_vvn = df2[ df2['Categoria'] == "Volume de negócios"]

    # Condição para actualizar o grafico
    # if "Volume de Negócios" not in categoria: raise PreventUpdate

    # Grafico do volume de negocios 
    fig = px.scatter(df_vvn, x='Mes/Ano', y="Resultado", color='CAE', text= df_vvn["Resultado"], #custom_data= 
                      hover_data=['Resultado'], hover_name=df_vvn['Tipo de resultados'],
                 title='<br><b>' + ', '.join(opcoes) + '</b>')
    
    fig_lines = px.line(df_vvn, x='Mes/Ano', y="Resultado", color='CAE')
    for trace in fig_lines.data:
        trace.showlegend = False
        fig.add_trace(trace)

     # Actualizando o layout (inicio)
    fig.update_layout(modebar_orientation="h")
    fig.update_layout(
             plot_bgcolor="rgba(0, 0, 0, 0)",
             paper_bgcolor="rgba(0, 0, 0, 0)",
             title={
                'text':'<b>'+resultados+'</b>'+" mensais<br>em "+ f'{ano}'+" no(s)<br>sectore(s):" ,
                'y': 0.98,
                'x': 0.01,
                'xanchor': 'left',
                'yanchor': 'top'},
             titlefont={
                        #'color': "black",#7'white',
                        "family":"sans-serif",
                        'size': 10},

             hovermode='closest',
             margin = dict(t = 5, l = 0, r = 0),

             xaxis = dict(title = '<b></b>',
                          visible = True,
                          color = "gray",
                          showline = True,
                          showgrid = False,
                          showticklabels = True,
                          linecolor = "black",
                          linewidth = 2,
                          ticks = 'outside',
                          tickfont = dict(
                             family = "sans-serif",
                             size = 10,
                             color ="black" )
                         ),

             yaxis = dict(title = '<b></b>',
                          visible = True,
                          color = 'orange',
                          showline = False,
                          showgrid = True,
                          gridcolor='grey',
                          showticklabels = False,
                          linecolor = 'orange',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = "sans-serif",
                             size = 10,
                             color = 'orange')
                         ),

            legend = {
                'title': '',
                'orientation': 'h',
                'bgcolor': "rgba(0, 0, 0, 0)",
                'x': 1.0,
                'y': 1.15,
                'xanchor': 'right',
                'yanchor': 'top'},

            font = dict(
                family = "sans-serif",
                size = 10,
                color = "black")
    )
    fig.update_traces(textposition='top center', textfont_size=8)
    return fig


# CallBack dos resultados do emprego
@callback(Output('ind_var_nps_c_ele', 'figure'),
              Input('ano_id_ele', 'value'),
              Input('resultados_id_ele', 'value'), 
              Input('categoria_id_ele', 'value'),
              Input('nivel_id_ele', 'value'),        
              Input('nivel_options_id_ele', 'value'))

# Resultados do emprego
def resultado_nps(ano, resultados, categoria, nivel, opcoes):
    
    # Copiando a dataset
    df = electricidade_df_melted.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    df_ = df[(df["Ano"] == ano) & (df['Tipo de resultados'] == resultados) & (df["Nível de codificação"] == nivel)]

    # filtrando a base de dados pela categoria de resultados e pelos sectores de actividade  tipos de indices e indicadores
    # para que tenha somente resultados do emprego
    df2 = df_[df_['Categoria'].isin(categoria)]
    df2 = df2[df2["CAE"].isin(opcoes)]

    # filtrando a base de dados para que tenha somente resultados do emprego
    df_nps = df2[ df2['Categoria'] == "Emprego"]

    # Condição para actualizar o grafico
    # if "Volume de Negócios" not in categoria: raise PreventUpdate

    # Grafico do emprego 
    fig = px.scatter(df_nps, x='Mes/Ano', y="Resultado", color='CAE', text= df_nps["Resultado"], #custom_data= 
                      hover_data=['Resultado'], hover_name= df_nps['Tipo de resultados'],
                 title='<br><b>' + ', '.join(opcoes) + '</b>')
    
    fig_lines = px.line(df_nps, x='Mes/Ano', y="Resultado", color='CAE')
    for trace in fig_lines.data:
        trace.showlegend = False
        fig.add_trace(trace)

     # Actualizando o layout (inicio)
    fig.update_layout(modebar_orientation="h")
    fig.update_layout(
             plot_bgcolor="rgba(0, 0, 0, 0)",
             paper_bgcolor="rgba(0, 0, 0, 0)",
             title={
                'text':'<b>'+resultados+'</b>'+" mensais<br>em "+ f'{ano}'+" no(s)<br>sectore(s):" ,
                'y': 0.98,
                'x': 0.01,
                'xanchor': 'left',
                'yanchor': 'top'},
             titlefont={
                        #'color': "black",#7'white',
                        "family":"sans-serif",
                        'size': 10},

             hovermode='closest',
             margin = dict(t = 5, l = 0, r = 0),

             xaxis = dict(title = '<b></b>',
                          visible = True,
                          color = "gray",
                          showline = True,
                          showgrid = False,
                          showticklabels = True,
                          linecolor = "black",
                          linewidth = 2,
                          ticks = 'outside',
                          tickfont = dict(
                             family = "sans-serif",
                             size = 10,
                             color ="black" )
                         ),

             yaxis = dict(title = '<b></b>',
                          visible = True,
                          color = 'orange',
                          showline = False,
                          showgrid = True,
                          gridcolor='grey',
                          showticklabels = False,
                          linecolor = 'orange',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = "sans-serif",
                             size = 10,
                             color = 'orange')
                         ),

            legend = {
                'title': '',
                'orientation': 'h',
                'bgcolor': "rgba(0, 0, 0, 0)",
                'x': 1.0,
                'y': 1.15,
                'xanchor': 'right',
                'yanchor': 'top'},

            font = dict(
                family = "sans-serif",
                size = 10,
                color = "black")
    )
    fig.update_traces(textposition='top center', textfont_size=8)
    return fig

# CallBack dos resultados do remunerações
@callback(Output('ind_var_rem_c_ele', 'figure'),
              Input('ano_id_ele', 'value'),
              Input('resultados_id_ele', 'value'), 
              Input('categoria_id_ele', 'value'),
              Input('nivel_id_ele', 'value'),        
              Input('nivel_options_id_ele', 'value'))

# Resultados do remunerações
def resultado_rem(ano, resultados, categoria, nivel, opcoes):
    
    # Copiando a dataset
    df = electricidade_df_melted.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    df_ = df[(df["Ano"] == ano) & (df['Tipo de resultados'] == resultados) & (df["Nível de codificação"] == nivel)]

    # filtrando a base de dados pela categoria de resultados e pelos sectores de actividade  tipos de indices e indicadores
    # para que tenha somente resultados do remunerações
    df2 = df_[df_['Categoria'].isin(categoria)]
    df2 = df2[df2["CAE"].isin(opcoes)]

    # filtrando a base de dados para que tenha somente resultados do remunerações
    df_nps = df2[ df2['Categoria'] == 'Remunerações']

    # Condição para actualizar o grafico
    # if "Volume de Negócios" not in categoria: raise PreventUpdate

    # Grafico do remunerações
    fig = px.scatter(df_nps, x='Mes/Ano', y="Resultado", color='CAE', text= df_nps["Resultado"], #custom_data= 
                      hover_data=['Resultado'], hover_name= df_nps['Tipo de resultados'],
                 title='<br><b>' + ', '.join(opcoes) + '</b>')
    
    fig_lines = px.line(df_nps, x='Mes/Ano', y="Resultado", color='CAE')
    for trace in fig_lines.data:
        trace.showlegend = False
        fig.add_trace(trace)

     # Actualizando o layout (inicio)
    fig.update_layout(modebar_orientation="h")
    fig.update_layout(
             plot_bgcolor="rgba(0, 0, 0, 0)",
             paper_bgcolor="rgba(0, 0, 0, 0)",
             title={
                'text':'<b>'+resultados+'</b>'+" mensais<br>em "+ f'{ano}'+" no(s)<br>sectore(s):" ,
                'y': 0.98,
                'x': 0.01,
                'xanchor': 'left',
                'yanchor': 'top'},
             titlefont={
                        #'color': "black",#7'white',
                        "family":"sans-serif",
                        'size': 10},

             hovermode='closest',
             margin = dict(t = 5, l = 0, r = 0),

             xaxis = dict(title = '<b></b>',
                          visible = True,
                          color = "gray",
                          showline = True,
                          showgrid = False,
                          showticklabels = True,
                          linecolor = "black",
                          linewidth = 2,
                          ticks = 'outside',
                          tickfont = dict(
                             family = "sans-serif",
                             size = 10,
                             color ="black" )
                         ),

             yaxis = dict(title = '<b></b>',
                          visible = True,
                          color = 'orange',
                          showline = False,
                          showgrid = True,
                          gridcolor='grey',
                          showticklabels = False,
                          linecolor = 'orange',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = "sans-serif",
                             size = 10,
                             color = 'orange')
                         ),

            legend = {
                'title': '',
                'orientation': 'h',
                'bgcolor': "rgba(0, 0, 0, 0)",
                'x': 1.0,
                'y': 1.15,
                'xanchor': 'right',
                'yanchor': 'top'},

            font = dict(
                family = "sans-serif",
                size = 10,
                color = "black")
    )
    fig.update_traces(textposition='top center', textfont_size=8)
    return fig

# CallBack dos resultados das horas trabalhada
@callback(Output('ind_var_horas_c_ele', 'figure'),
              Input('ano_id_ele', 'value'),
              Input('resultados_id_ele', 'value'), 
              Input('categoria_id_ele', 'value'),
              Input('nivel_id_ele', 'value'),        
              Input('nivel_options_id_ele', 'value'))

# Resultados das horas trabalhadas
def resultado_horas(ano, resultados, categoria, nivel, opcoes):
    
    # Copiando a dataset
    df = electricidade_df_melted.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    df_ = df[(df["Ano"] == ano) & (df['Tipo de resultados'] == resultados) & (df["Nível de codificação"] == nivel)]

    # filtrando a base de dados pela categoria de resultados e pelos sectores de actividade  tipos de indices e indicadores
    # para que tenha somente resultados do horas trabalhadas
    df2 = df_[df_['Categoria'].isin(categoria)]
    df2 = df2[df2["CAE"].isin(opcoes)]

    # filtrando a base de dados para que tenha somente resultados do horas trabalhadas
    df_nps = df2[ df2['Categoria'] == 'Horas trabalhadas']

    # Condição para actualizar o grafico
    # if "Volume de Negócios" not in categoria: raise PreventUpdate

    # Grafico do horas trabalhadas
    fig = px.scatter(df_nps, x='Mes/Ano', y="Resultado", color='CAE', text= df_nps["Resultado"], #custom_data= 
                      hover_data=['Resultado'], hover_name= df_nps['Tipo de resultados'],
                 title='<br><b>' + ', '.join(opcoes) + '</b>')
    
    fig_lines = px.line(df_nps, x='Mes/Ano', y="Resultado", color='CAE')
    for trace in fig_lines.data:
        trace.showlegend = False
        fig.add_trace(trace)

     # Actualizando o layout (inicio)
    fig.update_layout(modebar_orientation="h")
    fig.update_layout(
             plot_bgcolor="rgba(0, 0, 0, 0)",
             paper_bgcolor="rgba(0, 0, 0, 0)",
             title={
                'text':'<b>'+resultados+'</b>'+" mensais<br>em "+ f'{ano}'+" no(s)<br>sectore(s):" ,
                'y': 0.98,
                'x': 0.01,
                'xanchor': 'left',
                'yanchor': 'top'},
             titlefont={
                        #'color': "black",#7'white',
                        "family":"sans-serif",
                        'size': 10},

             hovermode='closest',
             margin = dict(t = 5, l = 0, r = 0),

             xaxis = dict(title = '<b></b>',
                          visible = True,
                          color = "gray",
                          showline = True,
                          showgrid = False,
                          showticklabels = True,
                          linecolor = "black",
                          linewidth = 2,
                          ticks = 'outside',
                          tickfont = dict(
                             family = "sans-serif",
                             size = 10,
                             color ="black" )
                         ),

             yaxis = dict(title = '<b></b>',
                          visible = True,
                          color = 'orange',
                          showline = False,
                          showgrid = True,
                          gridcolor='grey',
                          showticklabels = False,
                          linecolor = 'orange',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = "sans-serif",
                             size = 10,
                             color = 'orange')
                         ),

            legend = {
                'title': '',
                'orientation': 'h',
                'bgcolor': "rgba(0, 0, 0, 0)",
                'x': 1.0,
                'y': 1.15,
                'xanchor': 'right',
                'yanchor': 'top'},

            font = dict(
                family = "sans-serif",
                size = 10,
                color = "black")
    )
    fig.update_traces(textposition='top center', textfont_size=8)
    return fig

#CallBack da tabela a ser exportada
@callback(Output("tabela_comercio_id_ele", 'data'),
              Input('nivel_id_c_ele', 'value'),
              Input('tipo_resultados_id_c_ele', 'value'), 
              Input('categoria_id_c_ele', 'value'),
              Input('ano_id_c_ele', 'value'))

def data_table_update(nivel, resultados, categoria, ano):
    
    # Copiando a dataset
    df = electricidade_df.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    if nivel:
        df = df[df["Nível de codificação"] == nivel]

    # Filtrando a base de dados pelo ano e o tipo de resultados
    if resultados:
        df = df[df["Tipo de resultados"] == resultados]

    # Filtrando a base de dados pelo ano e o tipo de resultados
    if categoria:
        df = df[df['Categoria'] == categoria]     

    # Filtrando a base de dados pelo ano 
    if ano:
        df = df[df["Ano"] == ano] 

    return df.to_dict("records")         