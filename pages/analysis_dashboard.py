from utils.import_utils import *
from app import app
from pages import sidebar, topbar

# =================================== Genomage =================================================
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
        t=5  # top margin
    )
)


def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.P("Analysis Dashboard", className="analysis_db_title"),
                html.Div([
                    html.Div("Step-1", className="step_arrow"),
                    html.Div("Step-2", className="step_arrow"),
                    html.Div("Step-3", className="step_arrow"),
                    html.Div("Step-4", className="step_arrow_selected"),
                    html.Div("Step-9", className="step_arrow_gray"),
                ], className="steps_container"),
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            html.P("", className="analysis_db_detail_text_head"),
                            html.P("", className="analysis_db_detail_text_head"),
                            html.P("", className="analysis_db_detail_text_head"),
                            html.P("", className="analysis_db_detail_text_head"),
                        ], width=1),
                        dbc.Col([
                            html.P("Title:", className="analysis_db_detail_text_head"),
                            html.P("Analysis:", className="analysis_db_detail_text_head"),
                            html.P("Pipeline:", className="analysis_db_detail_text_head"),
                            html.P("Action:", className="analysis_db_detail_text_head"),
                        ], width=2),
                        dbc.Col([
                            html.P("Project 1", className="analysis_db_detail_text"),
                            html.P("WGS", className="analysis_db_detail_text"),
                            html.P("BWA-GATK", className="analysis_db_detail_text"),
                            html.Div(['Pause │ ', html.Span(' Abort', style={'color': 'red'})],
                                     className="analysis_db_detail_text"),
                        ], width=3),
                        dbc.Col([
                            html.P("Computing Speed: ", className="analysis_db_detail_text_head"),
                            html.P("% Completion: ", className="analysis_db_detail_text_head"),
                            html.P("Status:", className="analysis_db_detail_text_head"),
                            html.P("Duration:", className="analysis_db_detail_text_head"),
                        ], width=3),
                        dbc.Col([
                            html.P("High", className="analysis_db_detail_text"),
                            html.P("90%", className="analysis_db_detail_text"),
                            html.P("◉", className="analysis_db_detail_text", style={'color': '#00EE00'}),
                            html.P("3hrs 20min", className="analysis_db_detail_text"),
                        ], width=2),
                        dbc.Col([
                            html.P("", className="analysis_db_detail_text_head"),
                            html.P("", className="analysis_db_detail_text_head"),
                            html.P("", className="analysis_db_detail_text_head"),
                            html.P("", className="analysis_db_detail_text_head"),
                        ], width=1)
                    ], no_gutters=True),
                ], className="analysis_db_detail_box"),
                html.Div([
                    dbc.Row([
                        dbc.Col([html.Div([
                            dcc.Graph(figure=go.Figure(layout=layout).
                                      add_trace(go.Scatter(x=['Bar-1', 'Bar-2', 'Bar-3', 'Bar-4',
                                                              'Bar-5', 'Bar-6', 'Bar-7', 'Bar-8',
                                                              'Bar-9', 'Bar-10'],
                                                           y=[95, 16, 75, 44, 35, 89, 4, 23, 78, 33],
                                                           hoverinfo='x+y',
                                                           mode='lines',
                                                           line=dict(width=0.5, color='#ABE3D6'),
                                                           stackgroup='one',
                                                           line_shape="spline"
                                                           )).
                                      add_trace(go.Scatter(x=['Bar-1', 'Bar-2', 'Bar-3', 'Bar-4',
                                                              'Bar-5', 'Bar-6', 'Bar-7', 'Bar-8',
                                                              'Bar-9', 'Bar-10'],
                                                           y=[95, 16, 75, 44, 35, 89, 4, 23, 78, 33],
                                                           hoverinfo='x+y',
                                                           mode='lines',
                                                           line=dict(width=0.5, color='#9CBDC6'),
                                                           stackgroup='one',
                                                           line_shape="spline"
                                                           )).
                                      update_xaxes(showticklabels=False, showline=True, linewidth=1,
                                                   linecolor='#676767').
                                      update_yaxes(showticklabels=True, showline=True, linewidth=0.5,
                                                   linecolor='#676767').
                                      update_layout({'xaxis_tickangle': -50, 'plot_bgcolor': 'rgba(0,0,0,0)',
                                                     'paper_bgcolor': 'rgba(0,0,0,0)', 'bargap': 0.45,
                                                     'showlegend': False, 'barmode': 'stack',
                                                     'font': dict(family="Arial", size=14, color="#676767")}),
                                      style={'height': 200}, config={'displayModeBar': False})
                        ], className='analysis_graph_left')], width=6),
                        dbc.Col([html.Div([
                            dcc.Graph(figure=go.Figure(layout=layout).
                                      add_trace(go.Scatter(x=['Bar-1', 'Bar-2', 'Bar-3', 'Bar-4',
                                                              'Bar-5', 'Bar-6', 'Bar-7', 'Bar-8',
                                                              'Bar-9', 'Bar-10'],
                                                           y=[22, 3, 40, 62, 85, 28, 64, 33, 11, 16],
                                                           hoverinfo='x+y',
                                                           line=dict(width=0.5, color='#ABE3D6'),
                                                           stackgroup='one',
                                                           line_shape="spline"
                                                           )).
                                      add_trace(go.Scatter(x=['Bar-1', 'Bar-2', 'Bar-3', 'Bar-4',
                                                              'Bar-5', 'Bar-6', 'Bar-7', 'Bar-8',
                                                              'Bar-9', 'Bar-10'],
                                                           y=[22, 3, 40, 62, 85, 28, 64, 33, 11, 16],
                                                           hoverinfo='x+y',
                                                           mode='lines',
                                                           line=dict(width=0.5, color='#9CBDC6'),
                                                           stackgroup='one', line_shape="spline"
                                                           )).
                                      update_xaxes(showticklabels=False, showline=True, linewidth=1,
                                                   linecolor='#676767').
                                      update_yaxes(showticklabels=True, showline=True, linewidth=0.5,
                                                   linecolor='#676767').
                                      update_layout({'xaxis_tickangle': -50, 'plot_bgcolor': 'rgba(0,0,0,0)',
                                                     'paper_bgcolor': 'rgba(0,0,0,0)', 'bargap': 0.45,
                                                     'showlegend': False,
                                                     'font': dict(family="Arial", size=14, color="#676767")}),
                                      style={'height': 200}, config={'displayModeBar': False})
                        ], className='analysis_graph_right')], width=6),
                    ], no_gutters=True),
                ], className='analysis_graph_container'),
            ], className="analysis_db_sub_main")
        ], className="screen_division_right")
    ], className="analysis_db_main")
