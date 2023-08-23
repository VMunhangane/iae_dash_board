import dash
import pandas as pd
import numpy as np
from dash import dcc, html, callback, Output, Input, dash_table
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
#from dash import 

# To create meta tag for each page, define the title, image, and description.
dash.register_page (__name__,
                    path = '/', #  is home page and it represents the url
                    name = "Síntese do IAE", # name of page, commonly used as name of link
                    title='Síntese IAE',  # title that appears on browser's tab
                    #image='pg1.png',  # image in the assets folder
                    description="Síntese do IAE"

                    )


# Temos que carregar a base com a informação da síntese
indices_df = pd.read_csv('indices_89_90_91.csv', low_memory=False, encoding="iso-8859-1")
sectores_var = list(indices_df.columns[6:])
# Fazer leitura da dataframe do comercio
comercio_df = pd.read_csv('resultados por sector de actividade.csv', low_memory=False, encoding="iso-8859-1", dtype= {'CAE': np.object_})


indices_df_melted=indices_df.melt(id_vars=["Categoria","Tipo de Indices ","Ano","date"], value_vars= sectores_var, var_name='indicadores')


# Funcação para mostrar um grafico vazio
def make_empty_fig():
    fig = go.Figure()
    fig.layout.paper_bgcolor = "#eeeeee" #'#E5ECF6'
    fig.layout.plot_bgcolor = "#eeeeee" #'#E5ECF6'

    return fig

# Vamos configurar o layout
layout = html.Div(
    [
        html.H6('Resultados do índice de actividade económica', style = {'font-family': 'Source Sans Pro', 'font-size': '16px',
                                                            'justifyContent': 'right', 'textAlign': 'center',"font-weight": "bold"}),
        dbc.Row(
            [
                
                dbc.Col(
                    
                    [
                        html.H6('Selecione os campos abaixo para poder verificar e analisar os resultados desejados:', 
                                                     style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),
                        html.Hr(),

                        dbc.Label('Selecione o ano:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify',"font-weight": "bold" }),
                        dcc.Dropdown(id='ano_id',value=indices_df["Ano"].max(),
                        placeholder='Anos',
                        multi=False,
                        options=[{'label': ano, 'value': ano}
                                  for ano in indices_df["Ano"].unique()]),
                        html.Hr(),

                        dbc.Label('Selecione o tipo de resultados:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),
                        dcc.RadioItems(id='resultados_id', value=list(indices_df.Categoria.unique())[0], 
                                       options=[{'label': html.Div(categoria,style={'color': '', 'padding-left': 10,\
                                                            'font-family': 'Source Sans Pro', 'font-size': '12px'}), 'value': categoria, }
                                  for categoria in indices_df['Categoria'].unique()], inline=False,
                                  
                                  inputStyle={'cursor': 'pointer'},                                        
                                  labelStyle={"display": "flex", 'padding': '0.5rem',
                                                                              'margin-left':'5px'}
                                      ),

                        html.Hr(),
                        dbc.Label('Selecione a(s) cactegoria(s) de resultados:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),

                        
                        #labelStyle={'padding': '0.5rem 4.6rem'}
                        dcc.Checklist(id='categoria_id', 
                                       options=[{'label': html.Div(categoria,style={'color': '', 'padding-left': 10,\
                                                            'font-family': 'Source Sans Pro', 'font-size': '12px'}), 'value': categoria, }
                                  for categoria in comercio_df['Categoria'].unique()], inline=False,
                                  inputStyle={'cursor': 'pointer'}, labelStyle={"display": "flex", 'padding': '0.5rem',
                                                                              'margin-left':'5px'}#labelStyle={'padding': '0.5rem 4.6rem'}
                                  ),

                        html.Hr(),
                        dbc.Label('Selecione os sectores de actividade económica:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),


                        dcc.Checklist(id='sectores_id', 
                        options=[{'label': html.Div(sector, style={'color': '', 'padding-left': 10,\
                                                    'font-family': 'Source Sans Pro', 'font-size': '12px'}), 'value': sector, }
                            for sector in sectores_var], inline=False,
                            inputStyle={'cursor': 'pointer'}, labelStyle={"display": "flex", 'padding': '0.5rem',
                                                                        'margin-left':'5px'}#labelStyle={'padding': '0.5rem 4.6rem'}
                            ),

                        

                        # dcc.Checklist( 
                        #         [
                        #             {
                        #                 "label": html.Div(['Global'], style={'color': '', 'padding-left': 10,\
                        #                                                         'font-family': 'Source Sans Pro', 'font-size': '12px',}),
                        #                 "value": 'Global',
                        #             },
                        #             {
                        #                 "label": html.Div(['Indústria'], style={'color': '', 'padding-left': 10,\
                        #                                                         'font-family': 'Source Sans Pro', 'font-size': '12px'}),
                        #                 "value": 'Indústria',
                        #             },
                        #             {
                        #                 "label": html.Div(['Energia '], style={'color': '', 'padding-left': 10,\
                        #                                                        'font-family': 'Source Sans Pro', 'font-size': '12px'}),
                        #                 "value": 'Energia ',
                        #             },

                        #             {
                        #                 "label": html.Div(['Comércio'], style={'color': '', 'padding-left': 10,\
                        #                                                        'font-family': 'Source Sans Pro', 'font-size': '12px'}),
                        #                 "value": 'Comércio',
                        #             },

                        #             {
                        #                 "label": html.Div(['Transportes'], style={'color': '','padding-left': 10,\
                        #                                                           'font-family': 'Source Sans Pro', 'font-size': '12px'}),
                        #                 "value": 'Transportes',
                        #             },
                        #             {
                        #                 "label": html.Div(['Turismo'], style={'color': '', 'padding-left': 10,\
                        #                                                       'font-family': 'Source Sans Pro', 'font-size': '12px'}),
                        #                 "value": 'Turismo',
                        #             },
                        #             {
                        #                 "label": html.Div(['Outros Serviços'], style={'color': '','padding-left': 10,\
                        #                                                               'font-family': 'Source Sans Pro', 'font-size': '12px'}),
                        #                 "value": 'Outros Serviços',
                        #             },

                        #         ], 
                        #         inputStyle={'cursor': 'pointer'}, labelStyle={"display": "flex", 'padding': '0.5rem', 'margin-left':'5px'}, 
                        #         id='sectores_id',
                        #         #labelStyle={"display": "flex", "align-items": "center"},
                        #     )


                    ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2),
                html.Br(),
                dbc.Col(
                    [
            
                    dbc.Row([
                    # Preparando o gráfico do volume de negócios            
                            dbc.Col(
                                [
                                html.H6('Volume de negócios:', style = {"textAlign": "left", 'font-family': 'Source Sans Pro',"font-size":" 1.2em"}),                                 
                                dcc.Graph(id='ind_var_vvn', style={'width': '100%','display': 'inline-block',},
                                config = {'modeBarButtonsToRemove':["zoom2d", "select2d", "lasso2d", "resetscale2d"],
                                'modeBarButtonsToAdd' : ['toImage','pan2d', 'autoScaled2d', 'zoomIn2d', 'zoomOut2d'],
                                    },
                                figure=make_empty_fig())
                                ], align="center"),

                # Preparando o gráfico do emprego
                            dbc.Col(
                                [
                                html.H6('Emprego:', 
                                style = {"textAlign": "left", 'font-family': 'Source Sans Pro', "font-size":" 1.2em"}),

                                dcc.Graph(id='ind_var_nps', style={'width': '100%','display': 'inline-block',},
                                config = {'modeBarButtonsToRemove':["zoom2d", "select2d", "lasso2d", "resetscale2d"],
                                          'modeBarButtonsToAdd' : ['toImage','pan2d', 'autoScaled2d', 'zoomIn2d', 'zoomOut2d'],
                                         },
                                figure=make_empty_fig())
                                ]),
                            ]),
                        
                        html.Br(),

                # Preparando o gráfico das remunerações
                        dbc.Row(
                            [
                            dbc.Col(
                                [
                                 html.H6('Remunerações:', 
                                         style = {"textAlign": "left", 'font-family': 'Source Sans Pro', "font-size":" 1.2em"}),
                                
                                dcc.Graph(id='ind_var_rem', style={'width': '100%','display': 'inline-block',},
                                config = {'modeBarButtonsToRemove':["zoom2d", "select2d", "lasso2d", "resetscale2d"],
                                    'modeBarButtonsToAdd' : ['toImage','pan2d', 'autoScaled2d', 'zoomIn2d', 'zoomOut2d'],
                                  },
                                figure=make_empty_fig())
                                ], align="center"),

                # Preparando o gráfico das horas trabalhadas
                            dbc.Col(
                                [
                                html.H6('Horas trabalhadas:', 
                                        style = {"textAlign": "left", 'font-family': 'Source Sans Pro', "font-size":" 1.2em"}),
                                
                                dcc.Graph(id='ind_var_horas',  style={'width': '100%','display': 'inline-block',},
                                config = {'modeBarButtonsToRemove':["zoom2d", "select2d", "lasso2d", "resetscale2d"],
                                    'modeBarButtonsToAdd' : ['toImage','pan2d', 'autoScaled2d', 'zoomIn2d', 'zoomOut2d'],
                                  },
                                figure=make_empty_fig())
                                ], align="center"),
                            ]),
                          
                    ], align="center", xs=10, sm=10, md=10, lg=10, xl=10, xxl=10),

            ],style = {'font-family': 'Source Sans Pro', 'font-size': '11px', 'justifyContent': 'right' }     
                ),
        html.Hr(),
         
        # Bloco dos comentários:
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label('Selecione o mês que pretende verificar os comentários dos resultados do índices de actividades económicas:',
                                  style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                        'justifyContent': 'right', "text-justify": "inter-word",
                                        'textAlign': 'justify', "font-weight": "bold"}),
                       
                        dcc.Dropdown(id='mes_id', placeholder='Selecione o mês', multi=False,
                             options=[
                            {'label': 'Janeiro', 'value': 1},
                            {'label': 'Fevereiro', 'value': 2},
                            {'label': 'Março', 'value': 3},
                            {'label': 'Abril', 'value': 4},
                            {'label': 'Maio', 'value': 5},
                            {'label': 'Junho', 'value': 6},
                            {'label': 'Julho', 'value': 7},
                            {'label': 'Agosto', 'value': 8},
                            {'label': 'Setembro', 'value': 9},
                            {'label': 'Outubro', 'value': 10},
                            {'label': 'Novembro', 'value': 11},
                            {'label': 'Dezembro', 'value': 12},
                                 ],
                            ),

                            html.Hr(),

                            html.Div(id='comentarios_id1'),

                    ],  className='column_left', xs=2, sm=2, md=2, lg=2, xl=2, xxl=2),
                
                dbc.Col(
                    [

                        html.Div(id='comentarios_id2'),

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
                        html.Br(),
                        html.H6('Selecione os campos abaixo para poder exportar e analisar os dados desejados:', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',\
                                                               'justifyContent': 'right', "text-justify": "inter-word",
                                                               'textAlign': 'justify', "font-weight": "bold"}),                        
                        html.Br(),


                        dcc.Dropdown(id='resultados_id2',   
                        placeholder='Selecione o tipo de resultados',
                        multi=False,
                        options=[{'label': tipo_resultado, 'value': tipo_resultado}
                                  for tipo_resultado in indices_df['Categoria'].unique()]),
                        
                        html.Br(), 

                        dcc.Dropdown(id='categoria_id2',   
                        placeholder='Selecione a cactegoria de resultados',
                        multi=False,
                        options=[{'label': tipo_categoria, 'value': tipo_categoria}
                                  for tipo_categoria in indices_df['Tipo de Indices '].unique()]),

                        html.Br(),

                        dcc.Dropdown(id='ano_id2',#value=indices_df["Ano"].max(),
                        placeholder='selecione o ano',
                        multi=False,
                        options=[{'label': ano, 'value': ano}
                                  for ano in indices_df["Ano"].unique()]),

                        html.Br(),


                    ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2),
                
                dbc.Col(
                    [
                        dash_table.DataTable(id="tabela_resultados_id",
                                  columns=[{"name":i, "id":i,
                                  "selectable":True, "hideable":True, "presentation":"dropdown"
                                  } for i in list(filter(lambda i: i not in ["Comentarios", "date"], indices_df.columns)) 
                                  ], data= indices_df.to_dict("records"),                                  

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

# CallBack dos resultados do volume de negócios 
@callback(Output('ind_var_vvn', 'figure'),
              Input('ano_id', 'value'),
              Input('resultados_id', 'value'), 
              Input('categoria_id', 'value'),        
              Input('sectores_id', 'value'))

# Resultados do volume de negócios
def resultado_vvn(ano, resultados, categoria, sector):
    
    # Copiando a dataset
    df_ = indices_df_melted.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    df_ano_resul = df_[(df_["Ano"] == ano) & (df_['Categoria'] == resultados)]

    # filtrando a base de dados pela categoria de resultados e pelos sectores de actividade  tipos de indices e indicadores
    # para que tenha somente resultados do Volume de Negócios
    df1 = df_ano_resul[df_ano_resul['Tipo de Indices '].isin(categoria)]
    df2 = df1[df1["indicadores"].isin(sector)]

    # filtrando a base de dados para que tenha somente resultados do Volume de Negócios
    df_vvn = df2[ df2['Tipo de Indices '] == "Volume de negócios"]

    # Condição para actualizar o grafico
    # if "Volume de Negócios" not in categoria: raise PreventUpdate

    # Grafico do volume de negocios 
    fig = px.scatter(df_vvn, x='date', y="value", color='indicadores', text= df_vvn['value'], #custom_data= 
                      hover_data=['value'], hover_name=df_vvn['Categoria'],
                 title='<br><b>' + ', '.join(sector) + '</b>')
    
    fig_lines = px.line(df_vvn, x='date', y="value", color='indicadores')
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
@callback(Output('ind_var_nps', 'figure'),
              Input('ano_id', 'value'),
              Input('resultados_id', 'value'), 
              Input('categoria_id', 'value'),        
              Input('sectores_id', 'value'))

# Resultados do emprego:
def resultado_emprego(ano, resultados, categoria, sector):
    
    # Copiando a dataset
    df_1 = indices_df_melted.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    df_ano_resul1 = df_1[(df_1["Ano"] == ano) & (df_1['Categoria'] == resultados)]

    # filtrando a base de dados pela categoria de resultados e pelos sectores de actividade
    # tipos de indices e indicadores para que tenha somente resultados do Emprego
    df1 = df_ano_resul1[df_ano_resul1['Tipo de Indices '].isin(categoria)]
    df2 = df1[df1["indicadores"].isin(sector)]

    # filtrando a base de dados para que tenha somente resultados do Emprego
    df_nps = df2[ df2['Tipo de Indices '] == "Emprego"]
    
    # Condição para actualizar o grafico
    #if "Emprego" not in categoria: raise PreventUpdate

    # Grafico do emprego
    fig = px.scatter(df_nps, x='date', y="value", color='indicadores', text= df_nps['value'], 
                      hover_data=['value'], hover_name=df_nps['Categoria'],
                 title='<br><b>' + ', '.join(sector) + '</b>')
    
    fig_lines = px.line(df_nps, x='date', y="value", color='indicadores')
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
                'x': 1.0,#0.5,
                'y': 1.15,
                'xanchor': 'right',
                'yanchor': 'top'},

            font = dict(
                family = "sans-serif",
                size = 10,
                color = "black")
    )
    fig.update_traces(textposition='top center', textfont_size=8)  # Actualizando o layout (fim)

    return fig


# CallBack dos resultados das remunerações
@callback(Output('ind_var_rem', 'figure'),
              Input('ano_id', 'value'),
              Input('resultados_id', 'value'), 
              Input('categoria_id', 'value'),        
              Input('sectores_id', 'value'))

# Resultados das remunerações:
def resultado_remuneracoes(ano, resultados, categoria, sector):
    
    # Copiando a dataset
    df_1 = indices_df_melted.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    df_ano_resul1 = df_1[(df_1["Ano"] == ano) & (df_1['Categoria'] == resultados)]


    # filtrando a base de dados pela categoria de resultados e pelos sectores de actividade  tipos de indices e indicadores\
    # para que tenha somente resultados das remunerações
    df1 = df_ano_resul1[df_ano_resul1['Tipo de Indices '].isin(categoria)]
    df2 = df1[df1["indicadores"].isin(sector)]

    # filtrando a base de dados para que tenha somente resultados das remunerações
    df_nps = df2[ df2['Tipo de Indices '] == "Remunerações"]
    
    # Condição para actualizar o grafico
    #if "Remunerações" not in categoria: raise PreventUpdate

    # Gráfico das remunerações
    fig = px.scatter(df_nps, x='date', y="value", color='indicadores', text= df_nps['value'], #custom_data= 
                      hover_data=['value'], hover_name=df_nps['Categoria'],
                 title='<br><b>' + ', '.join(sector) + '</b>')
    
    fig_lines = px.line(df_nps, x='date', y="value", color='indicadores')
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
    fig.update_traces(textposition='top center', textfont_size=8)  # Actualizando o layout (fim)

    return fig

# CallBack dos resultados das remunerações
@callback(Output('ind_var_horas', 'figure'),
              Input('ano_id', 'value'),
              Input('resultados_id', 'value'), 
              Input('categoria_id', 'value'),        
              Input('sectores_id', 'value'))

# Resultados das remunerações:
def resultado_remuneracoes(ano, resultados, categoria, sector):
    
    # Copiando a dataset
    df_1 = indices_df_melted.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    df_ano_resul1 = df_1[(df_1["Ano"] == ano) & (df_1['Categoria'] == resultados)]


    # filtrando a base de dados pela categoria de resultados e pelos sectores de actividade  tipos de indices e indicadores\
    # para que tenha somente resultados das remunerações
    df1 = df_ano_resul1[df_ano_resul1['Tipo de Indices '].isin(categoria)]
    df2 = df1[df1["indicadores"].isin(sector)]

    # filtrando a base de dados para que tenha somente resultados das remunerações
    df_nps = df2[ df2['Tipo de Indices '] == "Horas trabalhadas"]
    
    # Condição para actualizar o grafico
    #if "Remunerações" not in categoria: raise PreventUpdate

    # Gráfico das remunerações
    fig = px.scatter(df_nps, x='date', y="value", color='indicadores', text= df_nps['value'], #custom_data= 
                      hover_data=['value'], hover_name=df_nps['Categoria'],
                 title='<br><b>' + ', '.join(sector) + '</b>')
    
    fig_lines = px.line(df_nps, x='date', y="value", color='indicadores')
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
    fig.update_traces(textposition='top center', textfont_size=8)  # Actualizando o layout (fim)

    return fig


# CallBack dos comentarios-1
@callback(Output('comentarios_id1', 'children'),
              #Output('comentarios_id2', 'children'),
              Input('ano_id', 'value'), 
              Input('mes_id', 'value'),)

def data_dos_comentarios(ano, mes):
    if mes == 1:
        label= "Janeiro"

    elif mes == 2:
        label= "Fevereiro"

    elif mes == 3:
        label= "Marco"

    elif mes == 4:
        label= 'Abril'

    elif mes == 5:
        label= 'Maio'

    elif mes == 6:
        label= 'Junho'

    elif mes == 7:
        label= 'Julho'

    elif mes == 8:
        label= 'Agosto'

    elif mes == 9:
        label= 'Setembro'

    elif mes == 10:
        label= 'Outubro'

    elif mes == 11:
        label= 'Novembro'

    else:
        label= 'Dezembro'

    if mes is None: raise PreventUpdate

    text1= html.H6('Periodo escolhido:',
                                        style = {'font-family': 'Source Sans Pro', 'font-size': '13px', 'justifyContent': 'right', "font-weight": "bold" }  )
    text2= html.H6('Ano: '+ str(ano),
                                        style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right' ,"font-weight": "bold"}  )
    text3= html.H6('Mês: '+ label,
                                        style = {'font-family': 'Source Sans Pro', 'font-size': '12px', 'justifyContent': 'right' ,"font-weight": "bold"}  )

    return text1, text2, text3


# CallBack dos comentarios-1
@callback(Output('comentarios_id2', 'children'),
              Input('ano_id', 'value'), 
              Input('mes_id', 'value'),)

def data_dos_comentarios1(ano, mes):

    # Copiando a dataset
    df_1 = indices_df[["Ano", 'Mês', "Comentarios"]].drop_duplicates(subset=["Ano", 'Mês']).copy()
    print(df_1)

    # Filtrando a base de dados pelo ano e o tipo de resultados
    comentarios = (df_1[(df_1["Ano"] == ano) & (df_1['Mês'] == mes)])
    comentarios["Comentarios"]
    print(comentarios["Comentarios"])

    

    if mes is None: raise PreventUpdate


    # if comeentarios.isna():
    #      return html.H6('Os resultados e os comentarios dos Índices de Actividades Económicas do periodo escolhido escolhido ainda não se encontram disponiveis',
    #                                     style = {'font-family': 'Source Sans Pro', 'font-size': '20px', 'justifyContent': 'center', })
    # else:
    #     return html.H6(list(comentarios)[0],
    #                                     style = {'font-family': 'Source Sans Pro', 'font-size': '20px', 'justifyContent': 'center', })

    #texto1= html.H6('Comentários', style = {'font-family': 'Source Sans Pro', 'font-size': '12px',
    #                                                      'justifyContent': 'right', 'textAlign': 'center',"font-weight": "bold"}, className="h5"),
   #texto2= 

    # return html.H6('Os resultados dos Índices de Actividades Económicas do mês de Janeiro de 2023, quando comparados com os do mês anterior, revelam uma queda do índice de volume de negócios em 6,8%. Os índices de remunerações e de emprego registaram crescimento de 1,8 % e 1,5% respectivamente. A variação negativa do volume de negócios, deveu-se ao decréscimo verificado nos sectores da Produção Industrial (14,2%), de Transportes e Armazenagem (9,6%), de Alojamento, Restauração e Similares (6,3%), de Comércio (3,7%), de Outros Serviços não Financeiros (1,4%) e de Energia, Água e Saneamento (0,6%). O crescimento ligeiro do índice de emprego no mês de Janeiro, foi resultado da variação positiva do indicador nos sectores da Produção Industrial e do sector de Comércio com 11,3% e 0,3% respectivamente. No mesmo período, os sectores de Transportes e Armazenagem, de Alojamento, Restauração e Similares e o sector de Outros Serviços não Financeiros registaram decréscimo de 0,4%, 0,3% e 0,1% respectivamente. A variação positiva de remunerações no período em referência, foi resultado do crescimento das remunerações nos sectores da Produção Industrial (6,6%), de Comércio (2,5%), de Outros Serviços não Financeiros (1,1%) e do sector dos Transportes e Armazenagem (0,1%). O sector de Alojamento, Restauração e Similares registou queda de 5,1%. Comparando os índices globais do mês de Janeiro de 2023 com os do período homólogo de 2022, os índices de volume de negócios, de remunerações e de emprego registaram crescimentos de 8,0%, 10,3% e 2,1% respectivamente.',
    #                                     style = {'font-family': 'Source Sans Pro', 'font-size': '13px', 'justifyContent': 'right', }, className="comentarios" )
    return html.H6(comentarios["Comentarios"], style = {'font-family': 'Source Sans Pro', 'font-size': '13px', 'justifyContent': 'right', }, className="comentarios" )
#texto1, texto2


#CallBack da tabela a ser exportada
@callback(Output("tabela_resultados_id", 'data'),
              Input('resultados_id2', 'value'), 
              Input('categoria_id2', 'value'),
              Input('ano_id2', 'value'))

def data_table_update(resultados2, categoria2, ano2):
    
    # Copiando a dataset
    df_2 = indices_df.copy()

    # Filtrando a base de dados pelo ano e o tipo de resultados
    if resultados2:
        df_2 = df_2[df_2["Categoria"] == resultados2]

    # Filtrando a base de dados pelo ano e o tipo de resultados
    if categoria2:
        df_2 = df_2[df_2['Tipo de Indices '] == categoria2]     

    # Filtrando a base de dados pelo ano 
    if ano2:
        df_2 = df_2[df_2["Ano"] == ano2] 

    return df_2.to_dict("records")         