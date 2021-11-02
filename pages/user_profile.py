from utils.import_utils import *
from app import app
from pages import sidebar, topbar


# =================================== Genomage =================================================
def create_layout():
    return html.Div([
        html.Div([
            sidebar.create_layout(),
        ], className="screen_division_left"),
        html.Div([
            topbar.create_layout(),
            html.Div([
                html.P("Personal Information", className="user_profile_title"),
                html.Div([
                    html.Div([
                        dbc.FormGroup([
                            dbc.Label("Account Type", className="user_profile_label", width=3),
                            dbc.Col(dbc.Select(
                                options=[
                                    {"label": "Option 1", "value": 1},
                                    {"label": "Option 2", "value": 2},
                                ], className="user_profile_input"
                            ), width=9),
                            dbc.Label("First Name", className="user_profile_label", width=3),
                            dbc.Col(dbc.Input(className="user_profile_input"), width=9),
                            dbc.Label("Last Name", className="user_profile_label", width=3),
                            dbc.Col(dbc.Input(className="user_profile_input"), width=9),
                            dbc.Label("Email", className="user_profile_label", width=3),
                            dbc.Col(dbc.Input(className="user_profile_input"), width=9),
                            dbc.Label("Organization", className="user_profile_label", width=3),
                            dbc.Col(dbc.Input(className="user_profile_input"), width=9),
                            dbc.Label("Organization Type", className="user_profile_label", width=3),
                            dbc.Col(dbc.Select(
                                options=[
                                    {"label": "Option 1", "value": 1},
                                    {"label": "Option 2", "value": 2},
                                ], className="user_profile_input"
                            ), width=9),
                            dbc.Label("Current Password", className="user_profile_label", width=3),
                            dbc.Col(dbc.Input(className="user_profile_input"), width=9),
                            dbc.Label("New Password", className="user_profile_label", width=3),
                            dbc.Col(dbc.Input(className="user_profile_input"), width=9),
                            dbc.Label("Confirm Password", className="user_profile_label", width=3),
                            dbc.Col(dbc.Input(className="user_profile_input"), width=9),
                        ], row=True)
                    ], className="user_profile_left_form"),
                    html.Div(dbc.Button("Update", color="success", className="user_profile_update"),
                             style={'text-align': 'right'})
                ], className="user_profile_borders")
            ], className="notification_sub_main")
        ], className="screen_division_right"),
    ], className="user_profile_main")
