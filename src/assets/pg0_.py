import dash
import pandas as pd
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.io as pio
import dash_table

# To create meta tag for each page, define the title, image, and description.
dash.register_page (__name__,
                    path = '/', #  is home page and it represents the url
                    name = "Síntese dos Índices de actividades económicas", # name of page, commonly used as name of link
                    title='Síntese IAE',  # title that appears on browser's tab
                    #image='pg1.png',  # image in the assets folder
                    description="Síntese dos índices de actividades económicas"

                    )

# page 1 data 
# Temos que carregar a base com a informação da síntese
# df = px.data.gapminder()

# Base de dados com os indices
indices_df = pd.read_csv('indices_20.csv', low_memory=False, encoding="iso-8859-1")


# Funcação para mostrar um grafico vazio
def make_empty_fig():
    fig = go.Figure()
    fig.layout.xaxis.range = [0, 6]
    fig.layout.yaxis.range = [0, 2]
    fig.layout.paper_bgcolor = "#eeeeee" #'#E5ECF6'
    fig.layout.plot_bgcolor = "#eeeeee" #'#E5ECF6'

    return fig

# Vamos configurar o layout
layout = html.Div(
    [
        html.H6('Síntese dos Índices de Actividades Económicas', style = {'font-family': 'Source Sans Pro', 'font-size': '16px',
                                                                           'justifyContent': 'right', 'textAlign': 'center'}),
        dbc.Row(
            [
                
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Label('Anos'),
                        dcc.Dropdown(id='ano_id',value=indices_df["Ano"].max(),
                        placeholder='Selecione o ano',
                        multi=False,
                        options=[{'label': ano, 'value': ano}
                                  for ano in indices_df["Ano"].unique()]),
                        
                        html.Hr(),
                        html.Br(),
                        html.Br(),
                        dbc.Label('Sectores de actividade económica'),
                        dcc.Dropdown(id='sectores_id',   
                        placeholder='Selecione o sector',
                        multi=True,
                        options=[{'label': sector, 'value': sector}
                                  for sector in indices_df.columns[4:]], 
                            style = {"width": "100%",  "align-items": "center","justify-content":"center" }),
                        


                    ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2),
                html.Br(),
                dbc.Col(
                    [
                        dbc.Row([
    
                # Vai ficar o gráfico            
                            dbc.Col(
                                [
                                html.H6('Índices agregados e variações mensais do volume de negócios', style = {"textAlign": "left", 
                                                                                                                'font-family': 'Source Sans Pro',
                                                                                                                 "font-size":" 1.2em"}),
                                dcc.Graph(id='ind_var_vvn',
                                figure=make_empty_fig())
                                ], align="center"),

                # Vai ficar o gráfico
                            dbc.Col(
                                [
                                html.H6('Índices agregados e variações mensais do emprego', style = {"textAlign": "left", 
                                                                                                                'font-family': 'Source Sans Pro',
                                                                                                                 "font-size":" 1.2em"}),
                                dcc.Graph(id='ind_var_nps',
                                figure=make_empty_fig())
                                ]),
                            ]),
                        
                        html.Br(),

                # Vai ficar o gráfico
                        dbc.Row([
                            dbc.Col(
                                [
                                html.H6('Índices agregados e variações mensais das remunerações', style = {"textAlign": "left", 
                                                                                                                'font-family': 'Source Sans Pro',
                                                                                                                 "font-size":" 1.2em"}),
                                dcc.Graph(id='ind_var_rem',
                                figure=make_empty_fig())
                                ], align="center"),

                # Vai ficar o gráfico
                            dbc.Col(
                                [
                                html.H6('Índices agregados e variações mensais das horas trabalhadas', style = {"textAlign": "left", 
                                                                                                                'font-family': 'Source Sans Pro',
                                                                                                                 "font-size":" 1.2em"}),
                                dcc.Graph(id='ind_var_horas',
                                figure=make_empty_fig())
                                ], align="center"),
                            ]),
                          
                    ], align="center", xs=10, sm=10, md=10, lg=10, xl=10, xxl=10),

            ],style = {'font-family': 'Source Sans Pro', 'font-size': '11px', 'justifyContent': 'right' }     
                ),
        html.Hr(),
         dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label('Breves Comentários de um determinado mes'),
                        dcc.Dropdown(id='mes_ind',   
                        placeholder='Selecione o mes',
                        multi=False,
                        options=[{'label': ano, 'value': ano}
                                  for ano in ['Janeiro', "Fevereiro", "Março"]]),
                    ],  className='column_left', xs=2, sm=2, md=2, lg=2, xl=2, xxl=2),

                dbc.Col(
                    [
                        
                        html.Div("Breves Comentários",
                        style = {"fontsize": 25, "textAlign": "center"})
                        # Vai ficar o gráfico
                    ], align="center", xs=10, sm=10, md=10, lg=10, xl=10, xxl=10)
            ],style = {'font-family': 'Source Sans Pro', 'font-size': '11px', 'justifyContent': 'right' }   
                ),
 
        # Uma linha para separar os resultados do VVN com o do NPS
        html.Hr(),#style={"height:2px;border-width:0;color:gray;background-color:gray"}),

        # Criação do bloco aonde ira ficar a tabela com a informação dos indices.
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H6('Índices agregados e variações mensais das remunerações', style={'textAlign': 'left'}),                        dbc.Label('Sectores de actividade económica'),

                        html.Br(),
                        dcc.Dropdown(id='ind_vs_var',   
                        placeholder='Selecione o indices ou variações',
                        multi=False,
                        options=[{'label': ind_var, 'value': ind_var}
                                  for ind_var in ['Indices', "Variacoes"]]),
                        
                        html.Br(),
                        dcc.Dropdown(id='ind_tipo',   
                        placeholder='Selecione os indices que pretende vericar',
                        multi=False,
                        options=[{'label': ind_var, 'value': ind_var}
                                  for ind_var in ['Indices', "Variacoes"]]),

                        html.Br(),
                        dcc.Dropdown(id='ano_ind',   
                        placeholder='Selecione o ano',
                        multi=False,
                        options=[{'label': ano, 'value': ano}
                                  for ano in ['2016', "2017", "2018"]]),

                    ], xs=2, sm=2, md=2, lg=2, xl=3, xxl=2),
                
                dbc.Col(
                    [
                        dash_table.DataTable(id="indices_resultados",
                                  columns=[{"name":i, "id":i,
                                  "selectable":True, "hideable":True,
                                  } for i in indices_df.columns
                                  ], data=indices_df.to_dict("records"),
                                  filter_action= "native",
                                  page_action= "native",
                                  page_current=0,
                                  page_size=6,
                                  #style_cell={"minWidth":100, "maxWidth":100, "width":100, "padding": "1.5px"}, # O estilo sera aplicado em toda tabela
                                  export_format="csv",
                                  style_cell_conditional=[
                                            {
                                                "if": {"column_id":c},
                                                "textAlign": "left"
                                            } for c in ["Categoria", "Tipo de Indices" ] # O estilo sera aplicado somente nas tabelas escolhidas
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
                                            "border": "1px solid black"
                                  },
                                  style_table = {"height": "300px", "overflowY":"auto"},
                                  #fixed_rows = {"headers": True},
                                  style_data_conditional=[
                                        {
                                            "if": {"row_index": "odd"},
                                            "backgroundColor": "rgb(248, 248, 248)"
                                        },
                                  ]
                                )
                    ], xs=9, sm=9, md=9, lg=9, xl=9, xxl=9),

            ], justify="center", align="left", style = {'font-family':'Source Sans Pro', 'font-size':'11px','justifyContent': 'right' }    
                ),
    ]           
                ),


@callback(Output('ind_var_vvn', 'figure'),
              Input('ano_id', 'value'),
              Input('sectores_id', 'value'),
              )

def plot_perc_pov_chart(ano, sector):
    #indicator = perc_pov_cols[indicator]
    df= indices_df.copy()
    df_ = (df
          [df['Ano'].eq(ano)]
          #.dropna(subset=sector)
          .sort_values("Mês"))
    df_ind=df_[df_["Categoria"]=='Indices ']
    df_var=df_[df_["Categoria"]=='Variação Mensal']

    if sector is None:
        raise PreventUpdate
    
    fig = go.Figure()
    print(df_ind[sector])  
    print(df_ind['Mês'])
# Indices do Volume de Negócios and Variação Mensal dos Indices do Volume de Negócios plot

    #fig.add_trace(go.Scatter(
    
    fig.add_trace(go.Scatter(
    name='Indices do Volume de Negócios',
        x=df_ind['Mês'],
        y=df_ind[sector],
        error_y=dict( type='data', # value of error bar given in data coordinates
                     symmetric=False,
            array=df_var[sector],
            visible=True),
        mode='lines',
        customdata= df_var[sector],
        hovertemplate = 'Indices: %{y:.2f}<extra></extra>'+";"+'Variação mensal: %{customdata:.2f}<extra></extra>',
        line=dict(color='#7fc97f', width=8),
        ))


    fig.add_trace(go.Scatter(
    
       name='Variação mensal',
        hoverinfo="none",
        x=df_ind['Mês'],
        y=df_ind[sector]+df_var[sector],
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=0),
        showlegend=False
    ))



    fig.add_trace(go.Scatter(
    
        #name='Lower Bound',
        hoverinfo="none",
        x=df_ind["Mês"],
        y=df_ind[sector]+0,
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines',
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
))


    # fig.update_layout(
    #   polar=dict(
    #     radialaxis=dict(
    #       visible=True,
    #     )),
    #   showlegend=True
    # )

    # # legend of the graph
    # fig.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.1,xanchor="right",x=0.950, 
    #                               font=dict(size=10,color="black")))


    # # Change background color 
    # fig.update_layout(
    #     template=None,
    #     polar = dict(radialaxis = dict(gridwidth=0.2,
    #                                range=[0,280],
    #                                showticklabels=True,  gridcolor = "black",
    #                                tickfont=dict(size=8,color="black")),

    #                  angularaxis = dict(showticklabels=True,#size=2,
    #                                rotation=-45,tickfont=dict(size=8,color="black"),
    #                                direction = "clockwise",
    #                                gridcolor = "black")))

    # # yxaxis legend size and color
    # fig.update_yaxes(tickangle=0, tickfont=dict(color="black"))
    # fig.update_xaxes(tickangle=90, tickfont=dict(color="black"))




    # fig = px.scatter(df,
    #                  x="Mês", 
    #                  y=sector,
    #                  #color='Population, total', 
    #                  #size=[30]*len(df),
    #                  #size_max=15,
    #                  #hover_name='Country Name',
    #                  #height=250 +(20*len(df)),
    #                  #color_continuous_scale='cividis',
    #                 #labels={gini: 'Gini Index'},
    #                 title=''.join(["Índices agregados e variações mensais do volume de negócios", '<br><b>', ', '.join(sector), '</b>']))
    #                 #title= "sector"+f'{sector[0]}' + '<b>: ' + f'{ano}' +'</b>')
    # fig.layout.paper_bgcolor = '#E5ECF6'
    # #fig.layout.xaxis.ticksuffix = '%'
    return fig



# def plot_gini_year_barchart(ano, sector):
#     if not ano:
#         raise PreventUpdate
#     df= indices_df.copy
#     df = df[df['Ano'].eq(ano)].sort_values("Mês")#.dropna(subset=[gini])
#     n_countries = len(df['Ano'])
#     fig = px.bar(df,
#                  x="Mês",
#                  y=sector, 
#                  orientation='h',
#                  height=200 + (n_countries*20), 
#                  title="var_ind" + ' ' + str(ano))
#     fig.layout.paper_bgcolor = '#E5ECF6'                 
#     return fig

# def plot_perc_pov_chart(year, indicator):
#     indicator = perc_pov_cols[indicator]
#     df = (perc_pov_df
#           [perc_pov_df['year'].eq(year)]
#           .dropna(subset=[indicator])
#           .sort_values(indicator))
#     if df.empty:
#         raise PreventUpdate

#     fig = px.scatter(df,
#                      x=indicator, 
#                      y='Country Name',
#                      color='Population, total', 
#                      size=[30]*len(df),
#                      size_max=15,
#                      hover_name='Country Name',
#                      height=250 +(20*len(df)),
#                      color_continuous_scale='cividis',
#                      title=indicator + '<b>: ' + f'{year}' +'</b>')
#     fig.layout.paper_bgcolor = '#E5ECF6'
#     #fig.layout.xaxis.ticksuffix = '%'
#     return fig
