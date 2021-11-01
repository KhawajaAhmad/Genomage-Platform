from utils.import_utils import *
from app import app
from pages import sidebar, topbar

layout = go.Layout(
    margin=go.layout.Margin(
        l=0,  # left margin
        r=0,  # right margin
        b=0,  # bottom margin
        t=20  # top margin
    )
)

layout2 = go.Layout(
    margin=go.layout.Margin(
        l=0,  # left margin
        r=0,  # right margin
        b=0,  # bottom margin
        t=10  # top margin
    )
)

layout3 = go.Layout(
    margin=go.layout.Margin(
        l=12,  # left margin
        r=5,  # right margin
        b=0,  # bottom margin
        t=0  # top margin
    )
)


def percent(value):
    return dcc.Graph(figure=go.Figure(layout=layout2, layout_showlegend=False).
                     add_trace(go.Pie(labels=['Completed', 'Not Completed'],
                                      values=[value, 100 - value],
                                      hole=.85,
                                      direction='clockwise',
                                      sort=False,
                                      hoverinfo='skip',
                                      marker=dict(colors=['#5cb323', '#c9c9c9'],
                                                  # line=dict(color='#ffffff', width=2)
                                                  ),
                                      textinfo='none'
                                      )).
                     update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                    'font': dict(family="Arial", size=9, color="#676767"),
                                    'annotations': [
                                        dict(text=str(value) + '%', x=0.5, y=0.5, font_size=9, showarrow=False)]
                                    }),
                     className="dashboard_percent",
                     config={'displayModeBar': False})
    # return daq.Knob(
    #     id='my-daq-knob',
    #     min=0,
    #     max=100,
    #     value=value,
    #     size=50,
    #     color='#FD5901'
    # )
    # return dcc.Graph(figure=go.Figure(layout=layout).
    #                  add_trace(go.Indicator(mode="gauge+number", value=value,
    #                                         gauge={'bar': {'color': '#FD5901'},
    #                                                'axis': {'visible': False}},
    #                                         domain={'x': [0, 1], 'y': [0, 1]},
    #                                         delta={'reference': 100})).
    #                  update_xaxes(gridcolor='#F2F2F2', showticklabels=False, showline=True,
    #                               linewidth=1, linecolor='#676767').
    #                  update_yaxes(gridcolor='#F2F2F2', showticklabels=True,
    #                               showline=True, linewidth=0.5, linecolor='#E2E2E2').
    #                  update_layout({'xaxis_tickangle': -50,
    #                                 'plot_bgcolor': 'rgba(0,0,0,0)',
    #                                 'paper_bgcolor': 'rgba(0,0,0,0)', 'bargap': 0.75,
    #                                 'font': dict(family="Arial", size=10,
    #                                              color="#676767")}),
    #                  style={'height': 48},
    #                  config={'displayModeBar': False})
    # return html.Div([
    #     html.P("◉", className='dashboard_table_percent_circle'),
    #     html.P(str(value) + "%", className='dashboard_table_text_percent')
    # ])


def get_variant_completion_bar():
    return dcc.Graph(figure=go.Figure(layout=layout3).
                     add_trace(go.Bar(y=['Completion-Bar'],
                                      x=[40],
                                      orientation='h',
                                      marker=dict(color='#2bc37f'))).
                     add_trace(go.Bar(y=['Completion-Bar'],
                                      x=[15],
                                      orientation='h',
                                      marker=dict(color='#6d91f9'),
                                      )).
                     add_trace(go.Bar(y=['Completion-Bar'],
                                      x=[5],
                                      orientation='h',
                                      marker=dict(color='#fd956b'),
                                      )).
                     add_trace(go.Bar(y=['Completion-Bar'],
                                      x=[40],
                                      orientation='h',
                                      marker=dict(color='#ebf1f8'),
                                      )).
                     update_xaxes(showticklabels=False, showline=False).
                     update_yaxes(showticklabels=False, showline=False).
                     update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                    'showlegend': False,
                                    'barmode': 'stack',
                                    }),
                     style={'height': 8}, config={'displayModeBar': False})


def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Project Title', className='dashboard_table_heading'),
                        html.P('Analysis Type', className='dashboard_table_heading'),
                        html.P('Pipeline', className='dashboard_table_heading'),
                        html.P('Current Step', className='dashboard_table_heading'),
                        html.P('% Completion', className='dashboard_table_heading'),
                    ], className='dash_table_top'),
                    html.Div([
                        html.P('Project 1', className='dashboard_table_text'),
                        html.P('WGS', className='dashboard_table_text'),
                        html.P('BWA-GATK', className='dashboard_table_text'),
                        html.Div([html.P('Variant Calling',
                                         # style={'color': '#2bc37f'},
                                         className='dashboard_table_text1'),
                                  html.Div(
                                      get_variant_completion_bar(),
                                      className='variant_bar'),
                                  ], className="variant_bar_container"),
                        html.P(percent(100), className='dashboard_table_percent_box')
                    ], className='dash_table_bottom'),
                    html.Div([
                        html.P('Project 2', className='dashboard_table_text'),
                        html.P('WES', className='dashboard_table_text'),
                        html.P('BWA-GATK', className='dashboard_table_text'),
                        html.Div([html.P('Variant Calling',
                                         # style={'color': '#6d91f9'},
                                         className='dashboard_table_text1'),
                                  html.Div(
                                      get_variant_completion_bar(),
                                      className="variant_bar"),
                                  ], className="variant_bar_container"),
                        html.P(percent(70), className='dashboard_table_percent_box')
                    ], className='dash_table_bottom'),
                    html.Div([
                        html.P('Project 3', className='dashboard_table_text'),
                        html.P('RNA seq', className='dashboard_table_text'),
                        html.P('BWA-GATK', className='dashboard_table_text'),
                        html.Div([html.P('Variant Calling',
                                         # style={'color': '#fd956b'},
                                         className='dashboard_table_text1'),
                                  html.Div(
                                      get_variant_completion_bar(),
                                      className="variant_bar"),
                                  ], className="variant_bar_container"),
                        html.P(percent(46), className='dashboard_table_percent_box')
                    ], className='dash_table_bottom'),
                    html.Div([
                        html.P('Project 4', className='dashboard_table_text'),
                        html.P('SARS-COV2', className='dashboard_table_text'),
                        html.P('BWA-GATK', className='dashboard_table_text'),
                        html.Div([html.P('Variant Calling',
                                         # style={'color': '#2bc37f'},
                                         className='dashboard_table_text1'),
                                  html.Div(
                                      get_variant_completion_bar(),
                                      className="variant_bar"),
                                  ], className="variant_bar_container"),
                        html.P(percent(28), className='dashboard_table_percent_box')
                    ], className='dash_table_bottom'),
                ], className='dashboard_table'),
                html.Div([
                    dbc.Row([
                        dbc.Col([html.Div([
                            dcc.Graph(figure=go.Figure(layout=layout).
                                      add_trace(go.Bar(x=['Bar-1', 'Bar-2', 'Bar-3', 'Bar-4',
                                                          'Bar-5', 'Bar-6', 'Bar-7', 'Bar-8',
                                                          'Bar-9', 'Bar-10'],
                                                       y=[22, 13, 40, 62, 85, 28, 64, 33, 11, 16],
                                                       hoverinfo='skip',
                                                       marker=dict(color='#ABE3D6'))).
                                      add_trace(go.Bar(x=['Bar-1', 'Bar-2', 'Bar-3', 'Bar-4',
                                                          'Bar-5', 'Bar-6', 'Bar-7', 'Bar-8',
                                                          'Bar-9', 'Bar-10'],
                                                       y=[22, 3, 40, 62, 85, 28, 64, 33, 11, 16],
                                                       hoverinfo='skip',
                                                       marker=dict(color='#9CBDC6'),
                                                       )).
                                      update_xaxes(showticklabels=False, showline=True, linewidth=1,
                                                   linecolor='#676767').
                                      update_yaxes(showticklabels=True, showline=True, linewidth=0.5,
                                                   linecolor='#676767').
                                      update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                                                     'paper_bgcolor': 'rgba(0,0,0,0)', 'bargap': 0.45,
                                                     'showlegend': False, 'barmode': 'stack',
                                                     'font': dict(family="Arial", size=12, color="#676767"),
                                                     'xaxis_title': "Time",
                                                     'yaxis_title': "No. of Analysis"}),
                                      style={'height': 240}, config={'displayModeBar': False})
                        ], className='graph1')], width=6),
                        dbc.Col([html.Div([
                            dcc.Graph(figure=go.Figure(layout=layout).
                                      add_trace(go.Bar(x=['Bar-1', 'Bar-2', 'Bar-3', 'Bar-4',
                                                          'Bar-5', 'Bar-6', 'Bar-7', 'Bar-8',
                                                          'Bar-9', 'Bar-10'],
                                                       y=[22, 3, 40, 62, 85, 28, 64, 33, 11, 16],
                                                       hoverinfo='skip',
                                                       marker=dict(color='#ABE3D6'))).
                                      add_trace(go.Scatter(x=['Bar-1', 'Bar-2', 'Bar-3', 'Bar-4',
                                                              'Bar-5', 'Bar-6', 'Bar-7', 'Bar-8',
                                                              'Bar-9', 'Bar-10'],
                                                           y=[22, 3, 40, 62, 85, 28, 64, 33, 11, 16],
                                                           hoverinfo='skip',
                                                           marker=dict(color='#9CBDC6'),
                                                           mode='lines',
                                                           line_shape='spline')).
                                      update_xaxes(showticklabels=False, showline=True, linewidth=1,
                                                   linecolor='#676767').
                                      update_yaxes(showticklabels=True, showline=True, linewidth=0.5,
                                                   linecolor='#676767').
                                      update_layout({'plot_bgcolor': 'rgba(0,0,0,0)',
                                                     'paper_bgcolor': 'rgba(0,0,0,0)', 'bargap': 0.45,
                                                     'showlegend': False,
                                                     'font': dict(family="Arial", size=12, color="#676767"),
                                                     'xaxis_title': "Time",
                                                     'yaxis_title': "No. of Analysis"
                                                     }),
                                      style={'height': 240}, config={'displayModeBar': False})
                        ], className='graph2')], width=6),
                    ], no_gutters=True),
                ], className='dashboard_graph_container'),
            ], className='dashboard_sub_main')
        ], className="screen_division_right"),
    ], className='dashboard_main')
