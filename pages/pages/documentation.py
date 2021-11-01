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
            html.P('documentation')
        ], className="screen_division_right"),
    ])
