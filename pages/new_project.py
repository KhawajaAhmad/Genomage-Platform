from utils.import_utils import *
from app import app
from pages import sidebar, topbar


def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.P('New Project', className='new_project_head'),
                dbc.FormGroup([
                    dbc.Label("Project Name", className="new_project_label", xs=12, sm=4, md=3, lg=3, xl=3),
                    dbc.Col(dbc.Input(type="text", className="new_project_field"),
                            xs=12, sm=8, md=9, lg=9, xl=9),
                    dbc.Label("More Info", className="new_project_label_bold", width=12),
                    dbc.Label("tags", className="new_project_label", xs=12, sm=4, md=3, lg=3, xl=3),
                    dbc.Col(dbc.Input(type="text", className="new_project_field"),
                            xs=12, sm=8, md=9, lg=9, xl=9),
                    dbc.Label("Project Summary", className="new_project_label", xs=12, sm=4, md=3, lg=3, xl=3),
                    dbc.Col(dbc.Input(type="text", className="new_project_field"),
                            xs=12, sm=8, md=9, lg=9, xl=9),
                    dbc.Label("Project Description", className="new_project_label", xs=12, sm=4, md=3, lg=3, xl=3),
                    dbc.Col(dcc.Textarea(className="new_project_field", style={'height': 80}),
                            xs=12, sm=8, md=9, lg=9, xl=9),
                    dbc.Label("Access", className="new_project_label_bold", width=12),
                    dbc.Label("Data Access", className="new_project_label", xs=12, sm=4, md=3, lg=3, xl=3),
                    dbc.Col(dcc.Dropdown(options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                        className='new_project_dropdown',
                        searchable=False
                    ),
                        xs=12, sm=8, md=9, lg=9, xl=9),
                    dbc.Label("Delete Data", className="new_project_label", xs=12, sm=4, md=3, lg=3, xl=3),
                    dbc.Col(dcc.Dropdown(options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                        className='new_project_dropdown',
                        searchable=False
                    ), xs=12, sm=8, md=9, lg=9, xl=9),
                    dbc.Label("Download Data", className="new_project_label", xs=12, sm=4, md=3, lg=3, xl=3),
                    dbc.Col(dcc.Dropdown(options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                        className='new_project_dropdown',
                        searchable=False
                    ), xs=12, sm=8, md=9, lg=9, xl=9),
                ], row=True, className='new_project_form')
            ], className='new_project_form_container')
        ], className="screen_division_right")
    ], className='new_project_main')
