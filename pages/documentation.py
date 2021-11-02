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
            html.P("COMING SOON", className="coming_soon_text")
        ], className="screen_division_right"),
    ], className="documentation_main")
