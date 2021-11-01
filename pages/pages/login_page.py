from utils.import_utils import *
from app import app


def create_layout():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(src="assets/logo.png", className='login_logo'),
                ], className="login_left")
            ], width=4),
            dbc.Col([
                html.Div([
                    html.Div([
                        html.Div([
                            html.P("Login", className='login_head'),
                            dbc.FormGroup([
                                dbc.Label("E-mail", html_for="example-email", className='login_label'),
                                dbc.Input(type="email", className='login_field'),
                                dbc.Label("Password", html_for="example-password", className='login_label'),
                                dbc.Input(type="password", className='login_field')
                            ]),
                            dbc.Button("LOGIN", outline=True, color="primary", className='login_btn',
                                       href="/dashboard"),
                        ], className='login_white_container')
                    ], className='login_mid')
                ], className="login_right")
            ], width=8),
        ], no_gutters=True),
    ])
    #     html.Div([
    #     html.Div([
    #         dbc.Row([
    #             dbc.Col([
    #                 html.Div([
    #
    #                 ], className="login_left")
    #             ], width=4),
    #             dbc.Col([
    #                 html.Div([
    #
    #                 ], className="login_right")
    #             ], width=8),
    #             # dbc.Col([], xs=12, sm=1, md=2, lg=3, xl=4),
    #             # dbc.Col([
    #             #     html.Div([
    #             #     html.P("GENOMAGE", className='login_logo'),
    #             #     html.Div([
    #             #         html.P("Login", className='login_head'),
    #             #         dbc.FormGroup([
    #             #             dbc.Label("E-mail", html_for="example-email", className='login_label'),
    #             #             dbc.Input(type="email", className='login_field'),
    #             #             dbc.Label("Password", html_for="example-password", className='login_label'),
    #             #             dbc.Input(type="password", className='login_field')
    #             #         ]),
    #             #         dbc.Button("LOGIN", outline=True, color="primary", className='login_btn', href="/dashboard"),
    #             #     ], className='login_white_container')
    #             # ], className='login_mid')
    #             # ], xs=12, sm=10, md=8, lg=6, xl=4),
    #             # dbc.Col([], xs=12, sm=1, md=2, lg=3, xl=4),
    #         ], no_gutters=True),
    #     ], className='login_white_border')
    # ], className='login_main')
